from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests 
import pytz
from emoji import emojize

root=Tk()
root.title("weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getWeather():
    try:
        
        city=textfield.get()
        geolocater=Nominatim(user_agent="geoapiExercies")
        location= geolocater.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f7f59e2685598d932267bf62f49f821e"
        json_data = requests.get(api).json()
        condition= json_data['weather'][0]['main']
        description= json_data['weather'][0]['description']
        temp= int(json_data['main']['temp']-273.15)
        pressure= json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
    
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","Feel","like",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","invalid name Enter")  

#search box
search_image=PhotoImage(file="search box.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)
textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),background="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()
search_icon=PhotoImage(file="search.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",background="#404040",command=getWeather)
myimage_icon.place(x=390,y=29.5)

#logo
logo_image=PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image,bg="#E7A6F7")
frame_myimage.pack(padx=5,pady=5,side="bottom")

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

 #label
 # Weather information labels (placeholders)
label1=Label(root,text="WIND",font=("helvetica",15,'bold'),fg="white",bg="#E7A6F7")
label1.place(x=120,y=400)

label2=Label(root,text="Humidity",font=("helvetica",15,'bold'),fg="white",bg="#E7A6F7")
label2.place(x=250,y=400)

label3=Label(root,text="Description",font=("helvetica",15,'bold'),fg="white",bg="#E7A6F7")
label3.place(x=430,y=400)

label4=Label(root,text="Pressure",font=("helvetica",15,'bold'),fg="white",bg="#E7A6F7")
label4.place(x=600,y=400)
#temperature
t=Label(font=("arial",80,"bold"),fg="#ee666d")
t.place(x=400,y=150)
#condition
c=Label(font=("arial",15,'bold'))
c.place(x=480,y=250)
#wind
w=Label(text=emojize(":smiling_face_with_halo:"),font=("arial",20,"bold"),bg="#EC7063")
w.place(x=120,y=430)
#humidity
h=Label(text=emojize(":slightly_smiling_face:"),font=("arial",20,"bold"),bg="#EC7063")
h.place(x=280,y=430)
#description
d=Label(text=emojize(":smiling_face_with_sunglasses:"),font=("arial",20,"bold"),bg="#EC7063")
d.place(x=450,y=430)
#pressure
p=Label(text=emojize(":grinning_face:"),font=("arial",20,"bold"),bg="#EC7063")
p.place(x=630,y=430)

root.mainloop()

