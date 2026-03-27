import pathlib
import argparse

parser = argparse.ArgumentParser(
    description="Small tool that reads path as an argument and prints it back"
)
parser.add_argument("path", help="Path to file or dierctory")

args = parser.parse_args()

print(args.path)