#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Maltego Entities
from canari.maltego.entities import Service

# Custom Entities
from EffectiveCouscous.entities.service.base import MetasploitService

# Maltego Transforms
from canari.maltego.transform import Transform

# API
import json
from EffectiveCouscous.tools.msftools import apitools

# GUI
import canari.easygui as gui
#--------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, EffectiveCouscous Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'




#_____________________________________________________________________________________________#

#                                       Services
#_____________________________________________________________________________________________#


class ToMetasploitService(Transform):
    """Spawns a Metasploit Service"""

    display_name = 'To Metasploit Service'
    transform_set = 'Msf__DB                    | Service                 | Associate'
    input_type = Service 

    def do_transform(self, request, response, config):
        # Spawn new Metasploit Service
        msfService = MetasploitService()

        # Select Service
        url = config['EffectiveCouscous.local.baseurl'] + 'workspaces' 
        workspaces = apitools.get_json_dict(url, config)
        title = "Workspace Choice"
        msg = """Choose a Metasploit Workspace for Service selection"""
        wsNames = []
        for workspace in workspaces:
            wsNames.append(workspace['name'])
        ws_choice = gui.choicebox(title=title, msg=msg, choices=(wsNames))

        serviceUrl = config['EffectiveCouscous.local.baseurl'] + 'services'
        params = (('workspace', '{0}'.format(ws_choice)),)
        services = apitools.get_json_dict(serviceUrl, config, params=params)
        title = "Service Choice"
        msg = """Choose a Metasploit Service to associate with this Service"""
        serviceNames = []
        serviceInfos = []
        for service in services:
            info = '%s      %s       %s' % (service['host']['address'], service['port'], service['info'])
            serviceInfos.append(info)
            serviceNames.append(service['info'])
        serviceInfos.append("Add Service")
        rawChoice = gui.choicebox(title=title, msg=msg, choices=(serviceInfos))
        service = {} 
        if "Add Service" in rawChoice:
            service['info'] = "Add Service" 
        else:
            for s in services:
                if (s['info'] in rawChoice) and (str(s['port']) in rawChoice):
                    service = s

        # If existing Service 
        if service['info'] != "Add Service":
            if service['info'] == '': msfService.info = '-'
            else: msfService.info = service['info']
            if service['name'] == '': msfService.name = '-'
            else: msfService.name = service['name']
            if service['proto'] == '': msfService.proto = '-'
            else: msfService.proto = service['proto']
            if service['port'] == '': msfService.port = '-'
            else: msfService.port = service['port']
            if service['host']['id'] is None: msfService.host_id = '-'
            else: msfService.hostid = service['host']['id']
            if service['id'] == '': msfService.id = '-'
            else: msfService.serviceid = service['id']
            if service['host']['workspace_id'] == '': msfService.workspaceid = '-'
            else: msfService.workspaceid = service['host']['workspace_id']
            msfService.createdat = service['created_at']
            msfService.updatedat = service['updated_at']
            msfService.state = service['state']

            # Added Dynamic Icon Selection here, but should placed somewhere else
            if service['state'] == 'open':
                msfService.icon_url = openport
            if service['state'] == 'closed':
                msfService.icon_url = closedport
            if service['state'] == 'filtered':
                msfService.icon_url = timedoutport
            if service['state'] == 'unknown':
                msfService.icon_url = unavailableport

            response += msfService 

        # If new Service
        if service['info'] == "Add Service":
            title = "New Service"
            msg = "Add properties to create a Service in Metasploit"
            fieldNames = ['Workspace', 'Host IP', 'Port number', 'Protocol',
                            'Service Name', 'Text (Info)', 'State']  
            fieldValues = []
            fieldValues = gui.multenterbox(msg, fields=fieldNames)
            while 1:                                                 
                if fieldValues == None: break                        
                errmsg = ""                                          
                for i in range(len(fieldNames)):                     
                    if fieldValues[i].strip() == "":                 
                        errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])                                       
                if errmsg == "":                                     
                    break 
                fieldValues = gui.multenterbox(errmsg, fieldValues, fields=fieldNames)                                         

            # Create Workspace in Metasploit
            dict = {}
            dict['workspace'] = fieldValues[0]
            dict['host'] = fieldValues[1]
            dict['port'] = fieldValues[2]
            dict['proto'] = fieldValues[3]
            dict['name'] = fieldValues[4]
            dict['info'] = fieldValues[5]
            dict['state'] = fieldValues[6]
            data = json.dumps(dict)
            post = apitools.post_json(serviceUrl, data) 

            # Fetch new workspace in Metasploit
            newService = post.json()['data']

            msfService.info = newService['info']
            msfService.name = newService['name']
            msfService.proto = newService['proto']
            msfService.hostid = newService['host']['id']
            msfService.newServiceid = newService['id']
            msfService.workspaceid = newService['host']['workspace_id']
            msfService.createdat = newService['created_at']
            msfService.updatedat = newService['updated_at']

            # Added Dynamic Icon Selection here, but should placed somewhere else
            if newService['state'] == 'open':
                msfService.icon_url = openport
            if newService['state'] == 'closed':
                msfService.icon_url = closedport
            if newService['state'] == 'filtered':
                msfService.icon_url = timedoutport
            if newService['state'] == 'unknown':
                msfService.icon_url = unavailableport

            response += msfService
         
        return response
