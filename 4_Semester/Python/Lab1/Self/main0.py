class Medicine:
    def change_amount(self,new_amount):
        self.amount=new_amount
    def __str__(self):
        return 'Препарат %s виробляється компанією %s. Є %s. В упаковці %i %s. Випускається %s' % (self.name, self.company, self.mechanism, self.amount, self.type, "за рецептом" if self.recipe_required  else "Без рецепта")

tables=Medicine()
tables.name='Цитрамон'
tables.company='Дарниця'
tables.mechanism='знеболюючі'
tables.amount=10
tables.type='таблетки'
tables.recipe_required=False



print(tables)


