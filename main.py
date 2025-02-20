def login():
    name = input("Enter your name: ")
    with open("base.txt", "r") as a:
        content = a.read()
        if name in content:
            password = input("Enter your password: ")
            comb = f"{name}:{password}"
            if comb in content:
                print(f"Привет, {name}")
                exit()
            else:
                print("Неверный пароль")
        else:
            print("Имени не существует!")
            exit()
def register():
    name = input("Enter your name: ")
    a = open("base.txt", "r")
    if name in a.read():
        print("Имя уже существует!")
        exit()
    else:
        print("Important: you can create random password\n(enter random)")
        password = input("Enter your password: ")
        if password == "random":
            import random
            password = "".join([random.choice("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890;$#~!?") for _ in range(random.randint(8,16))])
            print(f"Your new password: {password}")
        comb = f"{name}:{password}"
        x = open("base.txt", "a")
        x.write(f"{comb}\n")
while True:
    select = input("Enter login or register: ")
    select2 = select.lower()
    select3 = select2.replace(" ", "")
    if select3 == "register": register()
    elif select3 == "login": login()
    else:
        print("Произошла ошибка.")
        exit()
