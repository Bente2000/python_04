#!/usr/bin/env python3

def secure_archive(file_name: str, action: str|None, content: str) -> tuple[bool, str]:
    if action == 'read':
        with open(file_name, 'r') as file:
            data = file.read()
        print(f"Read this: {data}")
        return True, data
    else:
        with open(file_name, 'w') as file:
            data = file.write("Write this")
        return True, data

if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    secure_archive("text.txt", 'read', "write this") #very much in progress
