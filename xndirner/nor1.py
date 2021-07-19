# Homework1 )))
#login = raw_input("Login: ")
#parol = raw_input("Parol: ")
d = {"user1":"pass1","user2":"pass2"}

def my_login(login):
    bol = True
    for i in d.keys():
        if login == i:
            bol = False
            print("duplicate login")
    return bol
#log=my_login(login)

def my_password(parol):
    bol = True
    for i in d.values():
        if parol == i:
            bol = False
            print("duplicate password")
    return bol
#pas=my_password(parol)

def stugum(log,pas):
    global d,login,parol
    if log and pas:
       d[login]=parol
    return d
#print(stugum(log,pas))

# Homework2 )))
b = [{"name":"bob","phone":357}]
while True:
    print(b)
    phone = int(input("Phone: "))
    name = raw_input("Name: ")
    def my_phone(phone):
        d = {}
        for i in range(len(b)):
            if phone == b[i]["phone"]:
                return "this number exists"
        d["name"]=name
        d["phone"]=phone
        b.append(d)
    my_phone(phone)


