import strore as st
import json
# s = st.Store()/

a = {1:'2'}
b={2:'3'}

# with open('/Users/mohamad/Documents/vscode/matlab/a.json','a') as file:
#     json.dump(a,file,indent=4)
# with open('/Users/mohamad/Documents/vscode/matlab/a.json','a') as file:
#     json.dump(b,file,indent=4)


with open("/Users/mohamad/Documents/vscode/matlab/jsons_file/store/hasan.json",'r')as file:
    s = json.loads(file)
    print(s)
