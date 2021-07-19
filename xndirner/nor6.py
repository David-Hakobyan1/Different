# barer@ voronq sksvum u verjanum en dzaynavornerov )))

fs = None
try:
    with open("file.txt") as f:
        f.readlines()
except FileNotFoundError as err:
    pass
if fs:
    print(fs)

def content():
    with open("file.txt") as f:
        return f.readlines()

def filter_list(mlist):
    return[el.replace("\n","")for el in mlist if el.replace("\n","")]

def main():
    vowels=("e","i","o","u","y","a")
    ml = content()
    filtered_list = filter_list(ml)
    filtered_list = str(filtered_list)
    st = ""
    for el in filtered_list:
        if el.isalpha() or el == " ":
            st+=el
    st1=st.split(" ")
    for i in st1:
        if i[0] in vowels and i[-1] in vowels:
            print(i)
main()
