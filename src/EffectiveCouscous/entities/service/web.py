#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Maltego Entities
from canari.maltego.entities import Entity

# Fields
from canari.maltego.message import *

# System-wide Icons
from EffectiveCouscous.entitytools.icon_factory import getOriginTool, getStateIcon
# -------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, EffectiveCouscous Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#_____________________________________________________________________________________________#

#                                       WEB SERVICES 
#_____________________________________________________________________________________________#


# Base Web Service ---------------------------------------------------------------------------#

class WebService(Entity):

    _category_ = 'Metasploit | Services | Web'
    _namespace_ = 'EffectiveCouscous.MetasploitService'

    # Entity properties
    display = StringEntityField('display', display_name='Display Name', is_value=True)
    proto = StringEntityField('proto', display_name='Protocol')
    name = StringEntityField('name', display_name='Name')
    info = StringEntityField('info', display_name='Info')
    port = StringEntityField('port', display_name='Port')
    state = StringEntityField('state', display_name='State', decorator=getStateIcon)
    host_id = StringEntityField('host_id', display_name='Host ID')
    id = StringEntityField('id', display_name='Service ID')
    workspace_id = StringEntityField('workspace_id', display_name='Workspace ID')
    created_at = StringEntityField('created_at', display_name='Created At')
    updated_at = StringEntityField('updated_at', display_name='Updated At')

    # Decorator properties
    origin_tool = StringEntityField('origin_tool', display_name='Origin Tool', decorator=getOriginTool)
    tool_icon = StringEntityField('tool_icon', display_name='Tool Icon')
    state_icon = StringEntityField('state_icon', display_name='State Icon')


# Microsoft ----------------------------------------------------------------------------------#

class IISWebService(Entity):

    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.MetasploitService.WebService'


class MicrosoftHTTPAPI(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Microsoft HTTP API'


# RPC
#________________________________
class RPCoverHttp(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'RPC over HTTP'


# Database
#________________________________
class OracleXMLDB(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Oracle XML DB'


# Apache
#________________________________
class ApacheTomcat(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Apache Tomcat'


class ApachePHP(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Apache PHP'


class ApacheHttpd(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Apache HTTPd'


# File Servers
#________________________________
class HTTPFileServer(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'HTTP File Server'


# VPN
#________________________________
class CiscoVPN(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Cisco VPN'


# Other Web Servers
#________________________________
class Lighttpd(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Lighttpd'


class Nginx(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Nginx'


class Jetty(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Jetty'


class NodeJS(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Node JS'


class WAF(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'WAF'


class OracleHTTPServer(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Oracle HTTP Server'


class GoAheadWebServer(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'GoAhead Web Server'


class Webmin(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Webmin'


class RocketWebServer(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Rocket Web Server'


class SquidProxyServer(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Squid Proxy Server'


class CommuniGatePro(Entity):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'CommuniDate Pro'


