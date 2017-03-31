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

from scap.collector.Checker import Checker
from scap.model.oval_common_5 import ExistenceEnumeration
from scap.model.oval_common_5 import OperatorEnumeration
from scap.model.oval_common_5 import CheckEnumeration

logger = logging.getLogger(__name__)
class TestType(Checker):
    def collect(self):
        # collect items matching obj
        items, existence_results = self.collect_object_items()

        # existence check
        if self.content.check_existence == 'all_exist':
            existence_result = ExistenceEnumeration.all_exist(existence_results)
        elif self.content.check_existence == 'any_exist':
            existence_result = ExistenceEnumeration.any_exist(existence_results)
        elif self.content.check_existence == 'at_least_one_exists':
            existence_result = ExistenceEnumeration.at_least_one_exists(existence_results)
        elif self.content.check_existence == 'none_exist':
            existence_result = ExistenceEnumeration.none_exist(existence_results)
        elif self.content.check_existence == 'only_one_exists':
            existence_result = ExistenceEnumeration.only_one_exists(existence_results)
        else:
            raise ValueError('Test ' + self.content.id + ' check_existence value is unknown: ' + self.content.check_existence)
        logger.debug('Computed existence result: ' + existence_result)

        # if no oval states, return true
        if len(self.content.states) == 0:
            logger.debug('No states to compare; test is true')
            return 'true'

        # for each item
        item_results = []
        for item in items:
            # for each state, compare item with state
            item_state_results = []
            for state in self.content.states:
                item_state_results.append(self.compare_item_state(item, state))

            # combine results with state_operator
            if self.content.state_operator == 'AND':
                item_results.append(OperatorEnumeration.AND(item_state_results))
            elif self.content.state_operator == 'ONE':
                item_results.append(OperatorEnumeration.ONE(item_state_results))
            elif self.content.state_operator == 'OR':
                item_results.append(OperatorEnumeration.OR(item_state_results))
            elif self.content.state_operator == 'XOR':
                item_results.append(OperatorEnumeration.XOR(item_state_results))
            else:
                raise ValueError('Test ' + self.content.id + ' state_operator value is unknown: ' + self.content.state_operator)

        # see if check is satisfied
        if self.content.check == 'all':
            result = CheckEnumeration.all(item_results)
        elif self.content.check == 'at least one':
            result = CheckEnumeration.at_least_one(item_results)
        elif self.content.check == 'none satisfy':
            result = CheckEnumeration.none_satisfy(item_results)
        elif self.content.check == 'only one':
            result = CheckEnumeration.only_one(item_results)
        else:
            raise ValueError('Test ' + self.content.id + ' check value is unknown: ' + self.content.check)

        return result

    def collect_object_items(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def compare_item_state(self, item, state):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
