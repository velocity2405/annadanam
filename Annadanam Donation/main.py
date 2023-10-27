import customtkinter as ctk
from tkinter import *
import tkinter as Tk
from tkinter import ttk
import csv
import random
import string
from datetime import datetime
from datetime import date
import smtplib
from tabulate  import tabulate
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from PIL import Image

import random 

welwin = ctk.CTk()
welwin.title("Welcome Page")
welwin.geometry("380x350")
welwin.resizable(False,False)

f_key = open('BRS_hack\Bingskey.txt', 'r')
USERS_FILE = r'BRS_hack\users.csv'
DONATIONS_FILE = r'BRS_hack\donations.csv'
AVAILABLE_FILE = r'BRS_hack\available_donations.csv'
EXPIRED_ORDERS = r'BRS_hack\Expired_orders.csv'
PAST_ORDERS = r'BRS_hack\past_orders.csv'
LOCATIONS = r"BRS_hack\user_locations.csv"
Bing_Map_Key = f_key.read()
app_password = "suns enhv fupf vvot"

def viewDonations(username):
        refwin = ctk.CTkToplevel()
        refwin.title("View all Donations")
        refwin.geometry("1500x300")

        with open(DONATIONS_FILE, mode='r') as donations_file:
            reader = csv.reader(donations_file)
            
            column_name = ("0","1","2","3","4","5","6","7","8","9")
            treeview_vehicles = ttk.Treeview(refwin,columns=column_name)
            treeview_vehicles['show'] = 'headings'
            
            style = ttk.Style(treeview_vehicles) 
            style.theme_use("clam") 
            style.configure("Treeview", background="black", 
                            fieldbackground="black", foreground="white",font=('Calibri', 13))
            style.configure('Treeview.Heading', background="PowderBlue",font=('Calibri', 13,'bold'))
          
            treeview_vehicles.column("0",width=100,anchor="center")
            treeview_vehicles.heading("0",text="Donation ID")

            treeview_vehicles.column("1",anchor="center")
            treeview_vehicles.heading("1",text="Name")

            treeview_vehicles.column("2",anchor="center")
            treeview_vehicles.heading("2",text="Username")

            treeview_vehicles.column("3",anchor="center")
            treeview_vehicles.heading("3",text="Item")

            treeview_vehicles.column("4",anchor="center")
            treeview_vehicles.heading("4",text="Quantity")

            treeview_vehicles.column("5",anchor="center")
            treeview_vehicles.heading("5",text="Category")

            treeview_vehicles.column("6",anchor="center")
            treeview_vehicles.heading("6",text="Shelf Life")

            treeview_vehicles.column("7",anchor="center")
            treeview_vehicles.heading("7",text="MD")

            treeview_vehicles.column("8",anchor="center")
            treeview_vehicles.heading("8",text="Best Before")

            treeview_vehicles.column("9",anchor="center")
            treeview_vehicles.heading("9",text="Donation Date")


            treeview_vehicles.pack(fill=Tk.BOTH, expand=True)

            for row in reader:
                if row[0]=="Donation ID":
                    continue
                else:
                    treeview_vehicles.insert("",Tk.END,values=row)
        refwin.mainloop()

def itemlist(num,name,username):
        n = int(num.get())
        global x
        x = 2

        items = ctk.CTk()
        items.geometry("500x500")
        items.resizable(False,False)
        items.title("Donation Window")

        def process_donations(name, username,food_data,field1,field2,field3,field4,field5,field6):
            global x
            with open(DONATIONS_FILE, mode='a', newline='') as donations_file:
                writer = csv.DictWriter(donations_file, fieldnames=food_data.keys())
                writer.writerow(food_data)
       

            with open(AVAILABLE_FILE, mode='a', newline='') as donations_file:
                writer = csv.DictWriter(donations_file, fieldnames=food_data.keys())
                writer.writerow(food_data)
               

            if x <= n:
                top.configure(text="Enter Details of item "+str(x))
                field1.delete(0, END)
                field2.delete(0, END)
                field3.delete(0, END)
                field4.delete(0, END)
                field5.delete(0, END)
                field6.delete(0, END)
                
         
                x = x+1
            else:
                items.destroy()

                
        top = ctk.CTkLabel(items,text="Enter Details of item 1",font=("Poplar Std",25))
        itemName = ctk.CTkLabel(items,text="Enter Item Name?",font=("Poplar Std",15))
        quantity = ctk.CTkLabel(items,text="Enter Quantity?",font=("Poplar Std",15))
        shelf_life = ctk.CTkLabel(items,text="Enter Shelf Life?",font=("Poplar Std",15))
        category = ctk.CTkLabel(items,text="Choose Category",font=("Poplar Std",15))
        manufacture = ctk.CTkLabel(items,text="Enter Manufacturing Date?",font=("Poplar Std",15))
        expiry = ctk.CTkLabel(items,text="Enter Expiry Date?",font=("Poplar Std",15))

        field1 = ctk.CTkEntry(items)
        field2 = ctk.CTkEntry(items)
        field3 = ctk.CTkEntry(items)
        field4 = ctk.CTkEntry(items)
        field5 = ctk.CTkEntry(items)
        field6 = ctk.CTkEntry(items)
        donation_date = datetime.now().date()
        
        def get(name,username,field1,field2,field3,field4,field5,field6,donation_date):
            iTem = field1.get()
            qUantity = field2.get()
            sHelfLife = field3.get()
            cAtegory = field4.get()
            manu_date = field5.get()
            exp_date = field6.get()
         
            number = random.randint(1111,9999)
       

            item = {"Donation ID": number,
                "Name": name,
                "Username": username,
                "Item": iTem,
                "Quantity": qUantity, 
                'Category': cAtegory, 
                'Shelf Life': sHelfLife, 
                'MD': manu_date, 
                'Best Before': exp_date,
                'Donation Date':donation_date,
                'Account Type': 'Individual'}
                
            process_donations(name,username,item,field1,field2,field3,field4,field5,field6)
            
        
        butdon = ctk.CTkButton(items,text="Donate",command=lambda:get(name,username,field1,field2,field3,field4,field5,field6,donation_date),height=40,width=100,corner_radius=6)
        
                
        top.pack()
        itemName.place(x=75,y=100)
        quantity.place(x=75,y=150)
        shelf_life.place(x=75,y=200)
        category.place(x=75,y=250)
        manufacture.place(x=75,y=300)
        expiry.place(x=75,y=350)


        field1.place(x=275,y=100)
        field2.place(x=275,y=150)
        field3.place(x=275,y=200)
        field4.place(x=275,y=250)
        field5.place(x=275,y=300)
        field6.place(x=275,y=350)

        butdon.place(x=200,y=400)

        items.mainloop()

def donating(name,username):
    don = ctk.CTkToplevel()
    don.title("Donations")
    don.resizable(False,False)
    numLabel = ctk.CTkLabel(don,text="How many items are you willing to donate?",font=("Poplar Std",18))
    num = ctk.CTkEntry(don)
    
    but1 = ctk.CTkButton(don,text="Proceed",command=lambda:itemlist(num,name,username),height=40,width=100,corner_radius=6)
    numLabel.pack(pady=10)
    num.pack(pady=10)
    but1.pack(pady=10)
    don.mainloop()

def logged_out1(ind):
        ind.destroy()

def individual(name,username):

    ind = ctk.CTk()
    ind.title("Donater Menu")
    ind.geometry("300x350")
    ind.resizable(False,False)
        
    head = ctk.CTkLabel(ind,font=("Poplar Std",25),text="Main Menu")
    map = ctk.CTkButton(ind,text="Generate a map",command=lambda:generate_map(name,username),height=40,width=100,corner_radius=6)
    donate = ctk.CTkButton(ind,text="Donate Food",command=lambda:donating(name,username),height=40,width=100,corner_radius=6)
    viewDon = ctk.CTkButton(ind,text="View Donations",command=lambda:viewDonations(username),height=40,width=100,corner_radius=6)
    logout = ctk.CTkButton(ind,text="Logout",command=lambda:logged_out1(ind),height=40,width=100,corner_radius=6)


    head.pack()
    map.pack(pady=20)
    donate.pack(pady=20)
    viewDon.pack(pady=20)
    logout.pack(pady=20)
    ind.mainloop()





def generate(avoidChoice,optimizeChoice,layerchoice,username,user):

    with open(LOCATIONS, mode='r') as fuser_location:
        mapuser = user.get()
        data = csv.DictReader(fuser_location)
   
        for row in data:
            if row['Username'] == mapuser:
                waypoint1_lat= row['Latitude']
                waypoint1_long = row['Longitude']
           
            elif row['Username'] == username:
                waypoint2_lat = row['Latitude']
                waypoint2_long = row['Longitude']
             
    fuser_location.close()


    choice1 = avoidChoice.get()
    avoid = ""

    if choice1 == "Tolls":
        avoid = 'tolls'
    elif choice1 == "Highways":
        avoid = 'highwayss'
    elif choice1 == "Both":
        avoid = 'tolls,highways'



    choice2 = optimizeChoice.get()
    optimize = ''   


    if choice2 == "Distance":
        optimize = 'distance'
    elif choice2 == "Time":
        optimize = 'time'
    elif choice2 == "Time with Traffic":
        optimize = 'timeWithTraffic'



    choice3 = layerchoice.get()
    mapLayer = ''

    if choice3 == 'Yes':
        mapLayer = "TrafficFlow"
    elif choice3 == 'No':
        mapLayer = "Basemap,Buildings"




    BingMapsKey = '4PeiHseS3BZWIvMgwXOu~_b4zW7lWh5IoNkEb6beqXg~Ah0awLZR1Qdnt1MM20DSTYl0bseNjNSXvmHAEmUtMKlfMqA2koNgsZAW6-jyNKmM'

    


    r = requests.get(f"https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?waypoint.1={waypoint1_lat},{waypoint1_long}&waypoint.2={waypoint2_lat},{waypoint2_long}&pushpin={waypoint1_lat},{waypoint1_long}&pushpin={waypoint2_lat},{waypoint2_long}&mapSize=800,800&avoid={avoid}&maxSolutions=1&mapLayer={mapLayer}&optmz={optimize}&format=png&mapMetadata=0&key={BingMapsKey}")


    f = open('Map.png', 'wb')
    f.write(r.content)
    f.close()

    img = Image.open("Map.png")
    img.show()
        
def generate_map(name, username):
    map = ctk.CTk()
    map.title("Map Generator")
    header = ctk.CTkLabel(map,text="Map Generator",font=("Poplar Std",15))
    userLabel = ctk.CTkLabel(map,text="Enter username of Receiver or Sender:")
    user = ctk.CTkEntry(map)
    
    
    avoidLabel = ctk.CTkLabel(map,text="What do you want to avoid")
    n=ctk.StringVar()
    avoidChoice = ctk.CTkComboBox(map,values=["Tolls","Highways","Both"],variable=n)
 

    optimizeLabel = ctk.CTkLabel(map,text="How do you want to optimize")
    k=ctk.StringVar()
    optimizeChoice = ctk.CTkComboBox(map,values=["Distance","Time","Time with Traffic"],variable=k)
   

    layerLabel = ctk.CTkLabel(map,text="Would you like to display Traffic")
    b=ctk.StringVar()
    layerchoice = ctk.CTkComboBox(map,values=["Yes","No"],variable=b)
   

    execute = ctk.CTkButton(map,text="Generate",command=lambda:generate(avoidChoice,optimizeChoice,layerchoice,username,user))

    
    header.pack(pady=10)

    userLabel.pack()
    user.pack()

    avoidLabel.pack()
    avoidChoice.pack()

    optimizeLabel.pack()
    optimizeChoice.pack()

    layerLabel.pack()
    layerchoice.pack()

    execute.pack(pady=10)

    map.mainloop()





def viewAvailable(username):
    refwin = ctk.CTkToplevel()
    refwin.title("Available Donations")
    refwin.geometry("1500x300")

    with open(AVAILABLE_FILE, mode='r') as donations_file:
        reader = csv.reader(donations_file)
        
        column_name = ("0","1","2","3","4","5","6","7","8","9")
        treeview_vehicles = ttk.Treeview(refwin,columns=column_name)
        treeview_vehicles['show'] = 'headings'

        style = ttk.Style(treeview_vehicles) 
        style.theme_use("clam") 
        style.configure("Treeview", background="black", 
                        fieldbackground="black", foreground="white",font=('Calibri', 13))
        style.configure('Treeview.Heading', background="PowderBlue",font=('Calibri', 13,'bold'))

        treeview_vehicles.column("0",width=80,anchor="center")
        treeview_vehicles.heading("0",text="Donation ID")

        treeview_vehicles.column("1",anchor="center")
        treeview_vehicles.heading("1",text="Name")

        treeview_vehicles.column("2",anchor="center")
        treeview_vehicles.heading("2",text="Username")

        treeview_vehicles.column("3",anchor="center")
        treeview_vehicles.heading("3",text="Item")

        treeview_vehicles.column("4",anchor="center")
        treeview_vehicles.heading("4",text="Quantity")

        treeview_vehicles.column("5",anchor="center")
        treeview_vehicles.heading("5",text="Category")

        treeview_vehicles.column("6",anchor="center")
        treeview_vehicles.heading("6",text="Shelf Life")

        treeview_vehicles.column("7",anchor="center")
        treeview_vehicles.heading("7",text="MD")

        treeview_vehicles.column("8",anchor="center")
        treeview_vehicles.heading("8",text="Best Before")

        treeview_vehicles.column("9",anchor="center")
        treeview_vehicles.heading("9",text="Donation Date")


        treeview_vehicles.pack(fill=Tk.BOTH, expand=True)

        for row in reader:
            if row[0]=="Donation ID":
                continue
            else:
                treeview_vehicles.insert("",Tk.END,values=row)
    refwin.mainloop()

def pastOrders(username):
    refwin = ctk.CTkToplevel()
    refwin.title("Order History")
    refwin.geometry("1500x300")

    with open(PAST_ORDERS, mode='r') as donations_file:
            reader = csv.reader(donations_file)
            
            column_name = ("0","1","2","3","4","5","6","7","8")
            treeview_vehicles = ttk.Treeview(refwin,columns=column_name)
            treeview_vehicles['show'] = 'headings'
            
            style = ttk.Style(treeview_vehicles) 
            style.theme_use("clam") 
            style.configure("Treeview", background="black", 
                            fieldbackground="black", foreground="white",font=('Calibri', 13))
            style.configure('Treeview.Heading', background="PowderBlue",font=('Calibri', 13,'bold'))

            treeview_vehicles.column("0",anchor="center")
            treeview_vehicles.heading("0",text="Name")

            treeview_vehicles.column("1",anchor="center")
            treeview_vehicles.heading("1",text="Username")

            treeview_vehicles.column("2",anchor="center")
            treeview_vehicles.heading("2",text="Item")

            treeview_vehicles.column("3",anchor="center")
            treeview_vehicles.heading("3",text="Quantity")

            treeview_vehicles.column("4",anchor="center")
            treeview_vehicles.heading("4",text="Category")

            treeview_vehicles.column("5",anchor="center")
            treeview_vehicles.heading("5",text="Shelf Life")

            treeview_vehicles.column("6",anchor="center")
            treeview_vehicles.heading("6",text="MD")

            treeview_vehicles.column("7",anchor="center")
            treeview_vehicles.heading("7",text="Best Before")

            treeview_vehicles.column("8",anchor="center")
            treeview_vehicles.heading("8",text="Donation Date")

            treeview_vehicles.pack(fill=Tk.BOTH, expand=True)

            for row in reader:
                treeview_vehicles.insert("",Tk.END,values=row)
    refwin.mainloop()

def send_request_email(recipient_email, organization_name,individual_name):
    smtp_server = 'smtp.gmail.com'  
    smtp_port = 587 


    email_address = 'ibrecipeapp@gmail.com'
    email_password = app_password

    
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = 'Donation Request from an Organization'


    message = f"Dear {individual_name},\n\nAn organization named '{organization_name}' has requested a donation from you. " \
              f"Please expect their arrival in a short span of time\n\n" \
              f"Thank you for your support!\n\nBest regards,\nAnnadanam Donation App"


    msg.attach(MIMEText(message, 'plain'))

    try:
       
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, email_password)

       
        server.sendmail(email_address, recipient_email, msg.as_string())

      
        server.quit()

    except Exception as e:
        print("An error occurred while sending the email:", str(e))

def request(org,name,username):
        req = ctk.CTk()
        req.geometry("300x300")
        req.title("Requests")
        req.resizable(False,False)
        
        top = ctk.CTkLabel(req,text="Select an Option",font=("Poplar Std",25))
        ord = ctk.CTkButton(req,text="View All Donations",command=lambda:viewAvailable(username),height=40,width=100,corner_radius=6)
        dons = ctk.CTkLabel(req,text="Enter Donation ID(s)?",font=("Poplar Std",15))
        field = ctk.CTkEntry(req)

        
        def requesting(name,username,field):
            donation_id = []
            id = field.get()
            donation_id.append(id)

            available_file = open(AVAILABLE_FILE,'r')
            request_file = open('BRS_hack\Request.txt', 'w')
            data = csv.DictReader(available_file)

            for i in range(len(donation_id)):
                for row in data:
                    if donation_id[i] == row['Donation ID']:
                        request_file.write(f'{name} has requested to accept your donation of ID '+row['Donation ID'])

                        fpastorders = open('BRS_hack\past_orders.csv', 'a', newline='',encoding="utf-8-sig")
                        fpastorders_write = csv.DictWriter(fpastorders, fieldnames=['Name', 'Username', 'Item', 'Quantity', 'Category', 'Shelf Life', 'MD', 'Best Before', 'Donation Date', 'Account Type'])
          

                        item = row['Item']
                        quantity =row['Quantity']
                        cat = row['Category']
                        manu = row['MD']
                        shelf = row['Shelf Life']
                        best = row['Best Before']
                        date = row['Donation Date']
                        type = row['Account Type']

                        rec = {'Name': name,
                        'Username': username,
                        'Item': item,
                        'Quantity': quantity,
                        'Category': cat,
                        'Shelf Life': shelf,
                        'MD': manu,
                        'Best Before':best,
                        'Donation Date': date,
                        'Account Type': type}
                               
                        fpastorders_write.writerow(rec)  


                        df = pd.read_csv(DONATIONS_FILE)
                        df = df.drop(df[(df['Donation ID'] == f'{donation_id[i]}')].index)
                        df.to_csv(DONATIONS_FILE,index=False)

                        df = pd.read_csv(AVAILABLE_FILE)
                        df = df.drop(df[(df['Donation ID'] == f'{donation_id[i]}')].index)
                        df.to_csv(AVAILABLE_FILE,index=False)


                        with open(USERS_FILE, mode='r') as users_file:
                            reader = csv.DictReader(users_file)
                            for b in reader:
                                if row['Name']==b['name']:
                                    recipient_email = b['email']
                                    individual_name = b['name']
                                    send_request_email(recipient_email, name,individual_name) 

                

            request_file.close()
            fpastorders.close()
            request_file.close()
            available_file.close()
            
        ex = ctk.CTkButton(req,text="Proceed",command=lambda:requesting(name,username,field),height=40,width=100,corner_radius=6)

        top.pack()
        ord.pack()
        dons.pack(pady=10)
        field.pack(pady=10)
        ex.pack(pady=10)
        req.mainloop()

def logged_out2(org):
        org.destroy()

def organization(name,username):
    org = ctk.CTk()
    org.title("Receiver Menu")
    org.geometry("300x350")
    org.resizable(False,False)

    head = ctk.CTkLabel(org,font=("Poplar Std",25),text="Main Menu")
    order = ctk.CTkButton(org,text="Request Orders",command=lambda:request(org,name,username),height=40,width=100,corner_radius=6)
    pastOrder = ctk.CTkButton(org,text="View Past Orders",command=lambda:pastOrders(username),height=40,width=100,corner_radius=6)
    map = ctk.CTkButton(org,text="Generate Map",command=lambda:generate_map(name,username),height=40,width=100,corner_radius=6)
    logout = ctk.CTkButton(org,text="Logout",command=lambda:logged_out2(org),height=40,width=100,corner_radius=6)

    head.pack()
    order.pack(pady=20)
    pastOrder.pack(pady=20)
    map.pack(pady=20)
    logout.pack(pady=20)

    org.mainloop()



def enter():
    login = ctk.CTk()
    login.title("Login Window")
    login.geometry("500x500")
    login.resizable(False,False)
  
    def logging():
        Name = field1.get()
        username = field2.get()
        password = field3.get()
        if Name and username and password:
            with open(USERS_FILE, mode='r') as users_file:
                reader = csv.DictReader(users_file)
                for row in reader:
                    acc_type = row["account_type"]
                    if row['name'] == Name and row['username'] == username and row['password'] == password:
                        status.configure(text="User ID & password approved!")
                        status.after(2000,login.destroy)
                        if acc_type=="Donater":
                            individual(Name,username)
                        else:
                            organization(Name,username)
                        
                    else:
                        status.configure(text="Invalid username or password!")
                       


    title = ctk.CTkLabel(login,font=("Poplar Std",25),text="Please enter your credentials!")
    name = ctk.CTkLabel(login,font=("Poplar Std",20),text="Name:")
    user = ctk.CTkLabel(login,font=("Poplar Std",20),text="User Name:")
    passw = ctk.CTkLabel(login,font=("Poplar Std",20),text="Password:")

    field1 = ctk.CTkEntry(login)
    field2 = ctk.CTkEntry(login)
    field3 = ctk.CTkEntry(login,show="*")
    log = ctk.CTkButton(login,text="Login",command=logging,height=40,width=100,corner_radius=6)

    status = ctk.CTkLabel(login,text="",font=("Poplar Std",15))
    title.pack()
    name.place(x=120,y=150)
    user.place(x=120,y=200)
    passw.place(x=120,y=250)
    field1.place(x=250,y=150)
    field2.place(x=250,y=200)
    field3.place(x=250,y=250)
    log.place(x=200,y=320)
    status.place(x=150,y=380)
    login.mainloop()

def create():
    create = ctk.CTk()
    create.title("Login Window")
    create.geometry("500x550")
    create.resizable(False,False)

    
    title = ctk.CTkLabel(create,font=("Poplar Std",25),text="Please enter your credentials!")
    name = ctk.CTkLabel(create,font=("Poplar Std",20),text="Name:")
    user = ctk.CTkLabel(create,font=("Poplar Std",20),text="User Name:")
    passw = ctk.CTkLabel(create,font=("Poplar Std",20),text="Password:")
    email = ctk.CTkLabel(create,font=("Poplar Std",20),text="Email:")
    type = ctk.CTkLabel(create,font=("Poplar Std",20),text="Account Type:")
    n=ctk.StringVar()
    typeChosen = ctk.CTkComboBox(create,values=["Donater","Receiver"],variable=n)

    lat = ctk.CTkLabel(create,font=("Poplar Std",20),text="Latitude:")
    lon = ctk.CTkLabel(create,font=("Poplar Std",20),text="Longitude:")
  
    field1 = ctk.CTkEntry(create)
    field2 = ctk.CTkEntry(create)
    field3 = ctk.CTkEntry(create,show="*")
    field4 = ctk.CTkEntry(create)
    field5 = ctk.CTkEntry(create)
    field6 = ctk.CTkEntry(create)
    
    def verify():
        verify = ctk.CTkToplevel()
        verify.title("Verification Window")
        verify.resizable(False,False)
        def generate_random_code():
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        confirmation_code = generate_random_code()

        codeLabel = ctk.CTkLabel(verify,font=("Poplar Std",20),text="Verification Code")
        code = ctk.CTkEntry(verify)
        
        
        def check():
        
            enteredCode = code.get()
            Name = field1.get()
            username = field2.get()
            password = field3.get()
            Email = field4.get()
            Type = typeChosen.get()
            latitude = field5.get()
            longitude = field6.get()
            
            new_user = {
            'name': Name,
            'username': username,
            'password': password,
            'email': Email,
            'account_type': Type,
            'confirmation_code': confirmation_code,
            'is_confirmed': "True",
            'latitude': latitude,
            'longitude':longitude}

            loca = {
                "Name":Name,
                "Username":username,
                "Latitude":latitude,
                "Longitude":longitude
            }

            if enteredCode==confirmation_code:
                with open(USERS_FILE, mode='a', newline='') as users_file:
                    writer = csv.DictWriter(users_file, fieldnames=new_user.keys())
                    writer.writerow(new_user)
            
                with open(r"BRS_hack\user_locations.csv", mode='a', newline='') as loco_file:
                    writer = csv.DictWriter(loco_file, fieldnames=["Name","Username","Latitude","Longitude"])
                    writer.writerow(loca)

                status.configure(text="Account Created Successfully!")
                status.after(5000,create.destroy)
                status.after(5000,verify.destroy)
            else:
                status.configure(text=" Invalid  Confirmation  Code!")

       
        verBut = ctk.CTkButton(verify,text="Verify",command=check,height=30,width=130,corner_radius=6)
        app_password = "suns enhv fupf vvot"
        
    
        Name = field1.get()
        username = field2.get()
        password = field3.get()
        Email = field4.get()
        Type = typeChosen.get()
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        email_address = 'ibrecipeapp@gmail.com'
        email_password = app_password

        email_server = smtplib.SMTP(smtp_server, smtp_port)
        email_server.starttls()

        email_server.login(email_address, email_password)

        subject = "Email Confirmation for Annadanam Donation App"
        message = f"Dear {Name},\n\nThank you for registering with Annadanam Donation App. To ensure the security of your account and complete the registration process, we require you to verify your email address.\n\nPlease find your unique verification code and username below:\n\nUsername: {username}\nVerification Code: {confirmation_code}\n\n-Bot Nexus"

        email_message = f'Subject: {subject}\n\n{message}'

        email_server.sendmail(email_address, Email, email_message)
        email_server.quit()

        new_user = {
        'name': Name,
        'username': username,
        'password': password,
        'email': Email,
        'account_type': Type,
        'confirmation_code': confirmation_code,
        'is_confirmed': "False",
        'achievements': ""}

        codeLabel.pack()
        code.pack()
        verBut.pack()
        verify.mainloop()


    cre = ctk.CTkButton(create,text="Create",command=verify,height=40,width=100,corner_radius=6)

    status = ctk.CTkLabel(create,text="",font=("Poplar Std",15))
    title.pack()
    name.place(x=120,y=100)
    user.place(x=120,y=150)
    passw.place(x=120,y=200)
    email.place(x=120,y=250)
    type.place(x=120,y=300)
    lat.place(x=120,y=350)
    lon.place(x=120,y=400)

    field1.place(x=250,y=100)
    field2.place(x=250,y=150)
    field3.place(x=250,y=200)
    field4.place(x=250,y=250)
    field5.place(x=250,y=350)
    field6.place(x=250,y=400)

    cre.place(x=200,y=450)
    typeChosen.place(x=250,y=300)
   
    status.place(x=150,y=490)
    create.mainloop()
    
def deleting(field1,field2,delabel):
        username = field1.get()
        password = field2.get() 
        with open(USERS_FILE, mode='r') as users_file:
                reader = csv.DictReader(users_file)
                for row in reader:
                    if row['username'] == username and row['password'] == password:
                        df = pd.read_csv(USERS_FILE)
                        df = df.drop(df[(df['username'] == f'{username}')].index)
                        df.to_csv(USERS_FILE,index=False)
                        delabel.configure(text="Successfully Deleted")
                    
def deleteAccount():
    delwin = ctk.CTkToplevel()
    delwin.geometry("300x300")

    user = ctk.CTkLabel(delwin,font=("Poplar Std",18),text="User Name:")
    passw = ctk.CTkLabel(delwin,font=("Poplar Std",18),text="Password:")
    delabel = ctk.CTkLabel(delwin,text="")

    field1 = ctk.CTkEntry(delwin)
    field2 = ctk.CTkEntry(delwin,show="*")


    
    delbut = ctk.CTkButton(delwin,text="Delete",height=40,width=100,corner_radius=6,command=lambda:deleting(field1,field2,delabel))

    user.place(x=30,y=100)
    passw.place(x=30,y=150)
    field1.place(x=135,y=100)
    field2.place(x=135,y=150)
    delbut.place(x=100,y=200)
    delabel.place(x=100,y=250)
    delwin.mainloop()
    

title = ctk.CTkLabel(welwin,font=("Poplar Std",22),text="Welcome to Project Annadanam!")
enter = ctk.CTkButton(welwin,text="Login",command=enter,height=50,width=120,corner_radius=6)
create = ctk.CTkButton(welwin,text="Create Account",command=create,height=50,width=120,corner_radius=6)
delete = ctk.CTkButton(welwin,height=50,width=120,corner_radius=6,text="Delete Account",command=deleteAccount)
text = ctk.CTkLabel(welwin,text="'Its not how much we give but how much love we put into giving'",font=("Poplar Std",12,"bold"))

title.pack(pady=10)
enter.pack(pady=20)
create.pack(pady=20)
delete.pack(pady=20)
text.pack(pady=10)
welwin.mainloop()