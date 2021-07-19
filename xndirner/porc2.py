a = ([('lname', u'Hakobyan'), ('login', u'ayos'), ('parol', u'iharke'), ('fname', u'David')])
try:
    login = open("textovil.txt", "w")
    parol = open("textovip.txt","w")
    try:
        login.write(a[1][1])
        parol.write(a[2][1])
    except Exception as e:
        print(e)
    finally:
        login.close()
        parol.close()
except Exception as ex:
    print(ex)



