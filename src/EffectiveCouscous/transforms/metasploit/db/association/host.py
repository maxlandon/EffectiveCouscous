#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Base Transforms
from EffectiveCouscous.transforms.metasploit.db.association.netblock import NetblockToMetasploitWorkspace

# Maltego Entities
from canari.maltego.message import Field 

# Maltego Transforms
from canari.maltego.transform import Transform

# Custom Host Entities
from EffectiveCouscous.transforms.common.entities import (MetasploitHost, 
                                                          LinuxHost, 
                                                          WindowsHost, 
                                                          AppleHost)

# API
import json
from EffectiveCouscous.msftools import apitools

# GUI
import canari.easygui as gui
#--------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, Effective-Couscous Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#_____________________________________________________________________________________________#

#                                       Workspaces     
#_____________________________________________________________________________________________#


# Generic Host
#-----------------------------------------------------------------
class HostToMetasploitWorkspace(NetblockToMetasploitWorkspace):
    """Adds properties associated to a Metasploit workspace"""

    display_name = "To Metasploit Host Workspace"
    transform_set = 'Metasploit | DB | Association'
    input_type = MetasploitHost
    


# Windows OS
#-----------------------------------------------------------------
class WindowsHostToMetasploitWorkspace(NetblockToMetasploitWorkspace):
    """Adds properties associated to a Metasploit workspace"""

    display_name = "To Metasploit Host Workspace"
    transform_set = 'Metasploit | DB | Association'
    input_type = WindowsHost
    

# Apple OS
#-----------------------------------------------------------------
class AppleHostToMetasploitWorkspace(NetblockToMetasploitWorkspace):
    """Adds properties associated to a Metasploit workspace"""

    display_name = "To Metasploit Host Workspace"
    transform_set = 'Metasploit | DB | Association'
    input_type = AppleHost
    

# Linux OS
#-----------------------------------------------------------------
class LinuxHostToMetasploitWorkspace(NetblockToMetasploitWorkspace):
    """Adds properties associated to a Metasploit workspace"""

    display_name = "To Metasploit Host Workspace"
    transform_set = 'Metasploit | DB | Association'
    input_type = LinuxHost
    

