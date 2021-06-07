import re

# A script to create an incident from an email message, add artifacts to the incident based on information
# present in the body of the message, and add any email attachments to the incident.

# The new incident owner - the email address of a user or the name of a group and cannot be blank.
# Change this value to reflect who will be the owner of the incident before running the script.
newIncidentOwner = ""

# Whitelist for IP V4 addresses
ipV4WhiteList = [
  #"127.0.0.0/8",                # Loopback
  #"192.168.0.0/16",             # Class B private network local communication (RFC 1918)
  #"198.18.0.0/15",              # Testing of inter-network communications between subnets (RFC 2544)
  #"169.254.0.0/16",             # Link-local (APIPA)
  #"224.0.0.0/4",                # Multicast
  #"192.88.99.0/24",             # 6to4 anycast relays (RFC 3068)
  #"0.0.0.0/8",                  # Broadcast message (RFC 1700)
  #"192.0.2.0/24",               # TEST-NET examples and documentation (RFC 5737)
  #"240.0.0.0/4",                # Reserved for  multicast assignments (RFC 5771)
  #"198.51.100.0/24",            # TEST-NET-2 examples and documentation (RFC 5737)
  #"203.0.113.0/24",             # TEST-NET-3 examples and documentation (RFC 5737)
  #"233.252.0.0/24",             # Multicast test network
  #"225.0.0.0-231.255.255.255",  # Reserved (RFC5771)
  #"234.0.0.0-238.255.255.255",  # Unicast-prefix-based
  #"239.0.0.0-239.255.255.255"   # Administrative Multicast
]

# Whitelist for IP V6 addresses
ipV6WhiteList = [
  #"::/8",                       # Reserved by IETF [RFC3513][RFC4291]
  #"0100::/8",                   # Reserved by IETF [RFC3513][RFC4291]
  #"0200::/7",                   # Reserved by IETF [RFC4048]
  #"0400::/6",                   # Reserved by IETF [RFC3513][RFC4291]
  #"0800::/5",                   # Reserved by IETF [RFC3513][RFC4291]
  #"1000::/4",                   # Reserved by IETF [RFC3513][RFC4291]
  #"4000::/3",                   # Reserved by IETF [RFC3513][RFC4291]
  #"6000::/3",                   # Reserved by IETF [RFC3513][RFC4291]
  #"8000::/3",                   # Reserved by IETF [RFC3513][RFC4291]
  #"A000::/3",                   # Reserved by IETF [RFC3513][RFC4291]
  #"C000::/3",                   # Reserved by IETF [RFC3513][RFC4291]
  #"E000::/4",                   # Reserved by IETF [RFC3513][RFC4291]
  #"F000::/5",                   # Reserved by IETF [RFC3513][RFC4291]
  #"F800::/6",                   # Reserved by IETF [RFC3513][RFC4291]
  #"FC00::/7",                   # Unique Local Addresses (ULA)
  #"FE00::/9",                   # Reserved by IETF [RFC3513][RFC4291]
  #"FEC0::/1                     # Reserved by IETF [RFC3879]
]

# Domain whitelist
domainWhiteList = [
  #"*.ibm.com"
]

class Utils:
  """ A class to collect some utilities used by the rest of the script. """

  @staticmethod
  def convertIPv4ToInt(address):
    """ A static method that converts a IPv4 address to a binary representation. """
    addressAsBinary = 0
    #split into octets
    octets = address.split(".")
    #startFromLeft
    lpos = 32 - 8
    for octet in octets:
      octetAsInt = int(octet)
      addressAsBinary = addressAsBinary + (octetAsInt << lpos)
      lpos = lpos - 8
    return addressAsBinary

  @staticmethod
  def convertIPV4v6ToInt(address):
    """ A static method that converts a IPv4 and IPv6 address to a binary representation. """
    addressAsBinary = 0
    # Split into hextets
    hextets = address.split(":")
    # It might be a V4 IP address in a V6 envelope
    if "." in hextets[-1]:
      return Utils.convertIPv4ToInt(hextets[-1])
    else:
      # Start from Left
      lpos = 128 - 16
      for hextet in hextets:
        if len(hextet) == 0:
          break
        hextetAsInt = int(hextet,16)
        addressAsBinary = addressAsBinary + (hextetAsInt << lpos)
        lpos = lpos - 16
      # If the previous loop has exited without covering all the hextets then it means there is a "::" present,
      # so we have to process the reamining hextets from the right
      if lpos > 0:
        rpos = 0
        for hextet in hextets[::-1]:
          if len(hextet) == 0:
            break
          hextetAsInt = int(hextet,16)
          addressAsBinary = addressAsBinary + (hextetAsInt << rpos)
          rpos = rpos + 16
      return addressAsBinary


class WhiteListElement(object):
  """ A class that represents a domain, IP address range or network segment that has been verified as not being suspicious. """

  # A text representation of the element
  asString = None

  def __init__(self, elementAsString):
    """ The constructor that takes one parameter - the textual representation of the element. """
    self.asString = elementAsString

  def __str__(self):
    """Method to return the text representation of the object."""
    return self.asString

  def __repr__(self):
    """Method to return the text representation of the object."""
    return u"WhiteListElement(\"{0}\")".format(self.asString)

  def test(self, other):
    """ A function intended to be inherited but overrided by subclasses. It should return True if the "other" object
    would be matched by this white list element.
    """
    return False


class IPAddress:
  """ A class for IP addresses, both IPv4 and IPv6. """

  # The IP address as a String, as originally presented to the constructor
  addressAsString = None

  # The IP Address as a binary representation
  addressAsBinary = None

  def __init__(self, newAddressAsString):
    """ The constructor, which takes one parameter - the string representation to be used to create the addressAsBinary. """
    self.addressAsString = newAddressAsString.strip()
    self.addressAsBinary = Utils.convertIPV4v6ToInt(self.addressAsString)

  def __str__(self):
    """Method to return the text representation of the object."""
    return self.addressAsString

  def __repr__(self):
    """Method to return the text representation of the object."""
    return "IPAddress(\"{0}\")".format(self.addressAsString)


class CIDR(WhiteListElement):
  """ A CIDR (Classless Inter-Domain Routing) is one of the possible types of white list element, representing either an explicit IP Address or
  a subnet in the form of an IP Address and a subnet mask suffix. E.G.
  127.0.0.1
  10.0.0.0/8
  fc00::/7
  """

  # The suffix/subnet mask (defaults to 0 when not present)
  cidrSuffix = 0
  # Width of the address in bits (32 for IPv4, 128 for IPv6)
  width = 32
  # The address as a binary number
  addressAsBinary = 0

  def __init__(self, newCIDR):
    """ CIDR constructor. This takes one parameter which is the textual representation of the CIDR. """
    # Store the textual representation in the base class
    super(CIDR, self).__init__(newCIDR)
    # Split at the subnet separator character (if present)
    cidrParts = self.asString.split("/")
    # The first part is interpreted the IP address
    self.addressAsBinary = Utils.convertIPV4v6ToInt(cidrParts[0])

    self.width = 128 if ":" in newCIDR else 32

    # If there is a suffix, interpret it correctly
    if len(cidrParts) > 1:
      self.cidrSuffix = int(cidrParts[1])
    else:
      self.cidrSuffix = self.width

  def test(self, anIPAddress):
    """ An IP address matches the CIDR if both of them have the same binary value when both are shifted right by the
    CIDR subnet mask suffix.
    """
    log.debug("Going to filter IPAddress {0} against {1}".format(anIPAddress, self))
    return (anIPAddress.addressAsBinary >> (self.width - self.cidrSuffix) == self.addressAsBinary >> (self.width - self.cidrSuffix))


class IPRange(WhiteListElement):
  """ A type of WhiteListElement that represents a range, from a lower bound to an upper bound, inclusive. """
  lowest = None
  highest = None

  def __init__(self, stringRepresentation):
    """ IPRange constructor that takes two parameters.
    Parameter "lowestAsText" - the lowest IP address in the range.
    Parameter "highestAsText" - the highest IP address in the range.
    """
    lowestAsText, highestAsText = stringRepresentation.split("-")
    super(IPRange, self).__init__(stringRepresentation)
    self.lowest = IPAddress(lowestAsText)
    self.highest = IPAddress(highestAsText)

  def test(self, anIPAddress):
    """ A method that returns true if anIPAddress is not below self.lowest and not above self.highest. """
    return self.highest.addressAsBinary >= anIPAddress.addressAsBinary and self.lowest.addressAsBinary <= anIPAddress.addressAsBinary

  def __str__(self):
    """Method to return the text representation of the object."""
    return "{0}-{1}".format(self.lowest, self.highest)

  def __repr__(self):
    """Method to return the text representation of the object."""
    return "IPRange(\"{0}-{1}\")".format(self.lowest, self.highest)


class Domain(WhiteListElement):
  """ A type of WhiteListElement that represents a domain or domain pattern. E.G.
  *.ibm.com
  mailserver.knowngood.com
  """

  # A regular expression to match the domain. Domains of the form "*.example.com" are converted to ".*.example.com"
  processedRegEx = None

  def __init__(self, stringRepresentation):
    """ Constructor for the Domain class. This takes one parameter - the domain pattern as a String. """
    # Save the string representation in the superclass
    super(Domain, self).__init__(unicode(stringRepresentation))
    # "ibm.com" and "*.ibm.com" are synonymous
    if (stringRepresentation.startswith("*.")):
      stringRepresentation = stringRepresentation[2:]
    self.processedRegEx = u"\A(?:\\S*\\.)*({0})\\Z".format(stringRepresentation.replace(".","\."))

  def test(self, urlString):
    """ A method that returns true if the value passed in urlString matches the regex in self.processedRegEx. """
    # Extract domain from urlString
    domain = re.sub(".*://([^/:|~`\s<>\"'{}]*)(?:[/:|~`\s<>\"'{}]|\Z).*", r"\1", urlString, re.IGNORECASE | re.UNICODE)
    # Match regex of this Domain object against extracted domain string
    matches = re.findall(self.processedRegEx, domain, re.IGNORECASE | re.UNICODE)
    return (matches != None) and (len(matches) > 0)

  def __str__(self):
    """Method to return the text representation of the object."""
    return u"{0}".format(self.asString)

  def __repr__(self):
    """Method to return the text representation of the object."""
    return u"Domain(\"{0}\")".format(self.asString)


class WhiteList(list):
  """ A class that extends the list class to support the white list facility. """

  def checkIsItemNotOnWhiteList(self, anItem):
    """ A method that checks if an item should be removed from the artifact list because if matches a whitelist element.
    Parameter "anItem" - the item in question.
    Return value: The item if it should be kept, None if it should be removed.
    """
    for whiteListEntry in self:
      if whiteListEntry.test(anItem):
        log.info(u"Filtering out {0} because it matched with whitelist entry {1}".format(anItem, self))
        return None
    return anItem

  @staticmethod
  def createFromIPv4Collection(theList):
    """ A static method to create a list of IPv4 WhiteListElements based on a list of strings.
    Parameter "theList" - the list of string representations of WhiteListElements suitable for IPv4.
    Return value: A WhiteList that can be used against IPv4 addresses.
    """
    completedList = WhiteList()
    for element in theList:
      if "-" in element:
        completedList.append(IPRange(element))
      else:
        completedList.append(CIDR(element))
    return completedList

  @staticmethod
  def createFromCollection(theList, constructor):
    """ A static method to create a list of WhiteListElements based on a list of strings.
    Parameter "theList" - the list of string representations of WhiteListElements.
    Parameter "constructor" - the class for objects that will populate the return value.
    Return value: A WhiteList that can be used against IPv4 addresses.
    """
    completedList = WhiteList()
    for element in theList:
      completedList.append(constructor(element))
    return completedList


class EmailProcessor(object):
  """ A class that facilitates processing the body contents of an email message.
  Once the EmailProcessor class has been instanciated, the other methods can be used to add artifacts to the
  incident.
  """

  # The body of the email - the plaintext and html versions of the same email, if present
  emailContents = []

  # The set of already-added artifacts. If an artifact is in the set then it will not be added to the incident
  # a second time.
  addedArtifacts = set()

  # Create Whitelist for IP V4 addresses from string representations
  ipV4WhiteListConverted = WhiteList.createFromIPv4Collection(ipV4WhiteList)

  # Create Whitelist for IP V6 addresses from string representations
  ipV6WhiteListConverted = WhiteList.createFromCollection(ipV6WhiteList, CIDR)

  # Create Whitelist domains from string representations
  domainWhiteListConverted = WhiteList.createFromCollection(domainWhiteList, Domain)

  def __init__(self):
    """The EmailProcessor constructor.
    As initilization it retrieves the email body as both text and HTML.
    """
    if (emailmessage.body.content is not None):
      self.emailContents.append(unicode(emailmessage.body.content))
    if (emailmessage.getBodyHtmlRaw() is not None):
      self.emailContents.append(unicode(emailmessage.getBodyHtmlRaw()))
    if (len(self.emailContents) == 0):
      log.error("Email message has no contents!")

  def addUniqueArtifact(self, theArtifact, artifactType, description):
    """This method adds a new unique artifact to the incident. Previously added artifacts are added to the
    "addedArtifacts" set. If the new artifact has already been added to the list then it is not added to the
    incident a second time.
    Parameter "theArtifact" - the value of the artifact to create.
    Parameter "artifactType" - the type of the artifact.
    Parameter "description" - the description of the artifact.
    No return value.
    """
    if (theArtifact, artifactType) in self.addedArtifacts:
      log.debug(u"Skipping previously added artifact {0} of type {1}, description {2}".format(theArtifact, artifactType, description))
    else:
      log.info(u"Adding artifact {0} of type {1}, description {2}".format(theArtifact, artifactType, description))
      incident.addArtifact(artifactType, theArtifact, description)
      self.addedArtifacts.add((theArtifact, artifactType))

  @staticmethod
  def printList(name, list):
    """A convenience method to log the contents of a list. The method will log each element in a list, along with
    its name and ordinal in the list.
    Parameter "name" - the name of the elements in the list e.g. "IP Address".
    Parameter "list" - the list to iterate through.
    No return value.
    """
    for num, value in enumerate(list):
      log.debug(u"{0} {1} {2}".format(name, num, value))

  @staticmethod
  def makeUrlPattern():
    """A method to return a regex pattern that includes a full URL including scheme, domain, path, hash and
    query string. It starts the match from the scheme name with optional "s", followed by "://" and continues until
    it finds a character that is not permitted in a URL. Because of the expectation that potentially harmful URLs
    are being modified for safety, the URL-invalid characters "[" and "]" will not terminate the match.
    Returns the requested pattern as a string.
    """
    return "((?:https?://[^^|~`\\s<>\"'{}]+)|(?:href=\"(?:[^^|~`\\s<>\"'{}]+)))"

  @staticmethod
  def fixURL(theURL):
    """Method to fix a list of bowdlerized URLs. Many systems attempts to make potentially dangerous URLs into
    unopenable but human-readible strings. Resilient will reject URL artifacts that do not conform to spec.
    In this case we are converting "www[.]dangerous[.]nasty" to "www.dangerous.nasty".
    If a URL is discovered in HTML anchor it will have href=" before it.
    If the URL does not contain :// then http:// is presumed.
    Parameter "list" - the list of URLs to fix.
    Returns a new list containing fixed versions of the original list.
    """
    retVal = re.sub(r"\[\.\]",".", theURL)
    retVal = re.sub(r"href=\"","", retVal)
    if ("://" not in retVal):
      retVal = "http://" + retVal
    return retVal

  @staticmethod
  def makeIPv4Pattern():
    """A method to return a pattern that matches valid IPv4 addresses.
    Returns a string containing a pattern that matches 4 instances of 1-3 decimal digits, separated by ".".
    """
    return "(?:[\d]{1,3}\.){3}[\d]{1,3}"

  @staticmethod
  def cleanIPv4(anAddress):
    """A method to filter out impossible IP4 addresses from a list of strings that have been matched by the pattern
    from makeIPv4Pattern().
    First each address is split into its component octets. If the maximum int value of an octet in an address is
    less than 256 then the address is valid. The return value is a set, to avoid unnecessary duplication.
    Parameter "addressList" - the list of addresses to filter.
    Returns a new set of valid addresses.
    """
    octets = anAddress.split(".")
    octetsAsIntArray = map(int, octets)
    if (len(octets) != 4) or max(octetsAsIntArray) > 255:
      return None
    else:
      return ".".join(map(str, octetsAsIntArray)) # eliminate leading zeros.

  @staticmethod
  def makeIPv6Pattern():
    """A method to return a pattern that will match IPv6 addresses.
    The pattern will match strings of the form:
    abcd:abcd:1234:abcd:abcd:abcd:abcd:abcd:abcd
    abcd:abcd::abcd:abcd:abcd:abcd:abcd
    abcd:abcd:abcd:abcd:abcd:abcd::abcd
    ::1
    ::ffff:192.0.1.1
    but it will also match strings such as
    16:38:37
    This necessitates a second cleaning stage, performed by cleanIPv6().
    """
    return "((?:(?:[A-Fa-f0-9]){0,4}:){1,7}(?:[A-Fa-f0-9]){1,4}(?:\\.[0-9]{1,3}){0,3})"

  @staticmethod
  def cleanIP(anAddress):
    """A method to filter invalid IP addresses from the addressList parameter. The list is presumed to derive
    from matching text based on the output of makeIPv6Pattern() or makeIPv4Pattern().
    If the method discovers that the address is encapsulated IPv4 then the method will return the result from calling
    cleanIPv4() on the IPv4 section. If the address is IPv6 the method will reject strings with more than 7 ":"s or
    more than one instance of "::". If there is no "::" then there must be 7 ":"s.
    """
    log.debug("Going to clean IP address {0}".format(anAddress))
    hextets = anAddress.split(":")
    # It might be a V4 IP address in a V6 envelope
    if "." in hextets[-1]:
      return EmailProcessor.cleanIPv4(hextets[-1])
    # At most 7 ":"
    if anAddress.count(":") < 8:
      # At most one instance of "::"
      if anAddress.count("::") < 2:
        if anAddress.count("::") == 1 or anAddress.count(":") == 7:
          return anAddress
    return None

  @staticmethod
  def makeHexPattern(length):
    """A method that returns a regex pattern that matches a case-insensitive hexadecimal number of exactly a specified
    length.
    Parameter "length" - the length of the pattern in digits/characters/nibbles
    Returns the corresponding pattern.
    """
    return "(?:\A|[^0-9a-zA-Z])([0-9a-fA-F]{" + str(length) + "})(?:[^0-9a-zA-Z]|\Z)"

  def processArtifactCategory(self, regex, artifactType, description, *optionalListModifierFn):
    """A method to process a category of artifact, based on a regular expression. Each match of the regex in the
    email message contents is added as an artifact of the same type and description. The optional list modifier
    function, if present, is run against the list of matches before the artifact addition takes place.
    Parameter "regex" - the regular expression to use to pick out the text to interpret as an artifact
    Parameter "artifactType" - the type of the artifact
    Parameter "description" - the description of the artifact
    Parameter "optionalListModifierFn" - a function to run across the list of matches to filter inappropriate values
    No return value.
    """
    for theText in self.emailContents:
      dataList = re.findall(regex, theText, re.UNICODE)
      if dataList is not None and len(dataList) > 0 :
        if optionalListModifierFn is not None:
          for aFunction in optionalListModifierFn:
            dataList = map(aFunction, dataList)
            dataList = [x for x in dataList if x is not None]

        self.printList(u"Found {0} ( {1} )".format(artifactType,description), dataList)
        map(lambda theArtifact: self.addUniqueArtifact(theArtifact, artifactType, description), dataList)
      else:
        log.debug(u"Could not find artifact {0} for regex {1}".format(artifactType,regex))

  def checkIPWhiteList(self, anAddress):
    """ A method to check a list of IP Addresses aginst the whitelist. """
    whiteList = self.ipV4WhiteListConverted if "." in anAddress.addressAsString else self.ipV6WhiteListConverted
    log.debug(u"Going to filter {0} against whitelist {1}".format(anAddress, whiteList))
    return whiteList.checkIsItemNotOnWhiteList(anAddress)

  def checkDomainWhiteList(self, aURL):
    """ A method to check a list of URLs aginst a whitelist. """
    log.debug(u"Going to filter {0} against whitelist {1}".format(aURL, self.domainWhiteListConverted))
    return self.domainWhiteListConverted.checkIsItemNotOnWhiteList(aURL)

  def processIPFully(self, theAddressAsString):
    """ A method to filter inadvertantly matched IP strings and then filter out IP addresses that appear on the whitelist.
    Parameter "theAddressAsString" - The address in question as a string
    Return value - if the address passes the tests then it is returned, otherwise None.
    """
    theAddressAsString = self.cleanIP(theAddressAsString)    # Remove invalid address matches
    if theAddressAsString is not None:
      theAddressAsObj = IPAddress(theAddressAsString)      # Convert to IPAddress object
      if theAddressAsObj is not None:
        theAddressAsObj = self.checkIPWhiteList(theAddressAsObj) # Check against whitelist
        if theAddressAsObj is not None:
          return theAddressAsObj.addressAsString         # Convert back to String
    return None                          # The address was filtered out

  def processAttachments(self):
    """ A method to process the email attachments, if present. Each non-inline email attachment is added as an
    attachment to the incident, and its name is added as an artifact. Inline attachments are assumed to be unimportant.
    No return value.
    """
    for attachment in emailmessage.attachments:
      if not attachment.inline:
        incident.addEmailAttachment(attachment.id)
        incident.addArtifact("Email Attachment Name", attachment.suggested_filename, "")

  def addBasicInfoToIncident(self):
    """A method to perform basic information extraction from the email message.
    The email message sender address, including personal name if present, is set as the reporter field
    in the incident. An artifact is created from the email message subject with the type "Email Subject".
    No return value.
    """
    newReporterInfo = emailmessage.from.address
    if emailmessage.from.name is not None:
      newReporterInfo = u"{0} <{1}>".format(emailmessage.from.name, emailmessage.from.address)
      log.info(u"Adding reporter field \"{0}\"".format(newReporterInfo))
      incident.reporter = newReporterInfo

      if emailmessage.subject is not None:
        self.addUniqueArtifact(u"{0}".format(emailmessage.subject), "Email Subject", "Suspicious email subject")

###
# Mainline starts here
###

# Create the email processor object, loading it with the email message body content.
processor = EmailProcessor()

# Create a suitable title for an incident based on the email
newIncidentTitle = u"Incident generated from email \"{0}\" via mailbox {1}".format(emailmessage.subject, emailmessage.inbound_mailbox)

# Check to see if a similar incident already exists
# We will search for an incident which has the same name as we would give a new incident
query_builder.equals(fields.incident.name, newIncidentTitle)
query_builder.equals(fields.incident.plan_status, "Active")
query = query_builder.build()
incidents = helper.findIncidents(query)

if len(incidents) == 0:
  # A similar incident does not already exist. Create a new incident and associate the email with it.
  log.info(u"Creating new incident {0}".format(newIncidentTitle))

  # Create an incident with a title based on the email subject, owned identified by variable newIncidentOwner
  emailmessage.createAssociatedIncident(newIncidentTitle, newIncidentOwner)

  # Add the subject to the incident as an artifact, and set the incident reporter.
  # This does not need to be done for an existing incident.
  processor.addBasicInfoToIncident()

else:
  # A similar incident already exists. Associate the email with this preexisting incident.
  log.info(u"Associating with existing incident {0}".format(incidents[0].id))
  emailmessage.associateWithIncident(incidents[0])

# Capture any URLs present in the email body text and add them as artifacts
processor.processArtifactCategory(processor.makeUrlPattern(), "URL", "Suspicious URL", processor.fixURL, processor.checkDomainWhiteList)

# Capture any IPv4 addresses present in the email body text and add them as artifacts
processor.processArtifactCategory(processor.makeIPv4Pattern(), "IP Address", "Suspicious IP Address", processor.processIPFully)

# Capture any IPv6 addresses present in the email body text and add them as artifacts
processor.processArtifactCategory(processor.makeIPv6Pattern(), "IP Address", "Suspicious IP Address", processor.processIPFully)

# Capture 32-character hexadecimal substrings in the email body text and add them as MD5 hash artifacts
processor.processArtifactCategory(processor.makeHexPattern(32), "Malware MD5 Hash", "MD5 hash of potential malware file")

# Capture 40-character hexadecimal substrings in the email body text and add them as SHA-1 hash artifacts
processor.processArtifactCategory(processor.makeHexPattern(40), "Malware SHA-1 Hash", "SHA-1 hash of potential malware file")

# Capture 64-character hexadecimal substrings in the email body text and add them as SHA-256 hash artifacts
processor.processArtifactCategory(processor.makeHexPattern(64), "Malware SHA-256 Hash", "SHA-256 hash of potential malware file")

# Add email message attachments to incident
processor.processAttachments()