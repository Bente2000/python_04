#!/usr/bin/env python3

import sys
from typing import IO

def ft_archive_creation(file: str) -> None:
    print(f"Accessing file '{file}'")
    f: IO[str] = open(file, mode="r", encoding="utf-8") #f = io.TextWrapperIO type
    text = f.read() #look in f aka TextIOWrapper for read(), io.read()
    #doesnt exist
    print(f"---\n\n{text}\n---")
    f.close()
    print(f"File '{file}' closed.")
    print(f"\nTransform data:\n---\n\n{text}\n---")
    transformed = text.replace('\n', '#\n')
    if not text.endswith('\n'):
        transformed += '\n'
    print(transformed)
    new_name = input("Enter new file name (or empty): ")
    if new_name != '':
        print(f"Saving data to '{new_name}'")
        new_file: IO[str] = open(new_name, mode='w', encoding="utf-8")
        new_file.write(transformed)
        print(f"Data saved in file '{new_name}'.")
        new_file.close()

if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 2:
        try:
            ft_archive_creation(sys.argv[1])
        except OSError as e: #includes not found, no permission, is directory
            print(f"Error opening file '{sys.argv[1]}': {e}")
    else:
        print(f"Usage: {sys.argv[0]} <file>")

