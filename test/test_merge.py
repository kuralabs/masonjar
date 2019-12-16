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

from pprintpp import pprint
from deepdiff import DeepDiff


def test_merge():
    from masonjar.dictionary.merge import merge

    left = {
        'v1': 1,
        'v2': 2,
        'aset': {1, 2, 3},
        'adict': {
            's1': ['a', 'b', True],
            's2': [],
            'alevel': {
                'leaf': 100,
            }
        }
    }

    right = {
        'v1': 10,
        'another': 100,
        'aset': {3, 4},
        'adict': {
            's1': ['a', 'c'],
            's3': 1024,
            'alevel': {
                'leaf': {
                    'override': True,
                },
                'notleaf': 10.18,
            }
        }
    }

    expected = {
        'adict': {
            'alevel': {
                'leaf': {
                    'override': True
                },
                'notleaf': 10.18,
            },
            's1': ['a', 'b', True, 'a', 'c'],
            's2': [],
            's3': 1024,
        },
        'another': 100,
        'aset': {1, 2, 3, 4},
        'v1': 10,
        'v2': 2,
    }

    merged = merge(left, right)
    pprint(merged)

    ddiff = DeepDiff(merged, expected)
    assert not ddiff
