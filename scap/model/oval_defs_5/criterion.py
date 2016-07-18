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

from scap.model.content import Content
import logging
from scap.engine.engine import Engine

logger = logging.getLogger(__name__)
class Criterion(Content):
    def from_xml(self, parent, el):
        super(self.__class__, self).from_xml(parent, el)

        if 'negate' in el.attrib and (el.attrib['negate'] == 'true' or el.attrib['negate'] == '1'):
            self.negate = True
        else:
            self.negate = False

        if 'applicability_check' in el.attrib and (el.attrib['applicability_check'] == 'true' or el.attrib['applicability_check'] == '1'):
            self.applicability_check = True
        else:
            self.applicability_check = False

        if 'test_ref' in el.attrib :
            self.test_ref = el.attrib['test_ref']
        else:
            logger.critical('test_ref not defined in criterion')
            import sys
            sys.exit()
