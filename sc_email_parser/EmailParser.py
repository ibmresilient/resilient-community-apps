import re

# A script to create an incident from an email message, and add artifacts to the incident based on information
# present in the body text of the message.

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
  asString = ""

  def __init__(self, elementAsString):
    """ The constructor that takes one parameter - the textual representation of the element. """
    self.asString = elementAsString

  def __str__(self):
    """Method to return the text representation of the object."""
    return self.asString

  def __repr__(self):
    """Method to return the text representation of the object."""
    return self.asString

  def test(self, other):
    """ A function intended to be inherited but overrided by subclasses. It should return True if the "other" object
    would be matched by this white list element.
    """
    return False


class IPAddress:
  """ A class for IP addresses, both IPv4 and IPv6. """

  # The IP address as a String, as originally presented to the constructor
  addressAsString=""

  # The IP Address as a binary representation
  addressAsBinary=0

  def __init__(self, newAddressAsString):
    """ The constructor, which takes one parameter - the string representation to be used to create the addressAsBinary. """
    self.addressAsString = newAddressAsString
    self.addressAsBinary = Utils.convertIPV4v6ToInt(self.addressAsString)

  def __str__(self):
    """Method to return the text representation of the object."""
    return self.addressAsString

  def __repr__(self):
    """Method to return the text representation of the object."""
    return self.addressAsString


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
    log.debug("Going to filter IPAddress {} against {}".format(anIPAddress, self))
    return (anIPAddress.addressAsBinary >> (self.width - self.cidrSuffix) == self.addressAsBinary >> (self.width - self.cidrSuffix))


class IPRange(WhiteListElement):
  """ A type of WhiteListElement that represents a range, from a lower bound to an upper bound, inclusive. """
  lowest = None
  highest = None
  
  def __init__(self, stringRepresentation):
    """ IPRange constructor that takes two parameters.
    Parameter 'lowestAsText' - the lowest IP address in the range.
    Parameter 'highestAsText' - the highest IP address in the range.
    """
    lowestAsText, highestAsText = stringRepresentation.split('-')
    super(IPRange, self).__init__(stringRepresentation)    
    self.lowest = IPAddress(lowestAsText)
    self.highest = IPAddress(highestAsText)

  def test(self, anIPAddress):
    """ A method that returns true if anIPAddress is not below self.lowest and not above self.highest. """
    return self.highest.addressAsBinary >= anIPAddress.addressAsBinary and self.lowest.addressAsBinary <= anIPAddress.addressAsBinary


class Domain(WhiteListElement):
  """ A type of WhiteListElement that represents a domain or domain pattern. E.G.
  *.ibm.com
  mailserver.knowngood.com
  """

  # A regular expression to match the domain. Domains of the form "*.customer.com" are converted to ".*.customer.com"
  processedRegEx = None
  
  def __init__(self, stringRepresentation):
    """ Constructor for the Domain class. This takes one parameter - the domain pattern as a String. """
    # Save the string representation in the superclass
    super(Domain, self).__init__(stringRepresentation)    
    self.processedRegEx = "://" + stringRepresentation.replace('.','\.').replace('*', ".*") + ".*"

  def test(self, urlString):
    """ A method that returns true if the value passed in urlString matches the regex in self.processedRegEx. """
    matches = re.findall(self.processedRegEx, urlString, re.IGNORECASE)
    return (matches != None) and (len(matches) > 0)


class EmailProcessor(object):
  """ A class that facilitates processing the body contents of an email message.
  Once the EmailProcessor class has been instanciated, the other methods can be used to add artifacts to the 
  incident.
  """

  # The body text of the email
  bodyText = ""

  # The set of already-added artifacts. If an artifact is in the set then it will not be added to the incident
  # a second time.
  addedArtifacts = set()

  # Standard Whitelist for IP addresses
  ipV4WhiteList = [
    CIDR('192.168.0.0/16'),               #   Class B private network local communication (RFC 1918)
    CIDR('198.18.0.0/15'),                #  Testing of inter-network communications between subnets (RFC 2544)
    IPRange('239.0.0.0-239.255.255.255'), #   Administrative Multicast
    CIDR('169.254.0.0/16'),
    CIDR('224.0.0.0/4'),
    CIDR('192.88.99.0/24'),               #   6to4 anycast relays (RFC 3068)
    CIDR('0.0.0.0/8'),                    #   Broadcast message (RFC 1700)
    CIDR('192.0.2.0/24'),                 #   TEST-NET examples and documentation (RFC 5737)
    CIDR('240.0.0.0/4'),                  #   Reserved for  multicast assignments (RFC 5771)
    CIDR('198.51.100.0/24'),              #   TEST-NET-2 examples and documentation (RFC 5737)
    CIDR('203.0.113.0/24'),               #   TEST-NET-3 examples and documentation (RFC 5737)
    CIDR('233.252.0.0/24'),               #   Multicast test network
    IPRange('234.0.0.0-238.255.255.255'),
    IPRange('225.0.0.0-231.255.255.255'),
    CIDR('127.0.0.1')
  ]

  ipV6WhiteList = [
    CIDR('fc00::/7'),                     #   Unique Local Addresses (ULA)
    CIDR('fec0::/10'),                    #   Site Local Addresses (deprecated - RFC 3879)
    CIDR('fe80::/10'),
    CIDR('ff00::/8'),
    CIDR('ff00::/12'),
    CIDR('::/8'),
    CIDR('0100::/8'),
    CIDR('0200::/7'),
    CIDR('0400::/6'),
    CIDR('0800::/5'),
    CIDR('1000::/4'),
    CIDR('4000::/3'),
    CIDR('6000::/3'),
    CIDR('8000::/3'),
    CIDR('A000::/3'),
    CIDR('C000::/3'),
    CIDR('E000::/4'),
    CIDR('F000::/5'),
    CIDR('F800::/6'),
    CIDR('FE00::/9')    
  ]

  # Customer-specific IP address whitelists
  # Add entries to these lists to whitelist the entries without disrupting the standard set above
  customIPv4WhiteList = []
  customIPv6WhiteList = []

  # Standard domain whitelist
  domainWhiteList=[Domain("*.ibm.com")]

  # Customer-specific domain whitelist
  customDomainWhiteList=[]

  def __init__(self, newBodyText):
    """The EmailProcessor constructor.
    It takes as its only parameter the body text of email message, expected to be a string.
    """
    self.bodyText = newBodyText
    self.ipV4WhiteList.extend(self.customIPv4WhiteList)
    self.ipV6WhiteList.extend(self.customIPv6WhiteList)
    self.domainWhiteList.extend(self.customDomainWhiteList)


  def addUniqueArtifact(self, theArtifact, artifactType, description):
    """This method adds a new unique artifact to the incident. Previously added artifacts are added to the 
    'addedArtifacts' set. If the new artifact as already been added to the list then it is not added to the 
    incident a second time.
    Parameter theArtifact - the value of the artifact to create
    Parameter artifactType - the type of the artifact
    Parameter description - the description of the artifact
    No return value.
    """
    if (theArtifact, artifactType) in self.addedArtifacts:
      pass
      log.debug(u"Skipping previously added artifact {0} of type {1}, description {2}".format(theArtifact, artifactType, description))
    else:
      log.info(u"Adding artifact {0} of type {1}, description {2}".format(theArtifact, artifactType, description))
      incident.addArtifact(artifactType, theArtifact, description)
      self.addedArtifacts.add((theArtifact, artifactType))

  def addRecipient(self, recipient):
    """A method to add the email address of the recipient of the email message to the incident as an artifact.
    If the recipient has a name as well as an address, the name is added as part of the artifact.
    Parameter 'recipient' - an object with a String 'address' and 'name' attribute.
    No return value.
    """
    fullData = recipient.address
    if recipient.name:
      fullData = recipient.name + " <" + recipient.address + ">"
    log.debug("Adding recipient " + fullData)
    self.addUniqueArtifact(fullData, "Email Recipient", "Suspicious email recipient")        


  def printList(self, name, list):
    """A convenience method to log the contents of a list. The method will log each element in a list, along with
    its name and ordinal in the list.
    Parameter 'name' - the name of the elements in the list e.g. "IP Address".
    Parameter 'list' - the list to iterate through.
    No return value.
    """
    for num, value in enumerate(list):
      log.debug("{0} {1} {2}".format(name, num, value))  

  @staticmethod
  def makeUrlPattern(scheme = "http"):
    """A method to return a regex pattern that includes a full URL including scheme, domain, path, hash and 
    query string. It starts the match from the scheme name with optional "s", followed by "://" and continues until
    it finds a character that is not permitted in a URL. Because of the expectation that potentially harmful URLs
    are being modified for safety, the URL-invalid characters '[' and ']' will not terminate the match.
    Parameter 'scheme' - the scheme (protocol) of the URL, defaults to "http".
    Returns the requested pattern as a string.
    """
    return scheme + "s?://[^^|~`\\s<>\"'{}]*"

  @staticmethod
  def fixURL(theURL):
    """Method to fix a list of bowdlerized URLs. Many systems attempts to make potentially dangerous URLs into
    unopenable but human-readible strings. Resilient will reject URL artifacts that do not conform to spec.
    In this case we are converting "www[.]dangerous[.]nasty" to "www.dangerous.nasty".
    Parameter 'list' - the list of URLs to fix.
    Returns a new list containing fixed versions of the original list.
    """
    return re.sub(r"\[\.\]",".",theURL)

  @staticmethod
  def makeIPv4Pattern():
    """A method to return a pattern that matches valid IPv4 addresses.
    Returns a string containing a pattern that matches 4 instances of 1-3 decimal digits, separated by '.'.
    """
    return "(?:[\d]{1,3}\.){3}[\d]{1,3}"

  @staticmethod
  def cleanIPv4(anAddress):
    """A method to filter out impossible IP4 addresses from a list of strings that have been matched by the pattern
    from makeIPv4Pattern(). 
    First each address is split into its component octets. If the maximum int value of an octet in an address is
    less than 256 then the address is valid. The return value is a set, to avoid unnecessary duplication.
    Parameter 'addressList' - the list of addresses to filter.
    Returns a new set of valid addresses.
    """
    octets = anAddress.split(".")
    if (len(octets) != 4) or max(map(int, octets)) > 255:
      return None
    else:
      return anAddress

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
    cleanIPv4() on the IPv4 section. If the address is IPv6 the method will reject strings with more than 7 ':"s or
    more than one instance of '::'. If there is no '::" then there must be 7 ':'s.
    """
    log.debug("Going to clean IP address " + anAddress)
    hextets = anAddress.split(":")
    # It might be a V4 IP address in a V6 envelope
    if "." in hextets[-1]:
      return EmailProcessor.cleanIPv4(hextets[-1])
    # At most 7 ":"
    if anAddress.count(':') < 8:
      # At most one instance of "::"
      if anAddress.count('::') < 2:
        if anAddress.count('::') == 1 or anAddress.count(':') == 7:
            return anAddress
    return None


  @staticmethod
  def makeHexPattern(length):
    """A method that returns a regex pattern that matches a case-insensitive hexidecimal number of exactly a specified
    length.
    Parameter 'length' - the length of the pattern in digits/characters/nibbles
    Returns the corresponding pattern.
    """
    return "[^0-9a-zA-Z]([0-9a-fA-F]{" + str(length) + "})[^0-9a-zA-Z]"


  def processArtifactCategory(self, regex, artifactType, description, *optionalListModifierFn):
    """A method to process a category of artifact, based on a regular expression. Each match of the regex in the
    bodyText is added as an artifact of the same type and description. The optional list modifier function, if present,
    is run against the list of matches before the artifact addition takes place.
    Parameter 'regex' - the regular expression to use to pick out the text to interpret as an artifact
    Parameter 'artifactType' - the type of the artifact
    Parameter 'description' - the description of the artifact
    Parameter 'optionalListModifierFn' - a function to run across the list of matches to filter inappropriate values
    No return value.
    """
    dataList = set(re.findall(regex, self.bodyText))
    if dataList is not None and len(dataList) > 0 :
      if optionalListModifierFn is not None:
        for aFunction in optionalListModifierFn:
          dataList = map(aFunction, dataList)
          dataList = [x for x in dataList if x is not None]

      self.printList("Found " + artifactType + " (" + description + ")", dataList)
      map(lambda theArtifact: self.addUniqueArtifact(theArtifact, artifactType, description), dataList)
    else:
      log.debug("Could not find artifact " + artifactType + " for regex " + regex)


  def checkIsItemNotOnWhiteList(self, anItem, whiteList):
    """ A method that checks if an IP Address should be removed from the artifact list because if matches a whitelist element.
    Parameter 'anItem' - the item in question.
    Return value: True if the item should be kept, false if it should be removed.
    """
    for whiteListEntry in whiteList:
      if whiteListEntry.test(anItem):
        log.info("Filtering out IP Address {} because it matched with whitelist entry {}".format(anItem, whiteListEntry))
        return None
    return anItem


  def checkIPWhiteList(self, anAddress):
    """ A method to check a list of IP Addresses aginst the whitelist. """
    whiteList = self.ipV4WhiteList if "." in anAddress.addressAsString else self.ipV6WhiteList
    log.debug("Going to filter {} against whitelist ".format(anAddress, whiteList))
    return self.checkIsItemNotOnWhiteList(anAddress, whiteList)


  def checkDomainWhiteList(self, aURL):
    """ A method to check a list of URLs aginst a whitelist. """
    log.debug("Going to filter {} against whitelist ".format(aURL, self.domainWhiteList))
    return self.checkIsItemNotOnWhiteList(aURL,self.domainWhiteList)


  def processIPFully(self, theAddressAsString):
    """ A method to filter inadvertantly matched IP strings and then filter out IP addresses that appear on the whitelist.
    Parameter "theAddressAsString" - The address in question as a string 
    Return value - if the address passes the tests then it is returned, otherwise None.
    """
    theAddressAsString = self.cleanIP(theAddressAsString)        # Remove invalid address matches
    if theAddressAsString is not None:
      theAddressAsObj = IPAddress(theAddressAsString)            # Convert to IPAddress object
      if theAddressAsObj is not None:
        theAddressAsObj = self.checkIPWhiteList(theAddressAsObj) # Check against whitelist
        if theAddressAsObj is not None:
          return theAddressAsObj.addressAsString                 # Convert back to String
    return None                                                  # The address was filtered out


  def addBasicInfoToIncident(self):
    """A method to perform basic artifact extraction on the email message.
    The artifacts concerned are the 'Email Sender', 'Email Sender Name', and the subject.
    No return value.
    """ 
    log.debug("Adding sender {0} {1}".format(emailmessage.from.address, emailmessage.from.name))
    if emailmessage.from.address is None:
      incident.reporter = mailmessage.from.address
    else:
      incident.reporter = "{0} <{1}>".format(emailmessage.from.name, emailmessage.from.address)
    self.addUniqueArtifact(u'{}'.format(emailmessage.subject), "Email Subject", "Suspicious email subject")

###
# Mainline starts here
###

# Create an incident with a title based on the email subject, owned by user admin@co3sys.com
newIncidentTitle = u"Incident generated from email \"{}\" via mailbox {}".format(emailmessage.subject, emailmessage.inbound_mailbox)
emailmessage.createAssociatedIncident(newIncidentTitle, "admin@co3sys.com")

# Create the email processor object, loading it with the email message body content.
processor = EmailProcessor(emailmessage.body.content)

# Add the 'Email Sender', 'Email Sender Name', and the subject to the incident as artifacts.
processor.addBasicInfoToIncident()

# Capture any URLs present in the email body text and add them as artifacts
processor.processArtifactCategory(processor.makeUrlPattern(), "URL", "Suspicious URL", processor.fixURL, processor.checkDomainWhiteList)

# Capture any IPv4 addresses present in the email body text and add them as artifacts
processor.processArtifactCategory(processor.makeIPv4Pattern(), "IP Address", "Suspicious IP Address", processor.processIPFully)

# Capture any IPv6 addresses present in the email body text and add them as artifacts
processor.processArtifactCategory(processor.makeIPv6Pattern(), "IP Address", "Suspicious IP Address", processor.processIPFully)

# Capture 32-nibble hexidecimal substrings in the email body text and add them as MD5 hash artifacts
processor.processArtifactCategory(processor.makeHexPattern(32), "Malware MD5 Hash", "MD5 hash of potential malware file")

# Capture 40-nibble hexidecimal substrings in the email body text and add them as SHA-1 hash artifacts
processor.processArtifactCategory(processor.makeHexPattern(40), "Malware SHA-1 Hash", "SHA-1 hash of potential malware file")

# Capture 64-nibble hexidecimal substrings in the email body text and add them as SHA-256 hash artifacts
processor.processArtifactCategory(processor.makeHexPattern(64), "Malware SHA-256 Hash", "SHA-256 hash of potential malware file")
