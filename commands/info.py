def enter(data: dict, mode: str):
    if mode == "user":
        if not data['logged']:
            print("You are not logged")
            return
        print(
            f"network id: {data['user']['guild_id']}\n"
            f"mac-adress: {data['user']['discord_id']}\n"
            f"ip: {data['user']['ip']}\n"
            f"login: {data['user']['login']}\n"
            f"password: {data['user']['password']}"
        )
    else:
        print(f"Incorrect mode \"{mode}\"")
