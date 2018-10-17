from resosuma import jsonifier as json
import argparse

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("csv_file", help="The path of the input CSV file",
                    type=str)
parser.add_argument("output", help="The path of the output file",
                    type=str)
args = parser.parse_args()

# Create a visualization from the input CSV in the given format
print("JSONifying graph")
json.create(args.csv_file, args.output)
print("Done.")
