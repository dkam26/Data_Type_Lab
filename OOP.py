class Car(object):
    """This is the car class"""
    
    def __init__(self,name='General',model='GM',type='saloon'):
      self.name=name
      self.model=model
      self.type=type
      
    def car_doors(self):
      if self.name is 'Opel' or self.name is 'Koenigsegg':
        self.num_of_doors=2
      else:
        self.num_of_doors=4
      return self.num_of_doors
    def car_wheels(self):
      if self.type is 'trailer':
          self.num_of_wheels=8
      else:
        self.num_of_wheels=4
    def is_saloon(self):
      if self.type is 'saloon':
        return True
      else:
        return False