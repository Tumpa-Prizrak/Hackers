import typing
import ast


def convert_from(data: str | typing.Iterable[str]):
    if isinstance(data, typing.Iterable):
        output = []
        for part in data:
            try:
                output.append(ast.literal_eval(part))
            except ValueError:
                output.append(part)
        return output
    try:
        return ast.literal_eval(data)
    except ValueError:
        return data
