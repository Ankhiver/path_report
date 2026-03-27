import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Small tool that takes a path as an argument and prints it back"
)
parser.add_argument("path", help="Path to a file or directory")
args = parser.parse_args()

path = Path(args.path)

if not path.exists():
    print(f"Path object '{path}' doesn't exist")
elif path.is_file():
    print(f"Path object '{path}' is a file.")
    print(f"File name: {path.name}")
    print(f"File suffix: {path.suffix}")
elif path.is_dir():
    print(f"Path object '{path}' is a directory.")
    items = list(path.iterdir())
    print(f"Number of files in this directory: {len(items)}")
else:
    print("There is an error with argument passed to the tool.")