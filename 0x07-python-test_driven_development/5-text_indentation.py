#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The input text.

    Raises:
        TypeError: If text is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = [".", "?", ":"]
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line:
            for separator in separators:
                line = line.replace(separator, f"{separator}\n\n")
            print(line)
