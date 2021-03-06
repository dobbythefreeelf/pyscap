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

from scap.model.xccdf_1_1 import FIX_STRATEGY_ENUMERATION, RATING_ENUMERATION
from scap.model.xccdf_1_1.HtmlTextWithSubType import HtmlTextWithSubType

logger = logging.getLogger(__name__)
class FixtextType(HtmlTextWithSubType):
    MODEL_MAP = {
        'attributes': {
            'fixref': {'type': 'NCNameType'},
            'reboot': {'type': 'BooleanType', 'default': False},
            'strategy': {'enum': FIX_STRATEGY_ENUMERATION, 'default': 'unknown'},
            'disruption': {'enum': RATING_ENUMERATION, 'default': 'unknown'},
            'complexity': {'enum': RATING_ENUMERATION, 'default': 'unknown'},
        },
    }
