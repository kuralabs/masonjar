# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 KuraLabs S.R.L
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Functions to merge dictionaries.
"""

from copy import deepcopy


def merge(left, right):
    """
    Recursively merge right dictionary into left.

    This algorithm will extend values that are lists and update sets from right
    to left.

    :param dict left: Base dictionary to join into.
    :param dict right: Additional dictionary to merge.

    :return: A copy of left with right merged in.
    :type: dict
    """
    assert isinstance(left, dict), 'Invalid left dictionary'
    assert isinstance(right, dict), 'Invalid right dictionary'

    left_copy = deepcopy(left)

    def _merge(a, b):

        for key in b:

            if key not in a:
                a[key] = b[key]
                continue

            for datatype, joiner in (
                (dict, lambda av, bv: _merge(av, bv)),
                (list, lambda av, bv: av.extend(bv)),
                (set, lambda av, bv: av.update(bv)),
            ):
                # Two subnode dictionaries
                if all([
                    isinstance(a[key], datatype),
                    isinstance(b[key], datatype),
                ]):
                    joiner(a[key], b[key])
                    break
            else:
                a[key] = b[key]

    _merge(left_copy, right)
    return left_copy


__all__ = [
    'merge',
]
