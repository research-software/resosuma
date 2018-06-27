from resosuma import visualizer as vis
import argparse

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("csv_file", help="The path of the input CSV file",
                    type=str)
parser.add_argument("output", help="The path of the output file",
                    type=str)
parser.add_argument("format", help="The output format",
                    choices=['svg', 'pdf', 'png'],
                    type=str)
args = parser.parse_args()

# Create a visualization from the input CSV in the given format
print("Creating graph")
vis.create(args.csv_file, args.output, args.format)
print("Done.")
