def get_content(fname):
    with open(fname) as f:
        return f.read()

def separate_text(mstr):
    mstr = mstr.replace("!",".").replace("?",".").replace("\n","")
    return mstr.split(".")

def filter_long_list(ml):
    return [el for el in ml if len(el.split()) > 4]

def my_rev(sent):
    ml = [el[::-1] for el in sent.split()]
    return " ".join(ml)

def print_my_sentences(mlist):
    for el in mlist:
        print(my_rev(el))

def main():
    filename = "file1.txt"
    mstr =  get_content(filename)
    ml = separate_text(mstr)
    newl = filter_long_list(ml)
main()
