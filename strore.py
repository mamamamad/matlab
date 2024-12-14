import json


class Store:
    """
    return 0 = faild
    return 1 = sucsses
    retuen 2 = bad input
    
    
    """
    
    def __init__(self):
        self.path_depots = '/depots_path.json'
        self.path_store = '/stors_path.json'
        self.admin = ''
        self.curently_path_store= ''
        self.curently_path_depot= ''
        
    
    def create_store(self,name:str):
        ''' this def can create a new strore.'''
        with open(self.path_store,'r+') as file:
            all_store = json.load(file)
            
            if name in all_store.key():
                return 0
            else:
                all_store[name]= f'/{name}.json'
                json.dump(all_store,self.path_store,indent= 4)
                return 1
            
    def select_store(self,name_store:str):
        '''this def select store in the all stores.'''
        with open(self.path_store,'r+') as file:
            all_store = json.load(file)
            
            if name_store in all_store.key():
                self.curently_path_store = all_store[name_store]
                return 1
            else:
                return 0
                
                   
    def add_object_store(self, name: str, number: int):
        '''this def add a new object in store.'''
        if name == '' or number < 0:
            return 2
        
        data_store = {}
        with open(self.curently_path_store,'r+') as file:
            data_store = json.load(file)
        
            if name in data_store.key():
                return 0
            else:
                data_store[name]=number
                json.dump(data_store,self.curently_path_store,indent=4)
    def update_object_store(self,name:str):
        '''This function updates an existing object using its name or number.'''

        if name == '' :
            return 2
        
        data_store = {}
        with open(self.curently_path_store,'r+') as file:
            data_store = json.load(file)
            
            if name in data_store.key():
                print(f"{name} = {data_store[name]}")   
                while(1):
                    chose_inp = int(input("1 = update name \n2 = update number\n3 = exit\nplease chose a option :"))  
                    if chose_inp == 1:
                        inp_name = inp_number("please enter new name: ")
                        if inp_name == '':
                            print("the unvalid input , try again")
                            continue
                        else :
                            data_store[inp_name] = data_store.pop(name)
                        json.dump(data_store,self.curently_path_store,indent=4) 
                        break                                                                                                                    
                    elif chose_inp == 2:
                        inp_number = int(input("please enter number: "))
                        if inp_number < 0 :
                            print("the unvalid input , try again")
                            continue
                        else:
                            data_store[name] = inp_number
                        
                        json.dump(data_store,self.curently_path_store,indent=4)
                        break
                    elif chose_inp == 3:
                        break
                    else:
                        print("the unvalid input.")
                        continue
    
    def show_stores(self):
        all_store = {}
        count = 1
        with open(self.path_store,'r') as file:
            all_store = json.load(file)
        
        for i in all_store.key():
            print(f'{count}-{i}')
        while(1):
            inp_store = int(input("please enter number of store:(Exit = 0) "))
            if inp_store > count or inp_store <0 :
                print("unvalid input , try again")
                continue
            else:
                count = 1 
                for i in all_store.keys():
                    if inp_store == count:
                        flag = self.select_store(i)
                    if flag == 0 :
                        print("bad input.")
                        continue
            
    def authorization_seller(self):
        while(1):
            with open("/seller_user.json",'r') as users_seller:
                username = input("please enter user name:(Exit = 0)") 
                password = input("please enter password: ")
                users_data = json.load(users_seller)
                if username in users_data.keys():
                    for i in range(1,4):
                        if password == users_data[username][0]:
                            self.select_store(users_data[username][1])
                        else:
                            print(f"unvalid password : {3-i} chance")
                            continue                            
                    
                    
                    
                     
    def menu(self):
        print("Welcome to store")
        inp = int(input("1 = Customers \n2 = The seller\n3 = Admin\n4 = Exit\nPlease chose a option: "))  
        if inp == 1:
            self.show_stores()
        elif inp == 2 :
            self.authorization_seller()
            # self.show_product()
            pass
        elif inp == 3:
            pass
        elif inp == 4:
            print(" Thanks for coming.\nGood by")
            exit(0)   
                
                        