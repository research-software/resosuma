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

from resosuma.graph.activitygraph import ActivityGraph as AG
from resosuma.graph.edge import Edge
from resosuma.graph.node import Node
import pytest
from resosuma.exceptions import CSVInputError


def test_add_activity():
    '''
    asd
    '''
    g = AG()
    activity = Edge("1", "does", "2")
    source = Node("1")
    target = Node("2")
    g.add_activity("1", "does", "2")
    assert activity in g.get_activities()
    assert source in g.get_nodes()
    assert target in g.get_nodes()
    assert len(g.get_activities()) == 1
    assert len(g.get_nodes()) == 2


def test_sets():
    '''
    asd
    '''
    g = AG()
    n1 = Node("1")
    n2 = Node("2")
    n3 = Node("3")
    n4 = Node("4")
    n5 = Node("5")
    e1 = g.add_activity("1", "does", "2")
    assert e1 in g.get_activities()
    assert len(g.get_activities()) == 1
    assert n1 in g.get_nodes()
    assert n2 in g.get_nodes()
    assert len(g.get_nodes()) == 2
    e2 = g.add_activity("3", "does", "4")
    assert e1 in g.get_activities()
    assert e2 in g.get_activities()
    assert len(g.get_activities()) == 2
    assert n1 in g.get_nodes()
    assert n2 in g.get_nodes()
    assert n3 in g.get_nodes()
    assert len(g.get_nodes()) == 4
    e3 = g.add_activity("1", "does", "4")
    assert e1 in g.get_activities()
    assert e2 in g.get_activities()
    assert e3 in g.get_activities()
    assert len(g.get_activities()) == 3
    assert n1 in g.get_nodes()
    assert n2 in g.get_nodes()
    assert n3 in g.get_nodes()
    assert n4 in g.get_nodes()
    assert len(g.get_nodes()) == 4
    e4 = g.add_activity("1", "does", "5")
    assert e1 in g.get_activities()
    assert e2 in g.get_activities()
    assert e3 in g.get_activities()
    assert e4 in g.get_activities()
    assert len(g.get_activities()) == 4
    assert n1 in g.get_nodes()
    assert n2 in g.get_nodes()
    assert n3 in g.get_nodes()
    assert n4 in g.get_nodes()
    assert n5 in g.get_nodes()
    assert len(g.get_nodes()) == 5
    assert Node("1") in g.get_nodes()
    assert Node("2") in g.get_nodes()
    assert Node("3") in g.get_nodes()
    assert Node("4") in g.get_nodes()
    assert Node("5") in g.get_nodes()


@pytest.fixture(scope="session")
def csv_file(tmpdir_factory):
    csv = "1,does,2\n1,does,3\n1,does,2\n2,does,4"
    fn = tmpdir_factory.mktemp("data").join("test.csv")
    fn.write(csv)
    return str(fn)


@pytest.fixture(scope="session")
def bad_csv_file(tmpdir_factory):
    csv = "1,does,2\n1,does,3\n1,does,2,badfourthcolumndata\n2,does,4"
    fn = tmpdir_factory.mktemp("data").join("test.csv")
    fn.write(csv)
    return str(fn)


def test_read_file(csv_file):
    ag = AG()
    ag.read_csv(csv_file)
    assert len(ag.get_activities()) == 3
    e1 = Edge("1", "does", "2")
    e2 = Edge("1", "does", "3")
    e3 = Edge("2", "does", "4")
    assert e1 in ag.get_activities()
    assert e2 in ag.get_activities()
    assert e3 in ag.get_activities()
    assert len(ag.get_nodes()) == 4
    n1 = Node("1")
    n2 = Node("2")
    n3 = Node("3")
    n4 = Node("4")
    assert n1 in ag.get_nodes()
    assert n2 in ag.get_nodes()
    assert n3 in ag.get_nodes()
    assert n4 in ag.get_nodes()


def test_read_file_with_csv_exception(bad_csv_file):
    ag = AG()
    with pytest.raises(CSVInputError):
        ag.read_csv(bad_csv_file)
