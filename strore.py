import json
import shamsi_datetime as persian_time
from datetime import datetime

class Store:
    """
    return 0 = faild
    return 1 = sucsses
    retuen 2 = bad input
    
    
    """
    
    def __init__(self):
        self.path_depots = '/home/mmd/vscode/matlab/database/depots_path.json'
        self.path_store = '/home/mmd/vscode/matlab/database/stors_path.json'
        self.admin = ''
        self.curently_path_store= ''
        self.curently_path_depot= ''
        self.store_sell_data_path = ''
        self.shopping_cart_dict={}
        self.data_product_curently_store = {}
        
    
    def create_store(self,name:str):
        ''' this def can create a new strore.'''
        with open(self.path_store,'r') as file:
            all_store = {}
            try:
                all_store = json.load(file)
                
            except:
                pass
        with open(self.path_store,'w') as file:
            if name in all_store.keys():
                    return 0
            else:
                all_store[name]= f'/{name}.json'
                print(all_store)
                json.dump(all_store,file,indent= 4)
                return 1
            
            
            
            
             
                
            
    def select_store(self,name_store:str):
        '''this def select store in the all stores.'''
        with open(self.path_store,'r+') as file:
            all_store = json.load(file)
            
            if name_store in all_store.keys():
                self.curently_path_store = all_store[name_store]
                self.store_sell_data_path = f'sell_{all_store[name_store]}'
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
        
            if name in data_store.keys():
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
            
            if name in data_store.keys():
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
        
        for i in all_store.keys():
            print(f'{count}-{i}')
            count += 1
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
    
    
    def show_store_product(self):
        with open(self.curently_path_store,'r') as file:
            object_store = json.load(file)
            count = 1
            for i ,j in object_store.items():
                print(f"{count} - {i} : price = {j[1]} : stock = {j[0]} : Description  = {j[2]}")
                count += 1
            self.data_product_curently_store=object_store
        
    def Buy_product(self,inp_prouduct : dict):
        select_product = input("Please enter the name product:")
        if select_product not in inp_prouduct.keys():
            inp = input("this product not exist.(try agein = 0 , menu = 1)")
            if inp == '0':
                self.Buy_product(inp_prouduct)
            else:
                pass
        else:
            number_product = input("please enter number of product: ")
            check = self.check_stock(inp_prouduct,number_product,select_product)
            if not check:
                print("This value is not available,Try Again")
                self.Buy_product(inp_prouduct)
            else:
                inp_prouduct[select_product][0] = check
                inp = input("going shopping cart?(1 = yes , 0 = no)")
                if inp == '1':
                    self.shopping_cart()
                    self.data_product_curently_store = inp_prouduct
                elif inp == '0':
                    self.Buy_product()
                else:
                    print('bad input,fuck you.\n shopping cart.....')
                    self.shopping_cart()  
                      
    def check_stock(self,inp_product:dict,number,name):
        if number > inp_product[name][0]:
            return 0
        else:
            date = str(persian_time.ShamsiDateTime())
            now = datetime.now()
            current_time = str(now.strftime("%H:%M:%S"))
            
            self.shopping_cart_dict[name] = [number,inp_product[name][1],date,current_time]
                
            return  int(inp_product[name][0])-number
        
    
    def shopping_cart(self):
        inp = input("1 = Payment\n2 = Menu")          
        n = 1
        for i ,j in self.shopping_cart.items():
            print(f'{n} - {i} | {j[0]} | {j[0]*j[1]}')
            n+=1
        if inp == '1':
            self.payment()
        elif inp == '2':
            pass
        else:
            print("bad input.")
            
    def save_all_data(self):
        try:
            with open(self.curently_path_store,'w') as file:
                json.dump(self.data_product_curently_store,file,indent=4)
            with open(self.store_sell_data_path,'w') as file:
                json.dump(self.shopping_cart_dict,file,indent=4)
        except:
            return 0 
                
    def payment(self):
        inp = input("are you sure for pament ?? (Yes = 1 , No = 0)")
        if inp == '1':
            i = self.save_all_data()
            print("thanks for shopping.")
            if i == 0 :
                print("eRooor")
            else:
                pass
        elif inp == '0':
            print("menu...")
            pass
          
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
                      
                
                        