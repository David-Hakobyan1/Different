# Ogtagorcvac bareri qanak@ )))

def filter_list(mlist):
    lis=[el.replace("\n","")for el in mlist if el.replace("\n","")]
    lis = str(lis)
    st=""
    for el in lis:
        if el.isalpha() or el==" ":
            st+=el
    st1=st.split(" ")
    count = 0
    for i in st1:
        count += 1
    f=open("file.txt","w")
    fc=f.write(count)
    print(count)
    
def main():
    ml = get_content()
    filtered_list = filter_list(ml)
main()

