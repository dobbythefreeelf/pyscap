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
import math
import re

logger = logging.getLogger(__name__)
class Function(object):
    # String Functions

    def f_string(args):
        # TODO If the argument is omitted, it defaults to a node-set with the context node as its only member.
        if isinstance(args, float):
            if args == math.nan:
                return 'NaN'
            elif args == -math.inf:
                return '-Infinity'
            elif args == math.inf:
                return 'Infinity'
            else:
                return str(args)
        elif args == True:
            return 'true'
        elif args == False:
            return 'false'
        else:
            return str(args)

    def f_concat(args):
        r = ''
        for a in args:
            r += a
        return r

    def f_starts_with(args):
        return args[0].startswith(args[1])

    def f_contains(args):
        return args[1] in args[0]

    def f_substring_before(args):
        return args[0].partition(args[1])[0]

    def f_substring_after(args):
        return args[0].partition(args[1])[2]

    def f_substring(args):
        if args[1] == -math.inf:
            return ''

        arg_1 = Function.f_round((args[1]))
        start = arg_1 - 1
        if start < 0:
            start = 0
        logger.debug('Substring start: ' + str(start))

        if len(args) > 2:
            if args[2] == -math.inf:
                return ''
            elif args[2] == math.inf:
                return args[0][start:]

            end = arg_1 - 1 + Function.f_round(args[2])
            logger.debug('Substring end: ' + str(end))

            return args[0][start:end]
        else:
            return args[0][start:]

    def f_normalize_space(args):
        # TODO If the argument is omitted, it defaults to the context node converted to a string, in other words the string-value of the context node.
        args = args.strip('\x20\x09\x0D\x0A')
        return re.sub(r'[\x20\x09\x0D\x0A]+', ' ', args)

    def f_translate(args):
        s = args[0]
        from_ = args[1]
        to = args[2]
        if len(to) > len(from_):
            to = to[:len(from_)]
        delete = from_[len(to):]
        from_ = from_[:len(to)]

        return s.translate(str.maketrans(from_, to, delete))

    # Boolean Functions

    def f_boolean(args):
        if isinstance(args, int) or isinstance(args, float):
            if args != 0 and args != math.nan:
                return True
            else:
                return False
        # TODO if nodeset; return len(set) > 0
        elif isinstance(args, str):
            return len(args) > 0
        else:
            return bool(args)

    # Number Functions

    def f_number(args):
        if isinstance(args, str):
            if '.' in args:
                return float(args)
            else:
                return int(args)
        elif args == True:
            return 1
        elif args == False:
            return 0
        # TODO a node-set is first converted to a string as if by a call to the string function and then converted in the same way as a string argument
        elif isinstance(args, int) or isinstance(args, float):
            return args
        else:
            return int(args)

    def f_round(args):
        if args == math.nan:
            return math.nan
        elif args == math.inf:
            return math.inf
        elif args == - math.inf:
            return - math.inf
        return round(args)

    FUNCTIONS = {
        # Node Set Functions
        # TODO
        # 'last': f_last,
        # TODO
        # 'position': f_position,
        # TODO
        # 'count': f_count,
        # TODO
        # 'id': f_id,
        # TODO
        # 'local-name': f_local_name,
        # TODO
        # 'namespace-uri': f_namespace_uri,
        # TODO
        # 'name': f_name,

        # String Functions
        'string': f_string,
        'concat': f_concat,
        'starts-with': f_starts_with,
        'contains': f_contains,
        'substring-before': f_substring_before,
        'substring-after': lambda x: x[0].partition(x[1])[2],
        'substring': f_substring,
        'string-length': lambda x: len(x),
        'normalize-space': f_normalize_space,
        'translate': f_translate,

        # Boolean Functions
        'boolean': f_boolean,
        'not': lambda x: not x,
        'true': lambda x: True, # x is to swallow the empty expression
        'false': lambda x: False, # x is to swallow the empty expression
        # TODO
        # 'lang': f_lang,

        # Number Functions
        'number': f_number,
        # TODO
        # 'sum': f_sum,
        'floor': lambda x: math.floor(x),
        'ceiling': lambda x: math.ceil(x),
        'round': f_round,
    }

    def __init__(self, name, function):
        self.name = name
        self.function = function
        self.children = []

    def evaluate(self, context_node, context_position, context_size, variables):
        child_evals = []
        for c in self.children:
            v = c.evaluate(context_node, context_position, context_size, variables)
            logger.debug('Evaluated child of ' + str(self) + ' to ' + str(v))
            child_evals.append(v)
        return self.function(*child_evals)

    def __str__(self):
        return 'Function ' + self.name + ': ' + str([str(x) for x in self.children])
