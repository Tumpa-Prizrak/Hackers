from sys import exit


def enter(data: dict):
    """
    Log out from the user
    Usage: exit
    """
    if data["logged"]:
        data.update({
            "user": {
                "login": "anonymous"
            },
            "logged": False
        })
        print("Logged out")
    else:
        exit(0)
