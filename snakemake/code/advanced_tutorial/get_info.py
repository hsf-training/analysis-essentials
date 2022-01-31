"""Extract information about a person."""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="person of interest")
parser.add_argument("infile", help="text file with information")
parser.add_argument("outfile", help="where to write extracted information")
args = parser.parse_args()

# -- find information
print("extracting information...")
found = None
with open(args.infile) as f:
    for ln in f:
        if ln.startswith(args.name):
            found = ln
            break  # assume only one line with info
if not found:
    raise ValueError(f"{args.infile} contains no info on '{args.name}'")
info = found[len(args.name):]  # assume space follows name
print("found information")
# -- write information
print("writing information...")
with open(args.outfile, "w") as f:
    f.write(info)
    f.write("\n")
print("done")
