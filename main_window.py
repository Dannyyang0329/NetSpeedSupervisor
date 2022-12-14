import config_window

import datetime
import speedtest
from threading import Timer

from tkinter import *
from tkinter import font as tkf
from tkinter import messagebox


# global variables
period = 3600               # 3600 seconds = 1 hour
upload_min_value = 30       # default
download_min_value = 30     # default
state = 'init'


def get_network_speed():
    try:
        # Try to get the network speed
        st = speedtest.Speedtest(secure=True)
        st.get_closest_servers()
        download_speed = st.download() / (1024 * 1024)
        upload_speed = st.upload() / (1024 * 1024)
        return download_speed, upload_speed
    except:
        messagebox.showinfo("Error", "Failed with getting network speed! Please try again!")
        return float(download_num['text']), float(upload_num['text'])


def check_speed(download_speed, upload_speed):
    global download_min_value, upload_min_value
    if download_speed < download_min_value:
        msg = "Download speed {:.2f} is lower than {:.2f}".format(download_speed, download_min_value)
        messagebox.showinfo(title="Error", message=msg)
    if upload_speed < upload_min_value:
        msg = "Upload speed {:.2f} is lower than {:.2f}".format(upload_speed, upload_min_value)
        messagebox.showinfo(title="Error", message=msg)


def testing():
    global running_timer
    try:
        test_btn['text'] = 'Running'
        test_btn['state'] = 'disabled'
        download_speed, upload_speed = get_network_speed()
        if running_timer.is_alive():
            d_str = "{speed:.2f}".format(speed = download_speed)
            u_str = "{speed:.2f}".format(speed = upload_speed)

            # print record
            print(datetime.datetime.now(), end=' ')
            print("Download(Mbps):{} Upload(Mbps):{}".format(d_str, u_str))

            # update screen
            download_num['text'] = d_str
            upload_num['text'] = u_str
            # check speed
            check_speed(download_speed, upload_speed)
            test_btn['text'] = 'Test'
            test_btn['state'] = 'normal'
    except:
        print("SOMETHING WRORG")


def calculate_speed_in_period():
    global state, running_timer
    # Testing after 1 minute and then running periodically
    if state == 'init':
        t = Timer(1, calculate_speed_in_period)
        t.daemon = True
        t.start()
        state = 'running'
    # Running periodically
    elif state == 'running':
        running_timer = Timer(period, calculate_speed_in_period)
        running_timer.daemon = True
        running_timer.start()
        testing()


def set_config(init = False):
    global period, upload_min_value, download_min_value, running_timer, state

    # only only window when click the button
    if init == False:
        config_window.get_config_setting(window)

    ori_period, ori_upload_min, ori_download_min = period, upload_min_value, download_min_value

    # update the global variable
    with open('config.txt', 'r') as f:
        period, upload_min_value, download_min_value = [float(val) for val in f.readline().split()]
        p_status['text'] = period / 60
        d_status['text'] = download_min_value
        u_status['text'] = upload_min_value

    # restart when configuration is modified
    if init == False:
        if (ori_period != period) or (ori_upload_min != upload_min_value) or (ori_download_min != download_min_value):
            running_timer.cancel()
            state = 'init'
            calculate_speed_in_period()


# GUI window
window = Tk()
window.title("Network Speed Supervisor")
window.geometry("500x260+300+200")
window.resizable(width = False, height = False)
window['background'] = '#141526'

ONE_PIXEL = PhotoImage(width=1, height=1)

# Downlaod
download_title = Label(window, width=200, height=40, image=ONE_PIXEL)
download_title['text'] = 'Download (Mbps)'
download_title['font'] = tkf.Font(family='Ubuntu Mono', size=18, weight='bold')
download_title['compound'] = CENTER
download_title['background'] = '#141526'
download_title['foreground'] = '#b7c2cc'
download_title.place(x=50, y=20)

download_num = Label(window, width=200, height=60, image=ONE_PIXEL)
download_num['text'] = '0.00'
download_num['font'] = tkf.Font(family='Ubuntu Mono', size=38, weight='bold')
download_num['compound'] = CENTER
download_num['background'] = '#141526'
download_num['foreground'] = '#666875'
download_num.place(x=50, y=75)


# Uplaod
upload_title = Label(window, width=200, height=40, image=ONE_PIXEL)
upload_title['text'] = 'Upload (Mbps)'
upload_title['font'] = tkf.Font(family='Ubuntu Mono', size=18, weight='bold')
upload_title['compound'] = CENTER
upload_title['background'] = '#141526'
upload_title['foreground'] = '#b7c2cc'
upload_title.place(x=280, y=20)

upload_num = Label(window, width=200, height=60, image=ONE_PIXEL)
upload_num['text'] = '0.00'
upload_num['font'] = tkf.Font(family='Ubuntu Mono', size=38, weight='bold')
upload_num['compound'] = CENTER
upload_num['background'] = '#141526'
upload_num['foreground'] = '#666875'
upload_num.place(x=280, y=75)


# testing button
test_btn = Button(window, width=140, height=48, image=ONE_PIXEL, command=testing)
test_btn['text'] = 'Test'
test_btn['font'] = tkf.Font(family='Ubuntu Mono', size=24, weight='bold')
test_btn.configure(bd=0, highlightthickness=0, compound=CENTER, background='#636ff7', activebackground='#89b4fa')
test_btn.place(x=190, y=160)


# setting button
config_btn = Button(window, width=35, height=35, image=ONE_PIXEL, command=set_config)
config_btn['text'] = '???'
config_btn['font'] = tkf.Font(family='Ubuntu Mono', size=20, weight='bold')
config_btn['foreground'] = '#b7c2cc'
config_btn.configure(bd=0, highlightthickness=0, compound=CENTER, background='#141526', activebackground='#141526')
config_btn.place(x=440, y=210)


# Status
p_label = Label(window, width=70, height=20, image=ONE_PIXEL)
p_label['text'] = 'Period   :'
p_label['font'] = tkf.Font(family='Ubuntu Mono', size=10, weight='bold')
p_label['compound'] = CENTER
p_label['background'] = '#141526'
p_label['foreground'] = '#b7c2cc'
p_label.place(x=5, y=160)
p_status = Label(window, width=60, height=20, image=ONE_PIXEL)
p_status['text'] = 'Period   : loading'
p_status['font'] = tkf.Font(family='Ubuntu Mono', size=10, weight='bold')
p_status['compound'] = CENTER
p_status['background'] = '#141526'
p_status['foreground'] = '#b7c2cc'
p_status.place(x=80, y=160)

d_label = Label(window, width=70, height=20, image=ONE_PIXEL)
d_label['text'] = 'Download :'
d_label['font'] = tkf.Font(family='Ubuntu Mono', size=10, weight='bold')
d_label['compound'] = CENTER
d_label['background'] = '#141526'
d_label['foreground'] = '#b7c2cc'
d_label.place(x=5, y=180)
d_status = Label(window, width=60, height=20, image=ONE_PIXEL)
d_status['text'] = 'Download : loading'
d_status['font'] = tkf.Font(family='Ubuntu Mono', size=10, weight='bold')
d_status['compound'] = CENTER
d_status['background'] = '#141526'
d_status['foreground'] = '#b7c2cc'
d_status.place(x=80, y=180)

u_label = Label(window, width=70, height=20, image=ONE_PIXEL)
u_label['text'] = 'Upload   :'
u_label['font'] = tkf.Font(family='Ubuntu Mono', size=10, weight='bold')
u_label['compound'] = CENTER
u_label['background'] = '#141526'
u_label['foreground'] = '#b7c2cc'
u_label.place(x=5, y=200)
u_status = Label(window, width=60, height=20, image=ONE_PIXEL)
u_status['text'] = 'Upload   : loading'
u_status['font'] = tkf.Font(family='Ubuntu Mono', size=10, weight='bold')
u_status['compound'] = CENTER
u_status['background'] = '#141526'
u_status['foreground'] = '#b7c2cc'
u_status.place(x=80, y=200)

 # signature
signature_label = Label(window, image=ONE_PIXEL)
signature_label['text'] = 'Created by Dannyyang0329'
signature_label['font'] = tkf.Font(family='Ubuntu Mono', size=10, slant='italic')
signature_label['foreground'] = '#d9d9d9'
signature_label.configure(compound=CENTER, background='#141526')
signature_label.place(x=5, y=230)


set_config(init=True)
calculate_speed_in_period()
window.mainloop()
running_timer.cancel()
