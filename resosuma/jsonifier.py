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
import json
from bidict import bidict


def create(csvpath: str, outputpath: str):
    '''
    Creates an activity graph from an input CSV file and saves the nodes
    and edges in separate JSON files.

    The CSV file must have 3 columns, of which the first contains
    actors of an action, the second the action, and the third the actee
    of the action.the

    Keyword arguments:
    csvpath --  the path of the CVS file
    outputpath -- the path of the outputfile (also the filename of the)
                  graphviz data file
    '''
    graph = AG()
    graph.read_csv(csvpath)

    # Get Node objects of graph
    nodes = graph.get_nodes()
    nodes_list = []

    # Nodes are always unique; Builds a simple list of node dicts with
    # id and label.
    i = 0
    for node in nodes:
        i = i + 1
        nodes_list.append({'id': i, 'label': node.get_label()})

    # Write the nodes list to a JSON file in the outputpath
    with open(outputpath + "nodes.json", "w") as file:
        json.dump(nodes_list, file)

    # Get Edge object of graph
    edges = graph.get_activities()
    edges_list = []
    for edge in edges:
        source_id = 0
        target_id = 0
        label = edge.get_label()
        for node in nodes_list:
            if node['label'] == edge.get_source().get_label():
                source_id = node['id']
            elif node['label'] == edge.get_target().get_label():
                target_id = node['id']
        edges_list.append({'from': source_id, 'to': target_id, 'label': label})
    # Write the edges list to a JSON file in the outputpath
    with open(outputpath + "edges.json", "w") as file:
        json.dump(edges_list, file)



