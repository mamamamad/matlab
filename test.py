import strore as st
import json
s = st.Store()
s.curently_path_store = '/Users/mohamad/Documents/vscode/matlab/a.json'
s.add_object_store('h',12,12)


with open("/Users/mohamad/Documents/vscode/matlab/jsons_file/store/hasan.json",'r')as file:
    s = json.load(file)
    print(s)
