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
__version__ = '0.1'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#_____________________________________________________________________________________________#

#                                       OPERATING SYSTEMS 
#_____________________________________________________________________________________________#


class MetasploitHost(Entity):
    # MetasploitHost is considered the base for host representation
    # in Maltego. Therefore, each host spawned from an equivalent
    # Metasploit Host, or spawned and creating an equivalent Metasploit
    # Host, will be an instance of this class
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host.MetasploitHost'
    alias = "MetasploitHost"
    
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


# Operating System Families
# ------------------------------

# Generic OS families, which might have some specialized properties added by some transforms.
# These generic OSs help to separate transforms, in case one transform set only applies to one OS.
# One example is Powershell Empire (a post-exploitation framework), which would only -mostly- apply
# to Windows hosts.

class LinuxHost(MetasploitHost):
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host'
    alias = 'Linux Host'
    #  _type_ = 'Linux Host'



class WindowsHost(MetasploitHost):
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host'
    alias = 'Windows Host'
    #  _type_ = 'Windows Host'



class AppleHost(MetasploitHost):
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host'
    #  _type_ = 'Apple Host'



# Embedded
# --------------------------

class EmbeddedOS(LinuxHost):
    _category_ = 'Operating Systems'
    _namespace_ = 'EffectiveCouscous.metasploit.host.os'




#_____________________________________________________________________________________________#

#                                           SERVICES 
#_____________________________________________________________________________________________#


class MetasploitService(Entity):
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service'
    _type_ = 'Metasploit Service' 

    display_name = StringEntityField('display_name', display_name='Display Name', is_value=True)
    info = StringEntityField('info', display_name='Info')
    name = StringEntityField('name', display_name='Name')
    proto = StringEntityField('proto', display_name='Protocol')
    port = StringEntityField('port', display_name='Port')
    host_id = StringEntityField('host_id', display_name='Host ID')
    id = StringEntityField('id', display_name='Service ID')
    workspace_id = StringEntityField('workspace_id', display_name='Workspace ID')
    created_at = StringEntityField('created_at', display_name='Created at')
    updated_at = StringEntityField('updated_at', display_name='Updated at')
    state = StringEntityField('state', display_name='State')

    # Icon
    # TO BE IMPLEMENTED INSTEAD OF IN TRANSFORMS


#_____________________________________________________________________________________________#

#                                           CREDENTIALS 
#_____________________________________________________________________________________________#


class MetasploitCredential(Entity):
    # The MetasploitCredential class does not contain all the properties stored in the 
    # Metasploit Credential JSON object. It is not necessary to retrieve them all, as
    # only having the cred ID and its service ID is sufficient for retrieving it and
    # processing it in other ways.
    _category_ = 'Penetration Testing'
    _namespace_ = 'metasploit.credential'
    
    name = Field('name', display_name='Name', is_value=True)
    id = Field('id', display_name='Credential ID' ) 
    logins_count = Field('logins_count', display_name='Logins Count')
    pub_username = Field('pub_username', display_name='Public Username')
    pub_type = Field('pub_type', display_name='Public Type')
    priv_data = Field('priv_data', display_name='Private Data')
    priv_type = Field('priv_type', display_name='Private Type')
    priv_jtr_format = Field('priv_jtr_format', display_name='Private JTR Format')
    origin_service_id = Field('origin_service_id', display_name='Origin Service ID')
    origin_type = Field('origin_type', display_name='Origin Type')
    origin_module = Field('origin_module', display_name='Origin Module')




#_____________________________________________________________________________________________#

#                                           HANDLERS 
#_____________________________________________________________________________________________#



class MetasploitExploitHandler(Entity):
    # The MetasploitExploitHandler is the base class for all Handler entities in Maltego.
    # Its properties are common to all Handlers
    _category_ = 'Metasploit Handler'
    _namespace_ = 'metasploit'

    payload = StringEntityField('payload', display_name='Payload')
    

class MetasploitBindHandler(Entity):
    # The MetasploitBindHandler is the base class for all Bind Handlers.
    # The MetasploitBindHandler has for properties the set of Options chosen when setting
    # the Bind Handler.
    _category_ = 'Metasploit Handler'
    _namespace_ = 'metasploit'

    # Base Options 
    LPORT = StringEntityField('LPORT', display_name='LPORT')
    RHOST = StringEntityField('RHOST', display_name='RHOST')
    EXITFUNC = EnumEntityField('EXITFUNC', choices=['', 'seh', 'thread', 'process', 'none'])

    # Advanced Options
    VERBOSE = EnumEntityField('VERBOSE', choices=['true', 'false'], display_name='VERBOSE')
    WORKSPACE = EnumEntityField('WORKSPACE', choices=['true', 'false'], display_name='WORKSPACE')

    AutoLoadStdapi = EnumEntityField('AutoLoadStdapi', choices=['true', 'false'], display_name='AutoLoadStdapi')
    AutoRunScript = StringEntityField('AutoRunScript', display_name='AutoRunScript')
    AutoSystemInfo = EnumEntityField('AutoSystemInfo', choices=['true', 'false'], display_name='AutoSystemInfo')
    AutoUnhookProcess = EnumEntityField('AutoUnhookProcess', choices=['true', 'false'], display_name='AutoUnhookProcess')
    AutoVerifySession = EnumEntityField('AutoVerifySession', choices=['true', 'false'], display_name='AutoVerifySession')
    AutoVerifySessionTimeout = IntegerEntityField('AutoVerifySessionTimeout', value=30, display_name='AutoVerifySessionTimeout')
    EnableStageEncoding= EnumEntityField('EnableStageEncoding', choices=['true', 'false'], display_name='EnableStageEncoding')
    EnableUnicodeEncoding= EnumEntityField('EnableUnicodeEncoding', choices=['true', 'false'], display_name='EnableUnicodeEncoding')
    HandlerSSLCert= StringEntityField('HandlerSSLCert', display_name='HandlerSSLCert')
    InitialAutoRunScript= StringEntityField('InitialAutoRunScript', display_name='InitialAutoRunScript')
    PayloadProcessCommandLine = StringEntityField('PayloadProcessCommandLine', display_name='PayloadProcessCommandLine')
    PayloadUUIDName = StringEntityField('PayloadUUIDName', display_name='PayloadUUIDName')
    PayloadUUIDRaw = StringEntityField('PayloadUUIDRaw', display_name='PayloadUUIDRaw')
    PayloadUUIDSeed = StringEntityField('PayloadUUIDSeed', display_name='PayloadUUIDSeed')
    PayloadUUIDTracking = EnumEntityField('PayloadUUIDTracking', choices=['true', 'false'], display_name='PayloadUUIDTracking')
    PrependMigrate = EnumEntityField('PrependMigrate', choices=['true', 'false'], display_name='PrependMigrate')
    PrependMigrateProc = StringEntityField('PrependMigrateProc', display_name='PrependMigrateProc')
    SessionCommunicationTimeout = IntegerEntityField('SessionCommunicationTimeout', value=300, display_name='SessionCommunicationTimeout')
    SessionExpirationTimeout = IntegerEntityField('SessionCommunicationTimeout', value=604800, display_name='SessionExpirationTimeout')
    SessionRetryTotal = IntegerEntityField('SessionRetryTotal', value=3600, display_name='SessionRetryTotal')
    SessionRetryWait = IntegerEntityField('SessionRetryWait', value=10, display_name='SessionRetryWait')
    StageEncoder = StringEntityField('StageEncoder', display_name='StageEncoder')
    StageEncoderSaveRegisters = StringEntityField('StageEncoderSaveRegisters', display_name='StageEncoderSaveRegisters')
    StageEncodingFallback = EnumEntityField('StageEncodingFallback', choices=['true', 'false'], display_name='StageEncodingFallback')
    


class MetasploitReverseHandler(Entity):
    # The MetasploitReverseHandler is the base class for all Reverse Handlers.
    # The MetasploitReverseHandler has for properties the set of Options chosen when setting
    # the Bind Handler.
    _category_ = 'Metasploit Handler'
    _namespace_ = 'metasploit'
    
    # Base options
    EXITFUNC = EnumEntityField('EXITFUNC', choices=['', 'seh', 'thread', 'process', 'none'])
    LHOST = StringEntityField('LHOST', display_name='LHOST') 
    LPORT = IntegerEntityField('LPORT', display_name='LPORT')
