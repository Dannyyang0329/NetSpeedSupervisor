from tkinter import *
from tkinter import font as tkf
from tkinter import messagebox
from functools import partial

def save_config(p_text, u_text, d_text):
    try:
        # get user's input in text box
        pt = p_text.get("1.0", "end-1c")
        ut = u_text.get("1.0", "end-1c")
        dt = d_text.get("1.0", "end-1c")
        # check input is valid or not
        p_val = float(pt)
        u_val = float(ut)
        d_val = float(dt)

        # save the setting if values are valid
        with open('config.txt', 'w') as f:
            tmp = str(p_val * 60) + " " + ut + " " + dt
            f.write(tmp)
    except:
        messagebox.showinfo("Error", "Value is invalid")


def get_config_setting(window):
    global setting_window

    # open sub window for setting
    setting_window = Toplevel()
    setting_window.title('Setting')
    setting_window.geometry('460x245+320+220')
    setting_window.resizable(width=False, height=False)
    setting_window['background'] = '#141526'

    ONE_PIXEL = PhotoImage(width=1, height=1)

    # period
    p_title = Label(setting_window, width=270, height=40, image=ONE_PIXEL)
    p_title['text'] = 'Period (minute)'
    p_title['font'] = tkf.Font(family='Ubuntu Mono', size=16, weight='bold')
    p_title['compound'] = CENTER
    p_title['background'] = '#141526'
    p_title['foreground'] = '#b7c2cc'
    p_title.place(x=25, y=20)

    p_text = Text(setting_window, width=8, height=1)
    p_text['font'] = tkf.Font(family="Ubuntu Mono", size=16)
    p_text.place(x=330, y=30)


    # upload limit
    u_title = Label(setting_window, width=270, height=40, image=ONE_PIXEL)
    u_title['text'] = 'Upload min speed (Mbps)'
    u_title['font'] = tkf.Font(family='Ubuntu Mono', size=16, weight='bold')
    u_title['compound'] = CENTER
    u_title['background'] = '#141526'
    u_title['foreground'] = '#b7c2cc'
    u_title.place(x=25, y=60)

    u_text = Text(setting_window, width=8, height=1)
    u_text['font'] = tkf.Font(family="Ubuntu Mono", size=16)
    u_text.place(x=330, y=70)


    # download limit
    d_title = Label(setting_window, width=270, height=40, image=ONE_PIXEL)
    d_title['text'] = 'Download min speed (Mbps)'
    d_title['font'] = tkf.Font(family='Ubuntu Mono', size=16, weight='bold')
    d_title['compound'] = CENTER
    d_title['background'] = '#141526'
    d_title['foreground'] = '#b7c2cc'
    d_title.place(x=25, y=100)

    d_text = Text(setting_window, width=8, height=1)
    d_text['font'] = tkf.Font(family="Ubuntu Mono", size=16)
    d_text.place(x=330, y=110)


    # save button
    save_btn = Button(setting_window, width=120, height=50, image=ONE_PIXEL, command=partial(save_config, p_text, u_text, d_text))
    save_btn['text'] = 'Save'
    save_btn['font'] = tkf.Font(family='Ubuntu Mono', size=24, weight='bold')
    save_btn.configure(bd=0, highlightthickness=0, compound=CENTER, background='#636ff7', activebackground='#89b4fa')
    save_btn.place(x=170, y=160)


    setting_window.transient(window)
    setting_window.grab_set()
    window.wait_window(setting_window)
