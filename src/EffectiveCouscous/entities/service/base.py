#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Fields
from canari.maltego.message import * 

# Icons
from EffectiveCouscous.resource import systems
# -------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, MSM Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#_____________________________________________________________________________________________#

#                                           SERVICES 
#_____________________________________________________________________________________________#


# Generic Service
class MetasploitService(Entity):
    
    # Static properties
    _category_ = 'Penetration Testing'
    _namespace_ = 'EffectiveCouscous.metasploit.service'
    _type_ = 'Metasploit Service' 


    # Entity properties
    display_name = StringEntityField('display_name', display_name='Display Name', is_value=True)
    info = StringEntityField('info', display_name='Info')
    name = StringEntityField('name', display_name='Name')
    proto = StringEntityField('proto', display_name='Protocol')
    port = StringEntityField('port', display_name='Port')
    host_id = StringEntityField('host_id', display_name='Host ID')
    id = StringEntityField('id', display_name='Service ID')
    workspace_id = StringEntityField('workspace_id', display_name='Workspace ID')
    created_at = StringEntityField('created_at', display_name='Created at')
    updated_at = StringEntityField('updated_at', display_name='Updated at')
    state = StringEntityField('state', display_name='State')

