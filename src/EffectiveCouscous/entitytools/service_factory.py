#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Custom Entities
# This line is not supposed to be here. In functions, import * is not possible.
# This should be changed so as to avoid circular references.
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

# The Service Factory is responsible for determining various values related to various
# types of Services (web, samba, sntp, smtp, ssh, etc.)


# I - General Functions
#__________________________________
# 1) getServiceEntity(service_name, service_info):  Is responsible for determining the type of Entity
#                                                   to be returned for transforms spawning Services.
#                                                   It looks at different fields of a Service, 
#                                                   prioritizes them and finds the good Entity.

# I - Decorator Functions
#__________________________________
# 2) getServiceIcon(service, service_info):     Responsible for determining the type of Icon to be
#                                               returned for a given Entity Field of a Service.

# 3) getStateIcon(service, state):  Responsible for determining the listening state of a Service,
#                                   and for returning the good icon.





# --------------    Services Classification & Identification Strings    ---------------- #

webservices = ['http', 'https', 'possible_wls', "www", "ncacn_http", "ccproxy-http", "ssl/http", "http-proxy"]
sambaservices = ['samba', 'netbios-ssn', 'smb', 'microsoft-ds', 'netbios-ns', 'netbios-dgm', 'netbios']




# ------------------------------   General Functions   --------------------------------- #

def getServiceEntity(service_name, service_info):
    from EffectiveCouscous.entities.service.base import MetasploitService

    service_entity = MetasploitService()
    name = service_name.lower()
    info = service_info.lower()

    if service_name or service_info:
        # Test directly for service names & service info: unlikely to have info without name
        #_________________________________________________________
        #
        #                   WEB SERVICES
        #_________________________________________________________
        if any(x in service_name for x in webservices):
            if service_info:
                #-------------------------------------
                # Microsoft
                if 'iis' in info:
                    service_entity = IISWebservice()
                elif 'httpapi' in info:
                    service_entity = MicrosoftHTTPAPI()
                #-------------------------------------
                # RPC
                elif 'rpc over http' in info:
                    service_entity = RPCoverHttp()
                #-------------------------------------
                # Databases
                elif 'oracle xml db' in info:
                    service_entity = OracleXMLDB()
                #-------------------------------------
                # Apache
                elif 'apache' in info:
                    if 'apache tomcat' in info:
                        service_entity = ApacheTomcat()
                    if 'apache php' in info:
                        service_entity = ApachePHP()
                    if 'apachehttpd' in info:
                        service_entity = ApacheHttpd()
                #-------------------------------------
                # VPN
                elif 'vpn' in info:
                    service_entity = CiscoVPN()
                #-------------------------------------
                # HTTP File Servers
                elif 'httpfileserver' in info:
                    service_entity = HTTPFileServer()
                #-------------------------------------
                # Other Web Servers
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
                    
                # Return Web Service if one is found
                return service_entity

    # Return Service Entity anyway
    return service_entity



# ----------------------------   Decorator Functions   ------------------------------- #

def getServiceIcon(service, service_info):
    pass


def getStateIcon(service, state):
    from EffectiveCouscous.resource import (openport, closedport, timedoutport, unavailableport)
    if state == 'open':
        service.state_icon = openport
    if state == 'closed':
        service.state_icon = closedport
    if state == 'filtered':
        service.state_icon = timedoutport
    if state == 'unknown':
        service.state_icon = unavailableport
