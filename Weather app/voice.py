import re
import speech_recognition
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request, urlopen
import requests
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class voice:
    def __init__(self, window):

        self.window = window

        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            print("Say something")

            #titles = tk.Label(master=window, text=title)
            #titles.configure(font=("DejaVu Sans", 15, "bold"))
            #titles.pack()
            #####################
            canvas = tk.Canvas(window, width=953, height=500)
            canvas.pack()
            img = ImageTk.PhotoImage(Image.open("953x500.png").resize((953, 500), Image.ANTIALIAS))
            canvas.background = img  # Keep a reference in case this code is put in a function.
            bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

            # Put a tkinter widget on the canvas.
            say = "Say something like... what's the weather like in your city"
            instr = tk.Label(window, bg='white', text=say)
            instr.configure(font=("DejaVu Sans", 15, "bold"))
            label_instr = canvas.create_window(953 / 2, 500 / 2, anchor=tk.CENTER, window=instr)

            appName = "TheWeatherApp"
            appNameDisp = tk.Label(window, bg='white', text=appName)
            appNameDisp.configure(font=("DejaVu Sans", 32, "bold"))
            label_appNameDisp = canvas.create_window(953 / 2, 200 / 2, anchor=tk.N, window=appNameDisp)

            version = "Data taken from weather.com | v1.0"
            versionDisp = tk.Label(window, fg='black', text=version)
            versionDisp.configure(font=("DejaVu Sans", 8))
            label_window = canvas.create_window(953 / 2, 500 - 20, anchor=tk.N, window=versionDisp)

            window.resizable(False, False)
            #####################

            audio = recognizer.listen(source)

        try:
            words = recognizer.recognize_google(audio)
        except:
            title = "Your internet connection seems broken. Fix it and try again later"


        try:
            matches = re.search("what's the weather like in (.*)", words)

            webpage = requests.get(f'https://www.google.com/search?q=temperature+in+{matches[1]}')
        except Exception as e:
            print(e)
            title = "Hmm, seems like I can't help you with that, could you please repeat?"
            try:
                webpage = requests.get(f'https://www.google.com/search?q=error')
            except:
                title = "Your internet connection seems broken. Fix it and try again later"

        '''
        if matches:
            print(f"Heyy, {matches[1]}.")
        '''



#req.close()
#page_soup = soup(webpage, "html.parser")
# print(page_soup.prettify())
        try:
            page_soup = soup(webpage.text, 'html.parser')
            temp = page_soup.find_all("div", {"class":"BNeawe iBp4i AP7Wnd"})
            city = page_soup.find_all("span", {"class":"BNeawe tAd8D AP7Wnd"})
            condition = page_soup.find_all("div", {"class":"BNeawe tAd8D AP7Wnd"})
        except:
            title = "Your internet connection seems broken. Fix it and try again later"
            temp = "null"
            city = "null"
            condition = "null"

        if len(temp) == 0 or len(city) == 0 or len(condition) == 0:
            print("Oops, didn't catch that one, please try again.")
            title = "Oops, didn't catch that one, please try again."
        flag = False

        try:
            for i in temp:
                for j in city:
                    if "," in j.string:
                        print(f"Right now in {j.string}, it is " + i.string, end=' (')
                        title = f"Right now in {j.string}, it is " + i.string + ' ('

                        for k in condition:
                            for char in k.string:
                                if flag:
                                    print(char.lower(), end='')
                                    title = title + char.lower()

                                if char =='\n':
                                    flag = True
                            title = title.rstrip() + ').'
                            print(').', end='')
                            break
                    else:
                        if not title == "Your internet connection seems broken. Fix it and try again later":
                            title = "Hmm, it seems like I don't know that, could you please repeat?"
                break
        except Exception as e:
            if not title == "Your internet connection seems broken. Fix it and try again later":
                title = "Not quite sure what you meant."
        #titles.destroy()
        ##############################

        ################################
        #canvas = tk.Canvas(window, width=953, height=500)
        #canvas.pack()

        if "sunny" in title:
            img = ImageTk.PhotoImage(Image.open("sunny.png").resize((953, 500), Image.ANTIALIAS))
        elif "rain" in title and "shower" in title:
            img = ImageTk.PhotoImage(Image.open("shower.png").resize((953, 500), Image.ANTIALIAS))
        elif "rain" in title:
            img = ImageTk.PhotoImage(Image.open("rain.png").resize((953, 500), Image.ANTIALIAS))
        elif "snow" in title:
            img = ImageTk.PhotoImage(Image.open("snow.png").resize((953, 500), Image.ANTIALIAS))
        elif "haze" in title:
            img = ImageTk.PhotoImage(Image.open("haze.png").resize((953, 500), Image.ANTIALIAS))
        elif "fog" in title:
            img = ImageTk.PhotoImage(Image.open("fog.png").resize((953, 500), Image.ANTIALIAS))
        elif "partly cloudy" in title:
            img = ImageTk.PhotoImage(Image.open("partly cloudy.png").resize((953, 500), Image.ANTIALIAS))
        elif "cloud" in title:
            img = ImageTk.PhotoImage(Image.open("cloudy.png").resize((953, 500), Image.ANTIALIAS))
        elif "windy" in title:
            img = ImageTk.PhotoImage(Image.open("windy.png").resize((953, 500), Image.ANTIALIAS))
        elif "storm" in title:
            img = ImageTk.PhotoImage(Image.open("thunderstorm.png").resize((953, 500), Image.ANTIALIAS))
        else:
            img = ImageTk.PhotoImage(Image.open("953x500.png").resize((953, 500), Image.ANTIALIAS))



        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # Put a tkinter widget on the canvas.
        instr.destroy()
        appNameDisp.destroy()
        versionDisp.destroy()
        titles = tk.Label(window, bg='white', text=title)
        titles.configure(font=("DejaVu Sans", 15, "bold"))
        label_window = canvas.create_window(953 / 2, 200 / 2, anchor=tk.N, window=titles)
        window.resizable(False, False)

