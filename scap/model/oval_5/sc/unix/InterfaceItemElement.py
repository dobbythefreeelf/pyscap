# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import logging

from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)
class InterfaceItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'name', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': 1},
            {'tag_name': 'type', 'min': 0, 'class': 'EntityItemInterfaceType', 'max': 1},
            {'tag_name': 'hardware_addr', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': 1},
            {'tag_name': 'inet_addr', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIPAddressStringType', 'max': 1},
            {'tag_name': 'broadcast_addr', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIPAddressStringType', 'max': 1},
            {'tag_name': 'netmask', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIPAddressStringType', 'max': 1},
            {'list': 'flags', 'tag_name': 'flag', 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemStringType', 'max': None},
        ],
        'attributes': {
        },
    }

