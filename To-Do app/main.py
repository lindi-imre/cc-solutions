#To-Do app first version, without error handling

#üres lista, ebbe fogjuk menteni a a todo elemeinket
todo_list = []
#üres list, ide mentjük, hogy valami meg van-e jelölve
mark_list = []
# Ezt a két listát egy dictionary-vel is lehetne helyettesíteni


#Ez a függvény add hozzá elemeket a todo_list-hez és a mark_list-hez False értékeket ad hozzá
def add_todo():
    # global használat: a fenti(3.sor) todo_list nevű változót szeretnénk ezen a függvényen belül használni, ezért kell
    # a global kulcsszó 
    global todo_list
    my_todo = input("Add an item: ")
    todo_list.append(my_todo)
    mark_list.append(False)


def list_todos():
    # global -> add_todo függvényben leírva
    global todo_list
    print("You saved the following to-do items:")
    iterator = 0
    for todo in todo_list:
        #Ha a mark_list pl: első eleménél megnézzük hogy a mark_list első eleme True-e, ha igen akkor [X]-el printelek
        #egyébként csak az üres szögletes zárójeleket printelem ki
        if mark_list[iterator]:
            print("\t" + str(iterator + 1) + ". [X] " "todo")
        else:
            print("\t" + str(iterator + 1) + ". [ ] " "todo")
        iterator += 1


#A mark_list adott elemét állítja True-ra.
def mark_todo():
    global todo_list
    global mark_list

    #Azért hívom meg a print todo-t mert először ki szeretném íratni az összes todo elemet.
    list_todos()
    todo_number = int(input("Which one you want to mark as completed: "))
    todo_number -= 1
    mark_list[todo_number] = True

# itt csak kiprinteljük a menüt és bekérjük mit szeretne a user
def print_menu():
    command = input("Please specify a command [list, add, mark, archive]: ")
    if command == "list":
        list_todos()
    elif command == "add":
        add_todo()
    elif command == "mark":
        mark_todo()


while True:
    print_menu()