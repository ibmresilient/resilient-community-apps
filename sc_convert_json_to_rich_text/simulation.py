def globals():
    return ['playbook']

class Incident():
    def addNote(self, value):
        print(value)

class Helper():
    def fail(err):
        print(err)
    def createRichText(self, value):
        return value

class Workflow():
    def __init__(self):
        self.properties = {}

    def addProperty(self, property, property_dict):
        self.properties[property] = property_dict

class Results():
    def __init__(self):
        self.results = {}

class Playbook():
    def __init__(self):
        self.functions = Results()

    def addProperty(self, property, property_dict):
        self.functions.results[property] = property_dict
    
workflow = Workflow()
playbook = Playbook()
helper = Helper()
incident = Incident()

data = {
    u'backingObject': {
    u'elapsed': 1906,
    u'stdout': u'traceroute to www.yahoo.fr (212.82.100.150), 15 hops max, 60 byte packets\n 1 _gateway (10.42.0.1) 0.053 ms 0.036 ms 0.018 ms\n 2 169.254.166.186 (169.254.166.186) 1.050 ms 1.286 ms 1.000 ms\n 3 a2.76.b09e.ip4.static.sl-reverse.com (158.176.118.162) 1.315 ms 1.611 ms a0.76.b09e.ip4.static.sl-reverse.com (158.176.118.160) 1.123 ms\n 4 8a.76.b09e.ip4.static.sl-reverse.com (158.176.118.138) 1.387 ms 1.326 ms 8e.76.b09e.ip4.static.sl-reverse.com (158.176.118.142) 1.256 ms\n 5 ae17.cbs02.tg01.lon01.networklayer.com (169.45.19.72) 3.384 ms ae16.cbs02.tg01.lon01.networklayer.com (169.45.19.70) 3.194 ms ae17.cbs02.tg01.lon01.networklayer.com (169.45.19.72) 3.162 ms\n 6 d.12.2da9.ip4.static.sl-reverse.com (169.45.18.13) 1.425 ms 1.559 ms 1.479 ms\n 7 ge-1-1-0.pat1.the.yahoo.com (195.66.224.129) 3.690 ms 3.134 ms ae2.pat1.loz.yahoo.com (195.66.224.115) 1.735 ms\n 8 ae-6.pat2.iry.yahoo.com (209.191.112.72) 12.696 ms 12.675 ms 12.596 ms\n 9 unknown.yahoo.com (209.191.112.133) 11.562 ms unknown.yahoo.com (66.196.65.25) 10.369 ms et-1-1-2.msr1.ir2.yahoo.com (66.196.65.19) 13.357 ms\n10 lo0.fab2-1-gdc.ir2.yahoo.com (77.238.190.3) 10.888 ms 10.849 ms 12.322 ms\n11 usw1-1-lba.ir2.yahoo.com (77.238.190.102) 12.993 ms 12.955 ms 11.786 ms\n12 w2.src.vip.ir2.yahoo.com (212.82.100.150) 11.422 ms 10.341 ms 10.345 ms\n',
    u'stderr_json': None,
    u'stdout_json': None,
    u'start': 1658325973337,
    u'end': 1658325975244,
    u'exitcode': 0,
    u'stderr': u'',
    u'commandline': u'traceroute -m 15 "www.yahoo.fr"'
  }
}

playbook.addProperty('convert_json_to_rich_text', {
    "version": 1.1,
    "header": "Artifact scan results for: xx",
    "padding": 10,
    "separator": u"<br />",
    "sort": True,
    "json": data,
    "json_omit_list": ["omit"],
    "incident_field": None
})
