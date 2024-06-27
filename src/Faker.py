import random
from faker import Faker

faker = Faker()

categories = [
            'Computadoras', 'Tablets', 'Celulares', 'Relojes Inteligentes', 
            'Pantallas', 'Videojuegos', 'Lavadoras'
        ]

category = random.choice(categories)
productname = faker.word(ext_word_list=categories)
nombre_computadora = faker.word(ext_word_list=['Computadora', 'Portátil', 'PC'])

print(category)
print(productname)
print(nombre_computadora)
