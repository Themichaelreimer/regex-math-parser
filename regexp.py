"""
regexp.py https://github.com/Themichaelreimer/regex-math-parser

Copyright 2022 Mike Reimer
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import re
from typing import Union
from decimal import Decimal

binary_operators = [r'\^', r'\*', r'\/', r'\+', r'\-']

digit_pattern = r'\-?\d+\.?\d*'
operator_pattern = r'[{}]'.format(
    ''.join(r'{}'.format(op) for op in binary_operators))  # When I print this the chars look double escaped
operation_pattern = r'({0})({1})({0})'.format(digit_pattern, operator_pattern)
bracket_pattern = r'(\({}\))'.format(operation_pattern)

binary_patterns = [r'({0})\s?({1})\s?({0})'.format(digit_pattern, op) for op in binary_operators]
patterns = [bracket_pattern, *binary_patterns]  # Each pattern in this list is in BEDMAS and in BEDMAS order


def eval(input: str) -> Union[Decimal,str]:
    """
    Returns an integer representing the result in an integer-only number system, or the string "ERROR"
    :param input:
    :return: Integer result, or 'ERROR'
    """
    for pattern_index, pattern in enumerate(patterns):
        operator = binary_operators[pattern_index - 1] if pattern_index > 0 else None
        # Hacky do while loop
        while True:

            search = re.search(pattern, input)
            if not search:
                break
            # Operator is none if the operation is brackets
            if not operator:
                partial_result = brackets(search.group(0))
            elif operator == r'\^':
                partial_result = exp(search.group(1), search.group(3))
            elif operator == r'\*':
                partial_result = mul(search.group(1), search.group(3))
            elif operator == r'\/':
                partial_result = div(search.group(1), search.group(3))
            elif operator == r'\+':
                partial_result = add(search.group(1), search.group(3))
            elif operator == r'\-':
                partial_result = sub(search.group(1), search.group(3))
            else:
                break

            start, end = search.span()
            input = input[:start] + str(partial_result) + input[end:]

    result = re.search(digit_pattern, input)
    if result:
        return Decimal(result.group(0))
    else:
        return "ERROR"


def brackets(input: str) -> Decimal:
    return eval(input[1:-1])


def exp(a: str, b: str) -> Decimal:
    return Decimal(a) ** Decimal(b)


def mul(a: str, b: str) -> Decimal:
    return Decimal(a) * Decimal(b)


def div(a: str, b: str) -> Decimal:
    return Decimal(a) / Decimal(b)


def add(a: str, b: str) -> Decimal:
    return Decimal(a) + Decimal(b)


def sub(a: str, b: str) -> Decimal:
    return Decimal(a) - Decimal(b)
