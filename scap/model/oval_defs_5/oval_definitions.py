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
class OVALDefinitions(Content):
    def __init__(self, parent, el):
        super(self.__class__, self).__init__(parent, el)

        from scap.model.oval_defs_5.definition import Definition
        self.definitions = {}
        for def_el in el.findall('./oval_defs_5:definitions/oval_defs_5:definition', Engine.namespaces):
            self.definitions[def_el.attrib['id']] = Definition(self, def_el)

        from scap.model.oval_defs_5.test import Test
        self.tests = {}
        for test_el in el.findall('./oval_defs_5:tests/oval_defs_5:test', Engine.namespaces):
            self.definitions[test_el.attrib['id']] = Test(self, test_el)

        from scap.model.oval_defs_5.object import Object
        self.objects = {}
        for obj_el in el.findall('./oval_defs_5:objects/oval_defs_5:object', Engine.namespaces):
            self.objects[obj_el.attrib['id']] = Object(self, obj_el)

        from scap.model.oval_defs_5.state import State
        self.states = {}
        for state_el in el.findall('./oval_defs_5:states/oval_defs_5:state', Engine.namespaces):
            self.states[state_el.attrib['id']] = State(self, state_el)

        from scap.model.oval_defs_5.variable import Variable
        self.variables = {}
        for var_el in el.findall('./oval_defs_5:variables/oval_defs_5:variable', Engine.namespaces):
            self.variables[var_el.attrib['id']] = Variable(self, var_el)
