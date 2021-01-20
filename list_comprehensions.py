'''
Practicing with list comprehensions:

Given a list of strings, return all vowels present in each string as a new string. Please wrap this in a function
INPUT -> ['hello', 'how', 'yeet', 'lamborghini', 'huracan']
OUTPUT -> ['eo', 'o', 'ee', 'aoii', 'uaa']
'''

test_1 = ['hello', 'how', 'yeet', 'lamborghini', 'huracan']
assert_1 = ['eo', 'o', 'ee', 'aoii', 'uaa']

def extract_vowels(lst:list) -> list:
    lst2 = []
    vowels = 'aeiou'
    for i in lst:
        new_word = ''
        for x in i:
            if x in vowels:
                new_word += x
        lst2.append(new_word)
    return lst2

ans = extract_vowels(test_1)
# print(ans)
# assert ans == assert_1 

# dino goes yee (slow mo = yeeeeeeeē)
def get_vowels(string:str) -> str:
    res = ''
    for i in string:
        if i in 'aeiou':
            res += i
    return res

def extract_vowels_v2(lst:list) -> list:
    '''wowee'''
    new_words = [get_vowels(x) for x in lst]
    return new_words

result = extract_vowels_v2(test_1)
# print(result)


'''
Given a dictionary of car models and their current prices, procure and return a list of all cars with prices above a given X

INPUT:
cars = {
    '911 GT3' : 290000,
    'S13 Silvia' : 23000,
    'Macan S' : 100000,
    'E90 M3' : 45000,
    'Audi S7' : 95000
}

price = 70000

OUTPUT: ['911 GT3', 'Macan S', 'Audi S7']
'''

cars = {
    '911 GT3' : 290000,
    'S13 Silvia' : 23000,
    'Macan S' : 100000,
    'E90 M3' : 45000,
    'Audi S7' : 95000
}

price = 70000

assert_2 = ['911 GT3', 'Macan S', 'Audi S7']

def cars_above_x(car_dict:dict, price:int) -> list:
    cars_over_x = []
    for i in car_dict:
        car_price = car_dict[i]
        if car_price > price:
            cars_over_x.append(i)
    return cars_over_x

# res3 = cars_above_x(cars, price)
# print(res3)

def cars_above_x_v2(car_dict:dict, price:int) -> list:
    cars_over_x = [x for x in car_dict if car_dict[x] > price]
    return cars_over_x
res4 = cars_above_x_v2(cars, price)
print(res4)