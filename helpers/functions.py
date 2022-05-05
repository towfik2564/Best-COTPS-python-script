
import time
import socket
import pandas as pd

def formatted_time(t, hours = False):
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    if hours:
        return '{:d}:{:02d}:{:02d}'.format(h, m, s)
    else: 
        return '{:02d}:{:02d}'.format(m, s)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) 
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Waiting is over')

def validate_machine():
    machine_id = socket.gethostname()
    print(f"ID of this machine: {machine_id}")
    print('Validating machine license')
    sheet_url = "https://docs.google.com/spreadsheets/d/1JsEsTGr4BdVTKDg8ulJJewG81dcHb6WfzXiBbWkasNQ/edit#gid=0"
    url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
    column_name = "machine_id"
    list = pd.read_csv(url, names=[column_name])
    list = list[column_name].to_list()
    del list[0]
    if machine_id in list:
        return True
    else:
        return False
  