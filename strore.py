import json
import shamsi_datetime as persian_time
from datetime import datetime
import os

class Store:
    """
    return 0 = faild
    return 1 = sucsses
    retuen 2 = bad input
    
    
    """
    
    def __init__(self):
        self.path_depots = '/Users/mohamad/Documents/vscode/matlab/jsons_file/depots_path.json'
        self.path_store = '/Users/mohamad/Documents/vscode/matlab/jsons_file/stors_path.json'
        self.admin = ''
        self.curently_path_store= ''
        self.curently_path_depot= ''
        self.store_sell_data_path = ''
        self.shopping_cart_dict={}
        self.data_product_curently_store = {}
        
    def check_exist_file(self,path):
        if os.path.exists(path):
            return 1
        else:
            return 0
            
 
    
    def create_store(self,name:str):
        ''' this def can create a new strore.'''
        
        all_store ={}
        if not self.check_exist_file(self.path_store):
            
            with open(self.path_store,'w') as file:
                all_store[name]= f'/Users/mohamad/Documents/vscode/matlab/jsons_file/store/{name}.json'
                
                json.dump(all_store,file,indent= 4)
                return 1
        else:
            with open(self.path_store,'r') as file:
                try:
                    all_store = json.load(file)  
                except:
                    pass
                    
            with open(self.path_store,'w') as file:
                if name in all_store.keys():
                        
                        json.dump(all_store,file,indent= 4)
                        print("the store exist.")
                        return 0
                else:
                    all_store[name]= f'/Users/mohamad/Documents/vscode/matlab/jsons_file/store/{name}.json'
                    json.dump(all_store,file,indent= 4)
                    return 1
            
                   
    def select_store(self,name_store:str):
        '''this def select store in the all stores.'''
        if not self.check_exist_file(self.path_store):
            print("the store is not exist.")
        else:
            with open(self.path_store,'r+') as file:
                all_store = json.load(file)
                
                if name_store in all_store.keys():
                    self.curently_path_store = all_store[name_store]
                    self.store_sell_data_path = f'/Users/mohamad/Documents/vscode/matlab/jsons_file/sell/sell_{all_store[name_store]}'
                    
                    return 1
                else:
                    return 0
                                
    def add_object_store(self, name: str, number: int,price:int,volume:int, desc:str ):
        '''this def add a new object in store.'''
        
        if not self.check_exist_file(self.curently_path_store):
            with open(self.curently_path_store,'w') as file:
                data_store = {}
                data_store[name]=[number,price]
                json.dump(data_store,file,indent=4)
        else:
            if name == '' or number < 0:
                return 2
            
            data_store = {}
            try:
                with open(self.curently_path_store,'r') as file:
                    data_store = json.load(file)
                
                with open(self.curently_path_store,'w') as file:
                    if name in data_store.keys():
                        return 0
                    else:
                        data_store[name]=[number,price,volume,desc]
                        json.dump(data_store,file,indent=4)
            except:
                    with open(self.curently_path_store,'w') as file:
                        if name in data_store.keys():
                            json.dump(data_store,file,indent=4)
                            print("this product exist.")
                            return 0
                        else:
                            data_store[name]=[number,price,volume,desc]
                            json.dump(data_store,file,indent=4)    
    def update_object_store(self,name:str):
        '''This function updates an existing object using its name or number.'''

        if name == '' :
            return 2
        data_store = {}
        if not self.check_exist_file(self.curently_path_store):
            print("this store is not exist.")
        else:
            with open(self.curently_path_store,'r') as file:
                data_store = json.load(file)
                
                if name in data_store.keys():
                    print(f"{name} = {data_store[name]}")   
                    while(1):
                        chose_inp = int(input("1 = update name \n2 = update number\n3 = update price\n4 = exit\nplease chose a option :"))  
                        if chose_inp == 1:
                            inp_name = input("please enter new name: ")
                            if inp_name == '':
                                print("the unvalid input , try again")
                                continue
                            else :
                                data_store[inp_name] = data_store.pop(name)
                            with open(self.curently_path_store,'w') as file:
                                    json.dump(data_store,file,indent=4) 
                            break                                                                                                                    
                        elif chose_inp == 2:
                            inp_number = int(input("please enter new number: "))
                            if inp_number < 0 :
                                print("the unvalid input , try again")
                                continue
                            else:
                                data_store[name][0] = inp_number
                            
                            with open(self.curently_path_store,'w') as file:
                                    json.dump(data_store,file,indent=4)
                            break
                        elif chose_inp == 3:
                            inp_number = int(input("please enter new price: "))
                            if inp_number < 0 :
                                print("the unvalid input , try again")
                                continue
                            else:
                                data_store[name][1] = inp_number
                            
                            with open(self.curently_path_store,'w') as file:
                                    json.dump(data_store,file,indent=4)
                            break
                        elif chose_inp == 4:
                            break
                        else:
                            print("the unvalid input.")
                            continue
    
    def show_stores(self):
        all_store = {}
        count = 1
        if not self.check_exist_file(self.path_store):
            print("not have store exist.")
            return 0
        else:
            with open(self.path_store,'r') as file:
                all_store = json.load(file)
            
            for i in all_store.keys():
                print(f'{count}-{i}')
                count += 1
            while(1):
                inp_store = input("please enter name of store:(Exit = 0) ")
                if inp_store in all_store.keys():
                    self.select_store(i)
                    return 1
                    
                elif inp_store == 0:
                    break
                else:
                    print("this store not exist.")
                    continue
                
    def show_store_product(self):
        if not self.check_exist_file(self.curently_path_store):
            print("not exist any prouduct. go to main")
            return 0
        else:
            # try:
                object_store = {}
                with open(self.curently_path_store,'r') as file:
                    object_store = json.load(file)
                    count = 1
                    for i ,j in object_store.items():
                        print(f"{count} - {i} : price = {j[1]} : stock = {j[0]} : Volume = {j[2]} :Description  = {j[3]}")
                        count += 1
                    self.data_product_curently_store=object_store
                    return 1
            # except:
            #     print(self.curently_path_store)
            #     print("not found store.")
                    
        
    def Buy_product(self,inp_prouduct : dict):
        select_product = input("Please enter the name product:")
        if select_product not in inp_prouduct.keys():
            inp = input("this product not exist.(try agein = 0 , menu = 1)")
            if inp == '0':
                self.Buy_product(inp_prouduct)
            elif inp == '1':
                pass
            else:
                print("bad input.")
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
                      
    def check_save_stock(self,inp_product:dict,number,name):
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
            if not self.check_exist_file(self.store_sell_data_path):
                with open(self.store_sell_data_path,'w') as file:
                    json.dump(self.shopping_cart_dict,file,indent=4)
            else:
                data = {}
                with open(self.store_sell_data_path,'r') as file:
                    data = json.load(file)
                        

        except:
            return 0 
    def delete_product(self,name:str):
        if not self.check_exist_file(self.curently_path_store):
            print("not exist.")
        else:
            with open(self.curently_path_store,'r') as file:
                data = json.load(file)
                if name in data.keys():
                    
                    data.pop(name)
                    with open(self.curently_path_store,'w') as file2:
                        json.dump(data,file2,indent=4)
                    print("product deleted.")
                else:
                    print("not founded product.")
        
    
    def delete_store(self,name:str):
        if not self.check_exist_file(self.path_store):
            print("not exist.")
        else:
            with open(self.path_store,'r') as file:
                data = json.load(file)
                if name in data.keys():
                    data.pop(name)
                    with open(self.path_store,'w') as file2:
                        json.dump(data,file2,indent=4)
                    
                    print("delete store.")
                else:
                    print("not store.")
        
        
        
        
        
        
    
                    
    def payment(self):
        inp = input("are you sure for payment ?? (Yes = 1 , No = 0)")
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
          
    def authorization_Admin(self):
        while(1):
            
            with open("/Users/mohamad/Documents/vscode/matlab/jsons_file/admin/Admins_user.json",'r') as users_seller:
                username = input("please enter user name:(Exit = 0)") 
                if username == '0':
                    break
                password = input("please enter password: ")
                users_data = json.load(users_seller)
                if username in users_data.keys():
                    for i in range(1,4):
                        if password == users_data[username]:
                            print("sucsses")
                            return 1
                        else:
                            print(f"unvalid password : {3-i} chance")
                            continue   
                    return 0                          
    def menu_admin(self):
        while(1):
            self.authorization_Admin()
            inp1 = input('Create or update product = 1 , Delete product = 2 , Delete store = 3 , Create store = 4  , Exit = 0')
            self.show_stores()
            
            if inp1 == '1':
                inp = input("Add product = 1 , Update product = 2 , Exit = 0: ")
                if inp == '1':
                    name = input('please enter name: ')
                    number = input('please enter number: ')
                    price = input('please enter price: ')
                    volume = input('please enter volume: ')
                    des = input('please enter Description: ')
                    self.add_object_store(name,int(number),int(price),int(volume),des)
                    print("added")
                elif inp == '2':
                    self.show_store_product()
                    name = input('please enter name: ')
                    self.update_object_store(name)
                    print("updated.")
                elif inp == '0':
                    pass
                else:
                    pass
            elif inp1 == '2':
                self.show_store_product()
                name = input('please enter name: ')
                self.delete_product(name)
                
            elif inp1 == '3':
                name = input('please enter name: ')
                self.delete_store(name)
            elif inp1 == '4':
                name = input('please enter name: ')
                self.create_store(name)
                price("created") 
            elif inp1 == '0':
                break 
            else:
                print("by.") 
    def menu(self)->None:
            inp = input("1 = Show product\n2 = Shopping cart\n3 = Menu\n4 = Exit :")
            if inp == '1':
                while(1):
                    if self.show_stores():
                        break
                    else:
                        continue
                if not self.show_store_product():
                    pass
                else:
                    self.Buy_product(self.data_product_curently_store)
                    while(1):
                        inp = input("Buy again = 1 , Continue = 2 :")
                        if inp == '1':
                            self.show_store_product()
                            self.Buy_product(self.data_product_curently_store)
                        elif inp == '2':
                            break
                        else:
                            print("bad input, try again.")
                    self.payment()
                    self.save_all_data()
            elif inp == '2':
                self.shopping_cart()
            elif inp == '3':
                pass
            elif inp == '4':
                exit()
            else:
                print("Bad input.Menu......")
                pass