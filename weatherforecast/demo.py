from tkinter import *
from tkinter import ttk,messagebox
from datetime import *
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
import pytz

def data_get():
    city1 = com.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city1)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f'{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E')
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    city= city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=572f77a27b6404a489c655a438944910").json()
    print(data)
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=int(data["main"]["temp"]-273.15))
    pre_label1.config(text=data["main"]["pressure"])




win = Tk()
win.title("Weather Forecasting App")
win.config(bg='blue')
win.geometry('700x650')
win.resizable(FALSE,FALSE)

weat_image=PhotoImage(file="weatherforecast/logo1.png")
weatherimage=Label(win,image=weat_image,bg="blue")
weatherimage.place(x=50,y=50,height=100,width=70)

name_label= Label(win, text="Weather Application", fg="black", font=("Times New Roman", 25, "bold"))
name_label.place(x=150, y=80,height=50,width=400)


city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com= ttk.Combobox(win,text="Weather App",values=list_name,
                  font=("Times New Roman", 15, "bold"),textvariable=city_name)
com.place(x=200, y=240,height=40,width=300)

done_button=Button(win,text="Done", font=("Times New Roman", 20, "italic"),command=data_get)
done_button.place(y=300,height=25,width=100,x=250)

w_label=Label(win, text="Weather Climate", fg="black", font=("georgia", 15, "italic"))
w_label.place(x=90,y=340,height=40,width=190)
w_label1=Label(win, text="", fg="black", font=("georgia", 15, "italic"))
w_label1.place(x=300,y=340,height=40,width=240)

wb_label=Label(win, text="Weather Description", fg="black", font=("georgia", 15, "italic"))
wb_label.place(x=90,y=400,height=40,width=190)
wb_label1=Label(win, text=" ", fg="black", font=("georgia", 15, "italic"))
wb_label1.place(x=300,y=400,height=40,width=190)

temp_label=Label(win, text="Temperature", fg="black", font=("georgia", 15, "italic"))
temp_label.place(x=90,y=460,height=40,width=190)
temp_label1=Label(win, text="", fg="black", font=("georgia", 15, "italic"))
temp_label1.place(x=300,y=460,height=40,width=190)

pre_label=Label(win, text="Pressure", fg="black", font=("georgia", 15, "italic"))
pre_label.place(x=90,y=520,height=40,width=190)
pre_label1=Label(win, text="", fg="black", font=("georgia", 15, "italic"))
pre_label1.place(x=300,y=520,height=40,width=190)

clock=Label(win,font=("Helvetica",30,'bold'),fg="white",bg="blue")
clock.place(x=40,y=160)

timezone=Label(win,font=("Helvetica",20),fg="white",bg="blue")
timezone.place(x=500,y=160)

long_lat=Label(win,font=("Helvetica",20),fg="white",bg="blue")
long_lat.place(x=400,y=160)




win.mainloop()
