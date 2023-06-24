class car:
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year

    def display(self):
        print(self.modelname,self.year)


c1=car('Fortuner :',2023)
c1.display()
c2=car('Thar     :',2022)
c2.display()
c3=car('Verna    :',2021)
c3.display()
