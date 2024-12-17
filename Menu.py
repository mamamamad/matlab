import strore as st


store = st.Store()
print("Welcome to store")
inp = int(input("1 = Customers \n2 = The seller\n3 = Admin\n4 = Exit\nPlease chose a option: "))
def menu(inp):


          
        if inp == 1:
            store.show_stores()
            inp = input("1 = Show product\n2 = Shopping cart\n3 = Menu\n4 = Exit :")
            if inp == '1':
                store.show_store_product()
            elif inp == '2':
                store.shopping_cart()
            elif inp == '3':
                menu(1)
            elif inp == '4':
                exit()
            else:
                print("Bad input.Menu......")
                menu()
        elif inp == 2 :
            store.authorization_seller()
            # self.show_product()
            pass
        elif inp == 3:
            # store.create_store('hasan')
            pass
            
        elif inp == 4:
            print(" Thanks for coming.\nGood by")
            exit(0) 
menu(inp)