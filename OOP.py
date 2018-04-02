
# Objects are instances of class
# Class is a blueprint for object

import random



class Coin:

    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)




        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print('Coin Spent')

    def __str__(self):
        return "{} {} {} Coin".format(self.value , self.name, self.color )




# inheritance

class Pound(Coin):

    def __init__(self):
        data = {
            'name': 'pound',
            'original_value': 1.00,
            'clean_color': 'gold',
            'rusty_color': 'greenish',
             'num_edges': 1,
            'diameter': 22.5,
            'thickness': 3.15,
            'mass': 9.5
        }
        super().__init__(**data)


# Polymorphism overriding rust() method
class Taka(Coin):

    def __init__(self):
        data = {
            'name': 'taka',
            'original_value': 5.00,
            'clean_color': 'silver',
            'rusty_color': 'black',
            'num_edges': 12,
            'diameter': 26.8, # mm
            'thickness': 5.25,
            'mass': 8.17 # g
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color





one_pound_coin = Pound()



print(one_pound_coin) # 1.0 pound gold Coin


taka_coin = Taka()
print(taka_coin)


















