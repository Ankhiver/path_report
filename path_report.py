import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Small tool that takes a path as an argument and prints it back"
)
parser.add_argument("path", help="Path to a file or directory")
args = parser.parse_args()

path = Path(args.path)

print(path)
print(path.exists())
print(path.is_file())
print(path.is_dir())