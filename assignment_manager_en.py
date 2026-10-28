import random

# Creating a Task class responsible for creating objects that represent a student's task.
class Tarefa:

    def __init__(self, nome: str, desc: str, prioridade: int, situacao="Ativa"):
        # The identifier is created using the random.choices() function from the random library, which takes random items from an iterable and returns a list,
        # which is then converted into a string using the .join() method, creating a random code for each task.
        self.padrao = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
        self.id = "".join(random.choices(self.padrao[0], k=5))
        self.nome = nome
        self.desc = desc
        self.situacao = situacao
        self.prioridade = prioridade

        # Here we verify that all attributes nome, desc, and situacao are strings and that prioridade is an integer greater than or equal to 1 and less than or equal to 4.
        # If any of them is of a different type than expected, the program will raise a TypeError accompanied by a message for the user.
        if any(not isinstance(atributo, str) for atributo in [self.nome, self.desc, self.situacao]) or not isinstance(self.prioridade, int) or (self.prioridade < 1 or self.prioridade > 4):
            raise TypeError(f"The name, description, and status of your task must be of type string/text.\nThe priority must be an integer.")

    # When the program needs to print the task, it will be done as follows.
    def __str__(self):
        return f"Task: '{self.nome}'\nDescription: '{self.desc}'\nIdentifier: '{self.id}'\nPriority: '{self.prioridade}'\nStatus: '{self.situacao}'\n"

    # I decided to create these two separately from the update function so that my code is easier to read; they simply modify the value of the status attribute.
    def concluir(self):
        self.situacao = "Completed"
        return self

    def abertura(self):
        self.situacao = "Active"
        return self

    # A method I created to update the description and priority attributes of a Task. By default, its parameters are None so that the user can edit one without necessarily editing the other.
    def atualizar(self, nova_desc=None, nova_prio=None):
        # If any of these parameters is None, the function returns the task itself without modifying it.
        # However, if it passes this first check, I verify whether the value is of the expected type; otherwise, I raise a TypeError.
        # If the inserted value passes all checks, the respective attribute is updated and the function returns the modified Task.
        if nova_desc is not None:
            if not isinstance(nova_desc, str):
                raise TypeError("The description must be a string attribute.")
            self.desc = nova_desc

        if nova_prio is not None:
            if not isinstance(nova_prio, int) or nova_prio < 1 or nova_prio > 4:
                raise TypeError("The priority must be an integer from 1 to 4 (inclusive).")
            self.prioridade = nova_prio

        return self

# Creating a class that will allow me to create an object that stores all the user's tasks.
class ConjuntoTarefas:
    def __init__(self):
        # With the initializer, I can create a dict with the key as the identifier of a task and its value as an object of the Task class.
        # Since I already created a __str__ method for the Task object, it will print each task in a standardized structure.
        self.tarefas = {}

    # So that I could create a dict with the structure mentioned above, I could perhaps use append(), but I preferred to create a special add method,
    # which uses the ability to insert a value into an object if we give it a default value.
    def __add__(self, other: Tarefa):
        # Here I check whether what we are trying to add to the ConjuntoTarefas object is of type Tarefa; if not, I raise a TypeError with an explanation for the user.
        if isinstance(other, Tarefa):
            self.tarefas[other.id] = other
            return self
        else:
            raise TypeError("The ConjuntoTarefas class only supports addition operations with an object of the 'Tarefa' class.")

    # Use the special __str__ method for viewing all tasks.
    def __str__(self):
        # If there are no tasks in the dict, I return this to the user.
        # If there are some, I create a variable res (result) as an empty string. I did this because I did not know how to return several values without creating a variable to store them.
        # Then I create a list called ordenadas that contains the values of the items in the dict/attribute 'tarefas'. I sort them from lowest to highest using a lambda function based on the 'prioridade' attribute of each Task in the list.
        # Finally, I concatenate each Task as a string in the variable res using a loop, and at the end I just return res, so I have a way to view all tasks using only a print()!
        if not self.tarefas:
            return "No tasks registered."
        res = ""
        ordenadas = sorted(self.tarefas.values(), key=lambda tar: tar.prioridade)
        for tarefa in ordenadas:
            res += f"{tarefa}\n"
        return res

# This function changes the status attribute to "Completed" and returns the object with the updated value.
def concluir_tarefa(tarefa):
    tarefa.situacao = "Completed"
    return tarefa

# This function creates a new Tarefa object, asking only for its name, description, and priority, since the identifier and status attributes are defined automatically when an object of this class is created.
def add_tarefa(no, descri, prio):
    tarefa = Tarefa(no, descri, prio)
    print("Operation completed successfully.")
    return tarefa

# This function works by using the two classes created before. First, we access the 'tarefas' attribute in the group. Since it is a dict, we can access a specific item using its key, which is the identifier. After accessing it, we can modify the 'situacao' attribute to "Active".
def reabrir_tarefa(identificador):
    grupo.tarefas[identificador].situacao = "Active"

print("Welcome, student!\n")

menu = """Your options are:

Add a new task - To create a new task, type 'add'.
Complete a task - To set a task's status to completed, type 'complete'.
Reopen a task - To change a completed task back to active, type 'reopen'.
Edit a task - To edit a task's description or priority, type 'edit'.
View tasks - To view a list of your tasks, type 'view'.
Exit the program - To end the program, type 'exit'."""

# Creating an object that will store all tasks.
grupo = ConjuntoTarefas()
print(menu)

# I will always use .lower() to standardize the user's inputs.
opcao = input("What would you like to do? ").lower()

# Starting a while loop that ensures the program continues running until the user types 'exit'.
while opcao != "exit":
    # To add a task, we collect the user's input for each required attribute and create a new Tarefa using the add_tarefa function.
    # Then we simply add it to the group variable. If a ValueError occurs, the program warns the user and returns to the option selection.
    if opcao == "add":
        try:
            nome = input("Enter the name of your task: ")
            descricao = input("Enter the description of your task: ")
            prioridade = int(input("Enter the priority of your task (an integer from 1 to 4): "))
            nova = add_tarefa(nome, descricao, prioridade)
            grupo += nova
            print("Task added successfully!")
        except ValueError:
            print("The priority must be an integer greater than or equal to 1 and less than or equal to 4. Please try again.")
            print()

    # To complete a task, we simply use the concluir() function. If the identifier does not exist, the program warns the user and returns to the option selection.
    elif opcao == "complete":
        identificador = input("Enter the identifier of your task (to know the identifier of a task, view your list of tasks): ")
        if identificador in grupo.tarefas:
            grupo.tarefas[identificador].concluir()
            print("Task completed successfully!")
        else:
            print(f"Identifier '{identificador}' was not found. Please try again.\n")

    # To reopen a task, it is the same process as completion, but this time using the abertura() function.
    elif opcao == "reopen":
        identificador = input("Enter the identifier of your task (to know the identifier of a task, view your list of tasks): ")
        if identificador in grupo.tarefas:
            grupo.tarefas[identificador].abertura()
            print("Task reopened successfully!")
        else:
            print(f"Identifier '{identificador}' was not found. Please try again.\n")

    # The most complex part is editing. We first ask for the task identifier. If it is not found, the program warns the user and returns to the options.
    elif opcao == "edit":
        identificador = input("Enter the identifier of your task (to know the identifier of a task, view your list of tasks): ")

        # If the modifier exists, we create a variable called modificar that corresponds to what the user wants to edit. If it exists, we ask the user for a new description or priority, depending on what they want to change. If they enter an invalid command, the program warns the user and returns to the options.
        if identificador in grupo.tarefas:
            modificar = input("Type 'desc' to change the description, 'prio' for the priority, or 'both' to change both: ").lower()

            try:
                if modificar == "desc":
                    descricao = input("Enter the new description of your task: ")
                    grupo.tarefas[identificador].atualizar(nova_desc=descricao, nova_prio=None)
                    print("Task edited successfully!")

                elif modificar == "prio":
                    prio = int(input("Enter the new priority of your task (an integer from 1 to 4): "))
                    grupo.tarefas[identificador].atualizar(nova_desc=None, nova_prio=prio)
                    print("Task edited successfully!")

                elif modificar == "both":
                    descricao = input("Enter the new description of your task: ")
                    prioridade = int(input("Enter the new priority of your task (an integer from 1 to 4): "))
                    grupo.tarefas[identificador].atualizar(nova_desc=descricao, nova_prio=prioridade)
                    print("Task edited successfully!")

            # We use this exception block in case the user enters an incompatible value for priority so we can alert them and return to the menu of options.
            except (ValueError, TypeError):
                print("The priority must be an integer greater than or equal to 1 and less than or equal to 4. Please try again.")

            else:
                print("The command entered does not exist.")
        else:
            print(f"Identifier '{identificador}' was not found. Please try again.\n")

    elif opcao == "view":
        print(grupo)
    else:
        print("The selected option does not exist in the program. Please try again.")
        print()

    print(menu)
    opcao = input("What would you like to do? ").lower()
    print()

print("The program has been closed.")
