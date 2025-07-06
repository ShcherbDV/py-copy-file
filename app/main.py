def copy_file(command: str) -> None:
    command_info = command.split()
    if len(command_info) != 3:
        return None
    elif command_info[0] != "cp":
        return None
    file_in_name = command_info[1]
    file_out_name = command_info[2]
    try:
        with (open(file_in_name, "r") as file_in,
              open(file_out_name, "w") as file_out):
            line = file_in.readline()
            file_out.write(line)
    except FileNotFoundError as e:
        print("Some of files is missing!", e)
