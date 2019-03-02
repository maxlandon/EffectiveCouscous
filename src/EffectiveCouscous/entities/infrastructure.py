#!/usr/bin/env python3.7.2

# -------------------- Imports --------------------- #

# Maltego Entities
from canari.maltego.entities import Entity

# Fields
from canari.maltego.message import StringEntityField

# Tool Factory
from EffectiveCouscous.entitytools.tool_factory import getOriginTool
# -------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, EffectiveCouscous Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



# This file redefines Netblock and IPv4Addresses, by overloading them with
# new attributes.



class Netblock(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    # Icon Properties
    origin_tool = StringEntityField('origin_tool', display_name='Origin Tool', decorator=getOriginTool)
    tool_icon = StringEntityField('tool_icon', display_name='Tool Icon')



class IPv4Address(Entity):
    _category_ = 'Infrastructure'
    _namespace_ = 'maltego'

    # Icon Properties
    origin_tool = StringEntityField('origin_tool', display_name='Origin Tool', decorator=getOriginTool)
    tool_icon = StringEntityField('tool_icon', display_name='Tool Icon')

