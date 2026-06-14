import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        cmd, source, dest = command.split()
        if cmd != "mv":
            raise ValueError("Invalid command: command must be 'mv'")
        if not os.path.exists(source):
            raise FileNotFoundError(f"{source} does not exist")
        if source[-1] == "/":
            raise ValueError(
                "Invalid command: source file must be a file, not a directory"
            )
        if dest[-1] == "/":
            dest = dest + source
        if os.path.dirname(dest) != "":
            os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(source, "r") as source_file, open(dest, "w") as dest_file:
            dest_file.write(source_file.read())
        os.remove(source)
