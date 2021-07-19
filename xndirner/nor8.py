# Teqstum ogtagorcvac tvanshanneri gumar@ )))

fc = None
try:
    with open("fil.txt") as f:
        fc = f.readlines()
except FileNotFoundError as err:
    pass
if fc:
    pass
    #print(fc)

def get_content():
    with open("fil.txt") as f:
        return f.readlines()

def list_filter(mlist):
    return [el.replace("\n","") for el in mlist if el.replace("\n","")]

def move():
    ml = get_content()
    print(ml)
    filtered_list = list_filter(ml)
    filtered_list = str(filtered_list)
    e = 0
    for el in filtered_list:
        if el.isdigit():
            e+=int(el)
    print(e)
move()

