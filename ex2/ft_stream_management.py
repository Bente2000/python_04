#!/usr/bin/env python3

import sys
from typing import IO

def ft_archive_creation(file: str) -> None:
    print(f"Accessing file '{file}'")
    f: IO[str] = open(file, mode="r", encoding="utf-8") #f = io.TextIOWrapper type
    text = f.read() #look in f aka TextIOWrapper for read(), io.read()
    #doesnt exist
    print(f"---\n\n{text}\n---")
    f.close()
    print(f"File '{file}' closed.")
    transformed = text.replace('\n', '#\n')
    if not text.endswith('\n'):
        transformed += '#'
    print(f"\nTransform data:\n---\n\n{transformed}\n---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush() #acts as a \n because it clears the stdout buffer
    new_name = sys.stdin.readline().rstrip('\n')
    if new_name != '':
        print(f"Saving data to '{new_name}'")
        try:
            new_file: IO[str] = open(new_name, mode='w', encoding="utf-8")
            new_file.write(transformed)
            new_file.close()
            print(f"Data saved in file '{new_name}'.")
        except OSError as e: #includes not found, no permission, is directory
            print(f"[STDERR] Error opening file '{new_name}': {e}",
                  file=sys.stderr)
            print("Data not saved.")
            sys.exit(1)
    else:
        print("Not saving data.")

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 2:
        try:
            ft_archive_creation(sys.argv[1])
        except OSError as e: #includes not found, no permission, is directory
            print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
                  file=sys.stderr) #2>/dev/null == stderr to nowhere to test
            sys.exit(1)
    else:
        print(f"Usage: {sys.argv[0]} <file>")
