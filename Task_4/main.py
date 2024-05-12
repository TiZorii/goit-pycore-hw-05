from colorama import Fore
import input_handler
import contact_operations

def main():
    print(Fore.CYAN + "Welcome to the assistant bot!")
    contacts = {}
    while True:
        user_input = input(Fore.BLUE + "Enter a command: ")
        command, *args = input_handler.parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.CYAN + "Good bye!")
            break

        elif command == "hello":
            print(Fore.GREEN + "How can I help you?")

        elif command == "add":
            contact_operations.add_contact(args, contacts)

        elif command == "change":
            contact_operations.change_contact(args, contacts)

        elif command == "phone":
            print(contact_operations.show_phone(args, contacts))

        elif command == "all":
            print(contact_operations.show_all(contacts))

        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    main()
