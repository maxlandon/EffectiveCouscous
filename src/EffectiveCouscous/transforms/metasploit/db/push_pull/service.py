#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Custom Entities
from EffectiveCouscous.transforms.common.entities import MetasploitService

# Maltego Messages
from canari.maltego.message import MaltegoException

# Maltego Transforms
from canari.maltego.transform import Transform

# API
import json
from EffectiveCouscous.msftools import apitools
# ---------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, Effective-Couscous Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#_____________________________________________________________________________________________#

#                                           Services
#_____________________________________________________________________________________________#


class PushService(Transform):
    """ Push Maltego properties to Metasploit Service"""

    display_name = 'Push Service'
    transform_set = 'Metasploit | DB | Service'
    input_type = MetasploitService 

    def do_transform(self, request, response, config):
        msfService = request.entity

        # Test for properties
        try:
            test = msfService['id']
        except KeyError:
            raise MaltegoException("This Service is not tied to a Metasploit Service. Please associate it with a Service before running this transform")
            return response

        dict = {}
        dict['id'] = msfService.workspace_id
        dict['name'] = msfService.name
        dict['created_at'] = msfService.created_at
        dict['updated_at'] = msfService.updated_at
        dict['info'] = msfService.info
        dict['proto'] = msfService.proto
        dict['port'] = msfService.port
        dict['host_id'] = msfService.host_id
        dict['state'] = msfService.state

        data = json.dumps(dict)
        url = config['EffectiveCouscous.local.baseurl'] + 'services/{0}'.format(msfService['id'])
        update = apitools.put_json(url, data, config)
        return response


class PullService(Transform):
    """ Pull Metasploit properties to Maltego Service"""

    display_name = 'Pull Service'
    transform_set = 'Metasploit | DB | Service'
    input_type = MetasploitService 

    def do_transform(self, request, response, config):
        msfService = request.entity

        # Test for properties
        try:
            test = msfService['id']
        except KeyError:
            raise MaltegoException("This Service is not tied to a Metasploit Service. Please associate it with a Service before running this transform")
            return response

        url = config['EffectiveCouscous.local.baseurl'] + 'services/{0}'.format(msfService['id'])
        service = apitools.get_json_dict(url, config)
        msfService.info = service['info']
        msfService.name = service['name']
        msfService.proto = service['proto']
        msfService.port = service['port']
        msfService.host_id = service['host']['id']
        msfService.service_id = service['id']
        msfService.workspace_id = service['host']['workspace_id']
        msfService.created_at = service['created_at']
        msfService.updated_at = service['updated_at']
        msfService.state = service['state']
        raise MaltegoException('Due to implementation limitations, it is not possible to refresh this Entity "as is". Please suppress it and spawn it again from its parent Entity to see it with its new properties.')
        return response


class DeleteService(Transform):
    """ Delete Metasploit Service associated to this Service Entity"""

    display_name = 'Delete Service'
    transform_set = 'Metasploit | DB | Service'
    input_type = MetasploitService 

    def do_transform(self, request, response, config):
        msfService = request.entity

        # Test for properties
        try:
            url = config['EffectiveCouscous.local.baseurl'] + 'services'
            data = '{ "ids": [%s] }' % msfService['id']
        except KeyError:
            raise MaltegoException("This Service is not tied to a Metasploit Service. Please associate it with a Service before running this transform")
            return response

        delete = apitools.delete_json(url, data, config)
        return response
