

import json
with open("QWERTYU.json","r") as file:
    data=json.load(file)
print("┌────────────────────────────────────┐")
print("│                                    │")
print("│                                    │")
print("│             NCS HOSPITAL           │")
print("│────────────────────────────────────│")
print("│        1.Enter                     │")
print("│        2.View All patients         │")
print("│        3.Search By Disease         │")
print("│        4.Search By Doctor          │")
print("│        5.Add Doctor                │")
print("│        6.Discharge Patient         │")
print("│        7.Add patient               │")
print("│        8.Patient Statistics        │")
print("│        9.Exit                      │")
print("│────────────────────────────────────│")
print("│                                    │")
print("└────────────────────────────────────┘")

def View():
    for i in data:
        print(f"-----Name = {i["Name"]}------")
def Search_Disease():
    Disease=input("Enter Disease Of the Patient: ")
    f=False
    for i in data:
        if Disease==i["Disease"]:
            print("Patient Found")
            print(f"-----Name = {i["Name"]}------")
            f=True
    
    if f==False:
        print("Patient Not Found")
def Search_Doctor():
    Doctors=input("Enter Doctor Name: ")
    f=False
    for i in data:
        for j in i["Doctors"]:
            if Doctors==j["Name"]:
                print(f"-----Name = {i["Name"]}------")
                f=True
    if f==False:
        print("Patient Not Found")
    
def Add_Doctor():
   Doc_name=input("Enter Doctor Name: ")
   Time=input("Enter Timing: ")
   D=input("Enter Days:")
   N=input("Enter Patient Name: ")
   for i in data:
       if i["Name"]==N:
           i["Doctors"].append({
               "Name":Doc_name,
               "Timing":Time,
               "Days":D
           })
           break
       else:
           break
       
        
def Discharge():
    Name=input("Enter Name of Patient: ")
    for i in data:
        if Name==i["Name"]:
            data.remove(i)
            break
def Add_patient():
    Name=input("Enter Name: ")
    Disease=input("Enter Disease: ")
    Status=input("Enter Status: ")
    Doc=input("Enter Name: ")
    Time=input("Enter Timing: ")
    Days=input("Enter Das: ")
    data.append({
        "Name": Name,
        "Disease": Disease,
        "Status": Status,
        "Doctors":[{
            "Name": Doc,
            "Timing": Time,
            "Days": Days    
        }] 
    })
def Patient_Statistics():
   Name=input("Enter Name: ")
   for i in data:
       if Name==i["Name"]:
           print(f"----- Name    =   {i["Name"]}    ------")
           print(f"----- Disease =   {i["Disease"]}         ------")
           print(f"----- Status  =   {i["Name"]}    ------")
        
def Receipt():
    pass
while True:
    choice=input("What would you like to do (1-9): ")
    if choice!="9":
        if choice=="2":
            View()
        if choice=="3":
            Search_Disease()
        if choice=="4":
            Search_Doctor()
        if choice=="5":
            Add_Doctor()
        if choice=="6":
            Discharge()
        if choice=="7":
            Add_patient()
        if choice=="8":
            Patient_Statistics()
    else:
        print("Program ended")
        break
with open("QWERTYU.json","w") as file:
    json.dump(data,file,indent=4)