#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Fields
from canari.maltego.message import *

# Icons
from EffectiveCouscous.resource import (openport, closedport, timedoutport, unavailableport)


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, MSM Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'


# ------------------    Services Classification & Identification Strings    -------------------- #

webservices = ['http', 'https', 'possible_wls', "www", "ncacn_http", "ccproxy-http", "ssl/http", "http-proxy"]
sambaservices = ['samba', 'netbios-ssn', 'smb', 'microsoft-ds', 'netbios-ns', 'netbios-dgm', 'netbios']




# -------------------   Functions   --------------------- #

def getServiceEntity():
    pass
