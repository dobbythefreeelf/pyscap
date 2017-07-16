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
import pytest

from expatriate import *

logging.basicConfig(level=logging.DEBUG)

doc = Document()

def test_op_mult():
    assert doc.xpath('2 * 4') == 8

def test_op_add():
    assert doc.xpath('2 + 4') == 6

def test_op_sub1():
    assert doc.xpath('2 - 4') == -2

def test_op_sub2():
    assert doc.xpath('4 - 2') == 2

def test_op_eq():
    assert doc.xpath('4 = 4') == True

def test_op_eq2():
    assert doc.xpath('4 = 2') == False

def test_op_ne():
    assert doc.xpath('4 != 4') == False

def test_op_ne2():
    assert doc.xpath('4 != 2') == True

def test_op_lt():
    assert doc.xpath('4 < 4') == False

def test_op_lt2():
    assert doc.xpath('2 < 4') == True

def test_op_le():
    assert doc.xpath('4 <= 3') == False

def test_op_le2():
    assert doc.xpath('2 <= 4') == True

def test_op_gt():
    assert doc.xpath('4 > 5') == False

def test_op_gt2():
    assert doc.xpath('4 > 2') == True

def test_op_ge():
    assert doc.xpath('4 >= 5') == False

def test_op_ge2():
    assert doc.xpath('5 >= 4') == True

def test_op_and():
    assert doc.xpath('true and true') == True

def test_op_and2():
    assert doc.xpath('true and false') == False

def test_op_or():
    assert doc.xpath('true or false') == True

def test_op_or2():
    assert doc.xpath('false or false') == False

def test_op_mod0():
    assert doc.xpath('5 mod 2') == 1

def test_op_mod1():
    assert doc.xpath('5 mod -2') == 1

def test_op_mod2():
    assert doc.xpath('-5 mod 2') == -1

def test_op_mod3():
    assert doc.xpath('-5 mod -2') == -1

def test_op_div0():
    assert doc.xpath('5 div 2') == 2

def test_op_negate():
    assert doc.xpath('-42') == -42

# def test_and_presides_or():
#     pytest.fail()
#
# def test_equality_presides_and():
#     pytest.fail()
#
# def test_comparison_presides_equality():
#     pytest.fail()
