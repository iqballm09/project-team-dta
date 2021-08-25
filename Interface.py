"""
PROGRAM GUI APLIKASI
Created By : Nurkholilah Harahap
"""

import string
import tkinter as tk
from tkinter import ttk, Tk, messagebox
# from module.ConvArea import AreaConverter
from module.ConvByte import ByteConverter
from module.ConvNumSys import NumberSysConverter
from module.ConvTemper import TemperatureConverter
from module.ConvTime import TimeConverter
from module.ConvMass import MassConverter
from module.ConvLength import LengthConverter


# Global Variables
string1 = ""
result1 = 0
string2 = ""
result2 = 0
string3 = ""
result3 = 0
string4 = ""
result4 = 0
string5 = ""
result5 = 0
string6 = ""
result6 = 0
string7 = ""
result7 = 0

# Main Screen


def main_window():
    # Initiate Screen
    calc = Tk()

    # Configure Screen
    calc.geometry('500x550')
    calc.resizable(0, 1)
    calc.configure(bg="powder blue", bd=10)
    calc.title(" Aplikasi Konversi Satuan")

    # Create Tab Screen
    tab_frame = ttk.Notebook(calc)
    tab_frame.grid()

    # Configure Tab Screen
    calc.bind("<Configure>", tab_frame.config(
        height=calc.winfo_height(), width=calc.winfo_width()))

    # Set style of Screen
    s1 = ttk.Style()
    s1.configure('color1.TFrame', background='#CCE5FF')
    s2 = ttk.Style()
    s2.configure('color2.TFrame', background='#C0C0C0')

    tab_frame.pack(fill="both", expand=True)  # used pack() instead of grid()
    return calc, tab_frame

# 1. Tab Untuk Massa


def massa_tab(tab_frame):
    # Initiate a Tab
    tab = ttk.Frame(tab_frame, height=100, width=100, style='color1.TFrame')
    text_input = tk.StringVar()
    text_output = tk.StringVar()
    combo_input = tk.StringVar()
    combo1_input = tk.StringVar()
    set_satuan = ("kg", "g", "ton", "kwintal", "ons")

    text_display_inp = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_input,
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)
    text_display_out = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_output, state='disabled',
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)

    combo = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo_input,
        state='readonly',
    )
    combo.current(0)  # set the selected item
    combo.grid(column=2, row=0)

    combo1 = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo1_input,
        state='readonly'
    )
    combo1.current(0)  # set the selected item
    combo1.grid(column=2, row=1)

    # List of Functions

    def btnClick(numbers):
        global string1
        string1 += str(numbers)
        text_input.set(string1)

    def btnClearDisplay():  # Function for "C" button
        global string1
        string1 = ''  # Reset operator
        text_input.set(string1)  # Reset TextBox
        text_output.set(string1)

    def btnEqualsInput():  # Function for "=" button
        global result1, string1
        selected = str(combo_input.get()) + str(combo1_input.get())
        if text_input.get().isdigit():
            obj = MassConverter(int(text_input.get()))
        else:
            obj = MassConverter(float(text_input.get()))
        dict_mass = {"tonton": obj.tontoton(), "tonkwintal": obj.tontokwintal(), "tonkg": obj.tontokg(), "tonons": obj.tontoons(), "tong": obj.tontog(),
                     "kwintalton": obj.kwintaltoton(), "kwintalkwintal": obj.kwintaltokwintal(), "kwintalkg": obj.kwintaltokg(), "kwintalons": obj.kwintaltoons(), "kwintalg": obj.kwintaltog(),
                     "kgton": obj.kgtoton(), "kgkwintal": obj.kgtokwintal(), "kgkg": obj.kgtokg(), "kgons": obj.kgtoons(), "kgg": obj.kgtog(),
                     "onston": obj.onstoton(), "onskwintal": obj.onskwintal(), "onskg": obj.onstokg(), "onsons": obj.onstoons(), "onsg": obj.onstog(),
                     "gton": obj.gtoton(), "gkwintal": obj.gtokwintal(), "gkg": obj.gtokg(), "gons": obj.gtoons(), "gg": obj.gtog()}
        result1 = dict_mass[selected]
        text_output.set(result1)

    def clicked():
        try:
            assert text_input.get().count(".") == 1 or text_input.get().isdigit()
            btnEqualsInput()
        except:
            if "," in text_input.get():
                messagebox.showerror("Error", "Please Use '.' instead ','")
            else:
                messagebox.showerror("Error", "Please input number only!")
            text_input.set("")

    def button_delete():
        global string1
        text = string1[:-1]
        string1 = text
        text_input.set(text)

    def sign_change():
        global string1
        if string1[0] == "-":
            temp = string1[1:]
        else:
            temp = "-"+string1
        string1 = temp
        text_input.set(temp)

    # Create buttons
    btn7 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=3, column=0, sticky="nsew")
    btn8 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=3, column=1, sticky="nsew")
    btn9 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=3, column=2, sticky="nsew")
    delete_one = tk.Button(tab, padx=3, bd=5, fg="black", font=('arial', 20, 'bold'),
                           text='X', bg='powder blue', command=lambda: button_delete()).grid(row=3, column=3, sticky="nsew")
    btn4 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=4, column=0, sticky="nsew")
    btn5 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=4, column=1, sticky="nsew")
    btn6 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=4, column=2, sticky="nsew")
    btnClear = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                         text='C', bg='powder blue', command=lambda: btnClearDisplay()).grid(row=4, column=3, sticky="nsew")
    btn1 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=5, column=0, sticky="nsew")
    btn2 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=5, column=1, sticky="nsew")
    btn3 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=5, column=2, sticky="nsew")
    signs = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="\u00B1", bg='powder blue', command=lambda: sign_change()).grid(row=5, column=3, sticky="nsew")
    btn0 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=6, column=0, sticky="nsew")
    point = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text='.', bg='powder blue', command=lambda: btnClick(".")).grid(row=6, column=1, sticky="nsew")
    btnEquals = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                          text='=', bg='powder blue', command=clicked).grid(row=6, columnspan=2, column=2, sticky="nsew")

    return tab

# 2. Tab untuk suhu


def temp_tab(tab_frame):
    # Initiate a Tab
    tab = ttk.Frame(tab_frame, height=100, width=100, style='color1.TFrame')
    text_input = tk.StringVar()
    text_output = tk.StringVar()
    combo_input = tk.StringVar()
    combo1_input = tk.StringVar()
    set_satuan = ("Celcius", "Fahrenheit", "Kelvin", "Reamur")

    text_display_inp = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_input,
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)
    text_display_out = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_output, state='disabled',
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)

    combo = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo_input,
        state='readonly'
    )
    combo.current(0)  # set the selected item
    combo.grid(column=2, row=0)

    combo1 = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo1_input,
        state='readonly'
    )
    combo1.current(0)  # set the selected item
    combo1.grid(column=2, row=1)

    # List of Functions
    def btnClick(numbers):
        global string2
        string2 += str(numbers)
        text_input.set(string2)

    def btnClearDisplay():  # Function for "C" button
        global string2
        string2 = ''  # Reset operator
        text_input.set(string2)  # Reset TextBox
        text_output.set(string2)

    def btnEqualsInput():  # Function for "=" button
        global result2, string2
        selected = str(combo_input.get()) + str(combo1_input.get())
        if text_input.get().isdigit():
            obj = TemperatureConverter(int(text_input.get()))
        else:
            obj = TemperatureConverter(float(text_input.get()))
        dict_mass = {"CelciusCelcius": obj.celtocel(), "CelciusFahrenheit": obj.celtofah(), "CelciusKelvin": obj.celtokel(), "CelciusReamur": obj.celtoream(),
                     "ReamurReamur": obj.reamtoream(), "ReamurCelcius": obj.reamtocel(), "ReamurFahrenheit": obj.reamtofah(), "ReamurKelvin": obj.reamtokel(),
                     "FahrenheitFahrenheit": obj.fahtofah(), "FahrenheitCelcius": obj.fahtocel(), "FahrenheitReamur": obj.fahtoream(), "FahrenheitKelvin": obj.fahtokel(),
                     "KelvinKelvin": obj.keltokel(), "KelvinCelcius": obj.keltocel(), "KelvinReamur": obj.keltoream(), "KelvinFahrenheit": obj.keltofah()}
        result2 = dict_mass[selected]
        text_output.set(result2)

    def clicked():
        try:
            assert text_input.get().count(".") == 1 or text_input.get().isdigit()
            btnEqualsInput()
        except:
            if "," in text_input.get():
                messagebox.showerror("Error", "Please Use '.' instead ','")
            else:
                messagebox.showerror("Error", "Please input number only!")
            text_input.set("")

    def button_delete():
        global string2
        text = string2[:-1]
        string2 = text
        text_input.set(text)

    def sign_change():
        global string2
        if string2[0] == "-":
            temp = string2[1:]
        else:
            temp = "-"+string2
        string2 = temp
        text_input.set(temp)

    # Create buttons
    btn7 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=3, column=0, sticky="nsew")
    btn8 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=3, column=1, sticky="nsew")
    btn9 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=3, column=2, sticky="nsew")
    delete_one = tk.Button(tab, padx=3, bd=5, fg="black", font=('arial', 20, 'bold'),
                           text='X', bg='powder blue', command=lambda: button_delete()).grid(row=3, column=3, sticky="nsew")
    btn4 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=4, column=0, sticky="nsew")
    btn5 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=4, column=1, sticky="nsew")
    btn6 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=4, column=2, sticky="nsew")
    btnClear = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                         text='C', bg='powder blue', command=lambda: btnClearDisplay()).grid(row=4, column=3, sticky="nsew")
    btn1 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=5, column=0, sticky="nsew")
    btn2 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=5, column=1, sticky="nsew")
    btn3 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=5, column=2, sticky="nsew")
    signs = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="\u00B1", bg='powder blue', command=lambda: sign_change()).grid(row=5, column=3, sticky="nsew")
    btn0 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=6, column=0, sticky="nsew")
    point = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text='.', bg='powder blue', command=lambda: btnClick(".")).grid(row=6, column=1, sticky="nsew")
    btnEquals = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                          text='=', bg='powder blue', command=clicked).grid(row=6, columnspan=2, column=2, sticky="nsew")
    return tab

# 3. Tab untuk waktu


def time_tab(tab_frame):
    # Initiate a Tab
    tab = ttk.Frame(tab_frame, height=100, width=100, style='color1.TFrame')
    text_input = tk.StringVar()
    text_output = tk.StringVar()
    combo_input = tk.StringVar()
    combo1_input = tk.StringVar()
    set_satuan = ("Menit", "Detik", "Jam", "Hari")

    text_display_inp = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_input,
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)
    text_display_out = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_output, state='disabled',
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)

    combo = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo_input,
        state='readonly',
    )
    combo.current(0)  # set the selected item
    combo.grid(column=2, row=0)

    combo1 = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo1_input,
        state='readonly'
    )
    combo1.current(0)  # set the selected item
    combo1.grid(column=2, row=1)

    # List of Functions
    def btnClick(numbers):
        global string3
        string3 += str(numbers)
        text_input.set(string3)

    def btnClearDisplay():  # Function for "C" button
        global string3
        string3 = ''  # Reset operator
        text_input.set(string3)  # Reset TextBox
        text_output.set(string3)

    def btnEqualsInput():  # Function for "=" button
        global result3, string3
        selected = str(combo_input.get()) + str(combo1_input.get())
        if text_input.get().isdigit():
            obj = TimeConverter(int(text_input.get()))
        else:
            obj = TimeConverter(float(text_input.get()))
        dict_mass = {"MenitMenit": text_input.get(), "MenitDetik": obj.menittodetik(), "MenitJam": obj.menittojam(), "MenitHari": obj.menittohari(),
                     "DetikDetik": text_input.get(), "DetikMenit": obj.detiktomenit(), "DetikJam": obj.detiktojam(), "DetikHari": obj.detiktohari(),
                     "JamJam": text_input.get(), "JamDetik": obj.jamtodetik(), "JamMenit": obj.jamtomenit(), "JamHari": obj.jamtohari(),
                     "HariHari": text_input.get(), "HariDetik": obj.haritodetik(), "HariJam": obj.haritojam(), "HariMenit": obj.haritomenit()}
        result3 = dict_mass[selected]
        text_output.set(result3)

    def clicked():
        try:
            assert text_input.get().count(".") == 1 or text_input.get().isdigit()
            btnEqualsInput()
        except:
            if "," in text_input.get():
                messagebox.showerror("Error", "Please Use '.' instead ','")
            else:
                messagebox.showerror("Error", "Please input number only!")
            text_input.set("")

    def button_delete():
        global string3
        text = string3[:-1]
        string3 = text
        text_input.set(text)

    def sign_change():
        global string3
        if string3[0] == "-":
            temp = string3[1:]
        else:
            temp = "-"+string3
        string3 = temp
        text_input.set(temp)

    # Create buttons
    btn7 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=3, column=0, sticky="nsew")
    btn8 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=3, column=1, sticky="nsew")
    btn9 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=3, column=2, sticky="nsew")
    delete_one = tk.Button(tab, padx=3, bd=5, fg="black", font=('arial', 20, 'bold'),
                           text='X', bg='powder blue', command=lambda: button_delete()).grid(row=3, column=3, sticky="nsew")
    btn4 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=4, column=0, sticky="nsew")
    btn5 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=4, column=1, sticky="nsew")
    btn6 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=4, column=2, sticky="nsew")
    btnClear = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                         text='C', bg='powder blue', command=lambda: btnClearDisplay()).grid(row=4, column=3, sticky="nsew")
    btn1 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=5, column=0, sticky="nsew")
    btn2 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=5, column=1, sticky="nsew")
    btn3 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=5, column=2, sticky="nsew")
    signs = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="\u00B1", bg='powder blue', command=lambda: sign_change()).grid(row=5, column=3, sticky="nsew")
    btn0 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=6, column=0, sticky="nsew")
    point = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text='.', bg='powder blue', command=lambda: btnClick(".")).grid(row=6, column=1, sticky="nsew")
    btnEquals = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                          text='=', bg='powder blue', command=clicked).grid(row=6, columnspan=2, column=2, sticky="nsew")
    return tab

# 4. Tab untuk Data


def byte_tab(tab_frame):
    # Initiate a Tab
    tab = ttk.Frame(tab_frame, height=100, width=100, style='color1.TFrame')
    text_input = tk.StringVar()
    text_output = tk.StringVar()
    combo_input = tk.StringVar()
    combo1_input = tk.StringVar()
    set_satuan = ("GB", "MB", "KB", "Byte")

    text_display_inp = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_input,
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)
    text_display_out = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_output, state='disabled',
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)

    combo = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo_input,
        state='readonly',
    )
    combo.current(0)  # set the selected item
    combo.grid(column=2, row=0)

    combo1 = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo1_input,
        state='readonly'
    )
    combo1.current(0)  # set the selected item
    combo1.grid(column=2, row=1)

    # List of Functions
    def btnClick(numbers):
        global string4
        string4 += str(numbers)
        text_input.set(string4)

    def btnClearDisplay():  # Function for "C" button
        global string4
        string4 = ''  # Reset operator
        text_input.set(string4)  # Reset TextBox
        text_output.set(string4)

    def btnEqualsInput():  # Function for "=" button
        global result4, string4
        selected = str(combo_input.get()) + str(combo1_input.get())
        if text_input.get().isdigit():
            obj = ByteConverter(int(text_input.get()))
        else:
            obj = ByteConverter(float(text_input.get()))
        dict_mass = {"GBGB": obj.gigatogiga(), "GBMB": obj.gigatomega(), "GBKB": obj.gigatokilo(), "GBByte": obj.gigatobyte(),
                     "MBGB": obj.megatogiga(), "MBMB": obj.megatomega(), "MBKB": obj.megatokilo(), "MBByte": obj.megatobyte(),
                     "KBGB": obj.kilotogiga(), "KBMB": obj.kilotomega(), "KBKB": obj.kilotokilo(), "KBByte": obj.kilotobyte(),
                     "ByteGB": obj.bytetogiga(), "ByteMB": obj.bytetomega(), "ByteKB": obj.bytetokilo(), "ByteByte": obj.bytetobyte()}
        result4 = dict_mass[selected]
        text_output.set(result4)

    def clicked():
        try:
            assert text_input.get().count(".") == 1 or text_input.get().isdigit()
            btnEqualsInput()
        except:
            if "," in text_input.get():
                messagebox.showerror("Error", "Please Use '.' instead ','")
            else:
                messagebox.showerror("Error", "Please input number only!")
            text_input.set("")

    def button_delete():
        global string4
        text = string4[:-1]
        string4 = text
        text_input.set(text)

    def sign_change():
        global string4
        if string4[0] == "-":
            temp = string4[1:]
        else:
            temp = "-"+string4
        string4 = temp
        text_input.set(temp)

    # Create buttons
    btn7 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=3, column=0, sticky="nsew")
    btn8 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=3, column=1, sticky="nsew")
    btn9 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=3, column=2, sticky="nsew")
    delete_one = tk.Button(tab, padx=3, bd=5, fg="black", font=('arial', 20, 'bold'),
                           text='X', bg='powder blue', command=lambda: button_delete()).grid(row=3, column=3, sticky="nsew")
    btn4 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=4, column=0, sticky="nsew")
    btn5 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=4, column=1, sticky="nsew")
    btn6 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=4, column=2, sticky="nsew")
    btnClear = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                         text='C', bg='powder blue', command=lambda: btnClearDisplay()).grid(row=4, column=3, sticky="nsew")
    btn1 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=5, column=0, sticky="nsew")
    btn2 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=5, column=1, sticky="nsew")
    btn3 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=5, column=2, sticky="nsew")
    signs = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="\u00B1", bg='powder blue', command=lambda: sign_change()).grid(row=5, column=3, sticky="nsew")
    btn0 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=6, column=0, sticky="nsew")
    point = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text='.', bg='powder blue', command=lambda: btnClick(".")).grid(row=6, column=1, sticky="nsew")
    btnEquals = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                          text='=', bg='powder blue', command=clicked).grid(row=6, columnspan=2, column=2, sticky="nsew")
    return tab

# 5. Tab untuk Decimal


def dec_tab(tab_frame):
    # Initiate a Tab
    tab = ttk.Frame(tab_frame, height=100, width=100, style='color1.TFrame')
    text_input = tk.StringVar()
    text_output = tk.StringVar()
    combo_input = tk.StringVar()
    combo1_input = tk.StringVar()
    set_satuan1 = ("Decimal", "Binary", "Hexa", "Octal")
    set_satuan2 = ("Decimal", "Binary", "Octal", "Hexa")

    text_display_inp = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_input,
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)
    text_display_out = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_output, state='disabled',
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)

    combo = ttk.Combobox(
        tab,
        values=set_satuan1,
        textvariable=combo_input,
        state='readonly',
    )
    combo.current(0)  # set the selected item
    combo.grid(column=2, row=0)

    combo1 = ttk.Combobox(
        tab,
        values=set_satuan2,
        textvariable=combo1_input,
        state='readonly'
    )
    combo1.current(0)  # set the selected item
    combo1.grid(column=2, row=1)

    # List of Functions
    def btnClick(numbers):
        global string5
        string5 += str(numbers)
        text_input.set(string5)

    def btnClearDisplay():  # Function for "C" button
        global string5
        string5 = ''  # Reset operator
        text_input.set(string5)  # Reset TextBox
        text_output.set(string5)

    def btnEqualsInput():  # Function for "=" button
        global result5, string5
        selected = str(combo_input.get()) + str(combo1_input.get())
        list_mass = ["DecimalDecimal", "DecimalBinary", "DecimalOctal", "DecimalHexa",
                     "BinaryDecimal", "BinaryBinary", "BinaryOctal", "BinaryHexa",
                     "HexaDecimal", "HexaBinary", "HexaOctal", "HexaHexa",
                     "OctalOctal", "OctalBinary", "OctalDecimal", "OctalHexa"]
        if selected in list_mass:
            obj = NumberSysConverter()
            result5 = obj.selectFunc(text_input.get(), selected)
        text_output.set(result5)

    def clicked():

        cond1 = text_input.get().count(".") == 1
        cond2 = text_input.get().isdigit()
        cond3 = all(c in string.hexdigits for c in text_input.get())
        try:
            assert cond1 or cond2 or cond3
            btnEqualsInput()
        except:
            if "," in text_input.get():
                messagebox.showerror("Error", "Please Use '.' instead ','")
            else:
                messagebox.showerror(
                    "Error", "Please input decimal, binary, hexadecimal or octal instead!")
            text_input.set("")

    def button_delete():
        global string5
        text = string5[:-1]
        string5 = text
        text_input.set(text)

    def sign_change():
        global string5
        if string5[0] == "-":
            temp = string5[1:]
        else:
            temp = "-"+string5
        string5 = temp
        text_input.set(temp)

    def btnClick(char):
        global string5
        string5 += str(char)
        text_input.set(string5)

    # Create buttons
    btn7 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=3, column=0, sticky="nsew")
    btn8 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=3, column=1, sticky="nsew")
    btn9 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=3, column=2, sticky="nsew")
    delete_one = tk.Button(tab, padx=3, bd=5, fg="black", font=('arial', 20, 'bold'),
                           text='X', bg='powder blue', command=lambda: button_delete()).grid(row=3, column=3, sticky="nsew")
    btn4 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=4, column=0, sticky="nsew")
    btn5 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=4, column=1, sticky="nsew")
    btn6 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=4, column=2, sticky="nsew")
    btnClear = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                         text='C', bg='powder blue', command=lambda: btnClearDisplay()).grid(row=4, column=3, sticky="nsew")
    btn1 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=5, column=0, sticky="nsew")
    btn2 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=5, column=1, sticky="nsew")
    btn3 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=5, column=2, sticky="nsew")
    signs = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="\u00B1", bg='powder blue', command=lambda: sign_change()).grid(row=5, column=3, sticky="nsew")
    btn0 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=6, column=0, sticky="nsew")
    point = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text='.', bg='powder blue', command=lambda: btnClick(".")).grid(row=6, column=1, sticky="nsew")
    btna = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='a', bg='powder blue', command=lambda: btnClick("a")).grid(row=6, column=2, sticky="nsew")
    btnb = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='b', bg='powder blue', command=lambda: btnClick("b")).grid(row=6, column=3, sticky="nsew")
    btnc = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='c', bg='powder blue', command=lambda: btnClick("c")).grid(row=7, column=0, sticky="nsew")
    btnd = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='d', bg='powder blue', command=lambda: btnClick("d")).grid(row=7, column=1, sticky="nsew")
    btne = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='e', bg='powder blue', command=lambda: btnClick("e")).grid(row=7, column=2, sticky="nsew")
    btnf = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='f', bg='powder blue', command=lambda: btnClick("f")).grid(row=7, column=3, sticky="nsew")
    btnEquals = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                          text='=', bg='powder blue', command=clicked).grid(row=8, columnspan=4, column=0, sticky="nsew")
    return tab

# 6. Tab untuk Panjang


def length_tab(tab_frame):
    # Initiate a Tab
    tab = ttk.Frame(tab_frame, height=100, width=100, style='color1.TFrame')
    text_input = tk.StringVar()
    text_output = tk.StringVar()
    combo_input = tk.StringVar()
    combo1_input = tk.StringVar()
    set_satuan = ("Mil", "Km", "Yard", "Meter")

    text_display_inp = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_input,
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)
    text_display_out = tk.Entry(tab, font=("sans-serif", 16, "bold"), textvariable=text_output, state='disabled',
                                bd=3, insertwidth=3, bg='powder blue', justify='right').grid(columnspan=2, padx=5, pady=8)

    combo = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo_input,
        state='readonly',
    )
    combo.current(0)  # set the selected item
    combo.grid(column=2, row=0)

    combo1 = ttk.Combobox(
        tab,
        values=set_satuan,
        textvariable=combo1_input,
        state='readonly'
    )
    combo1.current(0)  # set the selected item
    combo1.grid(column=2, row=1)

    # List of Functions
    def btnClick(numbers):
        global string6
        string6 += str(numbers)
        text_input.set(string6)

    def btnClearDisplay():  # Function for "C" button
        global string6
        string6 = ''  # Reset operator
        text_input.set(string6)  # Reset TextBox
        text_output.set(string6)

    def btnEqualsInput():  # Function for "=" button
        global result6, string6
        selected = str(combo_input.get()) + str(combo1_input.get())
        if text_input.get().isdigit():
            obj = LengthConverter(int(text_input.get()))
        else:
            obj = LengthConverter(float(text_input.get()))
        dict_mass = {"MilMil": obj.miltomil(), "MilKm": obj.miltokm(), "MilYard": obj.miltoyard(), "MilMeter": obj.miltom(),
                     "KmKm": obj.kmtokm(), "KmMil": obj.kmtomil(), "KmYard": obj.kmtoyard(), "KmMeter": obj.kmtom(),
                     "YardYard": obj.yardtoyard(), "YardKm": obj.yardtokm(), "YardMil": obj.yardtomil, "YardMeter": obj.yardtom(),
                     "MeterMeter": obj.mtom(), "MeterMil": obj.mtomil(), "MeterKm": obj.mtokm(), "MeterYard": obj.mtoyard()}
        result6 = dict_mass[selected]
        text_output.set(result6)

    def clicked():
        try:
            assert text_input.get().count(".") == 1 or text_input.get().isdigit()
            btnEqualsInput()
        except:
            if "," in text_input.get():
                messagebox.showerror("Error", "Please Use '.' instead ','")
            else:
                messagebox.showerror("Error", "Please input number only!")
            text_input.set("")

    def button_delete():
        global string6
        text = string6[:-1]
        string6 = text
        text_input.set(text)

    def sign_change():
        global string6
        if string6[0] == "-":
            temp = string6[1:]
        else:
            temp = "-"+string6
        string6 = temp
        text_input.set(temp)

    # Create buttons
    btn7 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=3, column=0, sticky="nsew")
    btn8 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=3, column=1, sticky="nsew")
    btn9 = tk.Button(tab, padx=3, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=3, column=2, sticky="nsew")
    delete_one = tk.Button(tab, padx=3, bd=5, fg="black", font=('arial', 20, 'bold'),
                           text='X', bg='powder blue', command=lambda: button_delete()).grid(row=3, column=3, sticky="nsew")
    btn4 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=4, column=0, sticky="nsew")
    btn5 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=4, column=1, sticky="nsew")
    btn6 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=4, column=2, sticky="nsew")
    btnClear = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                         text='C', bg='powder blue', command=lambda: btnClearDisplay()).grid(row=4, column=3, sticky="nsew")
    btn1 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=5, column=0, sticky="nsew")
    btn2 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=5, column=1, sticky="nsew")
    btn3 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=5, column=2, sticky="nsew")
    signs = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="\u00B1", bg='powder blue', command=lambda: sign_change()).grid(row=5, column=3, sticky="nsew")
    btn0 = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=6, column=0, sticky="nsew")
    point = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text='.', bg='powder blue', command=lambda: btnClick(".")).grid(row=6, column=1, sticky="nsew")
    btnEquals = tk.Button(tab, padx=5, bd=8, fg="black", font=('arial', 20, 'bold'),
                          text='=', bg='powder blue', command=clicked).grid(row=6, columnspan=2, column=2, sticky="nsew")
    return tab


# Window program
def window_program(calc):
    calc.mainloop()  # Run cal object with all settings : )
