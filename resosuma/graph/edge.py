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

from resosuma.graph.node import Node


class Edge:
    '''
    An edge in a directed graph. Edges have a source and a target node.

    Attributes:
    source_node -- A resosuma.graph.node.Node, the source of the edge
    target_node -- A resosuma.graph.node.Node, the target of the edge
    label -- The label string of the edge
    '''

    def __init__(self, source: str, label: str, target: str):
        '''
        Constructor setting attributes.

        Note that this function explicitly creates Node objects from
        the source and target arguments.

        Keyword arguments:
        source -- the name of the source node
        label -- the name of the edge
        target -- the name of the target node
        '''
        self.source_node = Node(source)
        self.label = label
        self.target_node = Node(target)

    def get_source(self):
        return self.source_node

    def get_target(self):
        return self.target_node

    def get_label(self):
        return self.label

    def __str__(self):
        src = self.source_node.get_label()
        trg = self.target_node.get_label()
        return 'Edge: ' + src + ' > ' + self.label + ' > ' + trg

    def __key(self):
        return (self.source_node, self.label, self.target_node)

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())
