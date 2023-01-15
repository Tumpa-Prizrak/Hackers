from typing import Any

import cli
from copy import deepcopy

from pprint import pprint
from utils import user
from utils.converter import convert_from
from utils.exceptions import ConvertError


def enter(data: dict):
    greet()
    fake_data = deepcopy(data)
    while True:
        try:
            user_input = input("faker | " + user.get_prefix(fake_data)).split() # type: ignore
        except KeyboardInterrupt:
            return print("\nExited faker. Your data has been returned to the normal state")
        try:
            user_input[1:] = convert_from(user_input[1:])
            for i in user_input:
                print(type(i), i)
            if user_input[0] == "exit":
                return print("Exited faker. Your data has been returned to the normal state")
            elif user_input[0] == "fake":
                replace_data(fake_data, user_input[1], user_input[2]) # type: ignore
                continue
            elif user_input[0] == "data":
                pprint(fake_data)
                continue
            elif user_input[0] == "faker":
                print("No way...")
                continue
            cli.input_handler(" ".join(user_input), fake_data) # type: ignore
        except IndexError:
            continue


def greet():
    print("Welcome to faker!")
    print("Enter \"fake <key> <value>\" to change your data")
    print("Enter \"data\" to output all data")


def replace_data(data: dict, link: str, value: Any):
    def get(data_: dict | list, list_: str, value_: Any) -> None:
        parts = list_.split(".")
        if len(parts) == 1:
            try:
                if isinstance(data_, dict):
                    return data_.update({parts[0]: value_})
                else:
                    data_[parts[0]] = value_ # type: ignore
                    return
            except AttributeError as e:
                raise ConvertError("Cannot get attribute") from e
        return get(data_[int(parts[0])] if parts[0].isdigit() else data_[parts[0]], ".".join(parts[1:]), value_) # type: ignore
    get(data, link, value)
