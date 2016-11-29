#To-Do app first version, without error handling

#üres lista, ebbe fogjuk menteni a a todo elemeinket
todo_list = []
#üres lista, ide mentjük, hogy valami meg van-e jelölve
mark_list = []
# Ezt a két listát egy dictionary-vel is lehetne helyettesíteni


#Ez a függvény ad hozzá elemeket a todo_list-hez, a mark_list-hez False értékeket ad hozzá
def add_todo():
    # global használat: a fenti(3.sor) todo_list nevű változót szeretnénk ezen a függvényen belül használni, ezért kell
    # a global kulcsszó 
    global todo_list
    my_todo = input("Add an item: ")
    todo_list.append(my_todo)
    mark_list.append(False)


# az elmentett elemek kiírása
def list_todos():
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
    # azért kell todo_number-1, mert a user 1-től látja a sorszámokat, viszont mi 0-tól indexelünk
    todo_number -= 1
    mark_list[todo_number] = True


# Ez a függvény kitörli mindkét listából a megadott indexen lévő elemeket, érdemes átnézni, mivel a törlés nem egyszerű
# dolog pythonban, mert ha törlünk akkor a következő elemek egy indexel előrébb csúsznak pl:
# 0 1 2 3 4 5 6 7 -> 3. elem törlése 0 1 2 3 4 5 6 mostmár látszik, hogy a 4ik elem volt az u, most pedig a 3ik lett 
# f e q w u t w q                    f e q u t w q
def archive_todos():
    global todo_list
    global mark_list

    iterator = 0
    while iterator < len(todo_list):
        # ha mark list[iterator] True akkor mindkát listából törlöm az elemet. ha pl:
        # iterator egyenlő 3al és mark_list[iterator] True akkor mark_list és todo_list-ből
        # is törli a 3ik elemet
        if mark_list[iterator]:
            del mark_list[iterator]
            del todo_list[iterator]
        else:
            #azért csak else ágban iterálok, mert ha törlök és pl törlöm a 3ik elemet akkor a 4ik elem a 3ik helyére csúszik
            # így legközelebb is a 3ik elemet kell megnéznem
            iterator += 1
    print("All completed tasks got deleted.")

# itt csak kiprinteljük a menüt és bekérjük mit szeretne a user
def print_menu():
    command = input("Please specify a command [list, add, mark, archive]: ")
    if command == "list":
        list_todos()
    elif command == "add":
        add_todo()
    elif command == "mark":
        mark_todo()
    elif command == "archive":
        archive_todos()

while True:
    print_menu()