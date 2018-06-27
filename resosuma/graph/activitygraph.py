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
from resosuma.graph.edge import Edge
import csv
from resosuma.exceptions import CSVInputError


class ActivityGraph:
    '''
    A directed graph representing activities in the research software
    sustainability space.
    '''

    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def add_activity(self, source: str, activity: str, target: str):
        '''
        Add an activity to the activity graph by mapping the provided
        string arguments to nodes and edges

        Keyword arguments:
        source -- the name of the source node of the activity
        activity -- the name of the activity
        target -- the name of the target node of the activity
        '''
        edge = Edge(source, activity, target)
        self.nodes.add(Node(source))
        self.nodes.add(Node(target))
        self.edges.add(edge)
        return edge

    def get_activities(self):
        return self.edges

    def get_nodes(self):
        return self.nodes

    def read_csv(self, file_path: str):
        '''
        Read a CSV file and map it to the activity graph.

        The CSV file must have three columns, of which the first
        represents the actor of an action, the second the action itself,
        and the third the actee of the action.

        Although the function tries to sniff the CSV dialect, it is
        suggested that the CSV file uses the default delimiter (,) and
        quotechar (").

        Keyword arguments:
        file_path -- the path to the CSV file to be read
        '''
        with open(file_path) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            for idx, row in enumerate(reader):
                if len(row) != 3:
                    raise(CSVInputError(str(row),
                                        "CSV row has more or less " +
                                        "than 3 columns " +
                                        "(line " + str(idx + 1) + ")."))
                self.add_activity(row[0], row[1], row[2])
