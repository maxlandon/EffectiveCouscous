#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Maltego Entities
from canari.maltego.entities import IPv4Address
from canari.maltego.message import Field

# Maltego Transforms
from canari.maltego.transform import Transform

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

#                                           Host
#_____________________________________________________________________________________________#


class AppendHostProperties(Transform):
    """Adds Host Properties to this IPv4Address"""

    display_name = 'Append Host Properties'
    transform_set = 'Metasploit | DB | Association'
    input_type = IPv4Address 

    def do_transform(self, request, response, config):
        ipAddress = request.entity
        ipValue = request.entity.value

        # Select Workspaces 
        url = config['EffectiveCouscous.local.baseurl'] + 'workspaces' 
        workspaces = apitools.get_json_dict(url, config)
        title = "Workspace Choice"
        msg = "Please choose a workspace for Host selection"
        wsNames = []
        for workspace in workspaces:
            wsNames.append(workspace['name'])
        choice = gui.choicebox(title=title, msg=msg, choices=(wsNames))

        # Select Hosts 
        url = config['EffectiveCouscous.local.baseurl'] + 'hosts' 
        params = (('workspace', '{0}'.format(choice)),)
        hosts = apitools.get_json_dict(url, config, params=params)
        title = "Host Choice"
        msg = """Choose a Metasploit Host to associate with this workspace \n
            Note: This will not automatically assign the IPv4Address
            value to workspace's network boundary."""
        hostInfos = []
        hostNames = []
        for host in hosts:
            hostInfo = '{0}      {1}'.format(host['address'], host['name'])
            hostInfos.append(hostInfo)
            hostNames.append(host['name'])
        hostInfos.append("Add Host")
        rawChoice = gui.choicebox(title=title, msg=msg, choices=(hostInfos))
        host = {}
        if "Add Host" in rawChoice:
            host['name'] = "Add Host" 
        else:
            for h in hosts:
                if h['address'] in rawChoice:
                    host = h

        # If existing host
        if host['name'] != "Add Host":
            ipAddress['ipv4-address'] = host['address']
            ipAddress += Field('id', host['id'], display_name='Host ID')
            ipAddress += Field('workspace_id', host['workspace_id'], display_name='Workspace ID')
            response + ipAddress

        # If New Host
        if host['name'] == 'Add Host':
            url = config['EffectiveCouscous.local.baseurl'] + 'hosts'
            title = "New Host"
            msg = """Enter Host properties for creating a Host in Metasploit"""
            fieldNames = ["Address", "MAC", "Host Name", "OS Name", "OS Flavor",
                            'OS SP', 'OS Language', 'Purpose', 'Info', 'Comments', 'Scope',
                            'Virtual Host', 'Architecture', 'State']
            fieldValues = []
            fieldValues = gui.multenterbox(title=title, msg=msg, fields=fieldNames, values=fieldValues)
            while 1:                                                 
                if fieldValues == None: break                        
                errmsg = ""                                          
                for i in range(len(fieldNames)):                     
                    if fieldValues[i].strip() == "":                 
                        errmsg += ('"%s" is a required field.\n\n' % fieldNames[i]) 
                if errmsg == "":                                     
                    break 
                fieldValues = gui.multenterbox(errmsg, fieldValues, fields=fieldNames)                                         
            dict = {}
            dict['workspace'] = choice 
            dict['host'] = fieldValues[0]
            dict['mac'] = fieldValues[1]
            dict['name'] = fieldValues[2]
            dict['os_name'] = fieldValues[3]
            dict['os_flavor'] = fieldValues[4]
            dict['os_sp'] = fieldValues[5]
            dict['os_lang'] = fieldValues[6]
            dict['purpose'] = fieldValues[7]
            dict['info'] = fieldValues[8]
            dict['comments'] = fieldValues[9]
            dict['scope'] = fieldValues[10]
            dict['virtual_host'] = fieldValues[11]
            dict['arch'] = fieldValues[12]
            dict['state'] = fieldValues[13]

            data = json.dumps(dict)
            post = apitools.post_json(url, data, config)

            # Fetch attributes of new Host
            host_dict = post.json()['data']
            ipAddress['ipv4-address'] = host_dict['address']
            ipAddress += Field('id', host_dict['id'], display_name='Host ID')
            ipAddress += Field('workspace_id', host['workspace_id'], display_name='Workspace ID')
            response + ipAddress

        return response
