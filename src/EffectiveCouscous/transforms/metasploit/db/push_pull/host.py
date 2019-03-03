#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Base Transforms
from EffectiveCouscous.transforms.metasploit.db.push_pull.netblock import (NetblockPushWorkspace,
                                                                           NetblockPullWorkspace,
                                                                           NetblockDeleteWorkspace)
# Custom Entities
from EffectiveCouscous.entities.host.base import MetasploitHost

# Maltego Messages
from canari.maltego.message import MaltegoException

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

#                                       HOST WORKSPACE
#_____________________________________________________________________________________________#


# GENERIC HOST
#--------------------------------------------------
class HostPushWorkspace(NetblockPushWorkspace):
    """ Push Maltego properties to Metasploit workspace."""

    display_name = 'Push Host Workspace'
    transform_set = 'Metasploit | DB | Workspace'
    input_type = MetasploitHost


class HostPullWorkspace(NetblockPullWorkspace):
    """ Pull Metasploit properties to Maltego workspace."""

    display_name = 'Pull Host Workspace'
    transform_set = 'Metasploit | DB | Workspace'
    input_type = MetasploitHost 


class HostDeleteWorkspace(NetblockDeleteWorkspace):
    """ Delete Workspace associated to this Netblock."""

    display_name = 'Delete Host Workspace'
    transform_set = 'Metasploit | DB | Workspace'
    input_type = MetasploitHost 



#_____________________________________________________________________________________________#

#                                           HOST
#_____________________________________________________________________________________________#


# GENERIC HOST
#--------------------------------------------------
class PushHost(Transform):
    """ Push Maltego properties to Metasploit Host"""
    
    display_name = 'Push Host'
    transform_set = 'Metasploit | DB | Host'
    input_type = MetasploitHost

    def do_transform(self, request, response, config):
        msfHost = request.entity

        # Test for properties
        try:
            test = msfHost['id']
        except KeyError:
            raise MaltegoException("This Host is not tied to a Metasploit Host. Please associate it with a Host before running this transform")
            return response

        dict = {}
        dict['id'] = msfHost['id']
        dict['address'] = msfHost['address']
        dict['mac'] = msfHost['mac']
        dict['comm'] = msfHost.comm
        dict['name'] = msfHost.name
        dict['state'] = msfHost['state']
        dict['os_name'] = msfHost['os_name']
        dict['os_flavor'] = msfHost['os_flavor']
        dict['os_sp'] = msfHost['os_sp']
        dict['os_lang'] = msfHost['os_lang']
        dict['os_family'] = msfHost['os_family']
        dict['arch'] = msfHost['arch']
        dict['detected_arch'] = msfHost['detected_arch']
        dict['workspace_id'] = msfHost['workspace_id']
        dict['purpose'] = msfHost['purpose']
        dict['info'] = msfHost['info']
        dict['comments'] = msfHost['comments']
        dict['scope'] = msfHost['scope']
        dict['virtual_host'] = msfHost['virtual_host']
        dict['note_count'] = msfHost['note_count']
        dict['vuln_count'] = msfHost.vuln_count
        dict['service_count'] = msfHost.service_count
        dict['host_detail_count'] = msfHost.host_detail_count
        dict['exploit_attempt_count'] = msfHost.exploit_attempt_count
        dict['cred_count'] = msfHost.cred_count
        dict['created_at'] = msfHost['created_at']
        dict['updated_at'] = msfHost['updated_at']

        data = json.dumps(dict)
        url = config['EffectiveCouscous.local.baseurl'] + 'hosts/{0}'.format(msfHost['id'])
        update = apitools.put_json(url, data, config)
        return response


class PullHost(Transform):
    """ Pull Metasploit properties to Maltego Host"""

    display_name = 'Pull Host'
    transform_set = 'Metasploit | DB | Host'
    input_type = MetasploitHost

    def do_transform(self, request, response, config):
        msfHost = request.entity

        # Test for properties
        try:
            url = config['EffectiveCouscous.local.baseurl'] + 'hosts/{0}'.format(msfHost['id'])
            host = apitools.get_json_dict(url, config)
        except KeyError:
            raise MaltegoException("This Host is not tied to a Metasploit Host. Please associate it with a Host before running this transform")
            return response

        msfHost['id'] = host['id']
        msfHost['ipv4-address'] = host['address']
        msfHost['mac'] = host['mac']
        msfHost['comm'] = host['comm']
        msfHost['name'] = host['name']
        msfHost['state'] = host['state']
        msfHost['os_name'] = host['os_name']
        msfHost['os_flavor'] = host['os_flavor']
        msfHost['os_sp'] = host['os_sp']
        msfHost['os_lang'] = host['os_lang']
        msfHost['os_family'] = host['os_family']
        msfHost['arch'] = host['arch']
        msfHost['detected_arch'] = host['detected_arch']
        msfHost['workspace_id'] = host['workspace_id']
        msfHost['purpose'] = host['purpose']
        msfHost['info'] = host['info']
        msfHost['comments'] = host['comments']
        msfHost['scope'] = host['scope']
        msfHost['virtual_host'] = host['virtual_host']
        msfHost['note_count'] = host['note_count']
        msfHost['vuln_count'] = host['vuln_count']
        msfHost['service_count'] = host['service_count']
        msfHost['host_detail_count'] = host['host_detail_count']
        msfHost['exploit_attempt_count'] = host['exploit_attempt_count']
        msfHost['cred_count'] = host['cred_count']
        msfHost['created_at'] = host['created_at']
        msfHost['updated_at'] = host['updated_at']
        return response


class DeleteHost(Transform):
    """ Delete Metasploit Host associated to this Host Entity"""

    display_name = 'Delete Host'
    transform_set = 'Metasploit | DB | Host'
    input_type = MetasploitHost 

    def do_transform(self, request, response, config):
        msfHost = request.entity

        # Test for properties
        try:
            test = msfHost['id']
        except KeyError:
            raise MaltegoException("This Host is not tied to a Metasploit Host. Please associate it with a Host before running this transform")
            return response

        url = config['EffectiveCouscous.local.baseurl'] + 'hosts'
        data = '{ "ids": [%s] }' % msfHost['id']
        delete = apitools.delete_json(url, data, config)
        return response
