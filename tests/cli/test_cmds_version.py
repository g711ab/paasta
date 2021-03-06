# Copyright 2015-2016 Yelp Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import
from __future__ import unicode_literals

import re

import pytest

from paasta_tools.cli.cli import main


def test_paasta_version(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(('-V',))
    assert excinfo.value.code == 0
    output = capsys.readouterr()[1]
    assert re.match('^paasta-tools \d+\.\d+\.\d+\n$', output)
