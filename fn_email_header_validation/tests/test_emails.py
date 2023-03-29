# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

def arc_only():
    return """Delivered-To: machkeenan@gmail.com
Received: by 2002:a17:90a:4d4d:0:0:0:0 with SMTP id l13-v6csp1057618pjh;
        Fri, 31 Aug 2018 10:35:27 -0700 (PDT)
X-Google-Smtp-Source: ANB0VdatpeYlSpQQPc6FwT0N23IbVEY8UC206+lLCD+kRQNGbv/Phzy2EEI7wRHul9jsRoSqXGAq
X-Received: by 2002:aca:3a03:: with SMTP id h3-v6mr7992109oia.270.1535736927372;
        Fri, 31 Aug 2018 10:35:27 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1535736927; cv=none;
        d=google.com; s=arc-20160816;
        b=LOrY4I09VSL0I6LUVm87+jvHrL/l4nr8GFWhiVeQXa5ygwzpwdaIZbRQzbadmqYK18
         +bspNBJPqYUXgbGltpBmynfJjSXFh15rZHraawSNMoarZ+OigHNEu0o01arQPV7NgR5E
         0BCLTYNN6usDwch16y9u1QsPVGclh8ftfZLNnpcfrP1VHMCW+381BMp59+RX4eAz/JVF
         37vVVXrYj9Raksc4c10VyhfJYyu2W9yzd60H4Rz7WUDFmlULnIFXTL5WuLRRnnZsdC6m
         XqCvwBAjD2xJPseD80X2+jTqErw9j0G+ioGbwY3QEb5NUEylSfWOE3UaeM2zLsKsfRCo
         Z3ng==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=content-transfer-encoding:message-id:importance:mime-version
         :references:sensitivity:date:to:from:subject:in-reply-to
         :arc-authentication-results;
        bh=5YySYNw9ydRNjDt8QJhexWl+70J4DHQoSgktGVHm/3U=;
        b=GmoZuUqh/rbYkffUVo+opqYnf2gzbqahHCmrDMlUniwmKJLvwwP1QEz3BtV/8sgMKd
         5CrvnFbV9gJodkVQBTr1gphgAV8huJ4V3CLnjfNWDXarKy05F74qjSxi2bR+iveKIKJ7
         M/4ECumtUMUDaRoZd3k01PzIHQOmhFRlWiXWjoUQt4Qwpo/1/Qqe0XNJntDSIPKnCE81
         J9d7mnJDhoGgCFITJ6+UXnCvDICSZ30K2SECDKc3x4kJC2ME+I778rh3ZozsfVAknxK4
         Lw11KgI1npFfHYQexydYljrgVMcW/yzeu3989uq0WF3XhG285bpHy+tFsTn4VrmkVOMy
         DC2w==
ARC-Authentication-Results: i=1; mx.google.com;
       spf=pass (google.com: domain of keenan.mach@ibm.com designates 148.163.156.1 as permitted sender) smtp.mailfrom=Keenan.Mach@ibm.com;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=ibm.com
Return-Path: <Keenan.Mach@ibm.com>
Received: from mx0a-001b2d01.pphosted.com (mx0a-001b2d01.pphosted.com. [148.163.156.1])
        by mx.google.com with ESMTPS id q66-v6si7532150oig.194.2018.08.31.10.35.27
        for <machkeenan@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Fri, 31 Aug 2018 10:35:27 -0700 (PDT)
Received-SPF: pass (google.com: domain of keenan.mach@ibm.com designates 148.163.156.1 as permitted sender) client-ip=148.163.156.1;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of keenan.mach@ibm.com designates 148.163.156.1 as permitted sender) smtp.mailfrom=Keenan.Mach@ibm.com;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=ibm.com
Received: from pps.filterd (m0098393.ppops.net [127.0.0.1])
	by mx0a-001b2d01.pphosted.com (8.16.0.22/8.16.0.22) with SMTP id w7VHStGV014018
	for <machkeenan@gmail.com>; Fri, 31 Aug 2018 13:35:26 -0400
Received: from smtp.notes.na.collabserv.com (smtp.notes.na.collabserv.com [158.85.210.103])
	by mx0a-001b2d01.pphosted.com with ESMTP id 2m79v7rte0-1
	(version=TLSv1.2 cipher=ECDHE-RSA-AES256-GCM-SHA384 bits=256 verify=NOT)
	for <machkeenan@gmail.com>; Fri, 31 Aug 2018 13:35:26 -0400
Received: from localhost
	by smtp.notes.na.collabserv.com with smtp.notes.na.collabserv.com ESMTP
	for <machkeenan@gmail.com> from <Keenan.Mach@ibm.com>;
	Fri, 31 Aug 2018 17:35:26 -0000
Received: from us1b3-smtp03.a3dr.sjc01.isc4sb.com (10.122.7.173)
	by smtp.notes.na.collabserv.com (10.122.47.39) with smtp.notes.na.collabserv.com ESMTP;
	Fri, 31 Aug 2018 17:35:24 -0000
Received: from us1b3-mail221.a3dr.sjc03.isc4sb.com ([10.168.214.88])
          by us1b3-smtp03.a3dr.sjc01.isc4sb.com
          with ESMTP id 2018083117352416-1938285 ;
          Fri, 31 Aug 2018 17:35:24 +0000 
In-Reply-To: 
Subject: dkim/arc test
From: "Keenan Mach" <Keenan.Mach@ibm.com>
To: machkeenan@gmail.com
Date: Fri, 31 Aug 2018 17:35:24 +0000
Sensitivity: 
References: 
MIME-Version: 1.0
Importance: Normal
X-Priority: 3 (Normal)
X-Mailer: IBM Verse Build 16007-1287 | IBM Domino Build SCN1812108_20180501T0841 May
 01, 2018 at 08:41
X-KeepSent: 5B2B6657:85174C89-002582FA:00609FF9;
 type=4; name=$KeepSent
X-LLNOutbound: False
X-Disclaimed: 57799
X-TNEFEvaluated: 1
X-LLNXfer: False
x-cbid: 18083117-6371-0000-0000-00000411D7A2
X-IBM-SpamModules-Scores: BY=0; FL=0; FP=0; FZ=0; HX=0; KW=0; PH=0;
 SC=0.413459; ST=0; TS=0; UL=0; ISC=; MB=0.000000
X-IBM-SpamModules-Versions: BY=3.00009645; HX=3.00000242; KW=3.00000007;
 PH=3.00000004; SC=3.00000266; SDB=6.01081601; UDB=6.00558013; IPR=6.00861586;
 BA=6.00006088; NDR=6.00000001; ZLA=6.00000005; ZF=6.00000009; ZB=6.00000000;
 ZP=6.00000000; ZH=6.00000000; ZU=6.00000002; MB=3.00023039; XFM=3.00000015;
 UTC=2018-08-31 17:35:25
X-IBM-AV-DETECTION: SAVI=unsuspicious REMOTE=unsuspicious XFE=unused
X-IBM-AV-VERSION: SAVI=2018-08-31 15:39:01 - 6.00008906
x-cbparentid: 18083117-6372-0000-0000-00004F93DB30
Message-Id: <OF5B2B6657.85174C89-ON002582FA.00609FF9-002582FA.00609FFC@notes.na.collabserv.com>
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable
X-Proofpoint-Virus-Version: vendor=fsecure engine=2.50.10434:,, definitions=2018-08-31_07:,,
 signatures=0
X-Proofpoint-Spam-Reason: safe

<div class=3D"socmaildefaultfont" dir=3D"ltr" style=3D"font-family:Arial, H=
elvetica, sans-serif;font-size:10.5pt" ><div dir=3D"ltr" >test</div></div><=
BR>

"""

def arc_only_fail():
    return """Delivered-To: machkeenan@gmail.com
Received: by 2002:a17:90a:4d4d:0:0:0:0 with SMTP id l13-v6csp1057618pjh;
        Fri, 31 Aug 2018 10:35:27 -0700 (PDT)
X-Google-Smtp-Source: ANB0VdatpeYlSpQQPc6FwT0N23IbVEY8UC206+lLCD+kRQNGbv/Phzy2EEI7wRHul9jsRoSqXGAq
X-Received: by 2002:aca:3a03:: with SMTP id h3-v6mr7992109oia.270.1535736927372;
        Fri, 31 Aug 2018 10:35:27 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1535736927; cv=none;
        d=google.com; s=arc-20160816;
        b=LOrY4I09VSL0I6LUVm87+jvHrL/l4nr8GFWhiVeQXa5ygwzpwdaIZbRQzbadmqYK18
         +bspNBJPqYUXgbGltpBmynfJjSXFh15rZHraawSNMoarZ+OigHNEu0o01arQPV7NgR5E
         0BCLTYNN6usDwch16y9u1QsPVGclh8ftfZLNnpcfrP1VHMCW+381BMp59+RX4eAz/JVF
         37vVVXrYj9Raksc4c10VyhfJYyu2W9yzd60H4Rz7WUDFmlULnIFXTL5WuLRRnnZsdC6m
         XqCvwBAjD2xJPseD80X2+jTqErw9j0G+ioGbwY3QEb5NUEylSfWOE3UaeM2zLsKsfRCo
         Z3ng==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=content-transfer-encoding:message-id:importance:mime-version
         :references:sensitivity:date:to:from:subject:in-reply-to
         :arc-authentication-results;
        bh=5YySYNw9ydRNjDt8QJhexWl+70J4DHQoSgktGVHm/3U=;
        b=GmoZuUqh/rbYkffUVo+opqYnf2gzbqahHCmrDMlUniwmKJLvwwP1QEz3BtV/8sgMKd
         5CrvnFbV9gJodkVQBTr1gphgAV8huJ4V3CLnjfNWDXarKy05F74qjSxi2bR+iveKIKJ7
         M/4ECumtUMUDaRoZd3k01PzIHQOmhFRlWiXWjoUQt4Qwpo/1/Qqe0XNJntDSIPKnCE81
         J9d7mnJDhoGgCFITJ6+UXnCvDICSZ30K2SECDKc3x4kJC2ME+I778rh3ZozsfVAknxK4
         Lw11KgI1npFfHYQexydYljrgVMcW/yzeu3989uq0WF3XhG285bpHy+tFsTn4VrmkVOMy
         DC2w==
ARC-Authentication-Results: i=1; mx.google.com;
       spf=pass (google.com: domain of keenan.mach@ibm.com designates 148.163.156.1 as permitted sender) smtp.mailfrom=Keenan.Mach@ibm.com;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=ibm.com
Return-Path: <Keenan.Mach@ibm.com>
Received: from mx0a-001b2d01.pphosted.com (mx0a-001b2d01.pphosted.com. [148.163.156.1])
        by mx.google.com with ESMTPS id q66-v6si7532150oig.194.2018.08.31.10.35.27
        for <machkeenan@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Fri, 31 Aug 2018 10:35:27 -0700 (PDT)
Received-SPF: pass (google.com: domain of keenan.mach@ibm.com designates 148.163.156.1 as permitted sender) client-ip=148.163.156.1;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of keenan.mach@ibm.com designates 148.163.156.1 as permitted sender) smtp.mailfrom=Keenan.Mach@ibm.com;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=ibm.com
Received: from pps.filterd (m0098393.ppops.net [127.0.0.1])
	by mx0a-001b2d01.pphosted.com (8.16.0.22/8.16.0.22) with SMTP id w7VHStGV014018
	for <machkeenan@gmail.com>; Fri, 31 Aug 2018 13:35:26 -0400
Received: from smtp.notes.na.collabserv.com (smtp.notes.na.collabserv.com [158.85.210.103])
	by mx0a-001b2d01.pphosted.com with ESMTP id 2m79v7rte0-1
	(version=TLSv1.2 cipher=ECDHE-RSA-AES256-GCM-SHA384 bits=256 verify=NOT)
	for <machkeenan@gmail.com>; Fri, 31 Aug 2018 13:35:26 -0400
Received: from localhost
	by smtp.notes.na.collabserv.com with smtp.notes.na.collabserv.com ESMTP
	for <machkeenan@gmail.com> from <Keenan.Mach@ibm.com>;
	Fri, 31 Aug 2018 17:35:26 -0000
Received: from us1b3-smtp03.a3dr.sjc01.isc4sb.com (10.122.7.173)
	by smtp.notes.na.collabserv.com (10.122.47.39) with smtp.notes.na.collabserv.com ESMTP;
	Fri, 31 Aug 2018 17:35:24 -0000
Received: from us1b3-mail221.a3dr.sjc03.isc4sb.com ([10.168.214.88])
          by us1b3-smtp03.a3dr.sjc01.isc4sb.com
          with ESMTP id 2018083117352416-1938285 ;
          Fri, 31 Aug 2018 17:35:24 +0000 
In-Reply-To: 
Subject: dkim/arc test
From: "Keenan Mach" <Keenan.Mach@ibm.com>
To: machkeenan@gmail.com
Date: Fri, 31 Aug 2018 17:35:24 +0000
Sensitivity: 
References: 
MIME-Version: 1.0
Importance: Normal
X-Priority: 3 (Normal)
X-Mailer: IBM Verse Build 16007-1287 | IBM Domino Build SCN1812108_20180501T0841 May
 01, 2018 at 08:41
X-KeepSent: 5B2B6657:85174C89-002582FA:00609FF9;
 type=4; name=$KeepSent
X-LLNOutbound: False
X-Disclaimed: 57799
X-TNEFEvaluated: 1
X-LLNXfer: False
x-cbid: 18083117-6371-0000-0000-00000411D7A2
X-IBM-SpamModules-Scores: BY=0; FL=0; FP=0; FZ=0; HX=0; KW=0; PH=0;
 SC=0.413459; ST=0; TS=0; UL=0; ISC=; MB=0.000000
X-IBM-SpamModules-Versions: BY=3.00009645; HX=3.00000242; KW=3.00000007;
 PH=3.00000004; SC=3.00000266; SDB=6.01081601; UDB=6.00558013; IPR=6.00861586;
 BA=6.00006088; NDR=6.00000001; ZLA=6.00000005; ZF=6.00000009; ZB=6.00000000;
 ZP=6.00000000; ZH=6.00000000; ZU=6.00000002; MB=3.00023039; XFM=3.00000015;
 UTC=2018-08-31 17:35:25
X-IBM-AV-DETECTION: SAVI=unsuspicious REMOTE=unsuspicious XFE=unused
X-IBM-AV-VERSION: SAVI=2018-08-31 15:39:01 - 6.00008906
x-cbparentid: 18083117-6372-0000-0000-00004F93DB30
Message-Id: <OF5B2B6657.85174C89-ON002582FA.00609FF9-002582FA.00609FFC@notes.na.collabserv.com>
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable
X-Proofpoint-Virus-Version: vendor=fsecure engine=2.50.10434:,, definitions=2018-08-31_07:,,
 signatures=0
X-Proofpoint-Spam-Reason: safe

<div class=3D"socmaildefaultfont" dir=3D"ltr" style=3D"font-family:Arial, H=
elvetica, sans-serif;font-size:10.5pt" ><div dir=3D"ltr" >diff</div></div><=
BR>

"""

def dkim_arc_success():
    return """Delivered-To: ibm.resilient123@gmail.com
Received: by 2002:a05:6358:6a53:b0:af:bbf4:d2b5 with SMTP id c19csp1116383rwh;
        Fri, 29 Jul 2022 08:11:51 -0700 (PDT)
X-Google-Smtp-Source: AGRyM1vD8c1wXres75beXSS8yX4eZHo1F7kFJ11Wfh9XCXk4WVE+fsqkjT2x/OO46LnOJCFFDXJU
X-Received: by 2002:a05:6870:e303:b0:10d:6dde:237d with SMTP id z3-20020a056870e30300b0010d6dde237dmr2278281oad.263.1659107511006;
        Fri, 29 Jul 2022 08:11:51 -0700 (PDT)
ARC-Seal: i=2; a=rsa-sha256; t=1659107511; cv=pass;
        d=google.com; s=arc-20160816;
        b=nsxzEk9V0WiYPBLgIL3UnsZlzRBZ6esd3uqm5mI7L2mswMnG7NiTUnL/rCyNpRSbI0
         PVxyKuL5NIhL5aTpZUlp3X5lCs1okyI+NYB2YNY9bWYFDZUIcZxGXTJr1Wsjq8wa3zQU
         vG3txTBS6UWvu0dkzlMaLB/J112vlBxIMSVYOegbLJooEems2gEfjKsVMuGJgK1lkUQe
         xnsDtI+3PwTLsd63CFjS0ZVSJxcNLduWFZRbyd0P6OsKk955zbucjitK42k/whmO0vVN
         0FOaxE8uZAhyazlndAzHfT5ZGXT/Z53KONjXW/AotjzBBSA9wlyL9ruCehDXOKzNcxzd
         esIg==
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=mime-version:msip_labels:content-language:accept-language
         :message-id:date:thread-index:thread-topic:subject:to:from
         :dkim-signature;
        bh=r1h6qLOg0jwQow80voJvBHfGyIWf2N41GHKuKlH7gRY=;
        b=SCcOalbhmZBG+aT60fNZKXqePNudHJOAtdjzhwT/xGkPWb2lUkUrtNDFD4ZvvmOelN
         YwZCyVy00s8kFOn12iByYj9KZr7aVWKZ9HQRmQta17IvZtHBXIz90qX98WaUrFtDjSzk
         dbcVvER1I/YLrBTSOV9uZP36fwp0B7k1y/1gWowqT/OSEv7bKuIZWMyHGgU0D3tprdQc
         OFko/iJ6sccg71IN3oRFyfdi9/zSRiISXGgU+4xZIbafeUdHPJzBqfCED5vL2HMKAO0r
         DRD8ZaKZ9wZ5Cf56yf+EthUJxBaQWjn8YuGwSvvarTyESYFe+9hZ8FpEnkjm/rc8LQOT
         fWrw==
ARC-Authentication-Results: i=2; mx.google.com;
       dkim=pass header.i=@ibm.com header.s=pp1 header.b=Q39jYzA1;
       arc=pass (i=1 spf=pass spfdomain=ie.ibm.com dkim=pass dkdomain=ie.ibm.com dmarc=pass fromdomain=ie.ibm.com);
       spf=pass (google.com: domain of shane.curtin@ie.ibm.com designates 148.163.156.1 as permitted sender) smtp.mailfrom=Shane.Curtin@ie.ibm.com;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=ibm.com
Return-Path: <Shane.Curtin@ie.ibm.com>
Received: from mx0a-001b2d01.pphosted.com (mx0a-001b2d01.pphosted.com. [148.163.156.1])
        by mx.google.com with ESMTPS id z13-20020a056808028d00b0033a1f5e0da6si2476195oic.218.2022.07.29.08.11.50
        for <ibm.resilient123@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Fri, 29 Jul 2022 08:11:50 -0700 (PDT)
Received-SPF: pass (google.com: domain of shane.curtin@ie.ibm.com designates 148.163.156.1 as permitted sender) client-ip=148.163.156.1;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@ibm.com header.s=pp1 header.b=Q39jYzA1;
       arc=pass (i=1 spf=pass spfdomain=ie.ibm.com dkim=pass dkdomain=ie.ibm.com dmarc=pass fromdomain=ie.ibm.com);
       spf=pass (google.com: domain of shane.curtin@ie.ibm.com designates 148.163.156.1 as permitted sender) smtp.mailfrom=Shane.Curtin@ie.ibm.com;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=ibm.com
Received: from pps.filterd (m0187473.ppops.net [127.0.0.1]) by mx0a-001b2d01.pphosted.com (8.17.1.5/8.17.1.5) with ESMTP id 26TEnci0005294 for <ibm.resilient123@gmail.com>; Fri, 29 Jul 2022 15:11:50 GMT
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=ibm.com; h=from : to : subject : date : message-id : content-type : mime-version; s=pp1; bh=r1h6qLOg0jwQow80voJvBHfGyIWf2N41GHKuKlH7gRY=; b=Q39jYzA1LK4hgRIpxS44A7ii0HJRWQhHGcai6IdTHFPSyICyP9p8U/Wq87F9EfxJLAVM WsZuzAMJArKpJbBXa7oanWVXDrS7yjUbYlP8P4dkNRNUlG8wB4hCNMrayBCMHPQQpnje jQ9l5pAROe0NgRGInMOkvNHdPpJFWeoKHUhxW1VTNWHamuIWcTKeOfznrL106UnX5ujs Cz5HW8ns/oz6o+2UzKVuD04VgUOyha4fupPRhd9kEL3clJGbgps1186G4f4ziU7/jH5o UDL1pfvDlpl1X5uzBkxpOoEXqG4XZKSh/wVwCV59x0y1OZn6n1N4i0fJh30ZbuF2pKrb Lg==
Received: from nam12-mw2-obe.outbound.protection.outlook.com (mail-mw2nam12lp2048.outbound.protection.outlook.com [104.47.66.48]) by mx0a-001b2d01.pphosted.com (PPS) with ESMTPS id 3hmhnfs01q-1 (version=TLSv1.2 cipher=ECDHE-RSA-AES256-GCM-SHA384 bits=256 verify=NOT) for <ibm.resilient123@gmail.com>; Fri, 29 Jul 2022 15:11:49 +0000
ARC-Seal: i=1; a=rsa-sha256; s=arcselector9901; d=microsoft.com; cv=none; b=cvTWy0hnF9qjAJxbpEjXaTngsFKih/CWnnCUnJbrmUS27sXED1EEmNL+/JhGgiZ53+Gk0/4hHH1F/Rgh7Iy+wbXYimmxRPYoh+2288t6sSGtp1XymGu3kPpVsZhdtwtLWBxpiZ3XEm4fnpOYKP+UKQKOO6cYNgS7IKG8xUermm30+dVDUhrmdWBx5eqS5f7O/jdoJbnFYWs+EQpFFQPEavZRgvs2tg1PfPxpUQxmG09MSPwNBUfW1UfJgH25Ics8LESMU3ooXBFJJdaurzD925T5upk4Q75LDl8VbqlpSEt8+4q11VN/qME+NhL5tjyfJToKjfeKbU2a1xbSIgoKTQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com; s=arcselector9901; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1; bh=r1h6qLOg0jwQow80voJvBHfGyIWf2N41GHKuKlH7gRY=; b=cEXE+WvU3K35m0r0U+6OYge7LkgiMsG8axM3R8So7AAHXDpeJNVMA6sO1qDrX3D2Tw5OY0GsX/rmxSD0/lGaNubUA0N6xcZcDT18v47/kltl+spuJguEkkmKrfLT9LbfItGwAHUrsSL931Oo2s7umZ25+oxEpzssX6qnlaBxHB9toqbux3wpQX8DxgMPudI3ABoUXpABPEiNnvkG1Qrbo3nwpQVVIfPFCtlaL12gRumPesQGZySQxgE4+6A3l53AhQ/LxSACFxYi5KI0V9NjlMxA4W4XU0et+VN0Ginn1S/eTxoCB2BXNemqHl/G90dU6Sp69NqwhXf87KJz0p8OaA==
ARC-Authentication-Results: i=1; mx.microsoft.com 1; spf=pass smtp.mailfrom=ie.ibm.com; dmarc=pass action=none header.from=ie.ibm.com; dkim=pass header.d=ie.ibm.com; arc=none
Received: from BN7PR15MB2387.namprd15.prod.outlook.com (2603:10b6:406:8b::16) by SA1PR15MB4369.namprd15.prod.outlook.com (2603:10b6:806:190::9) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.5482.11; Fri, 29 Jul 2022 15:11:48 +0000
Received: from BN7PR15MB2387.namprd15.prod.outlook.com ([fe80::2450:f606:5c07:ce1d]) by BN7PR15MB2387.namprd15.prod.outlook.com ([fe80::2450:f606:5c07:ce1d%4]) with mapi id 15.20.5458.025; Fri, 29 Jul 2022 15:11:48 +0000
From: Shane Curtin <Shane.Curtin@ie.ibm.com>
To: "ibm.resilient123@gmail.com" <ibm.resilient123@gmail.com>
Subject: DKIM
Thread-Topic: DKIM
Thread-Index: AQHYo12GgSq3u1nclEOCQWaNvcJCTg==
Date: Fri, 29 Jul 2022 15:11:48 +0000
Message-ID: <BN7PR15MB23876819148BBEF072245522B9999@BN7PR15MB2387.namprd15.prod.outlook.com>
Accept-Language: en-US
Content-Language: en-US
X-MS-Has-Attach: 
X-MS-TNEF-Correlator: 
msip_labels: 
x-ms-publictraffictype: Email
x-ms-office365-filtering-correlation-id: 9d367da2-5ced-4ea5-6eb6-08da7174a88c
x-ms-traffictypediagnostic: SA1PR15MB4369:EE_
x-ms-exchange-senderadcheck: 1
x-ms-exchange-antispam-relay: 0
x-microsoft-antispam: BCL:0;
x-microsoft-antispam-message-info: tCEWluedwaaHyyx73HXeE8xOKW8z7wV9JDWJNSb0uKGd/n5Il+OyNHNB+MXZ3rAP4kbez9u0aelemFdi+QgkIRN4yWexR9xI/kreZmbzqQlhT7mW2fmNJ2WP202gH3nGK3rHdLQU6acH3Rxxj/gsm8FmIx/62KWADkZv4tmSoYOlxYmsDh3c0xe3n9C+df+V5rrO1KqsigF4P+RhF0qfQ3svaebzGsgDuwbyoT5P/cUEWqiPbSr9tYMNn1JE8qssoEFH6tTdsK8JCRaVpzJ/GMQqV12q6ipqjd7I2bLf/hSkqzFxG8fZjacdnNNCCxRGZTD0pj0zed0nLqnWsH0Gtyc2t9T4rbDbm22eJpWENDHcdXrLhV738RstVdGDYjnX3Sx43+fylkHoo5pzP2nckNtXsUHmvXYZQF1A4oe/Cu1IHZnIbGiodPCJRyOycQOdVBhIkJbmlWuTQTJhmaLFbOrcyon/UiR4B/VMJu0vFhD7w9lPW8fGomnxNszO81IQtu+Xn1iD0bUxJa9PfiMVJhWEr9w3EEHN9bCEy+NuItn3/XXkia1FaBjngnixFK1cA0IwORlFBtjFPb+QnM6124fH06/N1j+eSxSLKq2TJ43wfCWWq/KWizYsBPoEMIr0tYTocOifIuyYPLKo+lX+8pIbsjeFO2EXctK4YH9GxeQ0kNjRRBrxKXRM7E3f3FdYEy1UbVyveKs3aOV38G1a5EqecSh+oTu5gdJk0Sm2/qPtO77efPrcoTYhvXRl0w6iUoHq/5ZtztKlsD4torltJl6Nm/6TCgXGFcsvx2fXt1paOUy3xms40F1u9nTQHKs9
x-forefront-antispam-report: CIP:255.255.255.255;CTRY:;LANG:en;SCL:1;SRV:;IPV:NLI;SFV:NSPM;H:BN7PR15MB2387.namprd15.prod.outlook.com;PTR:;CAT:NONE;SFS:(13230016)(136003)(39860400002)(366004)(346002)(396003)(376002)(6916009)(91956017)(38100700002)(122000001)(86362001)(71200400001)(3480700007)(33656002)(5660300002)(66946007)(478600001)(41300700001)(66446008)(38070700005)(66556008)(76116006)(66476007)(64756008)(8676002)(316002)(7116003)(558084003)(4270600006)(8936002)(6506007)(2906002)(19627405001)(186003)(26005)(9686003)(52536014)(83380400001)(55016003)(7696005);DIR:OUT;SFP:1101;
x-ms-exchange-antispam-messagedata-chunkcount: 1
x-ms-exchange-antispam-messagedata-0: rUxPhebnpTWVvDIjgho0u8lQgb7WITH6CQQUkjMvBZBSPkvjMetUrzZnR+a429laLT9R+IV/5wIJ/B16mYL8zLxGDaA+bLDB6Si9UyGWfy/ohurZHTt9wpfXcjhZmLt4L5WKBrqcxz/cOfpuTe5ki4/U6Nf9xeLf3wxTFuQyH1FhltRrj+959dFh6yVvIGLHCjQXzHeaWJ/aeOJMv7zP32/GYBkQXIfB/qjTF+ngEXMXJN+FZhiOtisuk0CZqbXo927vi8Oe5R5JH5gT8WyX6+CxQFabS+Hcx2/GZELC73czLt5NDNeZ4tGPCajhTgFLffTLCQ3avt57j1rBVy2V3pm7GWaHI5xwB6rP1FmtrRezoIMAvo0OPJ0cIzgB4FJTBn//gZMsvCDlZAlP35mgo2Y4fPlNtxhnSO8M8gMSWOaU8SwaDskB7bkFj2eZvILajhBcnPNu3XK9aHO50hqbSHDXhCUKX2dSVce3JOYK3rQgOHnBdK0h4Cbz1HRh6PQVnSBObDUw/Dt5Ty2bDhFZMBfA/FhydTD7r1hDgLatnXRVPepFAGlgWML36fIBM53AG8+kv46XrLLBKa8Qef5/IgiOwi3Tyx/f/ZzPfnjE9xjewNQgrjvR0X4a2286BOJAYNNmBnI7ebiRqQAwOT0HtJl02WS3M1/S3TO9xCD209MhUD3KgeHyhCkaRgnLbAAKuhnV6jIeJ5abEGKAMa8HXpJl89BZsYcpCfE9j6pd+P5et9HDBFx/ZGi2MiscjdQofGpwOgCRkRNjOG4v0Cjmp2FL1PRSwRtafJFaM2twBKSnODSzFVMIVKfkGqQqalGyhvVCZKWmK2zOvvdo5Kjz3NnWMVyO1Ot58S+75jeNnM8kanHC4BYhAIUjth9W1YHampxvwFQh7P+fJEco5oNjv9W23FkaTL85vlKEHALv9nsobDrXHaDTFmJDTFY/JgyPP78mDXD5DGL3ZwI6D6/h9MY1h2xT0bO2t5mxRhS7/8MaH/oVcrJma21WMw/Atkob4mECsvogOr+i5jWACI6D4EotWODTTsAWrBHHOdzCFZIyBqu6hX8vdyLixKw3EwSRNLdwWTLRvWI4uuwwbao/1ToS3niOfmNCOYKh3AjeltOyHv4IkfMu9HJzioGmS0Ot9u86EIwHbDzZ0OWnP+FC2BkE5nRL4C1d0GREhMgEu3Cbt4D7EVrFUs6kLqabdPheJK9Vd76HfhiMDiFQgAzvhIvqiPhu1TyFOxzHLXLl5/O8qqDMM9SwMYQ0X/t6tenfisZ8XUhOaVwol4AydsUWX+oShuDwiebLyjnv1UyFrj4dT6m/+PyPTShN4IhCjtQoB01Aa+I9awFm6lIYkHVDsZTQSKgCF1ifBGfdMOiOM3hTsv1jf0G5uqVMp7lgM7bC1o7ocrk8BfJuOgcq2YFsr8DHiVT7CRKM0lvn97hp1QadtvNhWe0JshhN0jlR/sPfUjnJzCMLy85yghZcnUCSHuW+6xRol48Uk4x2TJalJjbvwTfP1+ZsjsroBASpwFqxYJ6h9uJCp92sPKXhwSsHAXBLNb6lPzpnNyJ5Dwdj8GRdv2WLHy96erc1vVr4Scac
Content-Type: multipart/alternative; boundary="_000_BN7PR15MB23876819148BBEF072245522B9999BN7PR15MB2387namp_"
MIME-Version: 1.0
X-OriginatorOrg: ie.ibm.com
X-MS-Exchange-CrossTenant-AuthAs: Internal
X-MS-Exchange-CrossTenant-AuthSource: BN7PR15MB2387.namprd15.prod.outlook.com
X-MS-Exchange-CrossTenant-Network-Message-Id: 9d367da2-5ced-4ea5-6eb6-08da7174a88c
X-MS-Exchange-CrossTenant-originalarrivaltime: 29 Jul 2022 15:11:48.3954 (UTC)
X-MS-Exchange-CrossTenant-fromentityheader: Hosted
X-MS-Exchange-CrossTenant-id: fcf67057-50c9-4ad4-98f3-ffca64add9e9
X-MS-Exchange-CrossTenant-mailboxtype: HOSTED
X-MS-Exchange-CrossTenant-userprincipalname: SjY+au3jJtIogokp6cgCoQkMBHQOixqyzwxv85Db0+IBMHvj3f33QOaQ4rKl0DTQp9KOLCPOpdopt12IdGrk4A==
X-MS-Exchange-Transport-CrossTenantHeadersStamped: SA1PR15MB4369
X-Proofpoint-ORIG-GUID: Pfs-K9ShHHLpB2LZ7usiUUGGPsJULOo4
X-Proofpoint-GUID: Pfs-K9ShHHLpB2LZ7usiUUGGPsJULOo4
X-Proofpoint-Virus-Version: vendor=baseguard engine=ICAP:2.0.205,Aquarius:18.0.883,Hydra:6.0.517,FMLib:17.11.122.1 definitions=2022-07-29_16,2022-07-28_02,2022-06-22_01
X-Proofpoint-Spam-Details: rule=outbound_notspam policy=outbound score=0 adultscore=0 mlxscore=0 malwarescore=0 clxscore=1011 impostorscore=0 priorityscore=1501 phishscore=0 suspectscore=0 spamscore=0 lowpriorityscore=0 mlxlogscore=564 bulkscore=0 classifier=spam adjust=0 reason=mlx scancount=1 engine=8.12.0-2206140000 definitions=main-2207290066

--_000_BN7PR15MB23876819148BBEF072245522B9999BN7PR15MB2387namp_
Content-Type: text/plain; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

This is mock email with DKIM enabled

Regards,

Apps Engineer
IBM Security SOAR

IBM Security

--_000_BN7PR15MB23876819148BBEF072245522B9999BN7PR15MB2387namp_
Content-Type: text/html; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

<html>
<head>
<meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Diso-8859-=
1">
<style type=3D"text/css" style=3D"display:none;"> P {margin-top:0;margin-bo=
ttom:0;} </style>
</head>
<body dir=3D"ltr">
<div style=3D"font-family: Arial, Helvetica, sans-serif; font-size: 12pt; c=
olor: rgb(0, 0, 0);" class=3D"elementToProof">
This is mock email with DKIM enabled<br>
</div>
<div>
<div style=3D"font-family: Arial, Helvetica, sans-serif; font-size: 12pt; c=
olor: rgb(0, 0, 0);">
<br>
</div>
<div id=3D"Signature">
<div><span style=3D"font-family: Arial, Helvetica, sans-serif;">Regards,</s=
pan>
<div><br>
</div>
<div><span style=3D"font-family: Arial, Helvetica, sans-serif;">Apps Engine=
er</span></div>
<div><span style=3D"font-family: Arial, Helvetica, sans-serif;">IBM Securit=
y SOAR</span></div>
<div><br>
</div>
<span style=3D"font-family: Arial, Helvetica, sans-serif;">IBM </span><span=
 style=3D"font-family: Arial, Helvetica, sans-serif;"><strong>Security</str=
ong></span></div>
</div>
</div>
</body>
</html>

--_000_BN7PR15MB23876819148BBEF072245522B9999BN7PR15MB2387namp_--"""

def no_headers():
    return """Received: from OPS64801.rsystems.local ([9.70.192.31]) by
 ops64801.rsystems.local ([9.70.192.31]) with mapi id 14.01.0438.000; Fri, 10
 Aug 2018 09:55:37 -0400
From: Resilient Admin <resadmin@rsystems.local>
To: "Resilient Systems, Inc." <incidents@rsystems.local>
Subject: with attachment
Thread-Topic: with attachment
Thread-Index: AdQwsc/8TogEgvfxSnGuxVwBJvTeRg==
Date: Fri, 10 Aug 2018 09:55:35 -0400
Message-ID: <A868B128D3046E4696FF38805B666DBA485C83@ops64801.rsystems.local>
Accept-Language: en-US
Content-Language: en-US
X-MS-Exchange-Organization-AuthAs: Internal
X-MS-Exchange-Organization-AuthMechanism: 04
X-MS-Exchange-Organization-AuthSource: ops64801.rsystems.local
X-MS-Has-Attach:
X-MS-Exchange-Organization-SCL: -1
X-MS-TNEF-Correlator:
Content-Type: multipart/alternative;
	boundary="_000_A868B128D3046E4696FF38805B666DBA485C83ops64801rsystemsl_"
MIME-Version: 1.0

--_000_A868B128D3046E4696FF38805B666DBA485C83ops64801rsystemsl_
Content-Type: text/plain; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

body

--_000_A868B128D3046E4696FF38805B666DBA485C83ops64801rsystemsl_
Content-Type: text/html; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

<html dir=3D"ltr">
<head>
<meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Diso-8859-=
1">
<style type=3D"text/css" id=3D"owaParaStyle"></style>
</head>
<body fpstyle=3D"1" ocsi=3D"0">
<div style=3D"direction: ltr;font-family: Tahoma;color: #000000;font-size: =
10pt;">body</div>
</body>
</html>

--_000_A868B128D3046E4696FF38805B666DBA485C83ops64801rsystemsl_--"""

def dkim_only():
    return """Delivered-To: ibm.resilient123@gmail.com
Received: by 2002:a05:6358:6a53:b0:af:bbf4:d2b5 with SMTP id c19csp1116383rwh;
        Fri, 29 Jul 2022 08:11:51 -0700 (PDT)
X-Google-Smtp-Source: AGRyM1vD8c1wXres75beXSS8yX4eZHo1F7kFJ11Wfh9XCXk4WVE+fsqkjT2x/OO46LnOJCFFDXJU
X-Received: by 2002:a05:6870:e303:b0:10d:6dde:237d with SMTP id z3-20020a056870e30300b0010d6dde237dmr2278281oad.263.1659107511006;
        Fri, 29 Jul 2022 08:11:51 -0700 (PDT)
Return-Path: <Shane.Curtin@ie.ibm.com>
Received: from mx0a-001b2d01.pphosted.com (mx0a-001b2d01.pphosted.com. [148.163.156.1])
        by mx.google.com with ESMTPS id z13-20020a056808028d00b0033a1f5e0da6si2476195oic.218.2022.07.29.08.11.50
        for <ibm.resilient123@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Fri, 29 Jul 2022 08:11:50 -0700 (PDT)
Received-SPF: pass (google.com: domain of shane.curtin@ie.ibm.com designates 148.163.156.1 as permitted sender) client-ip=148.163.156.1;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@ibm.com header.s=pp1 header.b=Q39jYzA1;
       arc=pass (i=1 spf=pass spfdomain=ie.ibm.com dkim=pass dkdomain=ie.ibm.com dmarc=pass fromdomain=ie.ibm.com);
       spf=pass (google.com: domain of shane.curtin@ie.ibm.com designates 148.163.156.1 as permitted sender) smtp.mailfrom=Shane.Curtin@ie.ibm.com;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=ibm.com
Received: from pps.filterd (m0187473.ppops.net [127.0.0.1]) by mx0a-001b2d01.pphosted.com (8.17.1.5/8.17.1.5) with ESMTP id 26TEnci0005294 for <ibm.resilient123@gmail.com>; Fri, 29 Jul 2022 15:11:50 GMT
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=ibm.com; h=from : to : subject : date : message-id : content-type : mime-version; s=pp1; bh=r1h6qLOg0jwQow80voJvBHfGyIWf2N41GHKuKlH7gRY=; b=Q39jYzA1LK4hgRIpxS44A7ii0HJRWQhHGcai6IdTHFPSyICyP9p8U/Wq87F9EfxJLAVM WsZuzAMJArKpJbBXa7oanWVXDrS7yjUbYlP8P4dkNRNUlG8wB4hCNMrayBCMHPQQpnje jQ9l5pAROe0NgRGInMOkvNHdPpJFWeoKHUhxW1VTNWHamuIWcTKeOfznrL106UnX5ujs Cz5HW8ns/oz6o+2UzKVuD04VgUOyha4fupPRhd9kEL3clJGbgps1186G4f4ziU7/jH5o UDL1pfvDlpl1X5uzBkxpOoEXqG4XZKSh/wVwCV59x0y1OZn6n1N4i0fJh30ZbuF2pKrb Lg==
Received: from nam12-mw2-obe.outbound.protection.outlook.com (mail-mw2nam12lp2048.outbound.protection.outlook.com [104.47.66.48]) by mx0a-001b2d01.pphosted.com (PPS) with ESMTPS id 3hmhnfs01q-1 (version=TLSv1.2 cipher=ECDHE-RSA-AES256-GCM-SHA384 bits=256 verify=NOT) for <ibm.resilient123@gmail.com>; Fri, 29 Jul 2022 15:11:49 +0000
ARC-Seal: i=1; a=rsa-sha256; s=arcselector9901; d=microsoft.com; cv=none; b=cvTWy0hnF9qjAJxbpEjXaTngsFKih/CWnnCUnJbrmUS27sXED1EEmNL+/JhGgiZ53+Gk0/4hHH1F/Rgh7Iy+wbXYimmxRPYoh+2288t6sSGtp1XymGu3kPpVsZhdtwtLWBxpiZ3XEm4fnpOYKP+UKQKOO6cYNgS7IKG8xUermm30+dVDUhrmdWBx5eqS5f7O/jdoJbnFYWs+EQpFFQPEavZRgvs2tg1PfPxpUQxmG09MSPwNBUfW1UfJgH25Ics8LESMU3ooXBFJJdaurzD925T5upk4Q75LDl8VbqlpSEt8+4q11VN/qME+NhL5tjyfJToKjfeKbU2a1xbSIgoKTQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com; s=arcselector9901; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1; bh=r1h6qLOg0jwQow80voJvBHfGyIWf2N41GHKuKlH7gRY=; b=cEXE+WvU3K35m0r0U+6OYge7LkgiMsG8axM3R8So7AAHXDpeJNVMA6sO1qDrX3D2Tw5OY0GsX/rmxSD0/lGaNubUA0N6xcZcDT18v47/kltl+spuJguEkkmKrfLT9LbfItGwAHUrsSL931Oo2s7umZ25+oxEpzssX6qnlaBxHB9toqbux3wpQX8DxgMPudI3ABoUXpABPEiNnvkG1Qrbo3nwpQVVIfPFCtlaL12gRumPesQGZySQxgE4+6A3l53AhQ/LxSACFxYi5KI0V9NjlMxA4W4XU0et+VN0Ginn1S/eTxoCB2BXNemqHl/G90dU6Sp69NqwhXf87KJz0p8OaA==
ARC-Authentication-Results: i=1; mx.microsoft.com 1; spf=pass smtp.mailfrom=ie.ibm.com; dmarc=pass action=none header.from=ie.ibm.com; dkim=pass header.d=ie.ibm.com; arc=none
Received: from BN7PR15MB2387.namprd15.prod.outlook.com (2603:10b6:406:8b::16) by SA1PR15MB4369.namprd15.prod.outlook.com (2603:10b6:806:190::9) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.5482.11; Fri, 29 Jul 2022 15:11:48 +0000
Received: from BN7PR15MB2387.namprd15.prod.outlook.com ([fe80::2450:f606:5c07:ce1d]) by BN7PR15MB2387.namprd15.prod.outlook.com ([fe80::2450:f606:5c07:ce1d%4]) with mapi id 15.20.5458.025; Fri, 29 Jul 2022 15:11:48 +0000
From: Shane Curtin <Shane.Curtin@ie.ibm.com>
To: "ibm.resilient123@gmail.com" <ibm.resilient123@gmail.com>
Subject: DKIM
Thread-Topic: DKIM
Thread-Index: AQHYo12GgSq3u1nclEOCQWaNvcJCTg==
Date: Fri, 29 Jul 2022 15:11:48 +0000
Message-ID: <BN7PR15MB23876819148BBEF072245522B9999@BN7PR15MB2387.namprd15.prod.outlook.com>
Accept-Language: en-US
Content-Language: en-US
X-MS-Has-Attach: 
X-MS-TNEF-Correlator: 
msip_labels: 
x-ms-publictraffictype: Email
x-ms-office365-filtering-correlation-id: 9d367da2-5ced-4ea5-6eb6-08da7174a88c
x-ms-traffictypediagnostic: SA1PR15MB4369:EE_
x-ms-exchange-senderadcheck: 1
x-ms-exchange-antispam-relay: 0
x-microsoft-antispam: BCL:0;
x-microsoft-antispam-message-info: tCEWluedwaaHyyx73HXeE8xOKW8z7wV9JDWJNSb0uKGd/n5Il+OyNHNB+MXZ3rAP4kbez9u0aelemFdi+QgkIRN4yWexR9xI/kreZmbzqQlhT7mW2fmNJ2WP202gH3nGK3rHdLQU6acH3Rxxj/gsm8FmIx/62KWADkZv4tmSoYOlxYmsDh3c0xe3n9C+df+V5rrO1KqsigF4P+RhF0qfQ3svaebzGsgDuwbyoT5P/cUEWqiPbSr9tYMNn1JE8qssoEFH6tTdsK8JCRaVpzJ/GMQqV12q6ipqjd7I2bLf/hSkqzFxG8fZjacdnNNCCxRGZTD0pj0zed0nLqnWsH0Gtyc2t9T4rbDbm22eJpWENDHcdXrLhV738RstVdGDYjnX3Sx43+fylkHoo5pzP2nckNtXsUHmvXYZQF1A4oe/Cu1IHZnIbGiodPCJRyOycQOdVBhIkJbmlWuTQTJhmaLFbOrcyon/UiR4B/VMJu0vFhD7w9lPW8fGomnxNszO81IQtu+Xn1iD0bUxJa9PfiMVJhWEr9w3EEHN9bCEy+NuItn3/XXkia1FaBjngnixFK1cA0IwORlFBtjFPb+QnM6124fH06/N1j+eSxSLKq2TJ43wfCWWq/KWizYsBPoEMIr0tYTocOifIuyYPLKo+lX+8pIbsjeFO2EXctK4YH9GxeQ0kNjRRBrxKXRM7E3f3FdYEy1UbVyveKs3aOV38G1a5EqecSh+oTu5gdJk0Sm2/qPtO77efPrcoTYhvXRl0w6iUoHq/5ZtztKlsD4torltJl6Nm/6TCgXGFcsvx2fXt1paOUy3xms40F1u9nTQHKs9
x-forefront-antispam-report: CIP:255.255.255.255;CTRY:;LANG:en;SCL:1;SRV:;IPV:NLI;SFV:NSPM;H:BN7PR15MB2387.namprd15.prod.outlook.com;PTR:;CAT:NONE;SFS:(13230016)(136003)(39860400002)(366004)(346002)(396003)(376002)(6916009)(91956017)(38100700002)(122000001)(86362001)(71200400001)(3480700007)(33656002)(5660300002)(66946007)(478600001)(41300700001)(66446008)(38070700005)(66556008)(76116006)(66476007)(64756008)(8676002)(316002)(7116003)(558084003)(4270600006)(8936002)(6506007)(2906002)(19627405001)(186003)(26005)(9686003)(52536014)(83380400001)(55016003)(7696005);DIR:OUT;SFP:1101;
x-ms-exchange-antispam-messagedata-chunkcount: 1
x-ms-exchange-antispam-messagedata-0: rUxPhebnpTWVvDIjgho0u8lQgb7WITH6CQQUkjMvBZBSPkvjMetUrzZnR+a429laLT9R+IV/5wIJ/B16mYL8zLxGDaA+bLDB6Si9UyGWfy/ohurZHTt9wpfXcjhZmLt4L5WKBrqcxz/cOfpuTe5ki4/U6Nf9xeLf3wxTFuQyH1FhltRrj+959dFh6yVvIGLHCjQXzHeaWJ/aeOJMv7zP32/GYBkQXIfB/qjTF+ngEXMXJN+FZhiOtisuk0CZqbXo927vi8Oe5R5JH5gT8WyX6+CxQFabS+Hcx2/GZELC73czLt5NDNeZ4tGPCajhTgFLffTLCQ3avt57j1rBVy2V3pm7GWaHI5xwB6rP1FmtrRezoIMAvo0OPJ0cIzgB4FJTBn//gZMsvCDlZAlP35mgo2Y4fPlNtxhnSO8M8gMSWOaU8SwaDskB7bkFj2eZvILajhBcnPNu3XK9aHO50hqbSHDXhCUKX2dSVce3JOYK3rQgOHnBdK0h4Cbz1HRh6PQVnSBObDUw/Dt5Ty2bDhFZMBfA/FhydTD7r1hDgLatnXRVPepFAGlgWML36fIBM53AG8+kv46XrLLBKa8Qef5/IgiOwi3Tyx/f/ZzPfnjE9xjewNQgrjvR0X4a2286BOJAYNNmBnI7ebiRqQAwOT0HtJl02WS3M1/S3TO9xCD209MhUD3KgeHyhCkaRgnLbAAKuhnV6jIeJ5abEGKAMa8HXpJl89BZsYcpCfE9j6pd+P5et9HDBFx/ZGi2MiscjdQofGpwOgCRkRNjOG4v0Cjmp2FL1PRSwRtafJFaM2twBKSnODSzFVMIVKfkGqQqalGyhvVCZKWmK2zOvvdo5Kjz3NnWMVyO1Ot58S+75jeNnM8kanHC4BYhAIUjth9W1YHampxvwFQh7P+fJEco5oNjv9W23FkaTL85vlKEHALv9nsobDrXHaDTFmJDTFY/JgyPP78mDXD5DGL3ZwI6D6/h9MY1h2xT0bO2t5mxRhS7/8MaH/oVcrJma21WMw/Atkob4mECsvogOr+i5jWACI6D4EotWODTTsAWrBHHOdzCFZIyBqu6hX8vdyLixKw3EwSRNLdwWTLRvWI4uuwwbao/1ToS3niOfmNCOYKh3AjeltOyHv4IkfMu9HJzioGmS0Ot9u86EIwHbDzZ0OWnP+FC2BkE5nRL4C1d0GREhMgEu3Cbt4D7EVrFUs6kLqabdPheJK9Vd76HfhiMDiFQgAzvhIvqiPhu1TyFOxzHLXLl5/O8qqDMM9SwMYQ0X/t6tenfisZ8XUhOaVwol4AydsUWX+oShuDwiebLyjnv1UyFrj4dT6m/+PyPTShN4IhCjtQoB01Aa+I9awFm6lIYkHVDsZTQSKgCF1ifBGfdMOiOM3hTsv1jf0G5uqVMp7lgM7bC1o7ocrk8BfJuOgcq2YFsr8DHiVT7CRKM0lvn97hp1QadtvNhWe0JshhN0jlR/sPfUjnJzCMLy85yghZcnUCSHuW+6xRol48Uk4x2TJalJjbvwTfP1+ZsjsroBASpwFqxYJ6h9uJCp92sPKXhwSsHAXBLNb6lPzpnNyJ5Dwdj8GRdv2WLHy96erc1vVr4Scac
Content-Type: multipart/alternative; boundary="_000_BN7PR15MB23876819148BBEF072245522B9999BN7PR15MB2387namp_"
MIME-Version: 1.0
X-OriginatorOrg: ie.ibm.com
X-MS-Exchange-CrossTenant-AuthAs: Internal
X-MS-Exchange-CrossTenant-AuthSource: BN7PR15MB2387.namprd15.prod.outlook.com
X-MS-Exchange-CrossTenant-Network-Message-Id: 9d367da2-5ced-4ea5-6eb6-08da7174a88c
X-MS-Exchange-CrossTenant-originalarrivaltime: 29 Jul 2022 15:11:48.3954 (UTC)
X-MS-Exchange-CrossTenant-fromentityheader: Hosted
X-MS-Exchange-CrossTenant-id: fcf67057-50c9-4ad4-98f3-ffca64add9e9
X-MS-Exchange-CrossTenant-mailboxtype: HOSTED
X-MS-Exchange-CrossTenant-userprincipalname: SjY+au3jJtIogokp6cgCoQkMBHQOixqyzwxv85Db0+IBMHvj3f33QOaQ4rKl0DTQp9KOLCPOpdopt12IdGrk4A==
X-MS-Exchange-Transport-CrossTenantHeadersStamped: SA1PR15MB4369
X-Proofpoint-ORIG-GUID: Pfs-K9ShHHLpB2LZ7usiUUGGPsJULOo4
X-Proofpoint-GUID: Pfs-K9ShHHLpB2LZ7usiUUGGPsJULOo4
X-Proofpoint-Virus-Version: vendor=baseguard engine=ICAP:2.0.205,Aquarius:18.0.883,Hydra:6.0.517,FMLib:17.11.122.1 definitions=2022-07-29_16,2022-07-28_02,2022-06-22_01
X-Proofpoint-Spam-Details: rule=outbound_notspam policy=outbound score=0 adultscore=0 mlxscore=0 malwarescore=0 clxscore=1011 impostorscore=0 priorityscore=1501 phishscore=0 suspectscore=0 spamscore=0 lowpriorityscore=0 mlxlogscore=564 bulkscore=0 classifier=spam adjust=0 reason=mlx scancount=1 engine=8.12.0-2206140000 definitions=main-2207290066

--_000_BN7PR15MB23876819148BBEF072245522B9999BN7PR15MB2387namp_
Content-Type: text/plain; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

This is mock email with DKIM enabled

Regards,

Apps Engineer
IBM Security SOAR

IBM Security

--_000_BN7PR15MB23876819148BBEF072245522B9999BN7PR15MB2387namp_
Content-Type: text/html; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

<html>
<head>
<meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Diso-8859-=
1">
<style type=3D"text/css" style=3D"display:none;"> P {margin-top:0;margin-bo=
ttom:0;} </style>
</head>
<body dir=3D"ltr">
<div style=3D"font-family: Arial, Helvetica, sans-serif; font-size: 12pt; c=
olor: rgb(0, 0, 0);" class=3D"elementToProof">
This is mock email with DKIM enabled<br>
</div>
<div>
<div style=3D"font-family: Arial, Helvetica, sans-serif; font-size: 12pt; c=
olor: rgb(0, 0, 0);">
<br>
</div>
<div id=3D"Signature">
<div><span style=3D"font-family: Arial, Helvetica, sans-serif;">Regards,</s=
pan>
<div><br>
</div>
<div><span style=3D"font-family: Arial, Helvetica, sans-serif;">Apps Engine=
er</span></div>
<div><span style=3D"font-family: Arial, Helvetica, sans-serif;">IBM Securit=
y SOAR</span></div>
<div><br>
</div>
<span style=3D"font-family: Arial, Helvetica, sans-serif;">IBM </span><span=
 style=3D"font-family: Arial, Helvetica, sans-serif;"><strong>Security</str=
ong></span></div>
</div>
</div>
</body>
</html>

--_000_BN7PR15MB23876819148BBEF072245522B9999BN7PR15MB2387namp_--
"""

def dkim_only_fail():
    return """Delivered-To: machkeenan@gmail.com
Received: by 2002:a17:90a:4d4d:0:0:0:0 with SMTP id l13-v6csp2422799pjh;
        Sat, 28 Jul 2018 17:28:01 -0700 (PDT)
X-Received: by 2002:a6b:6709:: with SMTP id b9-v6mr9003935ioc.272.1532824081583;
        Sat, 28 Jul 2018 17:28:01 -0700 (PDT)
Return-Path: <3EQpdWwgTCnolm-pcnjwYaamslrq.emmejc.amkkYaficclYlekYgj.amk@gaia.bounces.google.com>
Received: from mail-sor-f69.google.com (mail-sor-f69.google.com. [209.85.220.69])
        by mx.google.com with SMTPS id m187-v6sor2365872ith.81.2018.07.28.17.28.01
        for <machkeenan@gmail.com>
        (Google Transport Security);
        Sat, 28 Jul 2018 17:28:01 -0700 (PDT)
Received-SPF: pass (google.com: domain of 3eqpdwwgtcnolm-pcnjwyaamslrq.emmejc.amkkyaficclylekygj.amk@gaia.bounces.google.com designates 209.85.220.69 as permitted sender) client-ip=209.85.220.69;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@accounts.google.com header.s=20161025 header.b=tn5NSYTT;
       spf=pass (google.com: domain of 3eqpdwwgtcnolm-pcnjwyaamslrq.emmejc.amkkyaficclylekygj.amk@gaia.bounces.google.com designates 209.85.220.69 as permitted sender) smtp.mailfrom=3EQpdWwgTCnolm-pcnjwYaamslrq.emmejc.amkkYaficclYlekYgj.amk@gaia.bounces.google.com;
       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=accounts.google.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=accounts.google.com; s=20161025;
        h=mime-version:date:feedback-id:message-id:subject:from:to;
        bh=48bImmZYHnJrEzzmfY5LHm/WUeKdXiM6zhFUWts1D6Y=;
        b=tn5NSYTTXIOFqp+g5GtAh2rKehCje5kM9f2vAGKQe4f/ks1aqEF0HzyMjyDOEw6PkE
         IbcsAApD0hLbyxsDX2pfYiZe6vs+xT5pYjrNIR1rnw5UIOO3vXXnl1/3huZ+WTstNbaZ
         y7BLqRja8KZdOhOr0f7viW4l1NvrNmNxLUck0y2vyoR/a15ppoafS4aDORPgqISQj/WA
         Ok0v13iiFAP77x1psAELaEV4tDOAEIJ1i3gOq1+ipvbLI5zfwlDlP77oEEC/gSjk714J
         vvuYpdvAqKol9WD8udlKMDYLyeTP+b53SG3/c9zaL3U33HQ7Os3tvOGmw+6Pq6J8Cz/t
         Zg7Q==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20161025;
        h=x-gm-message-state:mime-version:date:feedback-id:message-id:subject
         :from:to;
        bh=48bImmZYHnJrEzzmfY5LHm/WUeKdXiM6zhFUWts1D6Y=;
        b=KpvmxJaEWFuIO6q7+gzMDVlSihaaGsozIGxON1c9A52M3j7pEDfGu+8iA+KTJV+lwD
         9F1Mh0zfL/h0Zor6Hx8J8wxkl9HoKpE2xdk8YOnwbkUoR9NdiUyJSAv+LDVVR3U/YJLk
         ddOwinVtpQauGfZx6QopZgd6mnApdWMRwfniqZPIZjRoJyUwuFKcj9DXrjAYRfBEkysS
         ioAVpvp4NJg2qjSb0lNApRcu+ZisCXEVlPsV6ENRvimb+VuGWnNLo9DHqXPASsonSrYh
         LPkzp6FNbegHQ0u8lxirzNfCQZkBi18C3Y+DUWKLfodDsj8p0k3qC4bENqWmPIloDlv9
         5Vdw==
X-Gm-Message-State: AOUpUlH645s4nk5zwVG67HYR6r3Qsmqj98YipJ+0y6a6ICvORrgBKhuj /is5Jv/pNGkuKo7Tmd9iCqzMNVcH+WJh
X-Google-Smtp-Source: AAOMgpdn3X0wEgJnHtxPac2VxAwnz+9wfARi42cP5Z8T1Cbka/FQUUSjIrAZ/fWXEdIf2zLxnhQ7XUIxt2R5sn4rn/xT5g==
MIME-Version: 1.0
X-Received: by 2002:a24:1a07:: with SMTP id 7-v6mr1578628iti.12.1532824081352; Sat, 28 Jul 2018 17:28:01 -0700 (PDT)
Date: Sun, 29 Jul 2018 00:27:59 +0000 (UTC)
X-Account-Notification-Type: 31-anexp#hsc-control_b
Feedback-ID: 31-anexp#hsc-control_b:account-notifier
X-Notifications: daf6dcccce000000
Message-ID: <6wIyQVDiXclD5wko00U1rQ.0@notifications.google.com>
Subject: Security alert
From: Google <no-reply@accounts.google.com>
To: machkeenan@gmail.com
Content-Type: multipart/alternative; boundary="000000000000df484d0572186a76"

--000000000000df484d0572186a76
Content-Type: text/plain; charset="UTF-8"; format=flowed; delsp=yes
Content-Transfer-Encoding: base64

S2VlbmFuIE1hY2gNCg0KTmV3IGRldmljZSBzaWduZWQgaW4gdG8NCm1hY2hrZWVuYW5AZ21haWwu
Y29tDQpZb3VyIEdvb2dsZSBBY2NvdW50IHdhcyBqdXN0IHNpZ25lZCBpbiB0byBmcm9tIGEgbmV3
IFdpbmRvd3MgZGV2aWNlLiBZb3UncmUNCmdldHRpbmcgdGhpcyBlbWFpbCB0byBtYWtlIHN1cmUg
aXQgd2FzIHlvdS4NCg0KDQoNCkNoZWNrIGFjdGl2aXR5DQo8aHR0cHM6Ly9hY2NvdW50cy5nb29n
bGUuY29tL0FjY291bnRDaG9vc2VyP0VtYWlsPW1hY2hrZWVuYW5AZ21haWwuY29tJmNvbnRpbnVl
PWh0dHBzOi8vbXlhY2NvdW50Lmdvb2dsZS5jb20vYWxlcnQvbnQvMTUzMjgyNDA3OTAwMD9yZm4l
M0QzMSUyNnJmbmMlM0QxJTI2ZWlkJTNEMTMzNTEwODI0MDk5NDE1OTYyNiUyNmV0JTNEMCUyNmFz
YWUlM0QyJTI2YW5leHAlM0Roc2MtY29udHJvbF9iPg0KPGh0dHBzOi8vYWNjb3VudHMuZ29vZ2xl
LmNvbS9BY2NvdW50Q2hvb3Nlcj9FbWFpbD1tYWNoa2VlbmFuQGdtYWlsLmNvbSZjb250aW51ZT1o
MzElMjZyZm5jJTNEMSUyNmVpZCUzRDEzMzUxMDgyNDA5OTQxNTk2MjYlMjZldCUzRDAlMjZhc2Fl
JTNEMiUyNmFuZXhwJTNEaHNjLWNvbnRyb2xfYj4NCg0KDQpZb3UgcmVjZWl2ZWQgdGhpcyBlbWFp
bCB0byBsZXQgeW91IGtub3cgYWJvdXQgaW1wb3J0YW50IGNoYW5nZXMgdG8geW91cg0KR29vZ2xl
IEFjY291bnQgYW5kIHNlcnZpY2VzLg0KwqkgMjAxOCBHb29nbGUgTExDLDE2MDAgQW1waGl0aGVh
dHJlIFBhcmt3YXksIE1vdW50YWluIFZpZXcsIENBIDk0MDQzLCBVU0ENCjE1MzI4MjQwNzkwMDAw
MDANCg==
--000000000000df484d0572186a76
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<html lang=3Den><head><meta content=3D"date=3Dno" name=3D"format-detection"=
><meta content=3D"email=3Dno" name=3D"format-detection"><style>.awl a {colo=
r: #FFFFFF; text-decoration: none;}.abml a {color: #000000; font-family: Ro=
boto-Medium,Helvetica,Arial,sans-serif; font-weight: bold; text-decoration:=
 none;}.adgl a {color: rgba(0, 0, 0, 0.87); text-decoration: none;}.afal a =
{color: #b0b0b0; text-decoration: none;}@media screen and (min-width: 600px=
) {.v2sp {padding: 6px 30px 0px;} .v2rsp {padding: 0px 10px;}}</style></hea=
d><body bgcolor=3D"#FFFFFF" style=3D"margin: 0; padding: 0;"><table border=
=3D0 cellpadding=3D0 cellspacing=3D0 height=3D"100%" style=3D"min-width: 34=
8px;" width=3D"100%"><Tbody><tr height=3D32px></tr><tr align=3Dcenter><td><=
table border=3D0 cellpadding=3D0 cellspacing=3D0 style=3D"padding-bottom: 2=
0px; max-width: 600px; min-width: 220px;"><Tbody><tr><td><table cellpadding=
=3D0 cellspacing=3D0><Tbody><tr><td></td><td><table border=3D0 cellpadding=
=3D0 cellspacing=3D0 style=3D"direction: ltr; padding-bottom: 7px;" width=
=3D"100%"><Tbody><tr><td align=3Dleft><img height=3D32 src=3D"https://www.g=
static.com/accountalerts/email/googlelogo_color_188x64dp.png" style=3D"widt=
h: 92px; height: 32px;" width=3D92></td><td align=3Dright style=3D"font-fam=
ily: Roboto-Light,Helvetica,Arial,sans-serif;">Keenan Mach</td><td align=3D=
right width=3D35><img height=3D28 src=3D"https://www.gstatic.com/accountale=
rts/email/anonymous_profile_photo.png" style=3D"width: 28px; height: 28px; =
border-radius: 50%;;" width=3D28></td></tr></Tbody></table></td><td></td></=
tr><tr><td height=3D5 style=3D"background:url(&#39;https://www.gstatic.com/=
accountalerts/email/hodor/4-corner-nw.png&#39;) top left no-repeat;" width=
=3D6><div></div></td><td height=3D5 style=3D"background:url(&#39;https://ww=
w.gstatic.com/accountalerts/email/hodor/4-pixel-n.png&#39;) top center repe=
at-x;"><div></div></td><td height=3D5 style=3D"background:url(&#39;https://=
www.gstatic.com/accountalerts/email/hodor/4-corner-ne.png&#39;) top right n=
o-repeat;" width=3D6><div></div></td></tr><tr><td style=3D"background:url(&=
#39;https://www.gstatic.com/accountalerts/email/hodor/4-pixel-w.png&#39;) c=
enter left repeat-y;" width=3D6><div></div></td><td><div style=3D"font-fami=
ly: Roboto-Regular,Helvetica,Arial,sans-serif;padding-left: 20px; padding-r=
ight: 20px;border-bottom: thin solid #f0f0f0; color: rgba(0,0,0,0.87); font=
-size: 24px;padding-bottom: 38px;padding-top: 40px;text-align: center; word=
-break: break-word;"><div class=3Dv2sp>New device signed in&nbsp;to<br><a s=
tyle=3D"font-family: Roboto-Regular,Helvetica,Arial,sans-serif;color: rgba(=
0,0,0,0.87); font-size: 16px; line-height: 1.8;">machkeenan@gmail.com</a></=
div></div><div style=3D"font-family: Roboto-Regular,Helvetica,Arial,sans-se=
rif; font-size: 13px; color: rgba(0,0,0,0.87); line-height: 1.6;padding-lef=
t: 20px; padding-right: 20px;padding-bottom: 32px; padding-top: 24px;"><div=
 class=3Dv2sp>Your Google Account was just signed in to from a new Windows =
device. You're getting this email to make sure it was you.<div style=3D"pad=
ding-top: 24px; text-align: center;"><a href=3D"https://accounts.google.com=
/AccountChooser?Email=3Dmachkeenan@gmail.com&amp;continue=3Dhttps://myaccou=
nt.google.com/alert/nt/1532824079000?rfn%3D31%26rfnc%3D1%26eid%3D1335108240=
994159626%26et%3D0%26asae%3D2%26anexp%3Dhsc-control_b" style=3D"display:inl=
ine-block; text-decoration: none;" target=3D"_blank"><table border=3D0 cell=
padding=3D0 cellspacing=3D0 style=3D"background-color: #4184F3; border-radi=
us: 2px; min-width: 90px;"><tbody><tr style=3D"height: 6px;"></tr><tr><td s=
tyle=3D"padding-left: 8px; padding-right: 8px; text-align: center;"><a href=
=3D"https://accounts.google.com/AccountChooser?Email=3Dmachkeenan@gmail.com=
&amp;continue=3Dhttps://myaccount.google.com/alert/nt/1532824079000?rfn%3D3=
1%26rfnc%3D1%26eid%3D1335108240994159626%26et%3D0%26asae%3D2%26anexp%3Dhsc-=
control_b" style=3D"font-family: Roboto-Regular,Helvetica,Arial,sans-serif;=
 color: #ffffff; font-weight: 400; line-height: 20px; text-decoration: none=
;font-size: 13px;text-transform: uppercase;" target=3D"_blank">Check activi=
ty</a></td></tr><tr style=3D"height: 6px;"></tr></tbody></table></a></div><=
/div></div></td><td style=3D"background:url(&#39;https://www.gstatic.com/ac=
countalerts/email/hodor/4-pixel-e.png&#39;) center left repeat-y;" width=3D=
6><div></div></td></tr><tr><td height=3D5 style=3D"background:url(&#39;http=
s://www.gstatic.com/accountalerts/email/hodor/4-corner-sw.png&#39;) top lef=
t no-repeat;" width=3D6><div></div></td><td height=3D5 style=3D"background:=
url(&#39;https://www.gstatic.com/accountalerts/email/hodor/4-pixel-s.png&#3=
9;) top center repeat-x"><div></div></td><td height=3D5 style=3D"background=
:url(&#39;https://www.gstatic.com/accountalerts/email/hodor/4-corner-se.png=
&#39;) top left no-repeat;" width=3D6><div></div></td></tr><tr><td></td><td=
><div style=3D"text-align: left;"><div style=3D"font-family: Roboto-Regular=
,Helvetica,Arial,sans-serif;color: rgba(0,0,0,0.54); font-size: 12px; line-=
height: 20px; padding-top: 10px;"><div>You received this email to let you k=
now about important changes to your Google Account and services.</div><div =
style=3D"direction: ltr;">&copy; 2018 Google LLC,<a class=3Dafal style=3D"f=
ont-family: Roboto-Regular,Helvetica,Arial,sans-serif;color: rgba(0,0,0,0.5=
4); font-size: 12px; line-height: 20px; padding-top: 10px;">1600 Amphitheat=
re Parkway, Mountain View, CA 94043, USA</a></div></div><div style=3D"displ=
ay: none !important; mso-hide:all; max-height:0px; max-width:0px;">15328240=
79000000</div></div></td><td></td></tr></Tbody></table></td></tr></Tbody></=
table></td></tr><tr height=3D32px></tr></Tbody></table><img height=3D1 src=
=3D"https://notifications.googleapis.com/email/a.gif?t=3DAFG8qyW7EHG25tw4PR=
U--sS0wMYstDrQVaobT2wpcSy97xXStTeTXYn8UlTMii-o4e1i_OzBFcv7tl5uE49uDDaHx0jfx=
EXaMQmtW1FR2FxhHEaOeXVVlqW4j9pJ15KRWvDP6RSkhmNE-rId3a93rbEAalMGEEODkWTRj7XU=
pOr-YA95QbQf9bXrYlkvXBi37pHvEUpwJoH08urekvfpdbCW96wf_4M_RYuR7clak5o" width=
=3D1></body></html>
--000000000000df484d0572186a76--"""