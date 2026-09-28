#!/usr/bin/env python3

import sys
from typing import IO

def ft_ancient_text(file: str) -> None:
    print(f"Accessing file '{file}'")
    f: IO[str] = open(file, mode="r", encoding="utf-8") #f = io.TextWrapperIO type
    text = f.read() #look in f aka TextIOWrapper for read(), io.read()
    #doesnt exist
    print("---\n")
    print(text)
    print("---")
    f.close()
    print(f"File '{file}' closed.")

if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 2:
        try:
            ft_ancient_text(sys.argv[1])
        except OSError as e: #includes not found, no permission, is directory
            print(f"Error opening file '{sys.argv[1]}': {e}")
    else:
        print(f"Usage: {sys.argv[0]} <file>")
