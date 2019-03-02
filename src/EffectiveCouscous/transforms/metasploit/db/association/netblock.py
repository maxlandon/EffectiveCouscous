#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Custom Entities
from EffectiveCouscous.entities.infrastructure import Netblock

# Maltego Entities
from canari.maltego.message import StringEntityField, Field

# Maltego Transforms
from canari.maltego.transform import Transform

# API
import json
from EffectiveCouscous.msftools import apitools

# GUI
import canari.easygui as gui

# Icons
from EffectiveCouscous.resource import tools
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

#                                       Workspaces     
#_____________________________________________________________________________________________#


class NetblockToMetasploitWorkspace(Transform):
    """Adds properties associated to a Metasploit workspace"""

    display_name = "To Metasploit Workspace"
    transform_set = 'Metasploit | DB | Association'
    input_type = Netblock

    def do_transform(self, request, response, config):
        netblock = request.entity
        netblockBoundary = request.entity.value

        # Select Workspaces
        url = config['EffectiveCouscous.local.baseurl'] + 'workspaces' 
        workspaces = apitools.get_json_dict(url, config)
        title = "Workspace Choice"
        msg = "Choose a Metasploit workspace to associate with this Netblock"

        wsNames = []
        for workspace in workspaces:
            wsNames.append(workspace['name'])
        wsNames.append("Add Workspace")

        workspace = {} 
        choice = gui.choicebox(msg=msg, title=title, choices=(wsNames))
        if choice == "Add Workspace":
            workspace['name'] = "Add Workspace" 
        else:
            for ws in workspaces:
                if ws['name'] == choice:
                    workspace = ws

        # If Existing Workspace
        if workspace['name'] != "Add Workspace":

            # Set tool icon
            netblock.origin_tool = 'Metasploit'
            # Add workspace Properties
            netblock += Field('workspace_id', workspace['id'], display_name='Workspace ID' )
            netblock += Field('name', workspace['name'], display_name='Workspace Name')
            if workspace['boundary'] is None: netblock += Field('boundary', '-', display_name='Workspace Boundary')
            else: netblock += Field('boundary', workspace['boundary'], display_name='Workspace Boundary')
            if workspace['description'] is None: netblock += Field('description', '-', display_name='Workspace Description')
            else: netblock += Field('description', workspace['description'], display_name='Workspace Description')
            if workspace['owner_id'] is None: netblock += Field('owner_id', '-', display_name='Workspace Owner ID')
            else: netblock += Field('owner_id', workspace['owner_id'], display_name='Workspace Owner ID')
            netblock += Field('limit_to_network', workspace['limit_to_network'], display_name='Limit to Network')
            if workspace['import_fingerprint'] is None: netblock += Field('import_fingerprint', '-', display_name='Import fingerprint')
            else: netblock += Field('import_fingerprint', workspace['import_fingerprint'], display_name='Import fingerprint')
            netblock += Field('created_at', workspace['created_at'], display_name='Workspace Created at')
            netblock += Field('updated_at', workspace['updated_at'], display_name='Workspace Updated at')
            # Add to response
            response + netblock

        # If New Workspace
        if workspace['name'] == "Add Workspace":
            msg = "New Workspace"
            fieldNames = ["Name"]
            fieldValues = gui.multenterbox(msg, fields=fieldNames)
            while 1:                                                 
                if fieldValues == None: break                        
                errmsg = ""                                          
                for i in range(len(fieldNames)):                     
                    if fieldValues[i].strip() == "":                 
                        errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])                                       
                if errmsg == "":                                     
                    break 
                fieldValues = gui.multenterbox(errmsg, fieldValues, fieldNames)                                         

            # Create Workspace in Metasploit
            dict = {}
            dict['name'] = fieldValues[0]
            data = json.dumps(dict)
            post = apitools.post_json(url, data, config) 

            # Fetch new workspace in Metasploit
            workspaces = apitools.get_json_dict(url, config)
            ws = []
            for workspace in workspaces:
                if workspace['name'] == dict['name']:
                    ws.append(workspace)      
            workspace = ws[0]

            # Set tool icon
            netblock.origin_tool = 'Metasploit'
            # Set Workspace Properties
            netblock += Field('workspace_id', workspace['id'], display_name='Workspace ID' )
            netblock += Field('name', workspace['name'], display_name='Workspace Name')
            netblock += Field('boundary', netblockBoundary, display_name='Workspace Boundary')
            if workspace['description'] is None: netblock += Field('description', '-', display_name='Workspace Description')
            else: netblock += Field('description', workspace['description'], display_name='Workspace Description')
            if workspace['owner_id'] is None: netblock += Field('owner_id', '-', display_name='Workspace Owner ID')
            else: netblock += Field('owner_id', workspace['owner_id'], display_name='Workspace Owner ID')
            netblock += Field('limit_to_network', workspace['limit_to_network'], display_name='Limit to Network')
            if workspace['import_fingerprint'] is None: netblock += Field('import_fingerprint', '-', display_name='Import fingerprint')
            else: netblock += Field('import_fingerprint', workspace['import_fingerprint'], display_name='Import fingerprint')
            netblock += Field('created_at', workspace['created_at'], display_name='Workspace Created at')
            netblock += Field('updated_at', workspace['updated_at'], display_name='Workspace Updated at')
            # Add to response
            response += netblock

        return response
