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
from graphviz import Digraph


def create(csvpath: str, outputpath: str, format: str):
    '''
    Creates an activity graph from an input CSV file and visualizes the
    graph via graphviz.

    The CSV file must have 3 columns, of which the first contains
    actors of an action, the second the action, and the third the actee
    of the action.the

    Keyword arguments:
    csvpath --  the path of the CVS file
    outputpath -- the path of the outputfile (also the filename of the)
                  graphviz data file
    format -- the format of the visualization output (svg, pdf, png)
    '''
    graph = AG()
    graph.read_csv(csvpath)
    dot = Digraph(comment='Research Software Sustainability Space Graph',
                  format=format)
    dot.attr(rankdir='LR', size='8,5')
    for n in graph.get_nodes():
        dot.node(n.get_label(), n.get_label())
    for e in graph.get_activities():
        if e.get_target() != e.get_source():
            # If source and target aren't the same, render as per
            # default, i.e., as a gray edge.
            dot.edge(e.get_source().get_label(),
                     e.get_target().get_label(), e.get_label(),
                     color='gray66')
    for e in graph.get_activities():
        if e.get_target() == e.get_source():
            # If source and target are the same, render so that the
            # edge and label are more readable, i.e., as a black edge.
            dot.edge(e.get_source().get_label(),
                     e.get_target().get_label(), e.get_label(),
                     color='black', rank='max')
    # Render and show in the default viewer
    dot.render(outputpath, view=True)
