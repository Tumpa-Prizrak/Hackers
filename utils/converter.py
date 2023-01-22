import typing
import ast


def convert_from(data: str | typing.Iterable[str]) -> typing.Union[str, typing.List[str]]:
    """
    Convert string to boolean, integer, float, complex or dict.

    Parameters
    ----------
    data: str | typing.Iterable[str]
        Data to convert.

    Returns
    -------
    typing.Union[str, typing.List[str]]
        Converted data.

    """
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