import strore as st
import inventory as inv


store = st.Store()
inventory = inv.Depots()
print("Welcome to store")
def menu(inp):


        if inp == 1:
            store.menu()
        elif inp == 2:
            store.menu_admin()
            pass
        elif inp == 3:
            inventory.menu_warehouser()
        elif inp == 4:
            print("Thanks for coming.\nGood by")
            exit(0) 
while (1):
    inp = int(input("1 = Stores \n2 = Admin\n3 = Warehouse\n4 = Exit\nPlease chose a option: "))
    menu(inp)