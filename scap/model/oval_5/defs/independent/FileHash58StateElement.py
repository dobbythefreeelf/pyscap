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

from scap.model.oval_5 import HASH_TYPE_ENUMERATION
from scap.model.oval_5 import WINDOWS_VIEW_ENUMERATION
from scap.model.oval_5.defs.independent.StateType import StateType

logger = logging.getLogger(__name__)
class FileHash58StateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'filehash58_state',
        'elements': [
            {'tag_name': 'filepath', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0},
            {'tag_name': 'path', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'filename', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'hash_type', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1, 'value_enum': HASH_TYPE_ENUMERATION},
            {'tag_name': 'hash', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'max': 1},
            {'tag_name': 'windows_view', 'class': 'scap.model.oval_5.defs.EntityStateType', 'min': 0, 'value_enum': WINDOWS_VIEW_ENUMERATION},
        ],
    }
