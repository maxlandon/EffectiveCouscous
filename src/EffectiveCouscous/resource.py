#!/usr/bin/env python3.7.2

# -------------------- Imports ----------------------- #

from pkg_resources import resource_filename
from os import path
# ---------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, EffectiveCouscous Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'

images = 'EffectiveCouscous.resources.images'
etc = 'EffectiveCouscous.resources.etc'



# -----------------------   Utility Functions   ------------------------- #

def imageicon(cat, name):
    return 'file://%s' % resource_filename('.'.join([ images, cat ]), name)

def imagepath(cat, name):
    return '%s' % resource_filename('.'.join([ images, cat ]), name)




#_____________________________________________________________________________________________#

#                                           IMAGES     
#_____________________________________________________________________________________________#


# Operating Systems --------------------------------------------------------------------------#

systems = dict(
    # Linux --------------------------------- /
    archlinux = imageicon('os', 'archlinux.png'),
    debian = imageicon('os', 'debian.png'),
    gentoo = imageicon('os', 'gentoo.png'),
    linux = imageicon('os', 'linux.png'),
    ubuntu = imageicon('os', 'ubuntu.png'),

    # Microsoft ----------------------------- /
    windows = imageicon('os', 'windows.png'),
    windows2000 = imageicon('os', 'windows2000.jpeg'),
    windowsxp = imageicon('os', 'windowsxp.jpeg'),
    windows2003 = imageicon('os', 'windows2003.jpg'),
    windows2008 = imageicon('os', 'windows2008.jpeg'),
    #  windowsvista
    windows2012 = imageicon('os', 'windows-server-2012.jpg'),
    windows7 = imageicon('os', 'windows7.jpeg'),
    #  windows10
    

    # HP ------------------------------------ /
    hp = imageicon('os', 'hp.png'),

    # Apple --------------------------------- /
    apple = imageicon('os', 'apple.gif'),

    # Cisco --------------------------------- /
    cisco = imageicon('os', 'cisco.gif'),

    # BSD ----------------------------------- /
    freebsd = imageicon('os', 'freebsd.png'),

    # Others -------------------------------- /
    # Generic ------------------------------- /
    generic = imageicon('os', 'generic_host.png' )

)


# Devices ------------------------------------------------------------------------------------#

devices = dict(
    # Apple --------------------------------- /
    ipad = imageicon('device', 'ipad.png'),
    macbook = imageicon('device', 'macbook.png')

    # Others -------------------------------- /
)


# Networking ---------------------------------------------------------------------------------#

    # Ports ----------------------- /
unavailableport = imageicon('networking', 'unavailableport.gif')
openport = imageicon('networking', 'openport.gif')
timedoutport = imageicon('networking', 'timedoutport.gif')
closedport = imageicon('networking', 'closedport.gif')

    # Interfaces ------------------ /
network_interface = imageicon('networking', 'networkinterface.png')



# Services -----------------------------------------------------------------------------------#

services = dict(
    # Generic ---------------------------- / 
    generic_service = imageicon('services', 'service-icon.png'),

    # Web Services ----------------------- / 
    generic_webservice = imageicon('services.web', 'web-service.png'),
    iis_web_service = imageicon('services.web', 'microsoft-iis.png'),
    nginx_web_service = imageicon('services.web', 'nginx.png')

    # Samba Services ----------------------- / 
    )



# Tools --------------------------------------------------------------------------------------#

tools = dict(
    metasploit = imageicon('logos', 'metasploit.png'),
    nmap = imageicon('logos', 'nmap.gif'),
    nessus = imageicon('logos', 'nessus.png')
    )





# -------------------------    MISCELLANEOUS   -------------------------- #

# flag
def flag(c):
    f = imageicon('flags', '%s.png' % c.lower())
    if path.exists(f[7:]):
        return f
    return None
