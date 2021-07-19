# Parentheses )))
s = "9-(4+(74)+25-1)-1"

def parentheses_l_r(s):
    st = ""
    for i in range(len(s)):
        if i == 0:
            if ord(s[i]) == 40 and 48>ord(s[i+1]) or ord(s[i+1])>57:
                break
            elif ord(s[i]) != 40 and 47>ord(s[i]) or 57<ord(s[i]):
                break
        else:
            if s[i] == "(":
                if  s[i-1] != "+" and s[i-1] != "-" \
                    and s[i-1] != "*" and s[i-1] != "/":
                    break
                else:
                    if ord(s[i+1]) < 48 or ord(s[i+1])> 57:
                        break
                 
            if s[i] == ")":
                if i<len(s)-1:
                    if s[i+1] != "*" and s[i+1] != "+" and s[i+1] != "-"\
                        and s[i+1] != "/":
                            break
                    else:
                        if (ord(s[i-1])<48) or (ord(s[i-1])>57): 
                            break
                else:
                    break
        st+=s[i]
    return st
fg = parentheses_l_r(s)

def parentheses(fg):
    lis = []
    if len(fg)!=len(s):
        lis.append(9)
        return lis
    else:
        for i in fg:
            if i == "(" or i == ")":
                lis.append(i)
    return lis
lis1 = parentheses(fg)

def check_sheet(lis1):
    if lis1==9:
        return lis1
    else:
        i=0
        for j in range(len(lis1)):
            if i+1 < len(lis1):
                if lis1[i] == "(" and lis1[i+1] == ")":
                    lis1.pop(i)
                    lis1.pop(i)
                    check_sheet(lis1)
                i+=1
            else:
                return lis1
lis2 = check_sheet(lis1)

def my_answer(lis2):
    if len(lis2) == 0:
        return True
    return False
print(my_answer(lis2))

