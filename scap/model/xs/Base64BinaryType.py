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

import base64
import logging
import re

from scap.model.xs.AnySimpleType import AnySimpleType

logger = logging.getLogger(__name__)
class Base64BinaryType(AnySimpleType):
    def parse_value(self, value):
        value = super(Base64BinaryType, self).parse_value(value)

        m = re.fullmatch(b'[a-zA-Z0-9+/= ]*', value)
        if not m:
            raise ValueError('xs:Base64Binary must match [a-zA-Z0-9+/= ]*')

        return base64.b64decode(value)

    def produce_value(self, value):
        return base64.b64encode(value)
