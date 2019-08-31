class FarmAnimal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight # kg
    family = 'family'
    def feed(self):
        print(f'{self.family} {self.name} накормлен.')

# FarmAnimal.feed()
# Подклассы

class Milk_Cattle(FarmAnimal):
    def get_milk(self):
        print(f'{self.family} {self.name}: cвежее молоко надоено!')

class Bird(FarmAnimal):
    def gather_eggs(self):
        print(f'{self.family} {self.name}: cвежие яйца собраны!')

# Классы видов животных

class Geese(Bird):
    family = 'гусь'
    voice = '«Га-га!»'

class Cow(Milk_Cattle):
    family = 'корова'
    voice = '«Мууу!»'

class Sheep(FarmAnimal):
    family = 'овца'
    voice = '«Бе-е-е!»'
    def shearing(self):
        print(f'{self.name}: шерсть сострижена')

class Hen(Bird):
    family = 'курица'
    voice = '«Ко-ко-ко!»'

class Goat(Milk_Cattle):
    family = 'коза'
    voice = '«Ме-е-е!»'

class Duck(Bird):
    family = 'утка'
    voice = '«Кря-кря!»'

# Объекты

geese_seryi = Geese('Серый', 3.3)
geese_belyi = Geese('Белый', 2.8)

cow_manjka = Cow('Манька', 535.0)

sheep_barashek = Sheep('Барашек', 121.0)
sheep_kudrjavyi = Sheep('Кудрявый', 137.0)

hen_koko = Hen('Ко-Ко', 1.1)
hen_kukareku = Hen('Кукареку', 1.3)

goat_roga = Goat('Рога', 112.0)

goat_kopyta = Goat('Копыта', 121.0)

duck_krjakva = Duck('Кряква', 5.2)

def feed_animals():
    geese_seryi.feed()
    geese_belyi.feed()
    cow_manjka.feed()
    sheep_barashek.feed()
    sheep_kudrjavyi.feed()
    hen_koko.feed()
    hen_kukareku.feed()
    goat_roga.feed()
    goat_kopyta.feed()
    duck_krjakva.feed()

def egg_gathering():
    hen_koko.gather_eggs()
    hen_kukareku.gather_eggs()
    duck_krjakva.gather_eggs()

def dairy():
    cow_manjka.get_milk()
    goat_roga.get_milk()
    goat_kopyta.get_milk()

def wool_shearing():
    sheep_barashek.shearing()
    sheep_kudrjavyi.shearing()

def uncle_joe_morning_procedure():
    print('\n Солнышко встаёт! \n Встал утром, прежде всего всех '
          'покорми:\n')
    feed_animals()
    print('\n Перед завтраком яйца собери, молока надои:\n')
    egg_gathering()
    dairy()
    print('\n После завтрака шерсть на продажу состриги:\n')
    wool_shearing()
    print('\n Теперь и подремать можно!')

def uncle_joe_daily_routine():
    print('\n Жизнь на ферме кипит, постоянно что-то происходит. \n'
          'Учись распознавать по голосу, кто где находится!\n')
    print(f'Если слышишь {Geese.voice}, это {geese_seryi.name} или '
          f'{geese_belyi.name}.')
    print(f'Если слышишь {Cow.voice}, это {cow_manjka.name}.')
    print(f'Если слышишь {Sheep.voice}, это {sheep_barashek.name} или '
          f'{sheep_kudrjavyi.name}.')
    print(f'Если слышишь {Hen.voice}, это {hen_koko.name} или '
          f'{hen_kukareku.name}.')
    print(f'Если слышишь {Goat.voice}, это {goat_roga.name} или '
          f'{goat_kopyta.name}.')
    print(f'Если слышишь {Duck.voice}, это {duck_krjakva.name}.')


def uncle_joe_evening_procedure():
    print('\n Дело к закату. \n Перед ужином всех животинок проверь, '
          'кто сколько жирку нагулял:\n')
    weight_comparison()

def weight_comparison():
    weight_dict = {
        geese_seryi.name: geese_seryi.weight,
        geese_belyi.name: geese_belyi.weight,
        cow_manjka.name: cow_manjka.weight,
        sheep_barashek.name: sheep_barashek.weight,
        sheep_kudrjavyi.name: sheep_kudrjavyi.weight,
        hen_koko.name: hen_koko.weight,
        hen_kukareku.name: hen_kukareku.weight,
        goat_roga.name: goat_roga.weight,
        goat_kopyta.name: goat_kopyta.weight,
        duck_krjakva.name: duck_krjakva.weight,
    }
    names_list = list(weight_dict.keys())
    weight_list = list(weight_dict.values())
    print(f'Тяжелее всех {names_list[weight_list.index(max(weight_list))]} '
          f'весом в {max(weight_list)} килограмм.')
    print(f'Вес всех животных: {sum(weight_dict.values())} килограм.')


def day_at_uncle_joe_farm():
    print('\nЧем заняться на ферме у дядюшки Джо?')
    uncle_joe_morning_procedure()
    uncle_joe_daily_routine()
    uncle_joe_evening_procedure()
    print('\n И спать пора ложиться, завтра будет новый день!')

day_at_uncle_joe_farm()
