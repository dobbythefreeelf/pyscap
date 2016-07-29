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

from scap.Checker import Checker
import logging

logger = logging.getLogger(__name__)
class Rule(Checker):
    def __init__(self, host, content, args=None):
        super(Rule, self).__init__(host, content, args)

        if self.args['check_selector'] not in self.content.checks:
            logger.critical('Check selector ' + self.args['check_selector'] + ' not found for rule ' + self.content.id)
            import sys
            sys.exit()
        check = self.content.checks[self.args['check_selector']]

        self.checker = None
        try:
            args = {'values': self.args['values']}
            self.checker = Checker.load(self.host, check, args)
        except ImportError:
            logger.warning('Unknown check type ' + check.__class__.__name__ + ' for rule ' + self.content.id)

    def check(self):
        if self.checker is None:
            return 'error'
        else:
            return self.checker.check()
