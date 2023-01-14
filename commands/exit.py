from sys import exit


def enter(data: dict):
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
