#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Base Custom entities
#  from EffectiveCouscous.entities.service.base import MetasploitService

# Fields
from canari.maltego.message import *
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


# The WebService class is the base class for all Web Services
class WebService(Entity):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'Web Service'


# Microsoft
#________________________________
class IISWebservice(WebService):
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service.web'
    _alias_ = 'IIS Web Service'


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


