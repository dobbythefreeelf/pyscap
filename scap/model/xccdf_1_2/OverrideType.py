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

from scap.model.xccdf_1_2 import RESULT_ENUMERATION
from scap.model.xs.DecimalType import DecimalType

logger = logging.getLogger(__name__)
class OverrideType(DecimalType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'old-result', 'enum': RESULT_ENUMERATION, 'min': 1, 'max': 1},
            {'tag_name': 'new-result', 'enum': RESULT_ENUMERATION, 'min': 1, 'max': 1},
            {'tag_name': 'remark', 'class': 'TextType', 'min': 1, 'max': 1},
        ],
        'attributes': {
            'time': {'type': 'DateTimeType', 'required': True},
            'authority': {'type': 'StringType', 'required': True},
        },
    }
