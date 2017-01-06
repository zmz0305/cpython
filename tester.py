import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help='the python script to be run')
parser.add_argument("-s", "--seed", type=int, default=0, 
					help='the seed for random generator')
parser.add_argument("-m", "--mode", default='FULL', 
					help='the NonDex mode')
parser.add_argument("-b", "--bin", default="/Users/zmz0305/workspace/\
				OneDrive/workplace/research/install-python/bin/python3.7",
				help="the modified python executable path")
args = parser.parse_args()
os.environ['PY_SRAND'] = str(args.seed)
os.environ['NONDEX_MODE'] = args.mode
os.system("{bin} {file}".format(bin=args.bin, file=args.file))


