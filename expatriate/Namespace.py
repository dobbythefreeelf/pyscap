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

from .Node import Node

logger = logging.getLogger(__name__)

class Namespace(Node):
    def __init__(self, document, document_order, parent, prefix, uri):
        super(Namespace, self).__init__(document, document_order, parent)

        self.prefix = prefix
        self.uri = uri

    def get_type(self):
        return 'namespace'

    def get_string_value(self):
        return self.uri

    def get_expanded_name(self):
        return (None, self.prefix)
