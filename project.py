import PySimpleGUI as sg
import tkinter
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import time
import re
from matplotlib import pyplot as p
import datetime as DT 
jk=0
exits=0

try:
    import mysql.connector
except:
    sg.Popup("please install mysql")


try:
    root = Tk()
    root.title(" shopping page ")
    root.geometry('1550x1000')
    
    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    def EXIT():
        exit()
    
    def go():
            u1 = simpledialog.askstring("user name", "Enter The Name of Database")
            p1 = simpledialog.askstring("user password", "Enter The Password of Database")
            if(u1=='' and p1==''):
                sg.Popup("entered data is not correct")
                exit()
            if(u1=='' or p1==''):
                sg.Popup("entered data is not correct")
                
            u1=str(u1)
            p1=str(p1)
            a = mysql.connector.connect(host="localhost", user=u1, password=p1)
            b = a.cursor()   
        
            try:
                b.execute("create database checking")
                a.commit()
                b.execute("use checking")
            except mysql.connector.errors.DatabaseError:
                    b.execute("use checking")
                    
            try:
                    b.execute("create table stem(product_id int,product_name char(20),product_company varchar(20),stock int, selling_price int,cost_price int)")
                    ab=("insert into stem(product_id,product_name,product_company,stock,cost_price) values(%s,%s,%s,%s,%s)")
                    ba=[(101,"t.v","samsung",1000,30000),(102,"mobile","samsung",1000,10000),(103,"laptop 4gb ","HP",1000,45000),(104,"laptop 8gb","dell",1000,60000),(105,"mobile","oppo",1000,18000),]
                    b.executemany(ab,ba)
                    a.commit()
                    ab=("insert into stem(product_id,product_name,product_company,stock,cost_price) values(%s,%s,%s,%s,%s)")
                    ba=[(106,"t.v","samsung",1000,30000),(107,"mobile","vivo y1s",1000,7990),(108,"laptop 4gb ","asus",1000,55000),(109,"laptop 8gb","apple",1000,60000),(110,"mobile","oppo f9",1000,18000)]
                    b.executemany(ab,ba)
                    ab=("insert into stem(product_id,product_name,product_company,stock,cost_price) values(%s,%s,%s,%s,%s)")
                    ba=[(111,"mobile","vivo v20 SE",1000,19990),(112,"mobile","vivo y20i",1000,11490),(113,"mobile","vivo X50",1000,33990),(114,"mobile","oppo A15",1000,9497),(115,"mobile","oppo A33",1000,10990),(116,"mobile","oppo find X2",1000,64990),(117,"mobile","oppo Reno 4 pro",1000,34709),(118,"mobile","oppo A31",1000,11000),(119,"mobile","oppo Reno 3 pro",1000,24000),(120,"mobile","vivo v20 SE",1000,19990),(121,"mobile","vivo y20i",1000,11490),(122,"mobile","vivo S5",1000,26700),]
                    b.executemany(ab,ba)
            except mysql.connector.errors.ProgrammingError:
                        pass 

            try:
                        b.execute("CREATE TABLE carts (id int,p_name varchar(255),p_sp int,quantity int ,total int ,c_name varchar(20))")
                        a.commit()
            except mysql.connector.errors.ProgrammingError:
                        pass

            

            try:
                        b.execute("CREATE TABLE datas (bill_id int(22) NOT NULL auto_increment PRIMARY KEY, c_name varchar(255), total int)")
                        a.commit()
            except mysql.connector.errors.ProgrammingError:
                        pass

            b.execute("update stem set selling_price=cost_price+cost_price*0.05 where selling_price is NULL")
            a.commit()
            #-----------------------------------------------------------------------------------------------------------
            
            def signup():
                window22_active =False
                window51_active =True
                wel=[
                    [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",40) , background_color='#7095db')]
                    ]
                frame=[[sg.Frame("",layout=wel)]]
                    
                layout2=[
                    [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                    [sg.Text("ENTER THE VALUES  ", justification='center',size=(180,2), font=("Arial",20))],
                    [ sg.Text("ENTER USER NAME  \t\t: "),sg.Input(key = "u_name", justification='center',size=(50,1),font=("Arial",15)) ],
                    [ sg.Text("CREATE USER ID  \t\t: "),sg.Input(key = "u_id", justification='center',size=(50,1),font=("Arial",15)) ],
                    [ sg.Text("CREATE THE PASSWORD \t \t: "),sg.Input(key = "u_pass", justification='center',size=(50,1),font=("Arial",15)) ],
                    [ sg.Text("ENTER THE MOBILE NO. \t \t: "),sg.Input(key = "u_mob", justification='center',size=(50,1),font=("Arial",15)) ],
                    [ sg.Text("ENTER THE ADDRESS  \t\t : "),sg.Input(key = "u_add", justification='center',size=(50,1),font=("Arial",15)) ],
                    [ sg.Text("ENTER THE E-MAIL ID\t\t : "),sg.Input(key = "u_email", justification='center',size=(50,1),font=("Arial",15)) ],
                    [sg.Button("SAVE",size=(20,1),font=("Arial",10)),sg.Button("exit",size=(20,1),font=("Arial",10))]
                    ]
                window51 = sg.Window('login', layout2,  location=(0,0),  size=(1550,800) ).finalize()
                window51.Maximize()
                rea=0
                while True:
                    u_n=0
                    j_k=1
                    event,values=window51.read()
                    if(event=="SAVE"):
                        u_name=values["u_name"]
                        u_id=values["u_id"]
                        u_pass=values["u_pass"]
                        u_mob=values["u_mob"]
                        u_add=values["u_add"]
                        u_email=values["u_email"]
                        with open("login.txt", "r") as f:
                            for i in f:
                                u , p = i.split(",")
                                p = p.strip()
                                if(u==u_name):
                                    j_k=0
                                    sg.Popup("user name already used \n create new user name")
                                    window51['u_name']("")
                                    window51['u_pass']("")
                                    window51['u_mob']("")
                                    window51['u_add']("")
                                    window51['u_email']("")
                                    window51['u_id']("")
                                    
                                regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
                                if(re.search(regex, u_email)):
                                    rea=1
                                else:
                                    u_n=1
                                       
                        if(u_name=="" or u_pass=="" or u_mob=="" or u_add=="" or u_email=="" ): 
                            sg.Popup("Incomplete Information")
                        
                        else:
                            if(j_k==0):
                                sg.Popup("entered data is not proper")
                                
                            elif(u_mob.isnumeric() and len(u_mob)==10 and rea==1 and u_n==0):
                                f = open("user_detail.txt", "a")
                                f.writelines(["\n", u_name, ",", u_pass,",",u_mob,",",u_add,",",u_email])
                                f.close()
                                f = open("login.txt", "a")
                                f.writelines(["\n", u_id, ",", u_pass])
                                f.close()
                                window51['u_name']("")
                                window51['u_pass']("")
                                window51['u_mob']("")
                                window51['u_add']("")
                                window51['u_email']("")
                                window51['u_id']("")
                                sg.Popup("complete")
                                sg.Popup("now login with your User ID and Password")
                    if(event=="exit"):
                        window51_active =False
                        window51.close()
                        window22_active =True
                        window22.UnHide()
                        break
            #______________________________________________________function _________________________________________________________________
                          
            
                                              
            #-------------------------------------------------------------admin display----------------------------------------------------------------

            def a_display():
                display=[
                        [sg.Text("press DISPLAY button to see all product " , font=("Arial",20)) ],
                        [sg.Button("DISPLAY",font=("Arial",15))],
                        [sg.MLine(size=(80, 40), key='l'+sg.WRITE_ONLY_KEY,font='Arial 12')],     
                        ]
                searches=[   
                                        [sg.Text("Enter The Code Of Product " , font=("Arial",20)) ],
                                        [sg.Input(key="code",font=("Arial",15))],
                                        [sg.Text("Enter The Quantity Of Product " , font=("Arial",20)) ],
                                        [sg.Input(key="quantity",font=("Arial",15))],
                                        [sg.Button("UPDATE",font=("Arial",15))]
                                    ]
                                    
                wel=[
                    [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",30) , background_color='#7095db')]
                    ]
                frame=[[sg.Frame("",layout=wel)]]
                frame1=[[sg.Frame("DISPLAY SCREEN",layout=display)]]
                frame2=[[sg.Frame("UPDATE",layout=searches)]]
                layout=[
                       [sg.Text("",size=(180,1)),sg.Button("EXIT",font=("Arial",15))],
                       [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                       [sg.Text("")  ],
                       [sg.Column(frame1),sg.Column(frame2)]
                       ]

                window3=sg.Window("SEARCH",layout).finalize()
                window3.Maximize()
                while True:
                    event,values=window3.read()
                    p_list=['Product Id : ',' Product Name : ' , 'Product company : ' , 'Stock Available : ' ,  'selling Price : ' , 'cost price : ' ]
                    b.execute("use checking")
                    b.execute("select * from stem")
                    k=b.fetchall()
                    lk =  [list(i) for i in k]
                    a.commit()
                    zx=0
                    if(event=="DISPLAY"):
                        if(zx==0):
                            window3['l'+sg.WRITE_ONLY_KEY]("")
                        for i in lk:
                            for j in range(len(i)) :
                                
                                window3['l'+sg.WRITE_ONLY_KEY].print(p_list[j],i[j],end='', text_color='#DB2777')
                                window3['l'+sg.WRITE_ONLY_KEY].print()
                            window3['l'+sg.WRITE_ONLY_KEY].print()
                    
                    if(event=="UPDATE"):
                        
                        codes=values["code"]
                        quantitys=values["quantity"]
                        ans=sg.popup_yes_no("do you want to update product quantity")
                        if(ans=="Yes"):
                            if(codes==''):
                                sg.popup("you have not entered code ")
                                window3['code']("")
                                window3['quantity']("") 
                            elif(quantitys==''):
                                sg.popup("you have not entered quantity ")
                                window3['code']("")
                                window3['quantity']("") 
                            else:
                                v1 = ("update stem set stock=stock+ %s where product_id= %s")
                                v2 = (int(quantitys), codes)
                                b.execute(v1, v2,)
                                a.commit()
                                sg.popup("updation complete")
                                window3['code']("")
                                window3['quantity']("") 
                        else:
                            sg.popup_cancel('not update ')
              
              
                    if(event=="EXIT"):
                        window3_active =False
                        window3.close()
                        window21_active =True
                        window21.UnHide()
                        break
                
            #--------------------------------------------------------------------------------------------------------------------------------
             
            #--------------------------------------------------------------------------------------------------------------------------------
            def add_product():
                window21.Hide()
                window5_active =True
                wel=[
                    [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",40) , background_color='#7095db')]
                    ]
                frame=[[sg.Frame("",layout=wel)]]
                frame2=[
                        [sg.Text("ENTER THE VALUES  ", justification='center',size=(180,2), font=("Arial",20))],
                        [ sg.Text("ENTER THE PRODUCT ID\t\t\t: "),sg.Input(key = "p_id", justification='center',size=(50,1),font=("Arial",15)) ],
                        [ sg.Text("ENTER THE PRODUCT NAME\t\t: "),sg.Input(key = "p_name", justification='center',size=(50,1),font=("Arial",15)) ],
                        [ sg.Text("ENTER THE PRODUCT COMPANY\t\t: "),sg.Input(key = "p_company", justification='center',size=(50,1),font=("Arial",15)) ],
                        [ sg.Text("ENTER THE STOCK \t \t \t: "),sg.Input(key = "p_stock", justification='center',size=(50,1),font=("Arial",15)) ],
                        [ sg.Text("ENTER THE COST PRICE\t  \t \t: "),sg.Input(key = "p_cp", justification='center',size=(50,1),font=("Arial",15)) ],
                        [sg.Text("",size=(20,1)),sg.Button("SAVE",size=(20,1),font=("Arial",10))]
                        ]
                frames=[[sg.Frame("",layout=frame2)]]
                layout2=[
                        [ sg.Text("",size=(180,1)),sg.Button("EXIT",font=("Arial",12)) ],
                        [ sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                        [sg.Column(frames)]
                        ]
                window5 = sg.Window('login', layout2,  location=(0,0),  size=(1550,800) ).finalize()
                window5.Maximize()
                while True:
                    event,values=window5.read()
                    p_id=values["p_id"]
                    p_name=values["p_name"]
                    p_company=values["p_company"]
                    p_stock=values["p_stock"]
                    p_cp=values["p_cp"]
                    if(event=="SAVE"):
                        p_id=values["p_id"]
                        p_name=values["p_name"]
                        p_company=values["p_company"]
                        p_stock=values["p_stock"]
                        p_cp=values["p_cp"]
                        if(p_id=='' and p_name=='' and p_company=='' and p_stock=='' and p_cp==''):
                            sg.Popup("you have not enter product detail")
                            window5['p_id']("")
                            window5['p_name']("")
                            window5['p_company']("")
                            window5['p_stock']("")
                            window5['p_cp']("")
                        elif(p_id=='' or p_name=='' or p_company=='' or p_stock=='' or p_cp==''):
                            sg.Popup("missing something")
                            window5['p_id']("")
                            window5['p_name']("")
                            window5['p_company']("")
                            window5['p_stock']("")
                            window5['p_cp']("")
                        
                        else:
                            n1 = "insert into stem(product_id,product_name,product_company,stock,cost_price) values(%s,%s,%s,%s,%s)"
                            n2 = (p_id, p_name,p_company,p_stock, p_cp)
                            b.execute(n1, n2,)
                            b.execute("update stem set selling_price=cost_price+cost_price*0.05 where selling_price is NULL")
                            a.commit()
                            sg.Popup("enter data had been updated")
                            window5['p_id']("")
                            window5['p_name']("")
                            window5['p_company']("")
                            window5['p_stock']("")
                            window5['p_cp']("")
                    if(event=='EXIT'):
                        window5_active =False
                        window5.close()
                        window21_active =True
                        window21.UnHide()
                        break
            #--------------------------------------------------------------------------------------------------------------------------------
            def add_admin():
                window21.Hide()
                window6_active =True
                wel=[
                    [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",40) , background_color='#7095db')]
                    ]
                frame=[[sg.Frame("",layout=wel)]]
                frame2= [
                        [ sg.Text("ENTER THE ADMIN ID\t\t\t: "),sg.Input(key = "ids", justification='center',size=(50,1),font=("Arial",15)) ],
                        [ sg.Text("ENTER THE PASSWORD\t\t\t: "),sg.Input(key = "passs", justification='center',size=(50,1),font=("Arial",15)) ],
                        [ sg.Text("ENTER THE SECURE QUESTION\t\t: "),sg.Input(key = "ques", justification='center',size=(50,1),font=("Arial",15)) ],
                        [ sg.Text("ENTER THE ANSWER OF QUESTION\t: "),sg.Input(key = "ans", justification='center',size=(50,1),font=("Arial",15)) ],
                        [sg.Text("",size=(20,1)),sg.Button("SAVE",size=(20,1),font=("Arial",10))]
                        ]
                frames=[[sg.Frame("",layout=frame2)]]
                layout2=[
                        [ sg.Text("",size=(180,1)),sg.Button("EXIT",font=("Arial",12)) ],
                        [ sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                        [sg.Column(frames)]
                        ]
                window6 = sg.Window('login', layout2,  location=(0,0),  size=(1550,800) ).finalize()
                window6.Maximize()
                while True:
                    event,values=window6.read()
                    ids=values["ids"]
                    passs=values["passs"]
                    ques=values["ques"]
                    ans=values["ans"]
                    if(event=="SAVE"):
                        if(ids=='' and passs=='' and ques=='' and ans==''):
                                 sg.Popup("you have enter nothing to save")
                        elif(ids=='' or  passs=='' or passs=='' or passs==''):
                                 sg.Popup("you have not enter either iadmin id or password to search")
                        else:
                                f = open("user.txt", "a")
                                f.writelines(["\n", ids, ",", passs])
                                f.close()
                                f = open("ques.txt", "a")
                                f.writelines(["\n", ids, ",", ques,",",ans])
                                f.close()
                                window6['ids']("")
                                window6['passs']("")
                                window6['ques']("")
                                window6['ans']("")
                                sg.Popup("enter DATA had been added ")
                    if(event=='EXIT'):
                            window6_active =False
                            window6.close()
                            window21_active =True
                            window21.UnHide()
                            break

            #-------------------------------------------------------------------------------------------------------------------------------
             
            
                        
            ch=0
            u_rep=0
            u_l=0
            ch=0
            ee=0
            res=0
            #--------------------------------------------------------------------------------------------------------------
            def sign_in():
                res=0
                a = mysql.connector.connect(host="localhost", user=u1, password=p1)
                b = a.cursor()
                b.execute("use checking")
                ch=0
                for i in range(0,5):
                    prompt10 = simpledialog.askstring("USER LOGIN", "Enter The Customer Full Name")
                    if not prompt10:
                        break
                    else:
                        prompt212 = simpledialog.askstring("USER LOGIN", "Enter The Password" ,show='*')
                        if not prompt212:
                            break
                        else:
                            u_l=1
                            ch=ch+1
                            with open("login.txt", "r") as f:
                                for i in f:
                                    u , p = i.split(",")
                                    p = p.strip()
                                    if(prompt10 == u and prompt212 == p):
                                        res=1
                                        break
                                                                            
                            if(res==1):
                                prompt10=str(prompt10)
                                cn=" select c_name from datas where c_name= %s " 
                                nc=(prompt10,)
                                b.execute(cn,nc,)
                                kn=b.fetchall()
                                if(kn==[]):
                                    aa="insert into datas( c_name ) values(%s)"
                                    bb=(prompt10,)
                                    b.execute(aa,bb,)
                                    
                                else:
                                    window2_active =True
                                    window22.Hide()
                                    wel=[
                                    [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",40) , background_color='#7095db')]
                                    ]
                                    frame=[[sg.Frame("",layout=wel)]]
                                    layout2=[
                                    [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                                    [sg.Text("Select Any Button To Move Ahead ", justification='center',size=(180,2), font=("Arial",20))],
                                    [sg.Button("SEARCH AND BUY",size=(180,2),font=("Arial",15))],
                                    [sg.Button("CART AND RETURN",size=(180,2),font=("Arial",15))],
                                    [sg.Button("BUY AND BILLING",size=(180,2),font=("Arial",15))],
                                    [sg.Button("RETURN AND REFUND",size=(180,2),font=("Arial",15))],
                                    [sg.Button("LOGOUT",size=(180,2),font=("Arial",15))],
                                    ]
                                    window2 = sg.Window('login', layout2,  location=(0,0),  size=(1550,800) ).finalize()
                                    window2.Maximize()
                                    window4_active =False
                                    window3_active =False
                                    window31_active =False
                                    while True:
                                        event,values=window2.read()
                                                                #------------------------------------------- USER BUY AND SEARCH --------------------------------------------------------
                                        if(event=="SEARCH AND BUY"):
                                            window2.Hide()
                                            prompt10=str(prompt10)
                                            window4_active =True
                
                                            search=[
                                                    [sg.Text("Enter The search item " , font=("Arial",20)) ],
                                                    [sg.Input(key="search",font=("Arial",15)),sg.Button("SEARCH",font=("Arial",10)),sg.Button("CLEAR",font=("Arial",10))],
                                                    [sg.MLine(size=(100, 40), key='l'+sg.WRITE_ONLY_KEY,font='Arial 12')],     
                                                    ]
                                            search2=[   
                                                    [sg.Text("Enter The Code Of Product " , font=("Arial",20)) ],
                                                    [sg.Input(key="code",font=("Arial",15))],
                                                    [sg.Text("Enter The Quantity Of Product " , font=("Arial",20)) ],
                                                    [sg.Input(key="quantity",font=("Arial",15))],
                                                    [sg.Button("ADD TO CARTS",font=("Arial",15))]
                                                    ]
                                            wel=[
                                                [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",40) , background_color='#7095db')]
                                                ]
                                            frame=[[sg.Frame("",layout=wel)]]
                                            frame1=[[sg.Frame("SEARCH",layout=search)]]
                                            frame2=[[sg.Frame("BUY",layout=search2)]]
                                            layout= [
                                                    [sg.Text("",size=(180,1)),sg.Button("EXIT",font=("Arial",15))],
                                                    [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                                                    [sg.Text("")  ],
                                                    [sg.Column(frame1),sg.Column(frame2)]
                                                    ]
                                            window4=sg.Window("SEARCH AND BUY",layout).finalize()
                                            window4.Maximize()
                                            while True:
                                                event,values=window4.read()
                                                p_list=['Product Id : ',' Product Name : ' , 'Product company : ' , 'Stock Available : ' ,  'selling Price : ' ]
                                                b.execute("select product_id,product_name,product_company,stock,selling_price from stem")
                                                k=b.fetchall()
                                                lk =  [list(i) for i in k]
                                                search=values["search"]
                                                if(event=="SEARCH"):
                                                    if(search == ""):
                                                        window4['search']('')
                                                        sg.Popup("you have enter nothing to search")
                                                    else:
                                                        for i in lk:
                                                            xy=0
                                                            if(i==''):
                                                                                sg.Popup("no match")
                                                            else:
                                                                                for j in range(len(i)) :
                                                                                    if(i[1]==search):
                                                                                        window4['l'+sg.WRITE_ONLY_KEY].print(p_list[j],i[j],end='', text_color='red')
                                                                                        window4['l'+sg.WRITE_ONLY_KEY].print()
                                                                                        xy=1
                                                                                if(xy>=1):
                                                                                    window4['l'+sg.WRITE_ONLY_KEY].print()
                                                if(event=="CLEAR"):
                                                    if(search == ''):
                                                        sg.Popup("nothing to clear")
                                                    else:
                                                        window4['search']('')
                                                        window4['l'+sg.WRITE_ONLY_KEY]('')
                                                if(event=="ADD TO CARTS"):
                                                    code=int(values["code"])
                                                    quantity=values["quantity"]
                                                    if(code=="" and quantity==""):
                                                        window4['code']("")
                                                        window4['quantity']("")
                                                        sg.Popup("you have not enter any value , please enter the value")
                                                    elif(code=="" ):
                                                        window4['code']("")
                                                        window4['quantity']("")
                                                        sg.Popup("you have not enter any code , please enter the code")
                                                    elif(quantity==""):
                                                        window4['code']("")
                                                        window4['quantity']("")
                                                        sg.Popup("you have not enter any quantity , please enter the quantity")
                                                    else:
                                                        co=("select selling_price from stem where product_id = %s")
                                                        de=(code,)
                                                        b.execute(co,de,)
                                                        cd = list(b.fetchone())
                                                        cd1 = cd[0]
                                                        a1 = ("select * from stem where product_id = '%s' ")
                                                        a2 = (code)
                                                        b.execute(a1, a2,)
                                                        data = b.fetchone()
                                                        a.commit()
                                                        if(data == []):
                                                            window4['code']("")
                                                            window4['quantity']("")
                                                            sg.Popup("not any id match,try again")
                                                        else:
                                                            b1 = ("select * from carts where id= %s " )
                                                            b2 = (code,)
                                                            b.execute(b1, b2,)
                                                            res = b.fetchall()
                                                            if(res == []):
                                                                k1 = ("select stock from stem where product_id = %s ")
                                                                k2 = (code,)
                                                                b.execute(k1, k2)
                                                                total = b.fetchone()                                                    
                                                                for i in total:
                                                                    if(i < int(quantity)):
                                                                        window4['code']("")
                                                                        window4['quantity']("")
                                                                        sg.Popup("sorry ,we have less present")
                                                                    else:
                                                                        up = (" update stem set stock=stock - %s where stem.product_id = %s")
                                                                        dation = (quantity, code,)
                                                                        b.execute(up, dation)
                                                                        a.commit()
                                                                        sql = "insert into carts(id,quantity,c_name) values(%s,%s ,%s)"
                                                                        v = (code, quantity, prompt10,)
                                                                        b.execute(sql, v)
                                                                        a.commit()
                                                                        sql1 = "insert into Rcarts(id,quantity,c_name) values(%s ,%s,%s)"
                                                                        v1 = (code, quantity, prompt10)
                                                                        b.execute(sql1, v1)
                                                                        a.commit()
                                                                        sg.Popup("the quantity of the product you enter is added")
                                                                        asd = ("update carts set total= %s*%s where id= %s and c_name =%s ")
                                                                        bs = (cd1, int(quantity), code ,prompt10,)
                                                                        b.execute(asd, bs,)
                                                                        a.commit()
                                                                        asd1 = ("update Rcarts set total= %s*%s where id= %s and c_name =%s ")
                                                                        bs1 = (cd1, int(quantity), code ,prompt10,)
                                                                        b.execute(asd1, bs1,)
                                                                        a.commit()
                                                                        up = ("update carts ,stem set carts.p_name=stem.product_company,carts.p_sp=stem.selling_price where stem.product_id = carts.id and carts.c_name = %s " )
                                                                        date = ( prompt10,)
                                                                        b.execute(up , date,)
                                                                        a.commit()
                                                                        window4['code']("")
                                                                        window4['quantity']("")
                                                                        a.commit()
                                                            else:
                                                                b.execute("select stock from stem where product_id='%s'" % (code))
                                                                se = b.fetchone()
                                                                for i in se:
                                                                    if int(quantity) > i:
                                                                        sg.Popup("enter valid quantity we have less stock  ")
                                                                    else:
                                                                        a1 = (" update carts set quantity=quantity + %s where carts.id= %s  and carts.c_name=%s")
                                                                        a2 = (quantity , code , prompt10,)
                                                                        b.execute(a1,a2,)
                                                                        a.commit()
                                                                        up = (" update stem set stock=stock - %s where stem.product_id = %s")
                                                                        dation = (quantity, code,)
                                                                        b.execute(up, dation)
                                                                        a.commit()
                                                                        sel = cd1 * int(quantity)
                                                                        asds = ("update carts set total=total +%s where id= %s and c_name=%s ")
                                                                        bss = (sel, code ,prompt10,)
                                                                        b.execute(asds, bss,)
                                                                        a.commit()
                                                                        sql1 = "insert into Rcarts(id,quantity,c_name) values(%s ,%s,%s)"
                                                                        v1 = (code, quantity, prompt10)
                                                                        b.execute(sql1, v1)
                                                                        a.commit()
                                                                        asd1 = ("update Rcarts set total= %s*%s where id= %s and c_name =%s ")
                                                                        bs1 = (cd1, int(quantity), code ,prompt10,)
                                                                        b.execute(asd1, bs1,)
                                                                        a.commit()
                                                                        up = ("update carts ,stem set carts.p_name=stem.product_company,carts.p_sp=stem.selling_price where stem.product_id = carts.id and carts.c_name = %s " )
                                                                        date = ( prompt10,)
                                                                        b.execute(up , date,)
                                                                        a.commit()
                                                                        window4['code']("")
                                                                        window4['quantity']("")
                                                                        sg.Popup("your purched item updated ")
                                                                        a.commit()
                                                if(event=="EXIT"):
                                                    window4_active =False
                                                    window4.close()
                                                    window2_active =True
                                                    window2.UnHide()
                                                    break
                              
                                                                #------------------------------------- USER CARTS AND RETURN -----------------------------------------------------------
                                        elif(event=="CART AND RETURN"):
                                            window2.Hide()
                                            prompt10=str(prompt10)
                                            window3_active =True
                                            cart=[
                                                [sg.Text("press CART button to see all product " , font=("Arial",20)) ],
                                                [sg.Button("CART",font=("Arial",15)),sg.Button("CLEAR",font=("Arial",15))],
                                                [sg.MLine(size=(80, 40), key='l'+sg.WRITE_ONLY_KEY,font='Arial 15')],     
                                                ]
                                            returns=[   
                                                [sg.Text("Enter The Code Of Product " , font=("Arial",20)) ],
                                                [sg.Input(key="code",font=("Arial",15))],
                                                [sg.Button("RETURNS",font=("Arial",15))]
                                                ]
                                            wel=[
                                                [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",30) , background_color='#7095db')]
                                                ]
                                            frame=[[sg.Frame("",layout=wel)]]
                                            frame1=[[sg.Frame("CARTS",layout=cart)]]
                                            frame2=[[sg.Frame("RETURNS",layout=returns)]]
                                            layout=[
                                                [sg.Text("",size=(180,1)),sg.Button("EXIT",font=("Arial",15))],
                                                [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                                                [sg.Text("")  ],
                                                [sg.Column(frame1),sg.Column(frame2)]
                                                ]
                                            window3=sg.Window("CARTS AND RETURNS",layout).finalize()
                                            window3.Maximize()
                                            while True:
                                                event,values=window3.read()
                                                plist=['Product Id : ',' Product company : ' , 'Product selling price : ' , 'quantity  ' ,  'total : ' ]
                                                if(event=="CART"):
                                                    #up = ("update carts ,stem set carts.p_name=stem.product_company,carts.p_sp=stem.selling_price where stem.product_id = carts.id and carts.c_name = %s " )
                                                    #date = ( prompt10,)
                                                    #b.execute(up , date,)
                                                    sel=("select id , p_name , p_sp , quantity , total from carts where c_name = %s" )
                                                    ect=(prompt10,)
                                                    b.execute(sel,ect,)
                                                    k=b.fetchall()  
                                                    for i in k:
                                                        for j in range(len(i)):
                                                            window3['l'+sg.WRITE_ONLY_KEY].print(plist[j],i[j],end='', text_color='red')
                                                            window3['l'+sg.WRITE_ONLY_KEY].print()
                                                        window3['l'+sg.WRITE_ONLY_KEY].print()
                                                    a.commit()

                                                elif(event=="RETURNS"):
                                                    window3['code']("")
                                                    code=values["code"]
                                                    ans=sg.popup_yes_no("do you want to delete product ")
                                                    if(ans=="Yes"):
                                                        if(code==''):
                                                            sg.Popup("you have not enter the code")
                                                        else:
                                                            quan=("select quantity from carts where id = %s and c_name=%s " )
                                                            tity=(code , prompt10,)
                                                            b.execute(quan , tity ,)
                                                            k=b.fetchall()
                                                            x=k[0]
                                                            x=x[0]
                                                            up = (" update stem set stock=stock + %s where stem.product_id = %s")
                                                            dation = (x, code,)
                                                            b.execute(up, dation)
                                                            a.commit()
                                                            dele=("delete from carts where id = %s and c_name = %s " )
                                                            te=(code , prompt10,)
                                                            b.execute(dele , te,)
                                                            a.commit()
                                                            dele1=("delete from Rcarts where id = %s and c_name = %s " )
                                                            te1=(code , prompt10,)
                                                            b.execute(dele1 , te,)
                                                            a.commit()
                                                    else:
                                                        sg.popup_cancel('not delete ')
                                                elif(event=="CLEAR"):
                                                        window3['l'+sg.WRITE_ONLY_KEY]('')
                                                elif(event=="EXIT"):
                                                    window3_active =False
                                                    window3.close()
                                                    window2_active =True
                                                    window2.UnHide()
                                                    break

                                                                #-------------------------------------------BUY AND BILL-------------------------------------------------------------
                                        elif(event=="BUY AND BILLING"):
                                            window2.Hide()
                                            prompt10=str(prompt10)
                                            window4_active =True
                                            carts=[
                                                 [sg.Text("In carts " , font=("Arial",20)) ,sg.Button("PROCESSED",font=("Arial",15))],
                                                 [sg.MLine(size=(80, 40), key='l'+sg.WRITE_ONLY_KEY,font='Arial 15')],     
                                                 ]
                                            total=[   
                                                 [sg.Text("The customer name" , font=("Arial",20))  ],
                                                 [sg.Input(key="c_n",font=("Arial",15))],
                                                 [sg.Text("The bill id" , font=("Arial",20))  ],
                                                 [sg.Input(key="b_i_d",font=("Arial",15))],
                                                 [sg.Text("The Total Amount" , font=("Arial",20))  ],
                                                 [sg.Input(key="amt",font=("Arial",15))],
                                                 [sg.Button("PAY",font=("Arial",15))]
                                                 ]
                                            wel=[
                                                [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",30) , background_color='#7095db')]
                                                ]
                                            frame=[[sg.Frame("",layout=wel)]]
                                            frame1=[[sg.Frame("CARTS",layout=carts)]]
                                            frame2=[[sg.Frame("total",layout=total)]]
                                            layout=[
                                                 [sg.Text("",size=(180,1)),sg.Button("EXIT",font=("Arial",15))],
                                                 [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                                                 [sg.Text("")  ],
                                                 [sg.Column(frame1),sg.Column(frame2)]
                                                 ]

                                            window31=sg.Window("CARTS AND RETURNS",layout).finalize()
                                            window31.Maximize()
                                            while True:
                                                event,values=window31.read()
                                                plist=['Product Id : ',' Product company : ' , 'Product selling price : ' , 'quantity  ' ,  'total : ' ]
                                                sel=("select id , p_name , p_sp , quantity , total from carts where c_name = %s" )
                                                ect=(prompt10,)
                                                b.execute(sel,ect,)
                                                k=b.fetchall()
                                                b.execute("select bill_id from datas where c_name = '%s' " %(prompt10))
                                                kl=b.fetchall()
                                                if(event=="PROCESSED"):
                                                    ans=sg.popup_yes_no("do you want to buy product")
                                                    if(ans=="Yes"):
                                                        if(k==[]):
                                                            sg.popup("no product in carts")
                                                        else:
                                                            for i in k:
                                                                for j in range(len(i)):
                                                                    window31['l'+sg.WRITE_ONLY_KEY].print(plist[j],i[j],end='', text_color='red')
                                                                    window31['l'+sg.WRITE_ONLY_KEY].print()
                                                                window31['l'+sg.WRITE_ONLY_KEY].print()
                                                            n=0
                                                            for i in k:
                                                                i=i[4]
                                                                n=n+int(i)
                                                            window31['amt'].update(n)
                                                            window31['c_n'].update(prompt10)
                                                            window31['b_i_d'].update(kl)
                                                            kl=kl[0]
                                                            kl=int(kl[0])
                                                            ct=" select total from datas where c_name= %s " 
                                                            tc=(prompt10,)
                                                            b.execute(ct,tc,)
                                                            kt=b.fetchall()
                                                            if(kt== [(None,)]):
                                                                aa="update datas set total= %s where bill_id = %s "  
                                                                bb=(n,kl,)
                                                                b.execute(aa,bb,)
                                                                a.commit()
                                                            else:
                                                                aa="update datas set total= total + %s where bill_id = %s "  
                                                                bb=(n,kl,)
                                                                b.execute(aa,bb,)
                                                                a.commit()
                                                    else:
                                                        sg.popup_cancel('buy cancel ')
                                                if(event=="PAY"):
                                                    if(k==[]):
                                                        sg.popup("no product in carts")
                                                    elif(prompt10==''):
                                                        sg.popup("customer name not enter")         
                                                    else:
                                                        prompt11 = simpledialog.askstring("Input1", "Enter The ATM Number")
                                                        if(len(prompt11)==16 ):
                                                            prompt12 = simpledialog.askstring("Input1", "Enter The PIN Code",show='*')
                                                            if(len(str(prompt12))>4 and len(str(prompt12))<8):
                                                                time.sleep(4)
                                                                sg.popup("thanku for buy product")
                                                                window31['l'+sg.WRITE_ONLY_KEY]('')
                                                                window31['amt']('')
                                                                window31['c_n']('')
                                                                window31['b_i_d']('')
                                                                
                                                                import datetime as DT 
                                                                today = DT.date.today()
                                                                asds = ("update Rcarts set dates=%s where c_name=%s and dates is NULL ")
                                                                bss = (today,prompt10,)
                                                                b.execute(asds, bss,)
                                                                a.commit()
                                                                b.execute("select id from carts ")
                                                                dele =b.fetchall()
                                                                for i in dele:
                                                                    i=i[0]
                                                                    d = ("delete from carts where id= '%s' ")
                                                                    t = (i,)
                                                                    b.execute(d, t)
                                                                a.commit()    
                                                            else:
                                                                 sg.popup("pin is not valid length is greater aur less then 4 to 8") 
                                                        else:
                                                             sg.popup("ATM Number is not equal to 16") 
                                                elif(event=="EXIT"):
                                                    window31_active =False
                                                    window31.close()
                                                    window2_active =True
                                                    window2.UnHide()
                                                    break
                                                                    
                                        elif(event=="RETURN AND REFUND"):
                                            window2.Hide()
                                            prompt10=str(prompt10)
                                            cart=[
                                            [sg.Text("press PRODUCT button to see all product you have " , font=("Arial",20)) ],
                                            [sg.Button("PRODUCT",font=("Arial",15)),sg.Button("CLEAR",font=("Arial",15))],
                                            [sg.MLine(size=(80, 40), key='l'+sg.WRITE_ONLY_KEY,font='Arial 15')],     
                                            ]
                                            returns=[   
                                            [sg.Text("Enter The Code Of Product " , font=("Arial",20)) ],
                                            [sg.Input(key="code",font=("Arial",15))],
                                            [sg.Text("Enter The Quantity Of Product To Return " , font=("Arial",20)) ],
                                            [sg.Input(key="quans",font=("Arial",15))],
                                            [sg.Button("RETURNS",font=("Arial",15))]
                                            ]
                                            wel=[
                                            [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",30) , background_color='#7095db')]
                                            ]
                                            frame=[[sg.Frame("",layout=wel)]]
                                            frame1=[[sg.Frame("CARTS",layout=cart)]]
                                            frame2=[[sg.Frame("RETURNS",layout=returns)]]
                                            layout=[
                                            [sg.Text("",size=(180,1)),sg.Button("EXIT",font=("Arial",15))],
                                            [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                                            [sg.Text("")  ],
                                            [sg.Column(frame1),sg.Column(frame2)]
                                            ]
                                            window3=sg.Window("CARTS AND RETURNS",layout).finalize()
                                            window3.Maximize()
                                            while True:
                                                event,values=window3.read()
                                                if(event=="EXIT"):
                                                    window3_active =False
                                                    window3.close()
                                                    window2_active =True
                                                    window2.UnHide()
                                                    break
                                                elif(event=="CLEAR"):
                                                    window3['l'+sg.WRITE_ONLY_KEY]('')
                                                elif(event=="PRODUCT"):
                                                    window3['code']("")
                                                    plist=['Product Id : ',' Product company : ' , 'Product selling price : ' , 'quantity  ' ,  'total : ' ]
                                                    up = ("update Rcarts ,stem set Rcarts.p_name=stem.product_company,Rcarts.p_sp=stem.selling_price where stem.product_id = Rcarts.id and Rcarts.c_name = %s " )
                                                    date = ( prompt10,)
                                                    b.execute(up , date,)
                                                    import datetime as DT 
                                                    today = DT.date.today() 
                                                    week_ago = today - DT.timedelta(days=7)
                                                    sel=("select id , p_name , p_sp , quantity , total from Rcarts where c_name = %s and dates >= %s " )
                                                    ect=(prompt10, week_ago,)
                                                    b.execute(sel,ect,)
                                                    k=b.fetchall()
                                                    a.commit()   
                                                    
                                                    for i in k:
                                                        if(int(i[3])<=0):
                                                            pass
                                                        else:
                                                            for j in range(len(i)):
                                                                    window3['l'+sg.WRITE_ONLY_KEY].print(plist[j],i[j],end='', text_color='red')
                                                                    window3['l'+sg.WRITE_ONLY_KEY].print()
                                                            window3['l'+sg.WRITE_ONLY_KEY].print()
                                                elif(event=="RETURNS"):
                                                    ans=sg.popup_yes_no("do you want to return product ")
                                                    sel=("select * from Rcarts where c_name = %s and dates = %s" )
                                                    ect=(prompt10, today,)
                                                    b.execute(sel,ect,)
                                                    k=b.fetchall()
                                                    if(ans=="Yes"):
                                                        quans=values["quans"]
                                                        code=values["code"]
                                                        if(code==''):
                                                            sg.Popup("you have not enter the code")
                                                        else:
                                                            print(k)
                                                            for i in k:
                                                                print(i[6])
                                                                if(today==i[6]):
                                                                    quan=("select quantity from Rcarts where id = %s and c_name=%s and dates = %s" )
                                                                    tity=(int(code) , prompt10, today,)
                                                                    b.execute(quan , tity ,)
                                                                    kl=b.fetchall()
                                                                    a.commit()
                                                                    print(kl)
                                                                    
                                                                    kl=kl[0]
                                                                    print(kl[0])
                                                                    if(int(kl[0])<=0):
                                                                            dele1=("delete from Rcarts where id = %s and c_name = %s and dates = %s " )
                                                                            te1=(code , prompt10, today,)
                                                                            b.execute(dele1 , te1,)
                                                                    elif(int(quans)>i[0]):
                                                                            sg.Popup("you have buy less product of this code")
                                                                            break
                                                                    else:
                                                                            if(kl==[]):
                                                                                 sg.Popup("you have not buy any product of this code") 
                                                                            else:
                                                                                up = (" update stem set stock=stock + %s where stem.product_id = %s")
                                                                                dation = (int(quans), int(code),)
                                                                                b.execute(up, dation)
                                                                                dele1=("update Rcarts set quantity=quantity - %s where id = %s and c_name = %s  and dates = %s" )
                                                                                te1=(quans, code , prompt10, today,)
                                                                                b.execute(dele1 , te1,)
                                                                                a.commit()
                                                                                sg.Popup("your product have been return ") 
                                                                                sg.Popup("refund will done on your account in 3-4 days") 
                                                                                window3['quans']("")
                                                                                window3['code']("")
                                                                                break
                                                                else:
                                                                    sg.Popup("not match ") 
                                                                    break
                                                    else:
                                                        sg.popup_cancel('not delete ')
                                                                        
                                                                #---------------------------------------------USER LOGOUT ------------------------------------------------------------
                                        elif(event=="LOGOUT"):
                                            ee=1
                                            window2_active =False
                                            window2.close()
                                            window22.UnHide()
                                            window22_active =False
                                            window22.close()
                                            break
                                    break                      
                            elif(ch!=1):
                                sg.Popup("entered wrong password")
                                                            
                if(ch==5 and ee==0 and res==0):         
                    ans=sg.popup_yes_no("do you forget your password ?")
                    if(ans=="Yes"):
                        with open("ques.txt", "r") as f:
                            for i in f:
                                u, q ,a = i.split(",")
                                q = q.strip()
                                a = a.strip()
                                prompt4 = simpledialog.askstring("Input1", "enter the admin ID")
                                prompt5 = simpledialog.askstring("Input2", q )
                                if(prompt4 == u and prompt5 == a):
                                    prompt6 = simpledialog.askstring("Input1", "enter the new password",show='*')
                                    f = open("user.txt", "w")
                                    f.writelines(u)
                                    prompt6 = ","+prompt6
                                    f.writelines(prompt6)
                                    f.close()
                                    sg.Popup("password updated , login now")
                                else:
                                    sg.Popup("not match")
                    else:
                        sg.Popup("no updation")
            #-----------------------------------------------------------------main program start---------------------------------------------------------------
                        
            sg.theme('BrightColors')
            window_active =True
            
            wel=[
                    [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",40) , background_color='#7095db')]
                ]
            frame=[[sg.Frame("",layout=wel)]]
            layout = [
                    [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                    [sg.Text('Select Any Button' , justification='center',size=(180,2), font=("Arial",20) )],
                    [sg.Button('Admin',size=(180,2),font=("Arial",15))],
                    [sg.Button("User",size=(180,2),font=("Arial",15))],
                    [sg.Button("Exit",size=(180,2),font=("Arial",15))],
            ]
            window = sg.Window('LOGIN PAGE', layout).finalize()
            window.Maximize()

            window2_active =False
            while True:
                root.withdraw()
                event,values=window.read()
                #---------------------------------------------------------Admin--------------------------------------------------------------
                
                ch=0
                ee=0
              #------------------------------------- ADMIN LOGIN --------------------------------------------------------
                if(event=="Admin"):
                            window21_active =False
                            window5_active =False
                            window6_active =False
                            window3_active =False
                            res=0   
                            
                      #------------------------------------- ADMIN LOGIN --------------------------------------------------------
                            #window.Hide()
                            
                            for i in range(0,5):
                                prompt1 = simpledialog.askstring("Input1", "enter the admin ID")
                                if not prompt1:
                                    break
                                else:
                                    prompt2 = simpledialog.askstring("Input2", "enter the password" ,show='*')
                                    if not prompt2:
                                        break
                                    else:
                                        with open("user.txt", "r") as f:
                                            for i in f:
                                                        u , p = i.split(",")
                                                        p = p.strip()
                                                        ch=ch+1
                                                        if(prompt1 == '' and prompt2 == ''):
                                                            sg.Popup("nothing entered anything")
                                                        elif(prompt1 == '' or prompt2 == ''):
                                                            sg.Popup("not entered passsword or ID ")
                                                        elif(prompt1 == u and prompt2 == p):
                                                            res=1
                                                            break
                                        if(res==1):
                                            
                                            window21_active =True
                                            
                                            wel=[
                                                        [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",40) , background_color='#7095db')]
                                                        ]
                                            frame=[[sg.Frame("",layout=wel)]]
                                        
                                            frame2=[
                                                            
                                                            [sg.Text("Select Any Button To Move Ahead ", justification='center',size=(180,2), font=("Arial",20))],
                                                            [sg.Button("DISPLAY DATA AND UPDATE",size=(180,2),font=("Arial",15))],
                                                            [sg.Button("ADD PRODUCT",size=(180,2),font=("Arial",15))],
                                                            [sg.Button("NEW ADMIN",size=(180,2),font=("Arial",15))],
                                                            [sg.Button("CUSTOMER DETAIL",size=(180,2),font=("Arial",15))],
                                                            [sg.Button("LOGOUT",size=(180,2),font=("Arial",15))]
                                                            ]
                                            frames=[[sg.Frame("",layout=frame2)]]
                                            layout2=[
                                                            [ sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                                                            [sg.Column(frames)]
                                                            ]
                                            window21 = sg.Window('login', layout2,  location=(0,0),  size=(1550,800) ).finalize()
                                            window21.Maximize()
                                                    
                                            while True:
                                                event,values=window21.read()
                                    #------------------------------------------------AFTER LOGIN -------------------------------------------------------------
                                    #--------------------------------------------------DISPLAY DATA-----------------------------------------------------------
                                                if(event=="DISPLAY DATA AND UPDATE"):
                                                    window21.Hide()
                                                    window3_active =True
                                                    a_display()  
                                #--------------------------------------------------------------------------------------------------------------------------------                            
                                                elif(event=="ADD PRODUCT"):
                                                    add_product()
                                                            
                                                elif(event=="NEW ADMIN"):
                                                    add_admin()
                                                            
                                                elif(event=="CUSTOMER DETAIL"):
                                                    pass
                                                
                                                elif(event == "LOGOUT" ):
                                                    ee=1
                                                    window21_active =False
                                                    window21.close()
                                                    window_active =True
                                                    window.UnHide()
                                                    break
                                            break        
                                        else:
                                                    sg.Popup("sorry entered password is wrong please try again")  
                                        if(ch==5):
                                            break         
                            if(ee==0 and ch==5):         
                                        ans=sg.popup_yes_no("do you forget your password ?")
                                        if(ans=="Yes"):
                                                    with open("ques.txt", "r") as f:
                                                        for i in f:
                                                            u, q ,a = i.split(",")
                                                            q = q.strip()
                                                            a = a.strip()
                                                            prompt4 = simpledialog.askstring("Input1", "enter the admin ID")
                                                            prompt5 = simpledialog.askstring("Input2", q )
                                                            if(prompt4 == u and prompt5 == a):
                                                                prompt6 = simpledialog.askstring("Input1", "enter the new password",show='*')
                                                                f = open("user.txt", "w")
                                                                f.writelines(u)
                                                                prompt6 = ","+prompt6
                                                                f.writelines(prompt6)
                                                                f.close()
                                                                sg.Popup("password updated , login now")
                                                            else:
                                                                sg.Popup("not match")
                                        else:
                                                    sg.Popup("no updation")
                                       
                        
                #-----------------------------------------------USER------------------------------------------------------------------------
                
                if(event=="User"):
                    window22_active =True
                    window2_active =False
                    window51_active =False
                    wel=[
                        [sg.Text('\n Welcome To Online Shopping App \n' , justification='center',size=(180,3), font=("Arial",40) , background_color='#7095db')]
                        ]
                    frame=[[sg.Frame("",layout=wel)]]
                    
                    layoutss = [
                    [sg.Image('images.png', 'center', size=(220, 220)),sg.Column(frame)],
                    [sg.Text('Select Any Button' , justification='center',size=(180,2), font=("Arial",20) )],
                    [sg.Button('login',size=(180,2),font=("Arial",15))],
                    [sg.Button("New User",size=(180,2),font=("Arial",15))],
                    [sg.Button("Exit",size=(180,2),font=("Arial",15))],
                    ]
                    window22 = sg.Window('LOGIN PAGE', layoutss).finalize()
                    window22.Maximize()
                    while True:
                        event,values=window22.read()
                        window22.Hide()
                        if(event=="login"):
                            sign_in()
                            break
                            
                        if(event=="New User"):
                            signup()
                            break
                            
                        if(event=="Exit"):
                            window22_active =False
                            window22.close()
                            window.UnHide()
                            window_active =True
                            break
                            
                   
                                                                               
                #--------------------------------------------------------------EXIT---------------------------------------------------------       
                elif(event=="Exit"):
                    window_active =False
                    window.close()
                    root.deiconify()
                    break
            
                
        
    image = Image.open('welcome-online-store_1280x@2x.jpg')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)
    button = Button(root,text='ENTER',relief=RAISED,font=('Arial Bold', 18),width=10,height=3,command=go)
    button.place(x=550, y=650)
    button1 = Button(root,text='EXIT',relief=RAISED,font=('Arial Bold', 18),width=10,height=3,command=EXIT)
    button1.place(x=850, y=650)
    root.mainloop()
    root.withdraw()
    
except mysql.connector.errors.ProgrammingError:
    sg.Popup("incorrect data")
    exit()