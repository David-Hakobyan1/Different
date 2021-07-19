#FUNCTION: open_file, filtered_files, filter_lis, end_func, main

def open_file():
    #open filerss.txt in f and return for reading
    with open("filerss.txt") as f:
        return f.read().strip()

def filtered_files(files):
    #filterer file and return list
    l=[]
    s = files.split('\n')
    for i in s:
        l.append(i.split(" "))
    return l

def filter_lis(lis):
    #sorted list return min and max word
    l=[]
    for i in lis:
        for j in i:
            l.append(j)
    s=sorted(l,key=len)
    n = s[0]
    p=s[-1]
    return [n,p]

def end_func(ft,st):
    #swap minimum(Word) and maximum(Word),return text
    minimums = ft[0]
    maximums = ft[1]
    s = ""
    for i in st:
        for j in i:
            if minimums == j:
                s +=" "+ maximums
            elif maximums == j:
                s +=" "+ minimums
            else:
                s+=" "+j
    print(s.strip())

def main():
    #function call
    files = open_file()
    print(files)
    f_f = filtered_files(files)
    fl = filter_lis(f_f)
    ends = end_func(fl,f_f)

#check main
if __name__ == "__main__":
    main()
