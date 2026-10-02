#!/usr/bin/env python3

def secure_archive(file_name: str, action: str|None="read", content: str|None="") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, 'r') as file:
                return True, file.read()
        elif action == "write":
            with open(file_name, 'w') as file:
                file.write(content)
                return True, "Content successfully written to file"
        else:
            return False, "Unknown action"
    except OSError as e:
        return False, f"Caught OSError: {e}"

if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    file = secure_archive("/not/existing/file", "read", "")
    print(file)
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    file = secure_archive("/etc/shadow", "read", "")
    print(file)
    print("\nUsing 'secure_archive' to read from a regular file:")
    file = secure_archive("text.txt", "read", "")
    print(file)
    print("\nUsing 'secure_content' to write previous content to a new file:")
    new_file = secure_archive("newest_file.txt", "write", file[1])
    print(new_file)
    with open("newest_file.txt", 'r') as file:
        print("New file content:", file.read())
