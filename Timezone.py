from datetime import datetime
import pytz

def Timezone():
    print("Choose Time zone! \n1.Asia\n2.EU\n3.America")
    Timezone_in=input("Input Time zone : ")
    if Timezone_in == "1":
            Asia()
    elif Timezone_in =="2":
            EU()
    elif Timezone_in =="3":
            America()
    else:
        print("Pls Choose 1 / 2 / 3 ")
             
def Asia():
    print("----------------------------------------------------------------")
    print("Choose Country \n1.Japan\n2.Chaina\n3.India")
    Time_country=input("Input Country : ")
    if Time_country == "1":
                 Japan()               
                 
    elif Time_country =="2":
        def Chaina():
                Time_in = input(("Input Chaina Times (hr/min(00:00)): "))
                Chaina()
                
    elif Time_country =="3":
        def India():
                Time_in = input(("Input India Times (hr/min(00:00)): "))
                India()
    else:
        print("Pls Choose 1 / 2 / 3 ")
     
def Japan():
                 Time_in = (input(("Input Japan Times (hr:min(00:00)): ")))
                 time_obj = datetime.strptime(Time_in, "%H:%M")
                 japan_tz = pytz.timezone('Asia/Tokyo')
                 thailand_tz = pytz.timezone('Asia/Bangkok')
                 japan_time = japan_tz.localize(time_obj)  
                 thailand_time = japan_time.astimezone(thailand_tz)  
                 print(f"Thailand Time: {thailand_time.strftime('%H:%M')}") 
                 
                 
def EU():
    print("----------------------------------------------------------------")
    print("Choose Country \n1.Germany\n2.England\n3.Portugal")
    Time_country = input("Input Time : ")
    if Time_country == "1":
            Asia()
    elif Time_country =="2":
            EU()
    elif Time_country =="3":
            America()
    else:
        print("Pls Choose 1 / 2 / 3 ")



def America():
    print("----------------------------------------------------------------")
    print("Choose Country \n1.USA\n2.Cannada\n3.Maxico")
    Time_country = input("Input Time : ")
    if Time_country == "1":
            Asia()
    elif Time_country =="2":
            EU()
    elif Time_country =="3":
            America()
    else:
        print("Pls Choose 1 / 2 / 3 ")
    
    
    
Timezone()