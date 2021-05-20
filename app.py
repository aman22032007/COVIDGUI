import main
import tkinter
import countrylist
from tkinter.messagebox import showinfo
from tkinter import font
from tkinter import *

mainWindow = tkinter.Tk()
mainWindow.title("Cases")
mainWindow.geometry('640x480')

msgfont = font.Font(size=20)
cases = main.execute_world()


def show_countries():
    fileList = tkinter.Listbox(mainWindow)
    fileList.grid(row=8, column=0, sticky='nws', rowspan=1)
    fileList.config(borderwidth=2, relief='sunken')

    for zone in countrylist.countries:
        fileList.insert(tkinter.END, zone)

    listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
    listScroll.grid(row=8, column=0, sticky='nws', rowspan=2, padx=220)
    fileList['yscrollcommand'] = listScroll.set

    def items_selected(event):
        """ handle item selected event
        """
        # get selected indices
        selected_indices = fileList.curselection()
        # get selected items
        selected_langs = ",".join([fileList.get(i) for i in selected_indices])
        print(selected_langs)
        fileList.destroy()
        listScroll.destroy()
        main.country = selected_langs
        if main.country == "the-world":
            label2.config(text=cases["TotalConfirmed"])
            label4.config(text=cases["TotalDeaths"])
            label6.config(text=cases["TotalRecovered"])
        else:
            cases2 = main.execute()
            label2.config(text=cases2[len(cases2)-1]["Confirmed"])
            label4.config(text=cases2[len(cases2) - 1]["Deaths"])
            label6.config(text=cases2[len(cases2) - 1]["Recovered"])
        return selected_langs

    country_to_show = fileList.bind('<<ListboxSelect>>', items_selected)


label1 = tkinter.Label(text="Coronavirus Cases:", bg='white', fg='#555555', font=msgfont)
label1.grid(row=1, column=0, padx='175')

label2 = tkinter.Label(text=cases["TotalConfirmed"], bg='white', fg='#aaa', font=msgfont)
label2.grid(row=2, column=0, padx='175')

label3 = tkinter.Label(text="Deaths:", bg='white', fg='#555555', font=msgfont)
label3.grid(row=3, column=0, padx='175')

label4 = tkinter.Label(text=cases["TotalDeaths"], bg='white', fg='#696969', font=msgfont)
label4.grid(row=4, column=0, padx='175')

label5 = tkinter.Label(text="Recovered:", bg='white', fg='#555555', font=msgfont)
label5.grid(row=5, column=0, padx='175')

label6 = tkinter.Label(text=cases["TotalRecovered"], bg='white', fg='#8ACA2B', font=msgfont)
label6.grid(row=6, column=0, padx='175')

button_to_chnage = tkinter.Button(text='view by country', command=show_countries)
button_to_chnage.grid(row=7, column=0)

mainWindow.configure(bg='white')
mainWindow.mainloop()
