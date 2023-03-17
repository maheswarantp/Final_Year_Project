import argparse
import cv2
import os
import shutil
import glob

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", help="data directory here")
parser.add_argument("-r", "--results", help="results directory")
args = parser.parse_args()

if not os.path.exists(args.data):
    print("No data directory found")

if not os.path.exists(args.results):
    os.mkdir(args.results)

