class laptop:
    def _init_(self,rbrand,rmodel,rprice):
        self.brand=rbrand
        self.model=rmodel
        self.price=rprice
    def _display_(self):
        print("brand is:",self.brand)
        print("model is:",self.model)
        print("price is:",self.price)
    def _del_(self):
        print("object has destroyed")
        lap=laptop("dell","inspiron",60000)
        lap.dispaly()
