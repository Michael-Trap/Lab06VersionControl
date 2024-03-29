# Michael Trapani - Lab 6

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(oldpass):
    newpass = ""
    for x in range(len(oldpass)):
        if int(oldpass[x]) < 7:
            newpass += str(int(oldpass[x]) + 3)    #offset by + 3
        else:
            newpass += str(int(oldpass[x]) + 3 - 10)    #offset by + 3 and remove tens digit. Modulo also works
    return newpass

def decoder(string):
    res = []
    for i in string:
        if int(i) > 2:
            res.append(str(int(i) - 3))
        else:
            res.append(str(int(i) + 10 - 3))

    res = ''.join(res)
    return res

def main():
    while True:
        menu()
        menu_input = int(input("\nPlease enter an option: "))
        if menu_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        if menu_input == 2:
            password = decoder(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {password}.\n')
        if menu_input == 3:
            exit()

if __name__ == '__main__':
    main()