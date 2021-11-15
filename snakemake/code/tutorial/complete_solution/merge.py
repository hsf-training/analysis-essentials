from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i","--intxt",nargs="+",required=True)
parser.add_argument("-o","--outtxt",required=True)
args = parser.parse_args()

outf = open(args.outtxt,"w")
for f in args.intxt :
    with open(f) as txt :
        outf.write(txt.read()+"\n")

outf.close() 
