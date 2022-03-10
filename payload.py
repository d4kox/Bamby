import os
os.system('C:')
def charge_exploit():
    git_url = input("Git URL >>> ")
    os.system('cd "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\exploits"')
    os.system('git clone ' + git_url)

def execute_exploit():
    interprete = input("Python or Bat File?[p/b] > ")
    name_folder = input("Name of Folder >>> ")
    name_file  = input("Name of File >>> ")
    if interprete == "p":
        os.system('cd "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\exploits"')
        os.system('cd '+ name_folder)
        os.system('python '+ name_file +'.pyw')
    elif interprete == "b":
        os.system('cd "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\exploits"')
        os.system('cd '+ name_folder)
        os.system('start '+ name_file +'.bat')
    else:
        print("[-] Err Detected")
        execute_exploit()
def question_exploit():
    exp_action = input("Exploit or Charge?[e/c]")
    if exp_action == "c":
        charge_exploit()
    elif exp_action == "e":
        execute_exploit()
    else:
        print("[-] Err Detected")
        question_exploit()
os.system('C:')
question_exploit()
