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
import math

logger = logging.getLogger(__name__)
class Literal(object):
    def __init__(self, value):
        self.value = value

    def evaluate(self, context_node, context_position, context_size, variables):
        return self.value

    def __str__(self):
        return 'Literal ' + hex(id(self)) + ': ' + str(self.value)

    def __repr__(self):
        return repr(self.value)
