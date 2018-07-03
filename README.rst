.. image:: https://travis-ci.org/research-software/resosuma.svg?branch=master
   :target: https://travis-ci.org/research-software/resosuma/builds
.. image:: https://img.shields.io/github/license/research-software/resosuma.svg
   :target: ../master/LICENSE


Resosuma
========

`resosuma` (short for **re**\ search **so**\ ftware **su**\ stainability **ma**\ p) is a package for
Python 3 which provides a data model (directed graph) for activities in the
research software sustainability space ("the space").

In the graph, *actors* (i.e., entities that act within the space) and *actees*
(i.e., entities which are acted on) are represented as nodes, and *actions*
are represented as edges.

Currently, a `resosuma` model can be instantiated by reading the data from
3-column CSV, where the first column is the *actor* of an *action*, the
second column is the *action* itself, and the third column is the *actee* of
the *action*.

Requirements
============

`resosuma` requires Python 3 (tested against 3.4, 3.5, 3.6).


Installation
============

Install resosuma with pip::

    pip install resosuma


Usage
=====

To instantiate a `resosuma` model of type `ActivityGraph`, you can call::

    from resosuma.graph.activitygraph import ActivityGraph
    
    graph = ActivityGraph()
    graph.read_csv(csvpath)


Once the model is instantiated, you can inspect it via::

    graph.get_activities()
    graph.get_nodes()

Scripts
-------

`visualize.py` visualizes the model via graphviz.::

    usage: visualize.py [-h] csv_file output {svg,pdf,png}
    
    positional arguments:
      csv_file       The path of the input CSV file
      output         The path of the output file
      {svg,pdf,png}  The output format
    
    optional arguments:
      -h, --help     show the help message and exit

How to cite
===========

The metadata necessary for citing `resosuma` can be found in the `CITATION.cff` file.


Contribute
==========

This project welcomes contributions. 
Please suggest features and report bugs via issues.