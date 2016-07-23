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

from scap.model.oval_defs_5.component.function import Function
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class End(Function):
    def from_xml(self, parent, el):
        super(End, self).from_xml(parent, el)

        if 'character' not in el.attrib:
            logger.critical('EndFunction does not define character')
            import sys
            sys.exit()
        self.character = el.attrib['character']

        self.values = []
        for comp_el in el:
            self.values.append(Component.load(self, comp_el))
        if len(self.values) != 1:
            logger.critical('EndFunction with != len(values)')
            import sys
            sys.exit()