import re

contacts = {}

def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(args):
    name, phone = args
    if name in contacts:
        return "Це ім'я вже існує."
    if not re.match(r"^\+\d{3}\s?\d{2}\s?\d{7}$", phone):
        return "Номер телефону в неправильному форматі."
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args):
    name, phone = args
    if name not in contacts:
        return "Такого імені немає в телефонній книзі."
    if not re.match(r"^\+\d{3}\s?\d{2}\s?\d{7}$", phone):
        return "неправильний формат."
    contacts[name] = phone
    return "Номер телефону оновлено."

def show_phone(args):
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Такого контакту не виявлено)."

def show_all(args):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Ваша телефонна книга порожня."

def handle_command(command, args):
    if command == "add" and len(args) == 2:
        return add_contact(args)
    elif command == "change" and len(args) == 2:
        return change_contact(args)
    elif command == "phone" and len(args) == 1:
        return show_phone(args)
    elif command == "all" and len(args) == 0:
        return show_all(args)
    elif command in ["close", "exit"]:
        print("Good bye!")
        exit()
    else:
        return "Invalid."

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        response = handle_command(command, args)
        print(response)

if __name__ == "__main__":
    main()
