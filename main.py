import os.path

PARAMETER = 4


def entering_new_contact():
    name = input("Enter Name: ")
    address = input("Address: ")

    while True:
        number = (input("Number: "))
        if number.isdigit():
            number = int(number)
            email = input("Email: ")
            break
        else:
            print("Renter a number")

    first_letter = name[0].lower()

    contact = [name, address, number, email]

    print(f"{name} has been successfully added to your contacts")

    return contact, first_letter


def adding_contact_to_file(contact, first_letter):
    file_name = f'{first_letter}.txt'

    with open(file_name, 'a', encoding='utf-8') as file_obj:
        for index in range(PARAMETER):
            file_obj.write(str(contact[index]) + " , ")

    file_obj.close()

def search_contact():
    name = input("Enter name of contact you want to search: ")

    first_letter = name[0]

    file_name = f'{first_letter}.txt'

    check_file = os.path.isfile(file_name)

    if check_file:
        with open(file_name, 'r', encoding='utf-8') as file_obj:
            lines = file_obj.readlines()

            for line in lines:
                if line.find(name) != -1:
                    contact = line.split(",")
                    print(f"Name:{contact[0]}")
                    print(f"Address:{contact[1]}")
                    print(f"Number:{contact[2]}")
                    print(f"Email:{contact[3]}")

                else:
                    print("The name entered is not available in your contacts")

        file_obj.close()
    else:
        print("The name entered is not available in your contacts")


def delete_contact():
    name = input("Enter name of contact you want to search: ")

    first_letter = name[0]

    file_name = f'{first_letter}.txt'

    check_file = os.path.isfile(file_name)

    if check_file:
        with open(file_name, 'r', encoding='utf-8') as file_obj:
            lines = file_obj.readlines()

            for line in lines:
                if line.find(name) != -1:
                    with open(file_name, 'w', encoding='utf-8') as deleting_file:
                        deleted_line = line.replace(line, "")

                        deleting_file.write(deleted_line)
                        deleting_file.close()

                        print(f"{name} has been deleted from your contacts")

                else:
                    print("The name entered is not available in your contacts")

        file_obj.close()
    else:
        print("The name entered is not available in your contacts")


def main():
    while True:
        answer = input(
            "Press 1 to add new contact.\n"
            "Press 2 to for search existing contact.\n"
            "Press 3 to delete existing contact.\n"
        )
        if answer.isdigit():
            answer = int(answer)

            if int(answer) == 1:
                contact, first_letter = entering_new_contact()
                adding_contact_to_file(contact, first_letter)
                break

            if int(answer) == 2:
                search_contact()
                break

            if int(answer) == 3:
                delete_contact()
                break

            else:
                print("Invalid input. Please try again\n")
        else:
            print("Invalid input. Please try again\n")


main()
