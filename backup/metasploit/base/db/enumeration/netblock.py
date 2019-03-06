#!/usr/bin/env python3.7.2

# -------------------- Imports ----------------------- #

# Custom Entities
from EffectiveCouscous.entities.infrastructure import Netblock, IPv4Address

# Maltego Message
from canari.maltego.message import Field, MaltegoException, LinkStyle, LinkColor

# Maltego Transforms
from canari.maltego.transform import Transform

# API
import json
from EffectiveCouscous.tools.msftools import apitools

# GUI
import canari.easygui as gui

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


class EnumerateWorkspaceIP(Transform):
    """ Enumerates one or more Hosts in Workspace"""

    display_name = "Enumerate Workspace IPs"
    transform_set = 'Metasploit | Netblock | Enumerate'
    input_type = Netblock

    def do_transform(self, request, response, config):
        netblock = request.entity
        
        # Test for properties
        try:
            url = config['EffectiveCouscous.local.baseurl'] + 'hosts'
            params = (('workspace', '{0}'.format(netblock['name'])),)
            hosts = apitools.get_json_dict(url, config, params=params)
            title = "Host Choice"
            msg = "Choose one or more Hosts for IPv4Address enumeration"
        except KeyError:
            raise MaltegoException("This Netblock is not tied to a Metasploit Workspace. Please associate it with a workspace before running this transform")
            return response

        # Select Hosts
        hostInfos = []
        hostMap = {}
        for host in hosts:
            hostInfo = '{0}      {1}'.format(host['address'], host['name'])
            hostInfos.append(hostInfo)
            hostMap[host['address']] = hostInfo
        rawChoice = gui.multchoicebox(title=title, msg=msg, choices=(hostInfos))

        for choice in rawChoice:
            for (address, mapped) in hostMap.items():
                if choice == mapped:
                    for host in hosts:
                        if address == str(host['address']):
                            entity = IPv4Address()
                            #  entity.ipv4address = host['address']
                            entity['ipv4-address'] = host['address']
                            entity += Field('id', host['id'], display_name='Host ID')
                            entity += Field('workspace_id', host['workspace_id'], display_name='Workspace ID')
                            entity.icon_url = network_interface
                            entity.origin_tool = 'Metasploit'
                            # Link Style
                            entity.link_color = LinkColor.LightGray
                            entity.link_thickness = 4
                            response += entity
        return response


