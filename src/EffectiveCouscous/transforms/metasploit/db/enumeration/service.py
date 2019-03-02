#!/usr/bin/env python3.7.2

# -------------------- Imports ----------------------- #

# Custom Entities
from EffectiveCouscous.entities.service.base import MetasploitService 
from EffectiveCouscous.entities.credential.credentials import MetasploitCredential

# Maltego Message
from canari.maltego.message import Field, MaltegoException, LinkStyle, LinkColor

# Maltego Transforms
from canari.maltego.transform import Transform

# API
import json
from EffectiveCouscous.msftools import apitools
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

#                                       Credentials
#_____________________________________________________________________________________________#


class EnumerateServiceCredentials(Transform):
    """ Enumerates Credentials for this Service"""

    display_name = 'Enumerate Service Credentials'
    transform_set = 'Metasploit | DB | Enumerate'
    input_type = MetasploitService

    def do_transform(self, request, response, config):
        service = request.entity

        # Test for properties
        try:
            ws_url = config['EffectiveCouscous.local.baseurl'] + 'workspaces/{0}'.format(service.workspace_id)
            workspace = apitools.get_json_dict(ws_url, config)['name'] 
            url = config['EffectiveCouscous.local.baseurl'] + 'credentials'
            params = (('workspace', '{0}'.format(workspace)), ('svcs', '{0}'.format(service.name)),)
            creds = apitools.get_json_dict(url, config, params=params)
        except KeyError:
            raise MaltegoException("This IPv4Address is not tied to a Metasploit Host. Please associate it with a Host before running this transform")
            return response

        # REWRITE FOR ALL CASES WHERE CREDENTIAL PROPERTIES ARE NOT EXISTING !!!!!!!!!!!!!!!!!
        # Filter for Service
        for cred in creds:
            try:
                if (int(cred['logins'][0]['service_id'])) == int(service.id):
                #  if ((int(cred['origin']['service_id'])) or (int(cred['logins'][0]['service_id']))) == int(service.id):
                    entity = MetasploitCredential()
                    entity.id = cred['id']
                    entity.logins_count = cred['logins_count']
                    entity.pub_username = cred['public']['username']
                    entity.pub_type = cred['public']['type']
                    entity.priv_data = cred['private']['data']
                    entity.priv_type = cred['private']['type']
                    entity.priv_jtr_format = cred['private']['jtr_format']
                    entity.origin_service_id = cred['origin']['service_id']
                    entity.origin_type = cred['origin']['type']
                    entity.origin_module = cred['origin']['module_full_name']
                    entity.name = '{}/{}'.format(entity.pub_username, entity.priv_data)
                    # Link Style
                    entity.link_color = LinkColor.DarkGreen
                    entity.link_thickness = 3
                    response += entity
            except KeyError as e:
                    continue 
            except IndexError as f:
                    continue 

        return response
