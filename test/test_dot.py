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

from deepdiff import DeepDiff


def test_dotify():
    from masonjar.dictionary.dot import dotify

    adict = {
        'key1': {
            'key2': {
                'key3': 'string1',
                'key4': 1000,
            },
        },
        'key4': {
            'key5': 'string2',
        },
    }

    contracted = dotify(adict)
    expected = {
        'key1.key2.key3': 'string1',
        'key1.key2.key4': 1000,
        'key4.key5': 'string2',
    }

    ddiff = DeepDiff(contracted, expected)
    assert not ddiff


def test_undotify():
    from masonjar.dictionary.dot import undotify

    dotdict = {
        'key1.key2.key3': 'string1',
        'key1.key2.key4': 1000,
        'key4.key5': 'string2',
    }

    expanded = undotify(dotdict)
    expected = {
        'key1': {
            'key2': {
                'key3': 'string1',
                'key4': 1000,
            },
        },
        'key4': {
            'key5': 'string2',
        },
    }

    ddiff = DeepDiff(expanded, expected)
    assert not ddiff
