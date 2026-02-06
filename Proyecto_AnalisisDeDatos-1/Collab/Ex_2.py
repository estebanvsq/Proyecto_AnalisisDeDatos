# For + Indices
def exercise_1():
    list_p = []
    while True:
        word = input("Input the word you want to add to the list (Type 0 to stop adding words): ")
        if word == '0':
            break
        list_p.append(word)
    for i in list_p:
        if len(i) >= 5:
            print(f"the word '{i}' have more than 5 characters. Full lenght: {len(i)}")
    print(list_p)

# For + Tuplas
def exercise2():
    tuple_p = (float(input("Input the axis X: ")), float(input("Input the axis Y: ")))
    aux = 0
    for i in tuple_p:
        aux += i ** 2
    print(f"The distance to the origin for the coors ({tuple_p[0]}, {tuple_p[1]}) is :{aux**(1/2)}")

# While + conversión
def exercise3():
    tuple_n = (2, 5, 8, 10)
    list_n = []

    for i in tuple_n:
        list_n.append(i)

    while True:
        option = (input("Type the position you want to edit (type '0' to exit): "))
        if int(option) > len(tuple_n):
            print("The tuple doesn't have enough items, try again.")
        elif int(option) == 0:
            print("Your final tuple will be showing in a moment...")
            break
        else:
            num_c = int(input(f"Input the number you want to switch instead '{list_n[int(option)-1]}': "))
            list_n[int(option)-1] = num_c

    f_tuple = tuple(list_n)
    print(f"The final tuple is {f_tuple}")

# Diccionario, Libros (Final)

f_menu = """Options: 

1 → Add a book.
2 → Rent a book.
3 → Edit info from a book.
0 → Exit.
"""

editInfo = """Choose what info you want to edit.
1 → Name of the author
2 → Price of the book
0 → None.
"""

def final_exercise():
    register = {}
    print("Welcome to the library! Here you can search, add or buy books and more :). ¿What you want to do?")
    while True:
        print(f_menu)
        ch = int(input("Your choose: "))
        match ch:
            case 1:
                newBook = (input("Name of the book: ")).capitalize()
                author = (input("Name of the author: ")).capitalize()
                price =  float(input("Price of the book: "))
                register.update({newBook: {'Author': author, 'Price': price}})
                print(f"The book '{newBook}' was added to the library :)")
            case 2:
                rBook = (input("Input the name of the book you want to rent: ")).capitalize()
                if rBook in register:
                    register.pop(rBook)
                else:
                    print("The book seems to be disappeared from our library, sorry :(")
            case 3:
                eBook = (input("Input the name of the book you want to edit: ")).capitalize()
                if eBook in register:
                    print(editInfo)
                    newInfoOp = int(input("Your choose: "))
                    match newInfoOp:
                        case 1:
                            newName = (input("Write the new name of the author: ")).capitalize()
                            register[eBook]['Author'] = newName
                            print("The name was updated.")
                        case 2:
                            newPrice = float(input("Input the new price for the book: "))
                            register[eBook]['Price'] = newPrice
                        case 0:
                            print("...")
                else:
                    print("The book seems to be disappeared from our library, sorry :(")
            case 0:
                print("Thanks for using our library data system! See you again.")
                break

final_exercise()