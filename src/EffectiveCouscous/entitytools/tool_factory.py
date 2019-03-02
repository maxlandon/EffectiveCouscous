#!/usr/bin/env python3.7.2

# -------------------- Imports ----------------------- #

# Custom Entities
# Custom entities are directly imported in functions using them,
# so to avoid circular references during imports.

# Icons
from EffectiveCouscous.resource import tools

# String search
import re
# ---------------------------------------------------- #


__author__ = 'Maxime Landon'
__copyright__ = 'Copyright 2019, EffectiveCouscous Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.2'
__maintainer__ = 'Maxime Landon'
__email__ = 'maximelandon@gmail.com'
__status__ = 'Development'



#---------------------------------------------------------------------------------------#
#                                   TOOL FACTORY                                        #
#---------------------------------------------------------------------------------------#

# The OS Factory is responsible for determining the Tool from which various Entities
# originate.


# I - General Functions
#__________________________________
# 1) getOriginTool(host, origin_tool):  Is responsible for determining the Tool from which
#                                       the Entity originates.




# ----------------------------   General Functions   --------------------------------- #

def getOriginTool(entity, origin_tool):
    tool = origin_tool.lower()

    # Test for tools
    if 'metasploit' in tool:
        entity.tool_icon = tools['metasploit']
 
