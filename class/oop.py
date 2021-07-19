####################################################################
#CLASS: university
#FUNCTION: __init__,__repr__
#BRIEF:
#PARAMS: (self,name,data,address)-gets name data address parameters
#OUTPUT:
#RETURN: self.name,self.data,self.address
####################################################################
class university():
    def __init__(self,name,data,address):
        self.name = name
        self.data = data
        self.address = address
    
    def __repr__(self):
         return self.name+","+str(self.data)+","+self.address


#create objects
SHPH = university("Shiraki petakan hamalsaran",1934,"Qaxaq Gyumri Paruyr Sevak 4")
HBI = university("Haykakan bjshkakan institut",1990,"Qaxaq Erevan Titogradyan 14")
HAPH = university("Hayastani azgayin politexnik hamalsaran",1933,"Qaxaq Erevan Teryan 105")
HAH = university("Hayastani amerikyan hamalsaran",1991,"Qaxaq Erevan Marshal Baghramyan 40")
EVBAAH = university("Erevani Valeri Bryusovi anvan azgayin hamalsaran",1935,"Qaxaq Erevan Tumanyan 42")
EPH = university("Erevani petakan hamalsaran",1919,"Qaxaq Erevan Alek Manukyan 1")
HRH = university("Hay-Rusakan hamalsaran",1997,"Qaxaq Erevan Hovsep Emin 123")
HFH = university("Hyastanum Fransiakan hamalsaran",2000,"Qaxaq Erevan Davit Anhaght 10")
HAMH = university("Hay azgayin mankavarjakan hamalsaran",1922,"Qaxaq Erevan Tigran Mec 17")
EABH = university("Erevani azgayin bjshkakan hamalsaran",1920,"Qaxaq Erevan Koryun 2")

#add university objects to the list
def filter_list(l):
    lis=[]
    for i in l:
        lis.append(str(i).split(","))
    return lis


#sorting by name or year or address,and displaying
def sort_n_d_a(filtered_list):
    n = int(input('Sort name (1),Sort data (2), sort address (3): '))
    n = int(n)-1
    filtered_list.sort(key=lambda i: i[n])
    for i in filtered_list:
        print("%s %d %s" % (i[0],int(i[1]),i[2]))


#function call
def main():
    l=[SHPH,HBI,HAPH,HAH,EVBAAH,EPH,HRH,HFH,HAMH,EABH]
    filtered_list = filter_list(l)
    sorts = sort_n_d_a(filtered_list)


#validation main
if __name__=="__main__":
    main()
