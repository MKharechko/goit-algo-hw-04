def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return f"Contact {name} updated"
    else:
        return f"Contact {name} not found"

def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, f"{name} not found")
 
def show_all(contacts):
        if contacts:
            return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return "No contacts found" 
def main():
    contacts = {}
    print("Welcome to the assistance bot")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can i help you: ")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()