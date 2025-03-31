class Car():
    def __init__(self, id, make, model, year):
        self.id = id
        self.make = make
        self.model = model
        self.year = year


    def to_dict(self):
        return {
            "id" : self.id,
            "make" : self.make,
            "model" : self.model,
            "year" : self.year
        }
