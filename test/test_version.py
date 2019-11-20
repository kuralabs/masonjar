# -*- coding: utf-8 -*-
#
# Copyright (C) 2017-2019 KuraLabs S.R.L
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


def test_semantic_version():
    """
    Check that version follows the Semantic Versioning 2.0.0 specification.

        http://semver.org/

    This is basically the basic test to bootstrap a pytest testing suite.
    """
    from masonjar import __version__

    mayor, minor, rev = map(int, __version__.split('.'))

    assert mayor >= 0
    assert minor >= 0
    assert rev >= 0
