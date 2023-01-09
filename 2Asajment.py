import threading

class Kocka:
    def __init__(self,a):
        self.a=a

    def zapremina_kocke(self): 
        zapremina=self.a*self.a*self.a
        return zapremina

    def duzina_stranica(self): 
        duzina=self.a*12
        return duzina
        
        
if __name__ == "__main__":
   
    c=Kocka(5)
    
    t1 = threading.Thread(target=Kocka.zapremina_kocke, args=[c])
    
    t2 = threading.Thread(target=c.duzina_stranica) 
   
    t2.start() 
    t1.start() 

    t2.join() 
    t1.join()
    
print("Duzina svih stranica ako je a=5: ",c.duzina_stranica())
print("Zapremina kocke za duzinu 5: ",c.zapremina_kocke())
print("Zavrseno")
