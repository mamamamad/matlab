import strore as st


store = st.Store()
print("Welcome to store")
def menu(inp):


          
        if inp == 1:
            store.menu()
        elif inp == 2 :
            pass
        elif inp == 3:
            store.menu_admin()
            pass
            
        elif inp == 4:
            print("Thanks for coming.\nGood by")
            exit(0) 
while (1):
    inp = int(input("1 = Customers \n2 = The seller\n3 = Admin\n4 = Exit\nPlease chose a option: "))
    menu(inp)