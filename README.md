# NetSpeedSupervisor

## Structure
```
.
├── config.txt
├── config_window.py
├── icon.ico
├── main_window.py
├── speedtest.py
└── Windows_Executable_Files
    ├── Files
    │   ├── config.txt
    │   ├── icon.ico
    │   └── main_window.exe
    └── main_window.exe.lnk

2 directories, 9 files
```

## Introduction
This is a network speed tracker. It can automatically test the download speed and upload speed periodically. If the testing speed is lower than your expectation, the program will notify you to let you know.

The testing period, expect upload speed and expect download speed can be set by yourself.

The unit of the parameters:
Period : minute
Upload : Mbps
Download : Mbps

## Usage
For windows user, there is a executable file `main_window.exe` in the Windows_Executable_File folder.

If you don't want to execute the program by executing exe file, you can execute main_window.py to start the program.

```
python main_window.py
```

To know more about speedtest, you can check this repository
https://github.com/sivel/speedtest-cli

## ScreenShots

* Main screen

    ![](https://i.imgur.com/ylfcDOo.png)

* Setting window

    ![](https://i.imgur.com/nD2tqYU.png)

* Error notification

    ![](https://i.imgur.com/VE4PFup.png)

* Record in terminal

    ![](https://i.imgur.com/zybnIs6.png)

