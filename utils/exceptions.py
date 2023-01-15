class ConvertError(Exception):
    pass

def exceptions_handler(e: Exception, parts):
    if isinstance(e, FileNotFoundError):
        g = "\\"
        print(f"Command \"{e.filename.split(g)[-1][:-3]}\" not found")
    elif isinstance(e, KeyboardInterrupt):
        print("Exiting...")
        exit(0)
    else:
        print(e.__class__.__name__ + ": " + str(e).replace("enter()", f'"{parts[0]}"'))
