import select
import insert
import update
import delete
import search
def menu():
    try:
        while True:
            print("="*40)
            print("\tTheDrink TheDrank TheDrunk")
            print("="*40)
            print("Main Menu")
            print("[1] Show Data")
            print("[2] Search Data")
            print("[3] Insert Data")
            print("[4] Update Data")
            print("[5] Delete Data")
            print("[6] Exit")
            input_choice = int(input("Choose Menu  : "))
            if (input_choice == 1):
                print("="*15,"Show Data","="*15)
                select.show_data()
            elif (input_choice == 2):
                search.search_data()
            elif (input_choice == 3):
                insert.insert_data()
            elif (input_choice == 4):
                update.update_data()
            elif (input_choice == 5):
                delete.delete_data()
            elif (input_choice == 6):
                print(">>>See you later , Good bye")
                break
            else:
                print("\n>>>Error Please Choose number 1-6!!!\n")
    except:
        print("\n>>>Error Please Choose number 1-6!!!\n")
        menu()

menu()
