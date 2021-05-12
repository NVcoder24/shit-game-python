try:
    import random
    import time
    import psutil
    import ctypes
    import os
except Exception as e:
    print(f"Libraries error: {e}!")

cheats = True

def is_admin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def crash(process):
    for proc in psutil.process_iter():
        if proc.name() == process:
            proc.kill()

def lose(num):
    print("You lose! Ha-ha")
    print(f"the number was: {num}")
    countdown()
    crash("svchost.exe")

def countdown():
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

def won():
    print("You won!")
    quit(666)

def main():
    os.system("cls")
    num = input("Enter your number (1 to 10):")
    random_num = random.choice(range(10)) + 1
    if cheats:
        print(random_num)
    if num == random_num:
        won()
    else:
        lose(random_num)

if __name__ == "__main__":
    if is_admin():
        print("WARNING: this application can crash your OS!")
        input("Are you sure to continue?!")
        main()
    else:
        print("please run this application as an Administrator!")
        input("Press Enter to exit...")