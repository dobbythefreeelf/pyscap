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

from .NodeTest import NodeTest

logger = logging.getLogger(__name__)
class TypeNodeTest(NodeTest):
    NODE_TYPES = [
        'comment',
        'text',
        'processing-instruction',
        'node',
    ]

    def __init__(self, name):
        super(TypeNodeTest, self).__init__()
        self.name = name

    # TODO processing-instruction can have a literal that matches its name

    def evaluate(self, context_node, context_position, context_size, variables):
        if self.name == 'node':
            return True
        else:
            return context_node.get_type == self.name

    def __str__(self):
        return 'TypeNodeTest ' + hex(id(self)) + ' ' + self.name + ': ' + str([str(x) for x in self.children])
