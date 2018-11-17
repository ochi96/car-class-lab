class Car:

    def __init__(self,name='General',model='GM',typ='saloon',speed=0):
        self.name=name
        self.model=model
        self.typ=typ
        self.speed=speed

    def num_of_doors(self): #something about functions and methods being bound,change testcar eventually
            if self.name=='Porshe'or self.name=='Koenigsegg':
                return 2
            else:
                return 4

        
    def is_saloon(self):
        if self.typ=='Trailer':
            return False
        return True   
        
    def num_of_wheels(self): #something about functions and methods being bound,change testcar eventually
        if self.typ=='trailer':
            num_of_wheels=8
            return num_of_wheels #substitutions??????
        else:
            num_of_wheels=4
            return num_of_wheels

    def drive(self,x):
        if self.name=='Mercedes':
            moving_speed=(self.speed+int((x*1000)/3))
            self.speed=moving_speed
            return self
        else:
            moving_speed=(self.speed+(x*11))
            self.speed=moving_speed
            return self
        
    

    


        
    
           

