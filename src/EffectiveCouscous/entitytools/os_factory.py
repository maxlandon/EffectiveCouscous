#!/usr/bin/env python3.7.2

# -------------------- Imports ----------------------- #

# Custom Entities
# Custom entities are directly imported in functions using them,
# so to avoid circular references during imports.

# Icons
from EffectiveCouscous.resource import systems, devices

# String search
import re
# ---------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = '2018'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#---------------------------------------------------------------------------------------#
#                                        OS FACTORY                                     #
#---------------------------------------------------------------------------------------#

# The OS Factory is responsible for determining various values related to Operating 
# Systems, throughout EffectiveCouscous.


# I - General Functions
#__________________________________
# 1) getOsEntity(os_name, name):    Is responsible for determining the type of Entity
#                                   to be returned for transforms spawning Hosts.
#                                   It looks at different fields of a Metasploit Host, 
#                                   prioritizes them and finds the good Entity.

# I - Decorator Functions
#__________________________________
# 2) getOsIcon(host, os):           Responsible for determining the type of Icon to be
#                                   returned for a given Entity Field of a Host.




# ----------------------------   General Functions   --------------------------------- #

def getOsEntity(os_name, name):
    from EffectiveCouscous.entities.host.hosts import (MetasploitHost,
                                                        WindowsHost,
                                                        LinuxHost,
                                                        AppleHost)
    os_entity = MetasploitHost()
    os_entity.icon_url = systems['generic']

    if os_name or name:
        if name:
            # 1) ________________________________________________________
            # Try with Name first, more reliable for Apple devices
            #....................................
            # Apple
            if re.search("macbook", name.lower(), re.I):
                os_entity = AppleHost()
                return os_entity
            elif re.search("ipad", name.lower(), re.I):
                os_entity = AppleHost()
                return os_entity
            #....................................
            # Linux
            elif ".home" in name.lower():
                os_entity = LinuxHost()
            # 2) ________________________________________________________
            # If the Name has not confirmed any device, use OS Name 
            elif os_name:
                #....................................
                # Windows
                if "windows" in os_name.lower():
                    if "windows 2003" in os_name.lower():
                        os_entity = WindowsHost()
                    elif "windows 2000" in os_name.lower():
                        os_entity = WindowsHost()
                    elif "windows 2008" in os_name.lower():
                        os_entity = WindowsHost()
                    elif "windows 2012" in os_name.lower():
                        os_entity = WindowsHost()
                    elif "windows xp" in os_name.lower():
                        os_entity = WindowsHost()
                    elif "windows 7" in os_name.lower():
                        os_entity = WindowsHost()
                    elif "windows vista" in os_name.lower():
                        os_entity = WindowsHost()
                    elif "windows 10" in os_name.lower():
                        os_entity = WindowsHost()
                    else:
                        os_entity = WindowsHost()
                    return os_entity
                #....................................
                # Apple
                elif re.search("ios", os_name.lower(), re.I):
                    os_entity = AppleHost()
                    return os_entity

                #....................................
                # Linux
                elif "linux" in os_name.lower():
                    if "arch" in os_name.lower():
                        os_entity = LinuxHost()
                    else:
                        os_entity = LinuxHost()
                    return os_entity
                #....................................
                # BSD
                #....................................
                # Embedded
                elif "embedded" in os_name.lower():
                    os_entity = EmbeddedOS()
        # 3) _______________________________________________________________
        # Both lookup methods failed if this point is reached. Spawn generic
        else:
            return os_entity
    # A Host needs to be returned anyway
    return os_entity





# ----------------------------   Decorator Functions   ------------------------------- #

def getOsIcon(host, os):
    from EffectiveCouscous.entities.host.hosts import (MetasploitHost,
                                                        WindowsHost,
                                                        LinuxHost,
                                                        AppleHost)
    if host.os_name or host.name:
        if host.name:
            # 1) ________________________________________________________
            # Try with Name first, more reliable for Apple devices
            #....................................
            # Apple
            if re.search("macbook", host.name.lower(), re.I):
                host.value = host.name
                host.icon_url = devices['macbook']
                return host
            elif re.search("ipad", host.name.lower(), re.I):
                host.value = host.name
                host.icon_url = devices['ipad']
                return host
            #....................................
            # Linux
            elif ".home" in host.name.lower():
                host.icon_url = systems['linux']
            # 2) ________________________________________________________
            # If the Name has not confirmed any device, use OS Name 
            elif host.os_name:
                    #....................................
                    # Windows
                    if "windows" in host.os_name.lower():
                        if "windows 2003" in host.os_name.lower():
                            host.icon_url = systems['windows2003']
                        elif "windows 2000" in host.os_name.lower():
                            host.icon_url = systems['windows2000']
                        elif "windows 2008" in host.os_name.lower():
                            host.icon_url = systems['windows2008']
                        elif "windows 2012" in host.os_name.lower():
                            host.icon_url = systems['windows2012']
                        elif "windows xp" in host.os_name.lower():
                            host.icon_url = systems['windowsxp']
                        elif "windows 7" in host.os_name.lower():
                            host.icon_url = systems['windows7']
                        elif "windows vista" in host.os_name.lower():
                            host.icon_url = systems['windowsvista']
                        elif "windows 10" in host.os_name.lower():
                            host.icon_url = systems['windows10']
                        else:
                            host.icon_url = systems['windows']
                    #....................................
                    # Apple
                    elif re.search("ios", host.os_name.lower(), re.I):
                        host.icon_url = systems['apple']

                    #....................................
                    # Linux
                    elif "linux" in host.os_name.lower():
                        if "arch" in host.os_name.lower():
                            host.icon_url = systems['archlinux']
                        #  if "debian"
                        #  if "ubuntu", etc...
                        else:
                            host.icon_url = systems['linux']
                    #....................................
                    # BSD
                    #....................................
                    # Embedded
                    elif "embedded" in host.os_name.lower():
                        host.icon_url = systems['generic']
        # 3) _______________________________________________________________
        # Both lookup methods failed if this point is reached. Spawn generic
        else:
            pass

