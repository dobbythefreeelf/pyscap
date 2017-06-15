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

from scap.model.xs import *
from scap.model.xs.RealGroupType import RealGroupType

logger = logging.getLogger(__name__)
class NamedGroupType(RealGroupType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'annotation', 'class': 'AnnotationElement', 'min': 0},
            {'tag_name': 'all', 'class': 'NamedGroupAllElement', 'min': 0, 'max': 1},
            {'tag_name': 'choice', 'class': 'SimpleExplicitGroupType', 'min': 0, 'max': 1},
            {'tag_name': 'sequence', 'class': 'SimpleExplicitGroupType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'name': {'type': 'NCNameType', 'required': True},
            'ref': {'prohibited': True},
            'minOccurs': {'prohibited': True},
            'maxOccurs': {'prohibited': True},
            '*': {},
        }
    }