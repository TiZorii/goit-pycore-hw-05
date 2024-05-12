from colorama import Fore

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return Fore.RED + "Contact not found."
        except ValueError:
            return Fore.RED + "Give me name and phone please."
        except IndexError:
            return Fore.RED + "Invalid number of arguments."
    return inner
