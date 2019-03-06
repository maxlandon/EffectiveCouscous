#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Custom Entities
from EffectiveCouscous.entities.service.web import *

# Icons
from EffectiveCouscous.resource import services
# -------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, EffectiveCouscous Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'


#---------------------------------------------------------------------------------------#
#                                   SERVICE FACTORY                                     #
#---------------------------------------------------------------------------------------#

# The Service Factory is responsible for determining the Entity spawned, related to various
# types of Services (web, samba, sntp, smtp, ssh, etc.)



# Services Classification & Identification Strings ------------------------------------- #

webservices = ['http', 'https', 'possible_wls', "www", "ncacn_http", "ccproxy-http", "ssl/http", "http-proxy"]
sambaservices = ['samba', 'netbios-ssn', 'smb', 'microsoft-ds', 'netbios-ns', 'netbios-dgm', 'netbios']



# Entity Generation -------------------------------------------------------------------- #

def getServiceEntity(service_name, service_info):
    from EffectiveCouscous.entities.service.base import MetasploitService

    service_entity = MetasploitService()
    name = service_name.lower()
    info = service_info.lower()

    if service_name or service_info:
         #  Test directly for service names & service info: unlikely to have info without name

        #  Web Services -------------------------------------------------- //
        if any(x in service_name for x in webservices):
            service_entity = WebService()
            if service_info:
                # Microsoft ............................/
                if 'iis' in info:
                    service_entity = IISWebService()
                elif 'httpapi' in info:
                    service_entity = MicrosoftHTTPAPI()
                # RPC ................................../
                elif 'rpc over http' in info:
                    service_entity = RPCoverHttp()
                # Databases ............................/
                elif 'oracle xml db' in info:
                    service_entity = OracleXMLDB()
                # Apache .............................../
                elif 'apache' in info:
                    if 'apache tomcat' in info:
                        service_entity = ApacheTomcat()
                    if 'apache php' in info:
                        service_entity = ApachePHP()
                    if 'apachehttpd' in info:
                        service_entity = ApacheHttpd()
                # VPN ................................../
                elif 'vpn' in info:
                    service_entity = CiscoVPN()
                # HTTP File Servers ..................../
                elif 'httpfileserver' in info:
                    service_entity = HTTPFileServer()
                # Other Web Servers ..................../
                elif 'lighttpd' in info:
                    service_entity = Lighttpd()
                elif 'nginx' in info:
                    service_entity = Nginx()
                elif 'jetty' in info:
                    service_entity = Jetty()
                elif 'nodejs' in info:
                    service_entity = NodeJS()
                elif 'waf' in info:
                    service_entity = WAF()
                elif 'oracle http server' in info:
                    service_entity = OracleHTTPServer()
                elif 'goahead' in info:
                    service_entity = GoAheadWebServer()
                elif 'webmin' in info:
                    service_entity = Webmin()
                elif 'rocket' in info:
                    service_entity = RocketWebServer()
                elif 'squid' in info:
                    service_entity = SquidProxyServer()
                elif 'communigate' in info:
                    service_entity = CommuniGatePro()

                """ Return Web Service if one is found """                 
                return service_entity

    # Return Service Entity anyway
    return service_entity




