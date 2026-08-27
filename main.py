import json
import string
from datetime import date
import csv


def seperate_weight_date(text):
    sep=text.find("-")
    if(sep==-1):
        sep=text.find("-")
    weight=float(text[:sep])
    date_text=text[sep+1:]
    date=org_date(date_text)
    result={"weight":weight,"date":date}
    return result

def org_date(text):
    date_sep1=text.find("/")
    date_sep2=text.find("/",date_sep1+1)
    day=text[:date_sep1]
    month=text[date_sep1+1:date_sep2]
    year=text[date_sep2+1:]
    date=year+"-"+month+"-"+day
    return date


def check_format(text):
    try:
        seperate_weight_date(text)
    except:
        return False
    return True

def add_mesurement(data,new):
    lena=len(data)
    index=0
    if new["date"]==None:
        data.append(new)
        return data
    comp_date=date.fromisoformat(new["date"])
    if lena==0 or date.fromisoformat(data[lena-1]["date"])<=date.fromisoformat(new["date"]):
        data.append(new)
        return data

    if date.fromisoformat(data[index]["date"])>=date.fromisoformat(new["date"]):
        data.insert(0,new)
        return data
    
    while(True):
        comp=int((lena+index)/2)
        date1=date.fromisoformat(data[comp]["date"])
        if(comp_date>date1):
            index=comp
        elif(comp_date<date1):
            lena=comp
        else:
            data.insert(lena,new)
            break
        if(lena==index+1):
            if(comp_date<date.fromisoformat(data[index]["date"])):
                data.insert(index,new)
            else:
                data.insert(lena,new)
            break
    return data
        
def print_data(data_file):
    try:
        with open(data_file,"r") as file:
            data=json.load(file)
        if(len(data)==0):
            print("There is nothing to see here. Add some measurements first!")
        else:
            for i in data:
                print("Date:",i["date"]," Weight:",i["weight"])
    except FileNotFoundError:
        print("No previous results were found :(") 


data_file="data.json"
menu=0
print("Menu:\n \
Press 1 to see previous weight measurements\n \
Press 2 to add a new result manually\n \
Press 3 to add new results from a file\n \
Press 4 to delete or change an existing result\n \
Press 5 to analyze results\n \
Press 6 to delete your data\n \
Press 7 to exit.")
while(menu!="7"):
    menu=input("Enter your choice (press 0 to see menu): ")
    if(menu=="1"):
        print_data(data_file)
    elif(menu=="2"):
        text_data=input("Enter your measurement and its date (\"12.34-day/month/year\"): ")
        while(text_data!="c" and check_format(text_data)==False):
            text_data=input("Please follow the format \"12.34-day/month/year\" (c to cancel): ")
        if text_data=="c":
            print("Returning to the main menu...")
        else:
            dic_data=seperate_weight_date(text_data)
            try:
                with open(data_file,"r") as file:
                    data=json.load(file)
                arr=add_mesurement(data,dic_data)
                with open(data_file,"w") as file:
                    json.dump(arr,file)
            except:
                data=[]
                arr=add_mesurement(data,dic_data)
                with open(data_file,"w") as file:
                    json.dump(arr,file)

    elif(menu=="3"):
        fileName=input("Enter the file name: ")
        select=input("CSV file or 12.34-day/month/year format? (1/2): ")
        if(select=="1"):
            try:
                with open(data_file,"r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                data=[]
            try:
                with open(fileName, "r") as csv_file:
                    csv_reader=csv.reader(csv_file)
                    next(csv_reader)
                    for line in csv_reader:
                        try:
                            line_date=org_date(line[1])
                        except:
                            line_date=None
                        dict_data={"weight":line[0],"date":line_date}
                        add_mesurement(data,dict_data)
                    with open(data_file, "w") as file:
                        json.dump(data,file)
                    print("Done :)")
                    print_data(data_file)
            except FileNotFoundError:
                print("File does not exist.")


        elif(select=="2"):
            try:
                with open(data_file,"r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                data=[]
            try:
                with open(fileName,"r") as file:
                    for line in file:
                        line=line.strip()
                        if(check_format(line)):
                            dict_data=seperate_weight_date(line)
                            add_mesurement(data,dict_data)
                        else:
                            print("Error! Couldn't process the data.")
            except FileNotFoundError:
                print("File does not exist.")
            with open(data_file, "w") as file:
                json.dump(data,file)
        else:
            print("Invalid choice :(")

    elif(menu=="4"):
        try:
            with open(data_file,"r") as file:
                data=json.load(file)
            index=0
            for i in data:
                index+=1
                print(index,")","Date:",i["date"]," Weight:",i["weight"])
        except FileNotFoundError:
            print("No previous results were found :(")
        if(len(data)==0):
            print("Empty!!")
        else:
            try:
                select=int(input("Select the measurement you want to modify: "))
                while(int(select)<=0 or int(select)>len(data)):
                    select=input("Select a valid measurement: ")
                choice=input("Delete or modify? d/m (c to cancel): ")
                while(True):
                    if(choice=="d"):
                        data.pop(int(select)-1)
                        break
                    elif(choice=="m"):
                        text_data=input("Enter the new measurement (\"12.34-day/month/year\"): ")
                        while(check_format(text_data)==False):
                            text_data=input("Enter the new measurement in the correct format (\"12.34-day/month/year\"): ")
                        dict_data=seperate_weight_date(text_data)
                        add_mesurement(data,dict_data)
                        data.pop(int(select)-1)
                        break
                    elif(choice=="c"):
                        break
                    else:
                        choice=input("Delete or modify? d/m (c to cancel): ")
                with open(data_file,"w") as file:
                    json.dump(data,file)
                print("Done :)")
                print_data(data_file)
            except:
                print("Invalid input :(")
        


    elif(menu=="5"):
        print("Under maintenance. Please try again later.")

    elif(menu=="6"):
        sure=input("Are you sure? (y/n) ")
        if(sure=="y"):
            data=[]
            with open(data_file,"w") as file:
                json.dump(data,file)
        elif(sure=="n"):
            print("Cancelled.")
        else:
            print("Invalid answer :((")
    
    elif(menu=="7"):
        print("Goodbye :)")

    elif(menu=="0"):
        print("Menu:\n \
Press 1 to see previous weight measurements\n \
Press 2 to add a new result manually\n \
Press 3 to add new results from a file\n \
Press 4 to delete or change an existing result\n \
Press 5 to analyze results\n \
Press 6 to delete your data\n \
Press 7 to exit.")
