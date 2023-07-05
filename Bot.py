import re
from collections import defaultdict

contact = defaultdict(dict)
lst_bey = ["good bye", "close", "exit"]
pattern = r'[A-Za-z]{1,} [0-9]{1,}'


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Please write Name and Phone, though a space"
        except KeyError:
            return "Sorry, this name is not found, try again"
        except ValueError:
            return "Sorry,Incorrect input, enter the name using the letters and the phone number using numbers.Name and Phone write through a space"
    return inner


def unknown_command(*args):
    return "Unknown command"


@input_error
def phones(*args):
    name = args[0]
    if len(args) > 1:
        return "Please write only username"
    if name in contact:
        return contact[name]
    else:
        raise KeyError


def show():
    string = ''
    x = ''
    for i, c in contact.items():
        string = f"{i}: {c}\n"
        x += string
    return x.strip("\n")


@input_error
def add(*args: list):
    string = ''
    for i in args:
        string = string + i + ' '
    if re.search(pattern, string):
        name = args[0]
        phone = args[1]
        if phone in contact[name]:
            return "This name or number already exists, if you want change number, use command - 'change'"
        else:
            contact[name] = phone
    elif len(args) < 2:
        raise IndexError
    else:
        raise ValueError

    return "Add success"


def hello(*args):
    return "How can i help you?"


@input_error
def change(*args):
    name = args[0]
    phone = args[1]
    if name in contact:
        contact[name] = phone
    else:
        return "Not found name"
    return "Change success"


def parser_text(text: str) -> tuple[callable, tuple[str] | None]:
    if text.startswith('add'):
        return add, text.replace("add", ' ').strip().split()
    elif text.startswith('hello'):
        return hello, text
    elif text.startswith('change'):
        return change, text.replace('change', ' ').strip().split()
    elif text.startswith('phone'):
        return phones, text.replace('phone', ' ').strip().split()
    elif text.startswith('show all'):
        return show, text.replace('show all', ' ').strip().split()
    return unknown_command, text


def main():
    while True:
        user_input = input(">>> Wait command:").casefold()
        if user_input in lst_bey:
            print("Good bye!")
            break
        command, data = parser_text(user_input)
        result = command(*data)
        print(result)


if __name__ == "__main__":
    main()
