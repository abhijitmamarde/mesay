import sys
import textwrap

def cowsay(message, cow_type="default", width=40):
    """
    Simulates the cowsay command.

    Args:
        message (str): The message to display.
        cow_type (str, optional): The type of cow to display. Defaults to "default".
        width (int, optional): The maximum width of the message bubble. Defaults to 40.
    """

    wrapped_message = textwrap.wrap(message, width=width)
    max_line_length = max(len(line) for line in wrapped_message) if wrapped_message else 0

    top_border = " " + "_" * (max_line_length + 2)
    bottom_border = " " + "-" * (max_line_length + 2)

    bubble = top_border + "\n"

    for line in wrapped_message:
        padding = " " * (max_line_length - len(line))
        bubble += f"| {line}{padding} |\n"

    bubble += bottom_border + "\n"

    cow = get_cow(cow_type)

    print(bubble + cow)
    print(f"Python version used: {sys.version}")

def get_cow(cow_type):
    default = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """

    if (not cow_type) or (cow_type.lower() not in ['stegosaurus', 'dragon']):
        cow_type == "default"

    if cow_type == "default":
        cow = default

    elif cow_type == "stegosaurus":
        cow = r"""
        \   /^\\_____
         \  (oo)\    )\/\
            (__)\    ||
                ||---||
                ||   ||
        """
    elif cow_type == "dragon":
      cow = r"""
       \   /\_/\
        \  (o o)
          > == <
         /  --  \
        /________\
        """

    return cow

def main():
    import argparse

    parser = argparse.ArgumentParser(description="A Python cowsay implementation.")
    parser.add_argument("message", nargs="*", default=["Moo!"], help="The message to display.")
    parser.add_argument("-t", "--type", choices=["default", "stegosaurus", "dragon"], default="default", help="The type of cow to display.")
    parser.add_argument("-w", "--width", type=int, default=40, help="The maximum width of the message bubble.")

    args = parser.parse_args()

    message = " ".join(args.message)

    cowsay(message, args.type, args.width)

if __name__ == "__main__":
    main()
