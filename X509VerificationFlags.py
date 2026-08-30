class X509VerificationFlags:
    NoFlag = 0
    IgnoreNotTimeValid = 1
    IgnoreCtlNotTimeValid = 2
    IgnoreNotTimeNested = 3
    IgnoreInvalidBasicConstraints = 4
    AllowUnknownCertificateAuthority = 5
    IgnoreWrongUsage = 6
    IgnoreInvalidName = 7
    IgnoreInvalidPolicy = 8
    IgnoreEndRevocationUnknown = 9
    IgnoreCtlSignerRevocationUnknown = 10
    IgnoreCertificateAuthorityRevocationUnknown = 11
    IgnoreRootRevocationUnknown = 12
    AllFlags = 13
