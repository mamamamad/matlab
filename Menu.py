import strore as st


store = st.Store()
def menu():
        print("Welcome to store")
        inp = int(input("1 = Customers \n2 = The seller\n3 = Admin\n4 = Exit\nPlease chose a option: "))  
        if inp == 1:
            store.show_stores()
        elif inp == 2 :
            store.authorization_seller()
            # self.show_product()
            pass
        elif inp == 3:
            pass
        elif inp == 4:
            print(" Thanks for coming.\nGood by")
            exit(0) 