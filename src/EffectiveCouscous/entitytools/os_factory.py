#!/usr/bin/env python3.7.2

# -------------------- Imports ----------------------- #

# Custom Entities
from EffectiveCouscous.transforms.common.entities import *

# Icons
from EffectiveCouscous.resource import systems, devices

# String search
import re


__author__ = 'Maxime Landon'
__copyright__ = '2018'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'


# The Service Factory is responsible for determining the type of Host 
# Entity to to be spawned from a transform.
# It takes care of icons as well. This is not done directly in the 
# Entities file, because for one Operating System version there might
# be several different devices/hosts identified.
# The filtering is therefore made here, and is more fine-grained.



# -----------------------   Functions   ------------------------- #

def getOsEntity(os_name, name):
    os_entity = MetasploitHost()
    os_entity.icon_url = systems['generic']

    if os_name or name:
        if name:
            # 1) ________________________________________________________
            # Try with Name first, more reliable for Apple devices
            #....................................
            # Apple
            if re.search("macbook", name.lower(), re.I):
                os_entity = AppleOperatingSystem()
                os_entity.value = name
                os_entity.icon_url = devices['macbook']
                return os_entity
            elif re.search("ipad", name.lower(), re.I):
                os_entity = AppleOperatingSystem()
                os_entity.value = name
                os_entity.icon_url = devices['ipad']
                return os_entity
            #....................................
            # Linux
            elif ".home" in name.lower():
                os_entity = LinuxOperatingSystem()
                os_entity.icon_url = systems['linux']
            # 2) ________________________________________________________
            # If the Name has not confirmed any device, use OS Name 
            elif os_name:
                    #....................................
                    # Windows
                    if "windows" in os_name.lower():
                        if "windows 2003" in os_name.lower():
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windows2003']
                        elif "windows 2000" in os_name.lower():
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windows2000']
                        elif "windows 2008" in os_name.lower():
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windows2008']
                        elif "windows 2012" in os_name.lower():
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windows2012']
                        elif "windows xp" in os_name.lower():
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windowsxp']
                        elif "windows 7" in os_name.lower():
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windows7']
                        elif "windows vista" in os_name.lower():
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windowsvista']
                        elif "windows 10" in os_name.lower():
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windows10']
                        else:
                            os_entity = WindowsOperatingSystem()
                            os_entity.icon_url = systems['windows']
                        return os_entity
                    #....................................
                    # Apple
                    elif re.search("ios", os_name.lower(), re.I):
                        os_entity = IOS()
                        os_entity.icon_url = systems['apple']
                        return os_entity

                    #....................................
                    # Linux
                    elif "linux" in os_name.lower():
                        if "arch" in os_name.lower():
                            os_entity = LinuxOperatingSystem()
                            os_entity.icon_url = systems['archlinux']
                        #  if "debian"
                        #  if "ubuntu", etc...
                        else:
                            os_entity = LinuxOperatingSystem()
                            os_entity.icon_url = systems['linux']
                        return os_entity
                    #....................................
                    # BSD
                    #....................................
                    # Embedded
                    elif "embedded" in os_name.lower():
                        os_entity = EmbeddedOS()
                        os_entity.icon_url = systems['generic']
        # 3) _______________________________________________________________
        # Both lookup methods failed if this point is reached. Spawn generic
        else:
            return os_entity
    # A Host needs to be returned anyway
    return os_entity



