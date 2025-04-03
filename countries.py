class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    
    def language(self):
        print("Hindi is the spoken language of India")

    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Washington DC is the capital of the United States of America.")
    
    def language(self):
        print("English is the spoken language of the United States of America")

    def type(self):
        print("The United States of America is a developed country")

obj_ind = India()
obj_usa = USA()

for country in(obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()