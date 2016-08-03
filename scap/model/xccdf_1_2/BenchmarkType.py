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
class BenchmarkType(Model):
    TAG_MAP = {
        '{http://checklists.nist.gov/xccdf/1.2}Profile': {'class': 'ProfileType'},
        '{http://checklists.nist.gov/xccdf/1.2}Value': {'class': 'ValueType'},
        '{http://checklists.nist.gov/xccdf/1.2}Group': {'class': 'GroupType'},
        '{http://checklists.nist.gov/xccdf/1.2}Rule': {'class': 'RuleType'},
        '{http://checklists.nist.gov/xccdf/1.2}TestResult': { 'class': 'TestResultType' },
    }

    def __init__(self):
        super(BenchmarkType, self).__init__()

        self.rules = {}
        self.values = {}
        self.profiles = {}
        self.profile_elements = {}
        self.test_results = {}
        self.selected_rules = []
        self.selected_profile = None

        self.required_attributes.append('id')
        self.ignore_attributes.extend([
            'Id',
            'resolved',
            'style',
            'style-href',
        ])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}status',
            '{http://purl.org/dc/elements/1.1/}dc-status',
            '{http://checklists.nist.gov/xccdf/1.2}title',
            '{http://checklists.nist.gov/xccdf/1.2}description',
            '{http://checklists.nist.gov/xccdf/1.2}front-matter',
            '{http://checklists.nist.gov/xccdf/1.2}rear-matter',
            '{http://checklists.nist.gov/xccdf/1.2}reference',
            '{http://checklists.nist.gov/xccdf/1.2}plain-text',
            '{http://cpe.mitre.org/language/2.0}platform-specification',
            '{http://checklists.nist.gov/xccdf/1.2}platform',
            '{http://checklists.nist.gov/xccdf/1.2}version',
            '{http://checklists.nist.gov/xccdf/1.2}metadata',
            '{http://checklists.nist.gov/xccdf/1.2}model',
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}notice':
            logger.info('Notice: \n' + sub_el.text)
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Profile':
            from scap.model.xccdf_1_2.Profile import Profile
            logger.debug('found profile ' + sub_el.attrib['id'])
            p = Profile()
            # save the sub_el for later so that profiles parse after rules, values
            self.profile_elements[sub_el.attrib['id']] = sub_el
            self.profiles[sub_el.attrib['id']] = p
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Value':
            self.values[sub_el.attrib['id']] = Model.load(self, sub_el)
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Group':
            g = Model.load(self, sub_el)
            self.rules.update(g.get_rules())
            self.values.update(g.get_values())
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Rule':
            r = Model.load(self, sub_el)
            self.rules[sub_el.attrib['id']] = r
            if r.selected:
                self.selected_rules.append(r.id)
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}TestResult':
            self.test_results[sub_el.attrib['id']] = Model.load(self, sub_el)
        else:
            return super(BenchmarkType, self).parse_sub_el(sub_el)
        return True

    def from_xml(self, parent, el):
        super(BenchmarkType, self).from_xml(parent, el)

        for profile_id, p in self.profiles.items():
            p.from_xml(self, self.profile_elements[profile_id])