from random import randint, choice
from config import *
import json

def gen_passwd(len = 8, nums = True, symbols = True, upper = True, lower = True):
    password = ""
    symbols_for_password = []
    if nums:
        symbols_for_password.extend(numbers)
    if symbols:
        symbols_for_password.extend(symbols_list)
    if upper:
        symbols_for_password.extend(upper_letters)
    if lower:
        symbols_for_password.extend(letters)
    for _ in range(len):
        password += choice(symbols_for_password)
        
    return password

def saved_passwords_to_file(login,password, site):
    try:
        with open("saved_passwords.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {site:{}}
    
    logpass = {login:password}
    data[site] = logpass
    
    with open("saved_passwords.json", "w") as f:
        json.dump(data, f, indent=4)
        
def get_saved_passwords(site):
    try:
        with open("saved_passwords.json", "r") as f:
            data = json.load(f)
        result = data[site]
    except FileNotFoundError:
        result = None
    return result
    

