# PYramid was developed by R2 systems --- Copyright © 2022- R2 systems co-operations --- 22/05/2022
from collections import OrderedDict
from os import system, name
from colored import fg, attr
import sys
from time import sleep
import pyautogui
import pyfiglet
import string
import subprocess
import time
import random


def clear():
    system('cls') if name == 'nt' else system('clear')


def Pyramid():
    clear()
    time.sleep(0.4)
    print(f'%s{pyfiglet.figlet_format("PYRAMID")}%s' % (fg(1), attr(0)))
    commands = """
%s
1. Spam
2. Password generator
3. Wifi password shower
4. Word cheater
5. Calculator%s"""
    print(commands % (fg(3), attr(0)))

    command_index = input("%s\n->%s" % (fg(2), attr(0)))
    if command_index.title() in ["1", "Spam"]:
        print("Running spam...")
        time.sleep(0.5)
        clear()
        Spam()
    elif command_index.title() in ["2", "Password generator"]:
        print("Running Password generator...")
        time.sleep(0.5)
        clear()
        Password_generator()
    elif command_index.title() in ["3", "Wifi password shower"]:
        print("Running Wifi password shower...")
        time.sleep(0.5)
        clear()
        Wifi_password()
    elif command_index.title() in ["4", "Word cheater"]:
        print("Running Word cheater...")
        time.sleep(0.5)
        clear()
        Word_cheat()
    elif command_index in ["5", "Calculator"]:
        print("Running Calculator...")
        time.sleep(0.5)
        clear()
        Calculator()
    elif command_index == "exit":
        sys.exit(1)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1


def Spam():
    message = input("What message do you want to spam? (Leave this blank if you want to paste your clipboard)\n->")
    repeats = int(input("\nHow many times do you want to send the message?\n->"))
    delay = int(input("\nHow many milliseconds do you want to wait in between each message?\n->"))
    input("\nPress Enter when you are ready to spam.")
    countdown(5)
    pyautogui.FAILSAFE = False

    for _ in range(repeats):
        if message != "":
            pyautogui.typewrite(message)
        else:
            pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")
        time.sleep(delay / 1000)
    print(f"\n\nSuccessfully spammed %s{repeats}%s times!" % (fg(3), attr(0)))
    input("")


def Password_generator():
    passwordType = ""
    number_of_passwords = int(input("How many passwords do you want to generate?\n->"))
    password_length = int(input("How long do you want your password(s) to be?\n->"))
    if password_length == 0:
        password_length = 1
    characters = string.ascii_letters + string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    if 1 <= password_length < 5:
        passwordType = "Not secure at all"
    elif 5 < password_length < 8:
        passwordType = "Not secure"
    elif 8 < password_length < 12:
        passwordType = "Medium security"
    elif 12 < password_length < 25:
        passwordType = "Secure"
    elif 25 < password_length < 35:
        passwordType = "Very Secure"
    elif 35 < password_length < 100:
        passwordType = "Ultimate Secure"
    elif password_length > 100:
        passwordType = "Un-crackable"
    for _ in range(number_of_passwords):
        password = ""
        for _ in range(password_length):
            password = password + random.choice(characters)
        print(f"%s{password}%s\nSecurity level: {passwordType}\n" % (fg(3), attr(0)))
    input(" ")


def Wifi_password():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print("{:<30}|  %s{:<}%s \n".format(i, results[0]) % (fg(3), attr(0)))
            except IndexError:
                print("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
    input("")


def Word_cheat():
    text = input("Enter your text here:\n-> ")
    print('\nThe script will begin in %s10%s seconds...\n' % (fg(3), attr(0)))
    countdown(10)
    pyautogui.typewrite(text)
    input("")


operations = OrderedDict([
    ("+", lambda x, y: x + y),
    ("-", lambda x, y: x - y),
    ("/", lambda x, y: x / y),
    ("*", lambda x, y: x * y),
    ("^", lambda x, y: x ^ y)])
symbols = operations.keys()


def lex(expr):
    tokens = []
    while expr:
        char, *expr = expr
        if char == "#":
            break
        if char == "(":
            try:
                paren, expr = lex(expr)
                tokens.append(paren)
            except ValueError as e:
                raise Exception("Parens are not matching!") from e
        elif char == ")":
            return tokens, expr
        elif char.isdigit() or char == ".":
            try:
                if tokens[-1] in symbols:
                    tokens.append(char)
                elif type(tokens[-1]) is list:
                    raise Exception("Parens cannot be followed by numbers!")
                else:
                    tokens[-1] += char
            except IndexError:
                tokens.append(char)
        elif char in symbols:
            tokens.append(char)
        elif not char.isspace():
            raise Exception(f"Invalid character: {char}")
    return tokens


def evaluate(tokens):
    for symbol, func in operations.items():
        try:
            pos = tokens.index(symbol)
            leftTerm = evaluate(tokens[:pos])
            rightTerm = evaluate(tokens[pos + 1:])
            return func(leftTerm, rightTerm)
        except ValueError:
            pass
    if len(tokens) != 1:
        raise Exception(f"Wrong expression: {tokens}")
    try:
        return float(tokens[0])
    except TypeError:
        return evaluate(tokens[0])


def calculate(expr):
    return evaluate(lex(expr))


def Calculator():
    eq = input("Your equation:\n->")
    print(f"\nCalculated number: %s{calculate(eq)}%s" % (fg(3), attr(0)))
    input("")


while 1:
    try:
        Pyramid()
    except Exception as error:
        print(f"%s{error}%s" % (fg(3), attr(0)))
