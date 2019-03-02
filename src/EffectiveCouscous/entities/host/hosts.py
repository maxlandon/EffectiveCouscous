#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Maltego Entities
from canari.maltego.entities import Entity

# Fields
from canari.maltego.message import *

# OS Factory
from EffectiveCouscous.entitytools.os_factory import getOsIcon, getOsEntity

# Tool Factory
from EffectiveCouscous.entitytools.tool_factory import getOriginTool
# -------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, MSM Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



# 1) MetasploitHost
#__________________________
# MetasploitHost is considered the base for host representation
# in Maltego.
# This will help because all atributes necessary to Metasploit-related
# interaction will be easier (finding, creating, deleting, identifying 
# a Metasploit Host)


# 2) Operating System based Hosts
#___________________________________
# Generic OS families, which might have some specialized properties added by some transforms.
# These generic OSs help to separate transforms, in case one transform set only applies to one OS.
# One example is Powershell Empire (a post-exploitation framework), which would only -mostly- apply
# to Windows hosts.

# The redundancy of attributes, instead of subclassing the MetasploitHost class, is for sake or
# clarity and consistency with the Maltego GUI, in which each Entity had to be entered manually, 
# as well as all of its respective properties, despite them being the same for all Host Entities.



#_____________________________________________________________________________________________#

#                                           HOSTS
#_____________________________________________________________________________________________#


class MetasploitHost(Entity):
    _category_ = 'Metasploit | Hosts'
    _namespace_ = 'EffectiveCouscous.host'

    name = StringEntityField('name', display_name='Host Name', is_value=True)
    ipv4address = StringEntityField('ipv4address', display_name='IPv4 Address')
    id = StringEntityField('id', display_name='Host ID')
    created_at = StringEntityField('created_at', display_name='Created At')
    mac = StringEntityField('mac', display_name='MAC')
    comm = StringEntityField('comm', display_name='Comm')
    state = StringEntityField('state', display_name='State')
    os_name = StringEntityField('os_name', display_name='OS Name')
    os_flavor = StringEntityField('os_flavor', display_name='OS Flavor')
    os_sp = StringEntityField('os_sp', display_name='OS SP')
    os_lang = StringEntityField('os_lang', display_name='OS Language')
    arch = StringEntityField('arch', display_name='Architecture')
    workspace_id = StringEntityField('workspace_id', display_name='Workspace ID')
    updated_at = StringEntityField('updated_at', display_name='Updated At')
    purpose = StringEntityField('purpose', display_name='Purpose')
    info = StringEntityField('info', display_name='Info')
    comments = StringEntityField('comments', display_name='Comments')
    scope = StringEntityField('scope', display_name='Scope')
    virtual_host = StringEntityField('virtual_host', display_name='Virtual Host')
    note_count = IntegerEntityField('note_count', display_name='Note Count')
    service_count = IntegerEntityField('service_count', display_name='Service Count')
    vuln_count = IntegerEntityField('vuln_count', display_name='Vulnerability Count')
    exploit_attempt_count = IntegerEntityField('exploit_attempt_count', display_name='Exploit Attempt Count')
    host_detail_count = IntegerEntityField('host_detail_count', display_name='Host Detail Count')
    cred_count = IntegerEntityField('cred_count', display_name='Credential Count')
    detected_arch = StringEntityField('detected_arch', display_name='Detected Architecture')
    os_family = StringEntityField('os_family', display_name='OS Family')

    # Icon Properties
    origin_tool = StringEntityField('origin_tool', display_name='Origin Tool', decorator=getOriginTool)
    tool_icon = StringEntityField('tool_icon', display_name='Tool Icon')




#---------------------------------------------------------------
#                   Operating System Base Hosts                |
#---------------------------------------------------------------

#   Linux
#_________________________________
class LinuxHost(Entity):
    _category_ = 'Metasploit | Hosts'
    _namespace_ = 'EffectiveCouscous.host.MetasploitHost'

    name = StringEntityField('name', display_name='Host Name', is_value=True)
    ipv4address = StringEntityField('ipv4address', display_name='IPv4 Address')
    id = StringEntityField('id', display_name='Host ID')
    mac = StringEntityField('mac', display_name='MAC')
    created_at = StringEntityField('created_at', display_name='Created At')
    state = StringEntityField('state', display_name='State')
    comm = StringEntityField('comm', display_name='Comm')
    os_name = StringEntityField('os_name', display_name='OS Name')
    os_flavor = StringEntityField('os_flavor', display_name='OS Flavor')
    os_sp = StringEntityField('os_sp', display_name='OS SP')
    os_lang = StringEntityField('os_lang', display_name='OS Language')
    arch = StringEntityField('arch', display_name='Architecture')
    workspace_id = StringEntityField('workspace_id', display_name='Workspace ID')
    updated_at = StringEntityField('updated_at', display_name='Updated At')
    purpose = StringEntityField('purpose', display_name='Purpose')
    info = StringEntityField('info', display_name='Info')
    comments = StringEntityField('comments', display_name='Comments')
    scope = StringEntityField('scope', display_name='Scope')
    virtual_host = StringEntityField('virtual_host', display_name='Virtual Host')
    note_count = IntegerEntityField('note_count', display_name='Note Count')
    service_count = IntegerEntityField('service_count', display_name='Service Count')
    vuln_count = IntegerEntityField('vuln_count', display_name='Vulnerability Count')
    exploit_attempt_count = IntegerEntityField('exploit_attempt_count', display_name='Exploit Attempt Count')
    host_detail_count = IntegerEntityField('host_detail_count', display_name='Host Detail Count')
    cred_count = IntegerEntityField('cred_count', display_name='Credential Count')
    detected_arch = StringEntityField('detected_arch', display_name='Detected Architecture')
    os_family = StringEntityField('os_family', display_name='OS Family')

    # Icon Properties
    origin_tool = StringEntityField('origin_tool', display_name='Origin Tool', decorator=getOriginTool)
    tool_icon = StringEntityField('tool_icon', display_name='Tool Icon')


#   Windows
#_________________________________
class WindowsHost(Entity):
    _category_ = 'Metasploit | Hosts'
    _namespace_ = 'EffectiveCouscous.host.MetasploitHost'

    name = StringEntityField('name', display_name='Host Name', is_value=True)
    ipv4address = StringEntityField('ipv4address', display_name='IPv4 Address')
    id = StringEntityField('id', display_name='Host ID')
    created_at = StringEntityField('created_at', display_name='Created At')
    mac = StringEntityField('mac', display_name='MAC')
    comm = StringEntityField('comm', display_name='Comm')
    state = StringEntityField('state', display_name='State')
    os_name = StringEntityField('os_name', display_name='OS Name')
    os_flavor = StringEntityField('os_flavor', display_name='OS Flavor')
    os_sp = StringEntityField('os_sp', display_name='OS SP')
    os_lang = StringEntityField('os_lang', display_name='OS Language')
    arch = StringEntityField('arch', display_name='Architecture')
    workspace_id = StringEntityField('workspace_id', display_name='Workspace ID')
    updated_at = StringEntityField('updated_at', display_name='Updated At')
    purpose = StringEntityField('purpose', display_name='Purpose')
    info = StringEntityField('info', display_name='Info')
    comments = StringEntityField('comments', display_name='Comments')
    scope = StringEntityField('scope', display_name='Scope')
    virtual_host = StringEntityField('virtual_host', display_name='Virtual Host')
    note_count = IntegerEntityField('note_count', display_name='Note Count')
    service_count = IntegerEntityField('service_count', display_name='Service Count')
    vuln_count = IntegerEntityField('vuln_count', display_name='Vulnerability Count')
    exploit_attempt_count = IntegerEntityField('exploit_attempt_count', display_name='Exploit Attempt Count')
    host_detail_count = IntegerEntityField('host_detail_count', display_name='Host Detail Count')
    cred_count = IntegerEntityField('cred_count', display_name='Credential Count')
    detected_arch = StringEntityField('detected_arch', display_name='Detected Architecture')
    os_family = StringEntityField('os_family', display_name='OS Family')

    # Icon Properties
    origin_tool = StringEntityField('origin_tool', display_name='Origin Tool', decorator=getOriginTool)
    tool_icon = StringEntityField('tool_icon', display_name='Tool Icon')


#   Apple
#_________________________________
class AppleHost(Entity):
    _category_ = 'Metasploit | Hosts'
    _namespace_ = 'EffectiveCouscous.host.MetasploitHost'

    name = StringEntityField('name', display_name='Host Name', is_value=True)
    ipv4address = StringEntityField('ipv4address', display_name='IPv4 Address')
    id = StringEntityField('id', display_name='Host ID')
    created_at = StringEntityField('created_at', display_name='Created At')
    mac = StringEntityField('mac', display_name='MAC')
    comm = StringEntityField('comm', display_name='Comm')
    state = StringEntityField('state', display_name='State')
    os_name = StringEntityField('os_name', display_name='OS Name')
    os_flavor = StringEntityField('os_flavor', display_name='OS Flavor')
    os_sp = StringEntityField('os_sp', display_name='OS SP')
    os_lang = StringEntityField('os_lang', display_name='OS Language')
    arch = StringEntityField('arch', display_name='Architecture')
    workspace_id = StringEntityField('workspace_id', display_name='Workspace ID')
    updated_at = StringEntityField('updated_at', display_name='Updated At')
    purpose = StringEntityField('purpose', display_name='Purpose')
    info = StringEntityField('info', display_name='Info')
    comments = StringEntityField('comments', display_name='Comments')
    scope = StringEntityField('scope', display_name='Scope')
    virtual_host = StringEntityField('virtual_host', display_name='Virtual Host')
    note_count = IntegerEntityField('note_count', display_name='Note Count')
    service_count = IntegerEntityField('service_count', display_name='Service Count')
    vuln_count = IntegerEntityField('vuln_count', display_name='Vulnerability Count')
    exploit_attempt_count = IntegerEntityField('exploit_attempt_count', display_name='Exploit Attempt Count')
    host_detail_count = IntegerEntityField('host_detail_count', display_name='Host Detail Count')
    cred_count = IntegerEntityField('cred_count', display_name='Credential Count')
    detected_arch = StringEntityField('detected_arch', display_name='Detected Architecture')
    os_family = StringEntityField('os_family', display_name='OS Family')

    # Icon Properties 
    origin_tool = StringEntityField('origin_tool', display_name='Origin Tool', decorator=getOriginTool)
    tool_icon = StringEntityField('tool_icon', display_name='Tool Icon')


#   Embedded
#_________________________________
class EmbeddedOS(LinuxHost):
    # Static Properties
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host.os'


#   Others
#_________________________________

