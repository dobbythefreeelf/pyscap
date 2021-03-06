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
import re

from scap.model.xs.List import List
from scap.model.xs.TokenType import TokenType

logger = logging.getLogger(__name__)
class NamespaceListType(TokenType):
    def parse_item(self, item_value):
        if item_value == '##any' or item_value == '##other' \
        or item_value == '##targetNamespace' or item_value == '##local':
            return item_value
        return Token().parse_value(item_value)

    def produce_item(self, item_value):
        if item_value == '##any' or item_value == '##other' \
        or item_value == '##targetNamespace' or item_value == '##local':
            return item_value
        return Token().produce_value(item_value)
