def total_salary(path):
    try:
        total_salary = 0
        total_developers = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    _, salary_str = line.strip().split(',')
                    salary = int(salary_str)
                    total_salary += salary
                    total_developers += 1
                except ValueError:
                    print("Ошибка при обработке строки:", line)
                    continue

        if total_developers == 0:
            return 0, 0

        average_salary = total_salary / total_developers

        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл", path, "не найдено.")
        return None
result = total_salary('D:/test.txt')

if result is not None:
    total, average = result
    print("Общая сумма зарплат:", total)
    print("Средняя зарплата:", average)    










def get_cats_info(path):
    cat_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_data = line.strip().split(',')
                    cat_id, cat_name, cat_age = cat_data
                    cat_info = {"id": cat_id, "name": cat_name, "age": int(cat_age)}
                    cat_list.append(cat_info)
                except ValueError:
                    print("Ошибка при обработке строки:", line)
                    continue
        return cat_list

    except FileNotFoundError:
        print("Файл", path, "не найдено.")
        return None


cats_info = get_cats_info('D:/cats.txt')

for cat in cats_info:
    print(cat)     










def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args,

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        return f"Contact {name} not found."
    
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} not found."

def show_all_contact(contacts):
    if not contacts:
        return "No contacts"
    else:
        return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])


def main(): 
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            print(show_all_contact(contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")
            
if __name__ == "__main__":
    main()
