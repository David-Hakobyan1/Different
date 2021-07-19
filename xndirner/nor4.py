# 4 ev avel tarer unecox barer@ )))

def get_content():
    with open("files.txt") as f:
        return f.readlines()

def filter_list(mlist):
    lis=[ el.replace("\n","")for el in mlist if el.replace("\n","")]
    st = ""
    lis=str(lis)
    for el in lis:
        if el.isalpha() or el==" ":
            st+=el
    st1=st.split(" ")
    for i in st1:
        if len(i)>=4:
            f=open("filers.txt","a")
            fc=f.write(i+",")
            print(i)
    f.close()
def main():
    ml = get_content()
    filtered_list = filter_list(ml)
main()
