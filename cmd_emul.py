import runpy


def input_handler(command: str, global_data: dict):
    if command == "":
        return
    parts = command.split()
    try:
        runpy.run_path(f"commands\\{parts[0]}.py")["enter"](global_data, *parts[1:])
    except FileNotFoundError as e:
        g = "\\"
        print(f"Command \"{e.filename.split(g)[-1][:-3]}\" not found")
    except Exception as e:
        print(e.__class__.__name__ + ": " + str(e).replace("enter()", f'"{parts[0]}"').title())


def get_prefix(data: dict):
    return f"shh:{data['user']['login']} $ "
