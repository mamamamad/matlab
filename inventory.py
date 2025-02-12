import json 
import shamsi_datetime as persian_time
from datetime import datetime
import os
import strore as s


st = s.Store()


class Depots:
    
    """
    return 0 = faild
    return 1 = sucsses
    retuen 2 = bad input
    
    
    """
    
    def __init__(self):
        self.path_depots = '/Users/mohamad/Documents/vscode/matlab/jsons_file/admin/warehouser/depots/depots_path.json'
        self.path_storre = '/Users/mohamad/Documents/vscode/matlab/jsons_file/stors_path.json'
        self.admin = ''
        self.curently_path_store= ''
        self.curently_path_depot= ''
        self.store_sell_data_path = ''
        
        self.data_product_curently_store = {}
    
    def check_exist_file(self,path):
        if os.path.exists(path):
            return 1
        else:
            return 0
        
        
    def create_depots(self, name:str):
        
        all_depots={}
        if not self.check_exist_file(self.path_depots):
            try:
                with open (self.path_depots , 'w') as file:
                    all_depots[name]= f'/Users/mohamad/Documents/vscode/matlab/jsons_file/admin/warehouser/depots/{name}.json'
                    json.dump(all_depots,file,indent=4)
                    return 1
            except:
                print("error")
        else:
            with open(self.path_depots , 'r') as file:
                try:
                    all_depots=json.load(file)
                except:
                    pass          
            with open (self.path_depots , 'w') as file:
                try:
                    if name in all_depots.keys():
                        json.dump(all_depots , file , indent = 4)
                        print(" depot exist")
                        return 0 
                    else:
                        all_depots[name]= f'/Users/mohammad/Document/vscode/matlab/jsons_file/depots/{name}.json'
                        json.dump(all_depots , file , indent = 4)
                        return 1
                except:
                    print("errooos")
            
        
    def select_depot(self , name_depot:str):
        
        if not self.check_exist_file(self.path_depots):
            print("the depot is not exist")
        else:
            with open (self.path_depots , 'r+') as file:
                all_depots=json.load(file)
                if name_depot in all_depots.keys():
                    
                    self.curently_path_depot=all_depots[name_depot]  
                    print(self.curently_path_depot)
                    return 1
                else:
                    return 0      
            
    def add_object_depot(self , name:str , number:int , price:int ,volume:int, desc:str):
        if not self.check_exist_file(self.currently_path_depot):
            with open(self.currently_path_depot , 'w') as file :
                data_depot={}
                
                data_depot[name]=[number , price , volume , desc]
                json.dump(data_depot , file , indent = 4)
        else:
            if name == '' or number < 0 :
                return 2
            data_depot={}
            try:
                with open(self.currently_path_depot , 'r') as file:
                    data_depot=json.load(file)
                with open(self.currently_path_depot , 'w')as file:
                    if name in data_depot.keys():
                        return 0 
                    else:
                        data_depot[name]=[number,price,volume,desc]
                        json.dump(data_depot , file , indent = 4)
                            
            except:
                with open (self.currently_path_depot , 'w') as file :
                    if name in data_depot.keys():
                        json.dump(data_depot , file , indent = 4)
                        print(" this product exist.")
                        return 0 
                    else:
                        data_depot[name]=[number , price , volume ,desc ]
                        json.dump(data_depot , file , indent = 4)
    
    
    def show_depot_product(self):
        if not self.check_exist_file(self.curently_path_depot):
            print("not exist any prouduct. go to main")
            return 0
        else:
            try:
                object_store = {}
                with open(self.curently_path_depot,'r') as file:
                    object_store = json.load(file)
                    count = 1
                    for i ,j in object_store.items():
                        print(f"{count} - {i} : price = {j[1]} : stock = {j[0]} : Volume = {j[2]} :Description  = {j[3]}")
                        count += 1
                    self.data_product_curently_store=object_store
                    return 1
            except:
                
                print("not found depot.")          
                
    def transfer(self, name: str, quantity: int, source_depot: str, target: str, target_type: str ):
        if not self.check_exist_file(self.path_depots):
            print("depots file not exist ")
            return 0  
        try:
        
            with open(self.path_depots, 'r') as file:
                all_depots = json.load(file)
            if source_depot not in all_depots:
                print("source depot  not exist")
                return 0
            source_path = all_depots[source_depot]
            if not self.check_exist_file(source_path):
                print("Source depot invalid")
                return 0
            with open(source_path, 'r') as file:
                source_data = json.load(file)
            if name not in source_data or source_data[name][0] < quantity:
                print( f"{name} does not exist in the source depot or low quantity.")
                return 0
            source_data[name][0] -= quantity
            if source_data[name][0] == 0:
                del source_data[name]
            with open(source_path, 'w') as file:
                json.dump(source_data, file, indent=4)
            if target_type == "depot":
                if target not in all_depots:
                    print("Target depot not exist ")
                    return 0
                target_path = all_depots[target]
                if not self.check_exist_file(target_path):
                    print("Target depot invalid")
                    return 0
                with open(target_path, 'r') as file:
                    target_data = json.load(file)
                if name in target_data:
                    target_data[name][0] += quantity
                else:
                    target_data[name] = source_data[name]
                    target_data[name][0] = quantity 

                with open(target_path, 'w') as file:
                    json.dump(target_data, file, indent=4)
            
            elif target_type == "store":
                if not self.check_exist_file(target):
                    print("Store file  not exist.")
                    return 0
                with open(target, 'r') as file:
                    store_data = json.load(file)
                if name in store_data:
                    store_data[name][0] += quantity  
                else:
                    store_data[name] = source_data[name]
                    store_data[name][0]=quantity
                with open(target, 'w') as file:
                    json.dump(store_data, file, indent=4)
            else:
                print("Invalid target type . Use 'depot' or 'store'.")
                return 0
            
            print("product successfully transfered.")
            return 1
        
        except :
            print("error transfer" )
            return 0
        
        
        
    def show_depots(self):
        all_depots = {}
        count = 1
        if not self.check_exist_file(self.path_depots):
            print("depot not exist ")
            return 0
        else:
            with open(self.path_depots,'r') as file:
                all_depots = json.load(file)
            
            for i in all_depots.keys():
                print(f'{count}-->{i}')
                count += 1
            while(1):
                inp_depots = input("please enter depot name :(Exit = 0) ")
                if inp_depots in all_depots.keys():

                    self.select_depot(inp_depots)
                    return 1
                    
                elif inp_depots == 0:
                    break
                else:
                    print("this depot not exist.")
                    continue    
    
    def authorization_warehouser(self):
        while(1):
            
            with open("/Users/mohamad/Documents/vscode/matlab/jsons_file/admin/warehouser/warehouser_user.json",'r') as users_seller:
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
                
    def menu_warehouser(self):
        self.authorization_warehouser()
        while(1):

            inp1 = input('view depot inventory = 1 , view store inventory = 2 , transformation = 3 , 4 = Create warehouse , 5 = Add object to warehouse , Exit = 0')
            
            
            if inp1 == '1':
                self.show_depots()
                self.show_depot_product()
            elif inp1 == '2':
                st.show_stores()
                
                
                

            elif inp1 == '3':
                name=input(" please enter the name of perfume : ")
                quantity=int(input(f" how much {name} do u want to transfer ? "))
                source=input(f"what is the name of source depot ? ")
                target_type=input("where is your destination ? /n depot or store")
                target=input(f"what is the name of target depot or store ? ")
                self.transfer(name , quantity , source , target , target_type )
            elif inp1 == '4':
                inp_name = input("please enter name for warehouse: ")
                if self.create_depots(inp_name):
                    print("succes.")
                else:
                    print("not succes.")
            elif inp1 == '5':
                self.show_depots()
                while(1):
                    try:
                        inp_name = input("please enter name for product:")
                    except:
                        print("bad input, please try again")
                        continue
                    try:
                        inp_number = int(input("please enter number for product(int):"))
                    except:
                        print("bad input, please try again")
                        continue
                    try:
                        inp_price = int(input("please enter price for product(int):"))
                    except:
                        print("bad input, please try again")
                        continue
                    try:
                        inp_volume = int(input("please enter volume for product(int):"))
                    except:
                        print("bad input, please try again")
                        continue
                    try:
                        inp_description = input("please enter description for product:")
                    except:
                        print("bad input, please try again")
                        continue
            
                    try:
                        self.add_object_depot(inp_name,inp_number,inp_price,inp_volume,inp_description)
                    except:
                        print("bad input, please try againlll")
                        continue
                    
                    inp_exit = input("countinue (1 = Yes , 0 = No) : ")
                    if inp_exit == '1':
                        continue
                    elif inp_exit == '0':
                        break
                    else:
                        print("bad input.")
            elif inp1 == '0':
        
                break 
            else:
                print("byyyyyyyyy.")             