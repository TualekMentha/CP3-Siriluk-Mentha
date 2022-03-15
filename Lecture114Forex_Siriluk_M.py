import requests
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import requests
import json

#colors
color0 = "#FFFFFF"   #white
color1 = "#000000"   #black
color2 = "#00B2EE"   #blue

root = Tk()
root.geometry('300x400')
root.title("My Currency Converter")
root.configure(bg=color0)
root.resizable(height=FALSE, width=FALSE)

#frames
top = Frame(root, width=300, height=60, bg=color2)
top.grid(row=0, column=0)


main = Frame(root, width=300, height=260, bg=color0)
main.grid(row=1, column=0)


def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()
    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'JPY':
        symbol = '¥'
    elif currency_2 == 'GPB':
        symbol = '£'
    elif currency_2 == 'AUD':
        symbol = '$'
    elif currency_2 == 'CAD':
        symbol = 'CA$'
    elif currency_2 == 'CHF':
        symbol = 'CHF'
    elif currency_2 == 'CNY':
        symbol = '¥'
    elif currency_2 == 'HKD':
        symbol = 'HK$'
    elif currency_2 == 'NZD':
        symbol = 'NZ$'
    elif currency_2 == 'SEK':
        symbol = 'kr'
    elif currency_2 == 'KRW':
        symbol = '₩'
    elif currency_2 == 'SGD':
        symbol = 'S$'
    elif currency_2 == 'NOK':
        symbol = 'kr'
    elif currency_2 == 'MXN':
        symbol = 'MX$'
    elif currency_2 == 'THB':
        symbol = 'THB'

    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "1fc91b9bcamsh7cf8a20128360a4p18f11bjsn3d271436a67a"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + "{:,.2f}".format(converted_amount)

    result['text'] = formatted

    print(converted_amount, formatted)

icon = Image.open("icon1.png")
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
name_app = Label(top, image=icon, compound=LEFT,text="Currency Converter", font=("Ivy 15 bold"), height=5, padx=13, pady=30, anchor=CENTER, bg=color2, fg=color0 )
name_app.place(x=0, y=0)

icon2 = Image.open("icon2.jpg")
icon2 = icon2.resize((300,70))
icon2 = ImageTk.PhotoImage(icon2)
name_logo = Label(image=icon2, compound=CENTER)
name_logo.place(x=0, y=325)

result = Label(main, text=" ", font=("Arial 15 bold"), width=17, height=2, pady=7, relief="solid", anchor=CENTER, bg=color2, fg=color1)
result.place(x=50, y=10)

currency = ['USD', 'EUR', 'JPY', 'GPB', 'AUD', 'CAD', 'CHF', 'CNY', 'HKD', 'NZD', 'SEK','KRW', 'SGD', 'NOK', 'MXN', 'INR', 'RUB', 'ZAR', 'TRY', 'BRL', 'TWD', 'DKK', 'THB' ]

from_tab = Label(main, text = "From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Arial 10 bold'), bg=color0, fg=color1)
from_tab.place(x=50, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Arial 12 bold'))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

to_tab = Label(main, text = "To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Arial 10 bold'), bg=color0, fg=color1)
to_tab.place(x=160, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Arial 12 bold'))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=('Arial 12 bold'), relief=SOLID)
value.place(x=50, y=160)

button = Button(main, text="Converter", width=10, padx=5, height=1, bg=color2, fg=color0, font=('Arial 10 bold'), relief=SOLID, command=convert)
button.place(x=100, y=200)



root.mainloop()




