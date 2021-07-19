# Fayleri xndir )))
def my_file1():
    with open("file3.txt") as f:
        return f.read().strip()

def my_file2():
    with open("file4.txt") as f1:
        return f1.read().strip()

def filter_1(file1,file2):
    sd=file1.split("\n")
    ds=file2.split("\n")
    return sd,ds

def write_file(sd,ds):
    f = open("file5.txt","a")
    for i in range(len(sd)):
        if sd[i].isdigit() and ds[i].isdigit():
            c = int(sd[i]) + int(ds[i])
            f.write(str(c)+"\n")
        else:
            f.write("-"+"\n")
    f.close()            

def main():
    file1 = my_file1()
    file2 = my_file2()
    files,files1 = filter_1(file1,file2)
    dg = write_file(files,files1)
main()
