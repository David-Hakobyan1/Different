# ayn naxadasutyunner@ vortex ogtagorcvel e mutqagrvac bar@ )))
n = "in"
fs = None
try:
    with open("files.txt") as f:
        fs = f.readlines()
except FileNotFoundError as err:
    pass
if fs:
    print(fs)

def get_content():
    with open("files.txt") as f:
        return f.readlines()

def filter_list(mlist):
    return [el.replace("\n","") for el in mlist if el.replace("\n","")]

def main():
    ml = get_content()
    filtered_list = filter_list(ml)
    e = 0
    st = ""
    for i in range(len(filtered_list)):
        for j in filtered_list[i]:
            if n[e] != j:
                e=0
                st+=j
            else:
                e+=1
                if e==len(n):
                    e = 0
                    print(filtered_list[i])
                else:
                    st+=j
main()              


