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
    return """Delivered-To: machkeenan@gmail.com
Received: by 2002:a17:90a:4d4d:0:0:0:0 with SMTP id l13-v6csp2422799pjh;
        Sat, 28 Jul 2018 17:28:01 -0700 (PDT)
X-Received: by 2002:a6b:6709:: with SMTP id b9-v6mr9003935ioc.272.1532824081583;
        Sat, 28 Jul 2018 17:28:01 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1532824081; cv=none;
        d=google.com; s=arc-20160816;
        b=mplH5YV1LL2yLRczcs3oFWNg9wpuEfvjch3j3UsbHNfJddIB5A0yk9BrSKqRemc1oo
         C555toW5guTYPmDXlcDhJ3D5NyTWiAiW5fNbq7+xLz1UKgiOiEqbfZgqiFYqqDQBAcqd
         +6Lk5OINCQXjZ4Yyban94UCaTqFmN249gFYkn1ReGtXkWB4QcAn5HFA8x5Yuov3AHxXT
         L96+nYkuJfkIHWWt6m/dUrIbvFSLKK4T1oYt/Mgn8sA/uFrB9uzhWAz84EBtPP5g3E/Z
         pVgN9x8W1gzZZK2/SyOo2nDFb8XzmKtXW8qDIgcAfCbX1SIYeYYeXYzDlNPhXdA0+BDp
         kitA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=to:from:subject:message-id:feedback-id:date:mime-version
         :dkim-signature:arc-authentication-results;
        bh=48bImmZYHnJrEzzmfY5LHm/WUeKdXiM6zhFUWts1D6Y=;
        b=c7hvEqXASF/Zba5QK5VrLe2UAk8U8BRTT86JWoP8TLUJVpb1NSBUqi2yVP7h6FvElc
         +IGBhSyDmOHQc8nR9v4d6WiXss9r/RlynUdiFNctaHAgvIATN6fZk9IC3wLyRv8Xyi2d
         rKyMXxWqe/SqJIp5x2b7UIyn72S6AsdhsEvzGOCLdwuGJrA0JGql5qhNcznaIJ/U6BeU
         ppznG5nmgaxO19ykNnRxlyJ1r3ikga3QcJeTGGB5X1+9U/l8ik5buouH78SVkpLfAd3U
         TDCGuO1LRcJLxDdpAThQdjuHvudE9U8/qeH3329x3oRexQueBZx2gMeoB0I9+ogf3OUA
         c0IQ==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@accounts.google.com header.s=20161025 header.b=tn5NSYTT;
       spf=pass (google.com: domain of 3eqpdwwgtcnolm-pcnjwyaamslrq.emmejc.amkkyaficclylekygj.amk@gaia.bounces.google.com designates 209.85.220.69 as permitted sender) smtp.mailfrom=3EQpdWwgTCnolm-pcnjwYaamslrq.emmejc.amkkYaficclYlekYgj.amk@gaia.bounces.google.com;
       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=accounts.google.com
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
dHRwczovL215YWNjb3VudC5nb29nbGUuY29tL2FsZXJ0L250LzE1MzI4MjQwNzkwMDA/cmZuJTNE
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
dHRwczovL215YWNjb3VudC5nb29nbGUuY29tL2FsZXJ0L250LzE1MzI4MjQwNzkwMDA/cmZuJTNE
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