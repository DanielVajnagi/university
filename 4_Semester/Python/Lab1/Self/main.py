class Medicine:
    def __init__(self,name,company,type,mechanism,amount=0,recipe_required=True):
         self.name=name
         self.company=company
         self.type=type
         self.amount=amount
         self.recipe_required=recipe_required
         self.mechanism=mechanism
    def change_amount(self,new_amount):
        self.amount=new_amount
    def __str__(self):
        return 'Препарат %s виробляється компанією %s. Є %s. В упаковці %i %s. Випускається %s' % (self.name, self.company, self.mechanism, self.amount, self.type, "за рецептом" if self.recipe_required  else "Без рецепта")

tables1=Medicine("Цитрамон", "Дарниця", "таблеток", "Знеболюючим", 10, False)
sashe1=Medicine("Німесил","Berlin Chemie","Саше","Болезаспокійливим",5)
print(tables1)
tables1.change_amount(20)
print(sashe1)
print(tables1)
