class Mashina():
    def __init__(self, anun, model, taretiv,):
        self.anun = anun
        self.model = model
        self.taretiv = taretiv
        
    def guyn(self,guyn):
        self.guyn = guyn
        print("guyn - {}:".format(self.guyn))
    
    def tvyalner(self):
        print("anun - {}: model - {}: taretiv - {}:".format(self.anun,self.model,self.taretiv))
    
    def sharjich(self,hzorutyun):
        self.hzorutyun = hzorutyun
        print("hzorutyun - {} dziauj:".format(self.hzorutyun))

n1 = Mashina("bmw","e200",2000)
n1.tvyalner()
n1.guyn("spitak")
n1.sharjich(200)
