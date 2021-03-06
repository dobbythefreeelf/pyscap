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
class NameDetailsType(Model):
    MODEL_MAP = {
        'tag_name': 'NameDetails',
        'elements': [
            {'tag_name': 'NameLine', 'list': 'name_lines', 'class': 'NameLineType'},
            {'tag_name': 'PersonName', 'in': 'person_name', 'class': 'PersonNameElement'},
            {'tag_name': 'JointPersonName', 'in': 'joint_person_name', 'class': 'JointPersonNameElement'},
            {'tag_name': 'OrganisationNameDetails', 'in': 'organisation_name_details', 'class': 'OrganisationNameDetailsElement'},
        ],
        'attributes': {
            'PartyType': {},
            'Code': {},
            '*': {},
        },
    }
