#!/usr/bin/env python3.7.2

# -------------------- Imports ----------------------- #

from pkg_resources import resource_filename
from os import path
# ---------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = '2018'
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


#               Operating Systems
#------------------------------------------------------

systems = dict(
    #________________
    # Linux
    archlinux = imageicon('os', 'archlinux.png'),
    debian = imageicon('os', 'debian.png'),
    gentoo = imageicon('os', 'gentoo.png'),
    linux = imageicon('os', 'linux.png'),
    ubuntu = imageicon('os', 'ubuntu.png'),
    #________________
    # Microsoft
    windows = imageicon('os', 'windows.png'),
    windows2000 = imageicon('os', 'windows2000.jpeg'),
    windowsxp = imageicon('os', 'windowsxp.jpeg'),
    windows2003 = imageicon('os', 'windows2003.jpg'),
    windows2008 = imageicon('os', 'windows2008.jpeg'),
    #  windowsvista
    windows2012 = imageicon('os', 'windows-server-2012.jpg'),
    windows7 = imageicon('os', 'windows7.jpeg'),
    #  windows10
    
    #________________
    # HP
    hp = imageicon('os', 'hp.png'),
    #________________
    # Apple
    apple = imageicon('os', 'apple.gif'),
    #________________
    # Cisco
    cisco = imageicon('os', 'cisco.gif'),
    #________________
    # BSD
    freebsd = imageicon('os', 'freebsd.png'),
    #________________
    # Others
    #________________
    # Generic
    generic = imageicon('os', 'generic_host.png' )
)


#                   Devices
#------------------------------------------------------

devices = dict(
    #________________
    # Apple
    ipad = imageicon('device', 'ipad.png'),
    macbook = imageicon('device', 'macbook.png')
)


#                   Networking
#------------------------------------------------------

# Ports
unavailableport = imageicon('networking', 'unavailableport.gif')
openport = imageicon('networking', 'openport.gif')
timedoutport = imageicon('networking', 'timedoutport.gif')
closedport = imageicon('networking', 'closedport.gif')

# Interfaces
networkinterface = imageicon('networking', 'networkinterface.png')


#                   Services
#------------------------------------------------------

services = dict(
    generic_service = imageicon('services', 'service-icon.png'),
    #________________
    # Web Services
    iis_web_service = imageicon('services.web', 'microsoft-iis.png')

    #________________
    # Samba Services
        )



#                   Logos
#------------------------------------------------------

nmap = imagepath('logos', 'nmap.gif')
metasploit = imagepath('logos', 'metasploit.png')
nessus = imagepath('logos', 'nessus.png')






# -------------------------    MISCELLANEOUS   -------------------------- #

# flag
def flag(c):
    f = imageicon('flags', '%s.png' % c.lower())
    if path.exists(f[7:]):
        return f
    return None
