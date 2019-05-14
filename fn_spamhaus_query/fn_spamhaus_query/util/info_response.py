# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""
The following is the full list of responses for the info API.
To avoid added queries that would increase latency we imbedding these responses in codebase.
and relying on an API call only in case of unknown error codes.
"""
STATIC_INFO_RESPONSE = {
    1002: {
        "dataset": "SBL",
        "explanation": "IP addresses are listed on the SBL because they appear to Spamhaus to be under the control of, used by, or made available for use by spammers and abusers in unsolicited bulk email or other types of Internet-based abuse that threatens networks or users.",
        "URL": "https://www.spamhaus.org/sbl/"
    },
    1003: {
        "dataset": "CSS",
        "explanation": "IP addresses that are involved in sending low-reputation email. CSS mostly targets static spam emitters that are not covered in the PBL or XBL, such as snowshoe spam operations, but may also include other senders that display a risk to our users, such as compromised hosts.",
        "URL": "https://www.spamhaus.org/css/"
    },
    1004: {
        "dataset": "CBL",
        "explanation": "One of the components of XBL, constituted by IP addresses of exploited systems. This includes machines operating open proxies, systems infected with trojans, and other malware vectors.",
        "URL": "https://www.abuseat.org/"
    },
    1009: {
        "dataset": "DROP",
        "explanation": "IP part of a netblock that is ‘hijacked’ or leased by professional spam or cyber-crime operations and therefore used for dissemination of malware, trojan downloaders, botnet controllers, etc.",
        "URL": "https://www.spamhaus.org/drop/"
    },
    1010: {
        "dataset": "PBL",
        "explanation": "IP address ranges which should not -according to the ISP controlling them- be delivering unauthenticated SMTP email to any Internet mail server except those provided for specifically by an ISP for that customer's use.",
        "URL": "https://www.spamhaus.org/pbl/"
    },
    1011: {
        "dataset": "PBL",
        "explanation": "IP address ranges which -according to Spamhaus’s systems assessment- are not expected be delivering unauthenticated SMTP email to any Internet mail server, such as dynamic and residential IP space.",
        "URL": "https://www.spamhaus.org/pbl/"
    },
    1020: {
        "dataset": "AuthBL",
        "explanation": "IP address is known to be performing authentication bruteforce activities or to be infected by a trojan engaging in such operations and/or using stolen credentials to access legitimate resources.",
        "URL": "https://www.spamhaus.org/???/"
    },
    2002: {
        "dataset": "DBL",
        "explanation": "The resource is or belongs to a domain name with poor reputation.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    2004: {
        "dataset": "DBL",
        "explanation": "The resource is or belongs to a domain known to be involved in phishing activities.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    2005: {
        "dataset": "DBL",
        "explanation": "The resource is or belongs to a domain known to be involved in the distribution of malware or otherwise malware-related activities.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    2006: {
        "dataset": "DBL",
        "explanation": "The resource is or belongs to a domain known to be used to command and control botnet resources.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    2102: {
        "dataset": "DBL",
        "explanation": "The resource is or belongs to a domain that -while legit- is being abused for spam or other nefarious activities, usually as a result of security issues of some sort.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    2103: {
        "dataset": "DBL",
        "explanation": "The resource is known to be or host an URL shortener that is being used for spam campaigns or other nefarious activities.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    2104: {
        "dataset": "DBL",
        "explanation": "The resource is or belongs to a domain that -while legit- is being abused for phishing purposes, usually as a result of security issues of some sort.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    2105: {
        "dataset": "DBL",
        "explanation": "The resource is or belongs to a domain that -while legit- is being abused for malware-propagation or other malware-related purposes, usually as a result of security issues of some sort.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    2106: {
        "dataset": "DBL",
        "explanation": "The resource is or belongs to a domain that -while legit- is being abused to host or operate a botnet command and control node, usually as a result of security issues of some sort.",
        "URL": "https://www.spamhaus.org/dbl/"
    },
    3002: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 0 and 2 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3003: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 2 and 3 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3004: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 3 and 4 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3005: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 4 and 5 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3006: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 5 and 6 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3007: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 6 and 7 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3008: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 7 and 8 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3009: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 8 and 9 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3010: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 9 and 10 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3011: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 10 and 11 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3012: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 11 and 12 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3013: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 12 and 13 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3014: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 13 and 14 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3015: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 14 and 15 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3016: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 15 and 16 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3017: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 16 and 17 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3018: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 17 and 18 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3019: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 18 and 19 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3020: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 19 and 20 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3021: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 20 and 21 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3022: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 21 and 22 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3023: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 22 and 23 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
    3024: {
        "dataset": "ZRD",
        "explanation": " This domain was first observed between 23 and 24 hours ago.",
        "URL": "https://www.spamhaus.org/zrd/"
    },
}
