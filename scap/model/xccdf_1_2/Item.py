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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class Item(Model):
    def __init__(self):
        super(Item, self).__init__()

        self.ignore_attributes.extend([
            'abstract',
            'cluster-id',
            'extends',
            'hidden',
            'prohibitChanges',
            'Id',
        ])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}status',
            '{http://purl.org/dc/elements/1.1/}dc-status',
            '{http://checklists.nist.gov/xccdf/1.2}version',
            '{http://checklists.nist.gov/xccdf/1.2}title',
            '{http://checklists.nist.gov/xccdf/1.2}description',
            '{http://checklists.nist.gov/xccdf/1.2}question',
            '{http://checklists.nist.gov/xccdf/1.2}reference',
            '{http://checklists.nist.gov/xccdf/1.2}metadata',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}warning':
            if 'category' in sub_el.attrib:
                logger.warning('Item ' + sub_el.attrib['category'] + ' warning: ' + sub_el.text)
            else:
                logger.warning(sub_el.text)
        else:
            return super(Item, self).parse_sub_el(sub_el)
        return True
