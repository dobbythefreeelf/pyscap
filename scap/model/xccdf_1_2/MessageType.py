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

from scap.model.xccdf_1_2 import MESSAGE_SEVERITY_ENUMERATION
from scap.model.xs.StringType import StringType

logger = logging.getLogger(__name__)
class MessageType(StringType):
    MODEL_MAP = {
        'attributes': {
            'severity': {'enum': MESSAGE_SEVERITY_ENUMERATION, 'required': True},
        }
    }

    def __init__(self, severity=None, *args, **kwargs):
        super(String, self).__init__(*args, **kwargs)

        if severity is not None:
            self.severity = severity
