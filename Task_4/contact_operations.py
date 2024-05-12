from colorama import Fore
from input_handler import input_error

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return Fore.GREEN + "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return Fore.GREEN + "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return Fore.GREEN + contacts[name]
    else:
        raise KeyError

@input_error
def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(Fore.GREEN + f"{name}: {phone}")
    else:
        return Fore.RED + "No contacts saved."
