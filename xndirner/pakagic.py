# Checking_brackets )))
st = "[(a,b),{3,7},{18:207},[1,7,10]]"
lis = []

def my_parentheses(st):
    for i in st:
        if  i == "(" or i == ")" or i == "{" \
            or i == "}" or i == "[" or i =="]":
            lis.append(i)
    return lis
lis1=my_parentheses(st)

def my_check(lis1):
    i = 0
    for j in range(len(lis1)):
        if i+1 < len(lis1):
            if  lis1[i] == "(" and lis1[i+1] == ")" \
                or lis1[i] == "{" and lis1[i+1] == "}" \
                or lis1[i] == "[" and lis1[i+1] == "]":
                lis1.pop(i)
                lis1.pop(i)
                my_check(lis1)
            i+=1
        else:
            return lis1
lis2=my_check(lis1)

def my_answer(lis2):
    if len(lis2) == 0:
        return True
    return False
print(my_answer(lis2))
     
