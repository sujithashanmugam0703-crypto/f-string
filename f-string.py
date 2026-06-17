todos = []

while True:
    user_action = input("type add, show, edit, exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1
            new_todo = input("enter new todo:")
            todos[number] = new_todo
        case 'complete':
            number = int(input("NUmber of the todo to complete:"))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye-Bye!!")