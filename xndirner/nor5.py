# Ogtagorcvac naxadasutyunneri qanak@ )))

fc = None
try:
    with open("files.txt") as f:
        fc = f.readlines()
except FileNotFoundError as err:
    pass
if fc:
    print(fc)

def get_content():
    with open("files.txt") as f:
        return f.readlines()

def filtered_list(mlist):
    return [el.count("\n") for el in mlist]

def main():
    ml = get_content()
    filter_list = filtered_list(ml)
    c = 0
    for i in filter_list:
        c+=int(i)
    print(c-1)
main()
