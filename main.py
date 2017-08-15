import threading
import time
import os
import subprocess
from time import localtime, strftime

from Tkinter import *  # Python 2
import ttk

# try:
#     from Tkinter import *  # Python 2
#     import ttk
# except ImportError:
#     from tkinter import *  # Python 3
#     import tkinter.ttk as ttk


def do_nothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def do_automate():
    textbox.insert('end', "*********************\n")
    textbox.see("end")
    textbox.insert('end', "  STARTING AUTOMATE  \n")
    textbox.see("end")
    textbox.insert('end', "*********************\n\n")
    textbox.see("end")
    lock_settings()
    configure_super_su()
    configure_date_time()
    configure_wifi()
    install_scala()
    install_dft_helper()
    install_system_bar_killer()
    install_boot_animation()
    textbox.insert('end', "*********************\n")
    textbox.see("end")
    textbox.insert('end', "  FINISHED AUTOMATE  \n")
    textbox.see("end")
    textbox.insert('end', "*********************\n")
    textbox.see("end")


def do_function(function):
    global t1
    t1 = threading.Thread(target=function, args=())
    t1.daemon = True
    progress_bar.start(20)
    t1.start()
    root.after(20, check_thread)


def check_thread():
    if t1.is_alive():
        root.after(20, check_thread)
    else:
        progress_bar.stop()


def lock_settings():
    textbox.insert('end', "Configuring Lock Settings\n")
    textbox.see("end")

    os.system('adb wait-for-device');
    os.system('adb shell input keyevent 3')

    textbox.insert('end', " Attempting to bring settings to the foreground.\n")
    textbox.see("end")
    secure_settings_cmp = 'com.android.settings/com.android.settings.SubSettings'
    secure_settings_extra_type = ':android:show_fragment'
    secure_settings_extra_string = 'com.android.settings.SecuritySettings'

    subprocess_command = [
        "adb", "shell", "am", "start",
        "-a", "android.intent.action.MAIN",
        "-n", secure_settings_cmp,
        "-e", secure_settings_extra_type, secure_settings_extra_string
    ]
    os.system('adb shell am force-stop com.android.settings')

    result = subprocess.check_output(subprocess_command, stderr=subprocess.STDOUT)
    textbox.insert('end', " [Debug] " + result.decode("utf-8") + "\n")
    textbox.see("end")

    textbox.insert('end', " Please wait while we tap away.\n")
    textbox.see("end")
    time.sleep(2)
    textbox.insert('end', " Setting screen off timeout to 2 minutes.\n")
    textbox.see("end")
    os.system(
        'adb shell sqlite3 data/data/com.android.providers.settings/databases/settings.db "update system set value=\'120000\' where name=\'screen_off_timeout\';"')
    time.sleep(2)
    # Verify Apps
    # textbox.insert('end', " *tap*\n")
    # textbox.see("end")
    # os.system('adb shell input tap 136 400')
    # time.sleep(2)
    textbox.insert('end', " *tap*\n")
    textbox.see("end")
    os.system('adb shell input tap 136 85')
    time.sleep(2)
    textbox.insert('end', " *tap*\n")
    textbox.see("end")
    os.system('adb shell input tap 136 60')
    time.sleep(1)
    textbox.insert('end', " Returning you to the home screen.\n")
    textbox.see("end")
    os.system('adb shell input keyevent 3')

    textbox.insert('end', "Finished configuring Lock Settings.\n\n")
    textbox.see("end")
    return


def configure_super_su():
    textbox.insert('end', "Configuring Super Su\n")
    textbox.see("end")

    os.system('adb wait-for-device');
    os.system('adb shell input keyevent 3')

    # The following will attempt to push supersu settings.

    textbox.insert('end', " Attempting to bring Super Su to the foreground.\n")
    textbox.see("end")
    cmp = 'eu.chainfire.supersu.MainActivity'
    fullCmpStr = str.rsplit(cmp, '.', 1)[0] + '/' + cmp

    os.system('adb shell am force-stop eu.chainfire.supersu')
    time.sleep(1)

    subprocess_command = [
        "adb", "shell", "am", "start",
        "-a", "android.intent.action.MAIN",
        "-n", fullCmpStr
    ]
    result = subprocess.check_output(
        subprocess_command,
        stderr=subprocess.STDOUT
    )
    textbox.insert('end', " [Debug] " + result.decode("utf-8") + "\n")
    textbox.see("end")

    textbox.insert('end', " Please wait while we tap away.\n")
    textbox.see("end")
    time.sleep(4)
    textbox.insert('end', " *tap*\n")
    textbox.see("end")
    os.system('adb shell input tap 58 278')
    time.sleep(2)
    textbox.insert('end', " *tap*\n")
    textbox.see("end")
    os.system('adb shell input tap 230 55')
    time.sleep(2)
    textbox.insert('end', " *tap*\n")
    textbox.see("end")
    os.system('adb shell input tap 136  427')
    time.sleep(2)
    textbox.insert('end', " *tap*\n")
    textbox.see("end")
    os.system('adb shell input tap 136  229')
    time.sleep(2)
    textbox.insert('end', " *tap*\n")
    textbox.see("end")
    os.system('adb shell input tap 154  355')
    time.sleep(1)
    textbox.insert('end', " Returning you to the home screen.\n")
    textbox.see("end")
    os.system('adb shell input keyevent 3')

    textbox.insert('end', "Finished configuring Super Su.\n\n")
    textbox.see("end")
    return


def configure_date_time():
    textbox.insert('end', "Configuring Date Time\n")
    textbox.see("end")

    os.system('adb wait-for-device')
    cur_time = strftime("%Y%m%d.%H%M%S", localtime())

    textbox.insert('end', " Setting timezone to 'America/Chicago'\n")
    textbox.see("end")
    os.system('adb shell setprop persist.sys.timezone "America/Chicago"')

    textbox.insert('end', " Setting time to: " + cur_time + "\n")
    textbox.see("end")
    os.system('adb shell date -s %s' % cur_time)

    textbox.insert('end', "Finished configuring Date/Time.\n\n")
    textbox.see("end")
    return


def configure_wifi():
    textbox.insert('end', "Configuring WiFi\n")
    textbox.see("end")

    os.system('adb wait-for-device')
    cur_time = strftime("%Y%m%d.%H%M%S", localtime())
    # cti_location = "wifi_conf/wpa_supplicant.conf"
    sprint_location = "wifi_conf/wpa_supplicant_SENDev.conf"
    device_location = "/data/misc/wifi/wpa_supplicant.conf"

    textbox.insert('end', " Pushing wireless settings: " + cur_time + "\n")
    textbox.see("end")

    subprocess_command = ["adb", "push", sprint_location, device_location]
    result = subprocess.check_output(subprocess_command, stderr=subprocess.STDOUT)
    textbox.insert('end', " [Debug] " + result.decode("utf-8"))
    textbox.see("end")

    textbox.insert('end', "Finished configuring Date/Time.\n\n")
    textbox.see("end")
    return


def install_scala():
    textbox.insert('end', "Installing Scala\n")
    textbox.see("end")

    os.system('adb wait-for-device')

    textbox.insert('end', " Remounting /system with read/write capabilities.\n")
    textbox.see("end")
    os.system('adb shell mount -o remount,rw /system')

    textbox.insert('end', " Pushing scala player to system/app/\n")
    textbox.see("end")
    os.system('adb push apk/scala_player_07_14_14.apk /system/app')

    textbox.insert('end', "Finished installing Scala\n\n")
    textbox.see("end")
    return


def install_dft_helper():
    textbox.insert('end', "Installing DFT Helper\n")
    textbox.see("end")

    os.system('adb wait-for-device')

    cmp = 'com.cti.dfthelper.MainActivity'
    full_cmp_str = str.rsplit(cmp, '.', 1)[0] + '/' + cmp

    subprocess_command = ["adb", "install", "apk/DFTHelper_no_log.apk"]

    result = subprocess.check_output(subprocess_command, stderr=subprocess.STDOUT)
    textbox.insert('end', " [Debug] " + result.decode("utf-8"))
    textbox.see("end")

    textbox.insert('end', " Starting DFT Helper\n")
    textbox.see("end")
    os.system('adb shell am start -a android.intent.action.MAIN -n %s' % full_cmp_str)

    time.sleep(1)
    textbox.insert('end', " Returning you to the home screen.\n\n")
    textbox.see("end")
    os.system('adb shell input keyevent 3')

    textbox.insert('end', "Finished installing DFT Helper\n\n")
    textbox.see("end")
    return


def install_system_bar_killer():
    textbox.insert('end', "Installing System Bar Killer\n\n")
    textbox.see("end")

    os.system('adb wait-for-device')

    cmp = 'com.cti.systembarkiller.MainActivity'
    full_cmp_str = str.rsplit(cmp, '.', 1)[0] + '/' + cmp

    subprocess_command = ["adb", "install", "apk/SystemBarKiller.apk"]
    result = subprocess.check_output(subprocess_command, stderr=subprocess.STDOUT)
    textbox.insert('end', " [Debug] " + result.decode("utf-8"))
    textbox.see("end")

    textbox.insert('end', " Starting System Bar Killer\n")
    textbox.see("end")
    os.system('adb shell am start -a android.intent.action.MAIN -n %s' % full_cmp_str)

    time.sleep(1)
    textbox.insert('end', " Returning you to the home screen.\n")
    textbox.see("end")
    os.system('adb shell input keyevent 3')

    textbox.insert('end', "Finished installing System Bar Killer\n\n")
    textbox.see("end")
    return


def install_boot_animation():
    textbox.insert('end', "Installing new boot animation\n")
    textbox.see("end")

    os.system('adb wait-for-device')

    subprocess_command = ["adb", "push", "other/bootanimation.zip", "/system/media"]
    result = subprocess.check_output(subprocess_command, stderr=subprocess.STDOUT)
    textbox.insert('end', " [Debug] " + result.decode("utf-8"))
    textbox.see("end")

    textbox.insert('end', "Finished installing new boot animation\n\n")
    textbox.see("end")
    return


def install_ram():
    textbox.insert('end', "Installing Remote Android Manager (R.A.M.)\n")
    textbox.see("end")

    os.system('adb wait-for-device')

    cmp = 'com.ctisolutions.remoteandroidmanager.MainActivity'
    fullCmpStr = str.rsplit(cmp, '.', 1)[0] + '/' + cmp

    subprocess_command = ["adb", "install", "-r", "apk/RAM_client.apk"]
    result = subprocess.check_output(subprocess_command, stderr=subprocess.STDOUT)
    textbox.insert('end', " [Debug] " + result.decode("utf-8"))
    textbox.see("end")

    textbox.insert('end', " Attempting to start R.A.M. Client")
    textbox.see("end")
    os.system('adb shell am start -a android.intent.action.MAIN -n %s' % (fullCmpStr))

    time.sleep(1)
    textbox.insert('end', " Returning you to the home screen.\n")
    textbox.see("end")
    os.system('adb shell input keyevent 3')

    textbox.insert('end', "Finished installing Remote Android Manager (R.A.M.)\n\n")
    textbox.see("end")
    return


def configure_scala(location):
    textbox.insert('end', "Configuring Scala for " + location + "\n")
    os.system('adb wait-for-device')

    if "sprint" in location:
        os.system('adb shell input keyevent 20')
        os.system('adb shell input text http://scala.corp.sprint.com/ContentManager')
        os.system('adb shell input keyevent 20')
        os.system('adb shell input text player_Scala')
        os.system('adb shell input keyevent 20')
        os.system('adb shell input text sprint')
    else:
        os.system('adb shell input keyevent 20')
        os.system('adb shell input text http://192.168.1.103/ContentManager')
        os.system('adb shell input keyevent 20')
        os.system('adb shell input text administrator')
        os.system('adb shell input keyevent 20')
        os.system('adb shell input text ctiadmin')
    return


def get_mac_address():
    textbox.insert('end', "Exporting mac address\n")

    os.system('adb wait-for-device')

    textbox.insert('end', " Turning on wifi.\n")
    os.system("adb shell svc wifi enable")
    time.sleep(2)

    textbox.insert('end', " attempting to read mac address from device.\n")
    f = open('macs.csv', 'a')
    mac = os.popen('adb shell cat sys/class/net/wlan0/address').read()
    mac = mac.replace('\n', '')
    f.write(mac)
    f.close()

    textbox.insert('end', "Mac address: " + mac.decode("utf-8") + " has been appended to macs.csv\n\n")
    textbox.see("end")
    return


def create_window():
    menu_bar = Menu(root)

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    global textbox
    textbox = Text(root)
    textbox.pack()

    textbox.insert('end', "Before using any of the scripts please wake the device and unlock the screen!\n")

    textbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=textbox.yview)

    global progress_bar
    progress_bar = ttk.Progressbar(root, orient='horizontal', mode='indeterminate')
    progress_bar.pack(expand=True, fill=BOTH, side=TOP)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    script_menu = Menu(menu_bar, tearoff=0)
    script_menu.add_command(
        label="Automate",
        command=lambda: do_function(do_automate)
    )
    script_menu.add_separator()
    script_menu.add_command(
        label="Configure Lock Settings",
        command=lambda: do_function(lock_settings)
    )
    script_menu.add_command(
        label="Configure Super Su",
        command=lambda: do_function(configure_super_su)
    )
    script_menu.add_command(
        label="Configure Date Time",
        command=lambda: do_function(configure_date_time)
    )
    script_menu.add_command(
        label="Configure Wifi",
        command=lambda: do_function(configure_wifi)
    )
    script_menu.add_command(
        label="Install Scala",
        command=lambda: do_function(install_scala)
    )
    script_menu.add_command(
        label="Install DFT Helper",
        command=lambda: do_function(install_dft_helper)
    )
    script_menu.add_command(
        label="Install System Bar Killer",
        command=lambda: do_function(install_system_bar_killer)
    )
    script_menu.add_command(
        label="Install Boot Animation",
        command=lambda: do_function(install_boot_animation)
    )
    script_menu.add_command(
        label="Install Ram",
        command=lambda: do_function(install_ram)
    )
    script_menu.add_command(
        label="Configure Scala (Sprint)",
        command=lambda: do_function(configure_scala("sprint"))
    )
    script_menu.add_command(
        label="Configure Scala (CTI)",
        command=lambda: do_function(configure_scala("cti"))
    )
    script_menu.add_separator()
    script_menu.add_command(
        label="Get Mac Address",
        command=lambda: do_function(get_mac_address)
    )
    menu_bar.add_cascade(label="Run Script", menu=script_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=lambda: do_nothing())
    menu_bar.add_cascade(label="Help", menu=help_menu)

    root.config(menu=menu_bar)
    root.mainloop()


def Main():
    global root
    root = Tk()
    create_window()


if __name__ == '__main__':
    Main()
