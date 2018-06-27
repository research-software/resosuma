#   Copyright 2018ff. Stephan Druskat
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from resosuma.graph.edge import Edge
from resosuma.graph.node import Node


def test_get_label():
    e = Edge("1", "does", "2")
    assert e.get_label() == "does"


def test_to_string():
    e = Edge("1", "does", "2")
    assert str(e) == "Edge: 1 > does > 2"


def test_source():
    e = Edge("1", "does", "2")
    assert e.get_source() == Node("1")


def test_target():
    e = Edge("1", "does", "2")
    assert e.get_target() == Node("2")
