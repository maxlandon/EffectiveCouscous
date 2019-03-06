#!/usr/bin/env python3.7.2

# -------------------- Imports ----------------------- #

# Custom Entities
from EffectiveCouscous.entities.host.base import MetasploitHost

# Custom Entities
from EffectiveCouscous.entities.infrastructure import IPv4Address

# Maltego Message
from canari.maltego.message import Field, MaltegoException, LinkStyle, LinkColor

# Maltego Transforms
from canari.maltego.transform import Transform

# API
import json
from EffectiveCouscous.tools.msftools import apitools

# Icons
from EffectiveCouscous.resource import network_interface
# ---------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, EffectiveCouscous Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#_____________________________________________________________________________________________#

#                                       IPv4 Addresses
#_____________________________________________________________________________________________#


#   GENERIC HOST
#---------------------------------------------------
class EnumerateHostIP(Transform):
    """ Enumerates all IP addresses that match this Host in Metasploit."""

    display_name = "Enumerate Host IPs"
    transform_set = 'Msf__DB                    | Host                     | Enumerate'
    input_type = MetasploitHost

    def do_transform(self, request, response, config):
        hostInput = request.entity
        
        # Get workspace & Test for Properties
        url = config['EffectiveCouscous.local.baseurl'] + 'workspaces' 
        workspaces = apitools.get_json_dict(url, config)
        workspace_name = ''
        try:
            for workspace in workspaces:
                if workspace['id'] == int(hostInput['workspace_id']):
                    workspace_name = workspace['name']
        except KeyError:
            raise MaltegoException("This Host is not tied to a Metasploit Workspace. Please associate it with a workspace before running this transform")
            return response

        #  try:
        url = config['EffectiveCouscous.local.baseurl'] + 'hosts'
        params = (('workspace', '{0}'.format(workspace_name)),)
        hosts = apitools.get_json_dict(url, config, params=params)

        # Select Hosts
        for host in hosts:
            if (host['name'] == hostInput.name) and (host['os_name'] == hostInput.os_name):
                entity = IPv4Address()
                entity.ipv4address = host['address']
                entity['ipv4-address'] = host['address']
                entity += Field('id', hostInput['id'], display_name='Host ID')
                entity += Field('workspace_id', hostInput['workspace_id'], display_name='Workspace ID')
                entity.icon_url = networkinterface
                entity.origin_tool = 'Metasploit'

                # Link Style
                entity.link_color = LinkColor.Black
                entity.link_thickness = 3
                response += entity

        return response