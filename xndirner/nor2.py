def get_sub_list(mlist,cnt):
    mlist.sort()
    return mlist[:cnt]
#print(get_sub_list([24,35,4,76,3],2))

def my_max(*args):
    lis = []
    for i in args:
        lis.append(i)
        for j in lis:
            if j > lis[0]:
                d = j
    return d
#print(my_max(12,23,45,7))

def is_polindrom(mstr):
    return mstr == mstr[::-1]
print(is_polindrom("bob"))
