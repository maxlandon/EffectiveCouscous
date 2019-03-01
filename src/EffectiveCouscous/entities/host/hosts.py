#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Fields
from canari.maltego.message import *

# OS Factory
from EffectiveCouscous.entitytools.os_factory import getOsIcon, getOsEntity

# Icons
from EffectiveCouscous.resource import systems
# -------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, MSM Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#_____________________________________________________________________________________________#

#                                           HOSTS
#_____________________________________________________________________________________________#


class MetasploitHost(Entity):
    # MetasploitHost is considered the base for host representation
    # in Maltego.
    # This will help because all atributes necessary to Metasploit-related
    # interaction will be easier (finding, creating, deleting, identifying 
    # a Metasploit Host)

    # Static Properties
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host'
    alias = "Metasploit Host"
    
    # Entity properties
    ipv4address = StringEntityField('address', display_name='IPv4 Address')
    id = StringEntityField('id', display_name='Host ID')
    created_at = StringEntityField('created_at', display_name="Host created at")
    mac = StringEntityField('mac', display_name='MAC')
    comm = StringEntityField('comm', display_name='Comm')
    name = StringEntityField('name', display_name='Host Name', is_value=True)
    state = StringEntityField('state', display_name='State')
    os_name = StringEntityField('os_name', display_name='OS Name', decorator=getOsIcon)
    os_flavor = StringEntityField('os_flavor', display_name='OS Flavor')
    os_sp = StringEntityField('os_sp', display_name='OS SP')
    os_lang = StringEntityField('os_lang', display_name='OS Language')
    arch = StringEntityField('arch', display_name='Architecture')
    workspace_id = StringEntityField('workspace_id', display_name='Workspace ID')
    updated_at = StringEntityField('updated_at', display_name='Host updated_at')
    purpose = StringEntityField('purpose', display_name='Purpose')
    info = StringEntityField('info', display_name='Info')
    comments = StringEntityField('comments', display_name='Comments')
    scope = StringEntityField('scope', display_name='Scope')
    virtual_host = StringEntityField('virtual_host', display_name='Virtual Host')
    note_count = StringEntityField('note_count', display_name='Note Count')
    vuln_count = StringEntityField('vuln_count', display_name='Vuln Count')
    service_count = StringEntityField('service_count', display_name='Service Count')
    host_detail_count = IntegerEntityField('host_detail_count', display_name='Host Detail Count')
    exploit_attempt_count = IntegerEntityField('exploit_attempt_count', display_name='Exploit Attempt Count')
    cred_count = StringEntityField('cred_count', display_name='Cred Count')
    detected_arch = StringEntityField('detected_arch', display_name='Detected Arch')
    os_family = StringEntityField('os_family', display_name='OS Family')



#---------------------------------------------------------------
#                   Operating System Base Hosts                |
#---------------------------------------------------------------

# Generic OS families, which might have some specialized properties added by some transforms.
# These generic OSs help to separate transforms, in case one transform set only applies to one OS.
# One example is Powershell Empire (a post-exploitation framework), which would only -mostly- apply
# to Windows hosts.

#   Linux
#_________________________________
class LinuxHost(MetasploitHost):
    # Static Properties
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host'
    alias = 'Linux Host'
    #  _type_ = 'Linux Host'


#   Windows
#_________________________________
class WindowsHost(MetasploitHost):
    # Static Properties
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host'
    alias = 'Windows Host'
    #  _type_ = 'Windows Host'


#   Apple
#_________________________________
class AppleHost(MetasploitHost):
    # Static Properties
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host'
    #  _type_ = 'Apple Host'



#   Embedded
#_________________________________
class EmbeddedOS(LinuxHost):
    # Static Properties
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host.os'


#   Others
#_________________________________

