def save_note(note):

    with open("notes.txt", "a") as file:
        file.write(note + "\n")


def read_notes():

    try:
        with open("notes.txt", "r") as file:
            return file.read()

    except:
        return "No notes available"


def add_task(task):

    with open("todo.txt", "a") as file:
        file.write(task + "\n")


def show_tasks():

    try:
        with open("todo.txt", "r") as file:
            return file.read()

    except:
        return "No tasks available"