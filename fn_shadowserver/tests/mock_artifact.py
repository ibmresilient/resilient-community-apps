class MockedResponse:
    def __init__(self):
        self.success = True
        self.status_code = 200
        self.text = 'mock text'
    def json(self):
        mock_successful_result = {
            "content": [
                {
                "adobe_malware_classifier": "malicious",
                "anti_virus": [
                    {
                    "signature": "Troj/Agent-APCU",
                    "vendor": "Sophos"
                    },
                    {
                    "signature": "W32/Lamer.CQ",
                    "vendor": "Fortinet"
                    },
                    {
                    "signature": "PUA.Win.Packer.Purebasic-2",
                    "vendor": "Clam"
                    },
                    {
                    "signature": "Win32.Generic.VC",
                    "vendor": "AVG"
                    },
                    {
                    "signature": "Gen:Win32.FileInfector.uwZ@a4T!Kcmi",
                    "vendor": "MicroWorld"
                    },
                    {
                    "signature": "Virus ( 004d554e1 )",
                    "vendor": "K7GW"
                    },
                    {
                    "signature": "W32.Sivis.A5",
                    "vendor": "QuickHeal"
                    },
                    {
                    "signature": "Trojan/Win32.FileInfector",
                    "vendor": "AhnLab"
                    },
                    {
                    "signature": "Win32:Malware-gen",
                    "vendor": "Avast"
                    },
                    {
                    "signature": "Trojan.PWS.Onlinegames.KEGA",
                    "vendor": "BitDefender"
                    },
                    {
                    "signature": "Trojan.GenericKD.40542465",
                    "vendor": "BitDefender"
                    },
                    {
                    "signature": "Gen.Win32.FileInfector",
                    "vendor": "Ikarus"
                    },
                    {
                    "signature": "Virus.Win32.sivis.a",
                    "vendor": "Sunbelt"
                    },
                    {
                    "signature": "Gen:Win32.FileInfector.uwZ@a4T!Kcmi",
                    "vendor": "BitDefender"
                    },
                    {
                    "signature": "PUA.Win.Packer.Purebasic-2",
                    "vendor": "Clam"
                    },
                    {
                    "signature": "Gen:Win32.Backdoor.ozZbauKWKdpb",
                    "vendor": "BitDefender"
                    },
                    {
                    "signature": "Win32.Generic.VC",
                    "vendor": "AVG"
                    },
                    {
                    "signature": "Virus ( 004d554e1 )",
                    "vendor": "K7GW"
                    },
                    {
                    "signature": "Win32.HLLW.Siggen.4657",
                    "vendor": "DrWeb"
                    },
                    {
                    "signature": "TR/Dropper.Gen8",
                    "vendor": "Avira"
                    },
                    {
                    "signature": "Win32/Zatoxp.C",
                    "vendor": "Eset"
                    },
                    {
                    "signature": "Win32:Malware-gen",
                    "vendor": "Avast"
                    },
                    {
                    "signature": "Virus ( 004d554e1 )",
                    "vendor": "K7"
                    },
                    {
                    "signature": "Trojan/Win32.FileInfector",
                    "vendor": "AhnLab"
                    },
                    {
                    "signature": "Win32:Lamer-A",
                    "vendor": "Avast"
                    },
                    {
                    "signature": "Gen:Win32.FileInfector.uwZ@a4T!Kcmi",
                    "vendor": "BitDefender"
                }],
            "entropic": "5.952427",
            "filesize": "2438340",
            "first_seen": "2016-08-25 02:44:39",
            "import_hash": "33f98db5bdb6a7013d52f0120248df35",
            "last_seen": "2016-08-25 02:44:39",
            "magic": "PE32 executable (GUI) Intel 80386, for MS Windows",
            "md5": "dfe1832e02888422f48d6896dc8e8f73",
            "pehash": "243c35935ecc9829f30b30c45839cbf6",
            "sha1": "c56ba498d41caa7be3c1eb5588cec27c413eb208",
            "sha256": "d8d395f8744335fba53b0a4308e7b380a0aca86bfc8939ded9f4c8c5cb1e838a",
            "sha512": "7ca1fdfe537913b8854227efc1f11b00d405f2d21e416e7023c4ebed2bfa887d2bc4d4d553ce41667c99def47ea05e6ce4a773c4ee7173927f1d263e724c16c2",
            "timestamp": "2016-08-25 02:44:39",
            "tlsh": "c1b52a5273fa0254f2f35f75a8b7a3944939fea11d22e08e1164314d88b6f808e75bb7",
            "type": "exe"
            }
                ],
            "inputs": {
                "shadowserver_artifact_type": "Malware SHA-1 Hash",
                "shadowserver_artifact_value": "c56ba498d41caa7be3c1eb5588cec27c413eb208"
            },
            "metrics": {
                "execution_time_ms": 386,
                "host": "My Host",
                "package": "fn-shadowserver",
                "package_version": "1.0.0",
                "timestamp": "2022-03-30 11:34:35",
                "version": "1.0"
            },
            "raw": None,
            "reason": None,
            "success": True,
            "version": 2.0
            }
        return mock_successful_result