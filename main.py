#Кортежі, Діапазони, Словники, Множини

# # Кортеж (tuple) – константний (immutable) список
# # можна працювати як зі звичайним списком,
# # тільки не можна нічого міняти (функції, які змінюють колекцію - відсутні в кортежі)
# # crud -> create, read, update, delete (у кортежі можна робити лише read)
#
# info = ("test1", 123) #це перший спосіб створити кортеж, краще писати з (), бо це читабельно
# print(info)
# print(type(info))
#
# #
# info = "test2", 1234, 1234445 #це другий спосіб створити кортеж, без ()
# print(info)
# print(type(info))
#
# # #
# print(info[0])
# #так як ми можемо кортеж тільки читати, то ми можемо звернутися до нього по індексу
# #
# # info[0] = 123  # TypeError: 'tuple' object does not support item assignment
# #цей еррор трапиться, якщо ми спробуємо замінити якесь значення у кортежі
#
# #ниже приклад, як можна з клавіатури проініціалізувати кортеж
# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: ")), num
# print(nums)

#####
import copy
#
info = "test2", 1234, 1234445
test = copy.deepcopy(info) #функція deepcopy дозволяє зробити копію обьєкта, у якого не існую функції робити копії у середині
print(test)

#
# info_copy = info
info_copy = info
print(info_copy)
print(info)

#
info_list = list(info) #так ми приводимо інфу до списку
print(info_list)
info_list.append(123) #якщо треба щось додати\змінити у незмінному кортежі
print(info_list)
print(info)
info = tuple(info_list) #так ми привели до тьюплу \ кортежу цей ліст\список і у списку додалось значення 123
print(info)
print(info_list)
print(info[1:3]) #з кон=ртежами також можна робити зрізи\слайси, слайс поверне нам копію, але не змінить оригінал
print(info)

#з цифрами кортеж часто використовують для статистики, дані які не можна змінити, бо вони вже отримані у статистиці

###########
for num in (1, 3, 4, 5, 6, "Hello", 7): #цикл відпрацював і вивев всі значення у колекції кортеж на скрін
    print(num)
#
for i in range(5):  # 0, 1, 2, 3, 4 - range генерує нам послідовність чисел
    print(i)
#
for _ in range(5): # тут змінна не буде далі використовуватись, тому можна її замінити символом "_"
    print("Hello")

# таку змінну створювати не можна, бо її складно читати та зрозуміти
# _ = "Vasya"
# print(_)

print(range(5))
print(range(1, 5))
print(range(1, 5, 2))
result = range(5)
print(result)
print(type(result))
#
numbers = list(range(10)) #якщо ми хочемо отримати доступ до значень колекції, то її треба привести до типу list
print(numbers)
#
numbers = list(range(3, 10))
print(numbers)
#
numbers = list(range(1, 10, 2))
print(numbers)
#
numbers = list(range(10, 0, -1))
print(numbers)
#
numbers = tuple(range(10, 0, -1)) #коли нам треба отримати значення у зворотньому порядку
print(numbers)
#
result = sorted(numbers) #щоб відсортувати значення у кортежі
print(result) #тут залишиться оригінал кортежу
print(numbers) #тут будуть відсортовані значення з кортежу

#############
##
# dict -> словник, колекція key: value, структура цієї колекції це пара "ключ:значення"
#ключ має бути унікальним, а значення - будь-яким
#ключі мають бути або цілочтслені, або типу даних string

# users = {
users = {
    1: "John",
    2: "Vasya",    #машина у консолі проігнорує перший ключ 2 Vasya, бо він дублований, але виведе ключ 2 qwerty
    3: [1, 3, 2],
    "key1": "some value",
    2.4: 123,
    True: 111,
    2: "qwerty",  #дублювати ключі не можна!
    33: 222
}
#

print(users)
print(type(users))
print(users[1])    # [1] -> це не індекс, а key, у словників немає індексів
print(users["key1"])
print(users[2.4])
print(users[True])   #True комп розшифровує, як одиницю, тому у консолі ми побачимо число 111
print(users[2])
print(users[3][1]) #цей приклад для ключа та значення у вигляді списка (всередині списка ми вже
#можемо звертатися до індексів, тому 3 - це ключ, а 1 - це індекс для списку [1, 3, 2]
#
#це приклад того, як вкладений список можна перетворити у словник
users_list = [
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
]

users_dict = dict(users_list)
print(users_dict)

users_list = list(users_dict) #так ми у консолі виведемо тільки ключі, без значень
print(users_list)

##################################################################
#Task1 - dictionaries:

countries_list = [
    ("Ukraine", ["Kyiv", "Dnipro", "Lviv", "Mykolayiv"]),
    ("USA", ["Los Angeles", "New York", "Detroit", "Nashvill"]),
    ("Germany", ["Hamburg", "Munich", "Dusseldorf", "Stuttgart"]),
    ("Netherlands", ["Rotterdam", "Maastricht", "Utrecht", "Vollendam"])
]

countries_dict = dict(countries_list)
print(countries_dict)
##################################################################
#Task2 - dictionaries:

dictionary = {'vehicles': ["bus", "truck"], 'animals': ["rat", "spider"], 'games': ["cards", "dice"]}
print(dictionary['animals'])


###########
##
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

print(users["+33333333"])
users["+33333333"] = "Petya" #ось так ми можемо зробити заміну значення у словнику, з Bob на Petya
print(users["+33333333"])

users["+4444444"] = "Test" #якщо ми звертаємось по ключу +444444, а його у списку немає, то так ми створюємо нову пару ключ:значення
print(users["+4444444"])

print(users)
#
#як ми можемо циклом вивести значення словника

for key in users:  #таким чином ми отримуємо доступ до ключів
    print(users[key], end=" ")

print()
#альтернативний варіант отримати доступ до ключів, застосувати функцію keys, у консоль виведе всі ключі
for key in users.keys():
    print(key, end=" ")

print()
print(users.keys())
print(list(users.keys()))

#якщо нам треба отримати окремо доступ до значень, в консоль виведе всі значення
for value in users.values():
    print(value, end=" ")

print()
print(users.values())

print()
for key, value in users.items(): #функція items дозволяє отримати доступ до пар ключів та значень, вона виведе у консоль ці пари
    print(f"key: {key} value: {value}")

print()
print(users.items())


#####

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
#
# print(users["+33333333"]) - щоб прочитати якесь значення по його ключу
#э також варіант прочитати якесь значення по ключу через функцію get
#окрім ключа ми також передаємо другий параметр key not exists, якщо ми звертаємось до ключа
#якого немає, то у консолі отримаємо key not exists
print(users.get("+33333333", "key not exists"))

# # del users["+55555555"] #функція pop дозволяє видалити значення по ключу
#тут також краще писати другий параметр key not exists, щоб у консоль вивело, що ключа не існує
deleted_value = users.pop("+555555551", "key not exists")
print(deleted_value)
print(users)

#функція clear дозволяє видалити всі значення із словника, у консолі бачимо пустий словник {}
users.clear()
print(users)

# # словник - це мутабельна колекція і тому можемо застосувати фкнція copy
users_1 = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
#
users_copy = users_1.copy()

print(users_1)
print(users_copy)
users_copy[111] = "qqqqqq"
print(users_1)
print(users_copy)

# функція update дозволяє додати в один словник значення з другого словника
#тут з дублікатів ключів залишиться тільки останній з них, а попередні дублікати будуть видалені
users_2 = {
    "+11111111": "eeeeeee",
    "+44444": "qqqqqq",
    "+12341234": "wwwwwww"
}
#
users_1.update(users_2)
print(users_1)
print(users_2)

##################
#нижче приклад з домашки, коли було треба знайти суму між найменшим та найбільшим позитивними числами у списку
nums = [1, 2, 3, 4, 5, 6]

index_start = 0
index_end = 0

for i in range(len(nums)): #ми робимо цикл, який йде з початку списка, якщо перемінна у списку більше нуля
#то ми її зберігаємо та йдемо далі по списку, коли ми знайшли число, то робимо break
    if nums[i] > 0:
        index_start = i
        break

for i in range(len(nums) - 1, -1, -1): #а другий цикл йде з кінця і робить те саме, тільки з кінця
#коли цикл знайшов число, то ми знов робимо break
    if nums[i] > 0:
        index_end = i
        break

my_sum = 0
for i in range(index_start + 1, index_end): #суму ми рахуємо між індексами, тому додаємо +1
    my_sum += nums[i]

print(my_sum)

################

#нижче приклад з вкладеними словниками, у ньому у якості значення кожного ключа є вкладений словник
# json
users = {
    "Vasya": {
        "phone": "123123",
        "email": "qwerty1@gmail.com",
        "hobbies": ["one", "two", "three"]
    },
    "Petya": {
        "phone": "1345555",
        "email": "aqwfafdbsdb@gmail.com",
        "hobby": "uerhukjshbdjbkhdf",
        "add_data": {
            1: "test-1",
            2: "test-2",
        }
    }
}

#ось таким чином ми будемо отримувати та виводи в консоль різні значення з вкладений списків
print(users["Vasya"]["hobbies"][1])
print(users.get("Vasya", "no key!").get("hobbies", "no key!")[2])
print(users["Petya"]["add_data"][2])
print(users.get("Petya", "no key!").get("add_data", "no key!").get(2, "no key!"))

#приклади того, як щось шукати по ключу
#v1

key = input("Enter key: ")
if key in users:
    print(users[key])
else:
    print("Nothing found!")

#v2 тут нам треба зберегти оригінальний варіант ключа, який написано з великої літери
#для цього ми користуємося функціями strip та lower
key = input("Enter key: ").strip().lower()
for curr_key in users.keys():
    if curr_key.lower() == key: #ми приводимо ключ до нижнього регістру та порівнуємо його з тим ключем, який ми ввели
        print(users[curr_key])
        break #як тільки ми знайшли ключ, то ставимо break, щоб припинити пошук
else:
    print("Nothing found!") #якщо не знайшли ключ, то виводимо nothing found

##############
# # Множини (set) представляють ще один вид набору, який зберігає тільки унікальні елементи.
# Дублікати значень буде видалено. У множині не може бути дублікатів.
#сама полекція Множини - вона про унікальність, про унікальні значення, коли треба видалити дублікати

#
users = {"Tom", "Bob", "Alice", "Tom"} #у консолі не буде дублікатів, буде тільки один Tom
print(users)
print(type(users))
#при цьому значення у множинах будуть виводитись у різній послідовності, а не по алфавіту та ін.
#і через це у множин немає індексації, ми не зможемо звертатися до різних значинь у множинах по індексу
# # #

#як привести список\ list до множини \ до set
people = ["Mike", "Bill", "Ted"]
users = set(people)
print(users)
# # # # #
#також ми можемо отримати довжину цієї колекції, у нашому випадку буде 3 елемента у колекції
print(len(users))
# # # #
#є також функція add, яка дозволяє нам додадти якесь значення до множини
users.add("Sam") # тут ми додали до колекцію Sam, але у множині його місце буде вставлено рандомно
print(users)
# # #
#як видалити якесь значення із колекції множини
users = {"Tom", "Bob", "Alice"}
#
user = "Tom"
if user in users:
    users.remove(user)  # якщо немає значення – генерується виняток, буде видалено тільки одне значення
print(users)
# # #
users = {"Tom", "Bob", "Alice"}
#
users.discard("Tim")  # елемент "Tim" відсутній, і метод нічого не робить
print(users)
# # # #
#щоб видалити всі значення із списку множини ми застосуємо функцію clear, у консолі побачимо пустий set()
users.clear()
print(users)
# ##
#цикл for може перебирати всы значиння у множині, але не по індексам, він просто виведе нам всі значення у списку множини
users = {"Tom", "Bob", "Alice"}

for user in users:
    print(user)
# #
# # # copy() функція копіювання працює так само як і в list, dict і тд
# #
#функція union дозволяє об'єднати множини в одну множину \ в один список множин
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.union(users2)
print(users3)
#у результаті ми отримаємо третій список множин вже без дублікатів, якщо вони були у списках множин 1 та 2
# #

#ще є корисна функція intersection, застосовується для того, щоб знайти що є спільного \ які елементи
#є спільними у двох списків множин, у нашому випадку це будуть Tom і Bob.

users = {"Tom", "Bob", "Alice"}
users2 = {"Tom", "Sam", "Kate", "Bob"}

# v1
users3 = users.intersection(users2)  # перетин множин (що загальне у першої множини з другим)
# v2
print(users & users2)
print(users3)
# #
#є ще варіація цієї функції, яка змінює оригінал users
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users.intersection_update(users2)  # те саме, тільки результат буде записаний в users
print(users)
#
print()
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
#
## функція diffference допомагає знайти ті значення, які у першій множині, але їх гнемає у другіє
#вона дозволяє знайти та показати різницю
# # v1
users3 = users.difference(users2)  # що є тільки першим і немає у другій множині
print(users3)  # {"Tom", "Alice"}
# v2 - ми можемо написати difference, або просто написати мінус, це одне й те саме
print(users - users2)
#
users.difference_update(users2)  #функція difference_update буде змынювати оригынальний список множини
print(users)
print(users2)
# # #
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
#
# # функція symmetric_difference дозволяє отримати унікальні значення з обох списків множин,
# і з першої, і з другої, отримати значення які не дублюються
#це є протилежність функціі intersection
# #v1
users3 = users.symmetric_difference(users2)  # унікальні значення першої та другої множин
print(users3)

# v2
#замість функції symmetric_difference ми можемо поставити оператор ^, це буде те й саме
users4 = users ^ users2

# ##
##використання функція issubset \ подмножество та issuperset \ надмножество
#подмножество = когда все елементы первого множества присутствуют во втором множестве, їх послідовність не важлива
#приклад застосування: коли якась група студентів ходить ще на якісь курси чи у гуртки
#

users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
print(users.issubset(superusers))  # True - тут ми перевіряємо, чи множина 1 э підмножиною множини 2
print(superusers.issubset(users))  # False
#
#
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
print(users.issuperset(superusers))  # False
print(superusers.issuperset(users))  # True

#
# # Тип frozen set є видом множин, які не можуть бути змінені (за типом tuple у list)
users = frozenset({"Tom", "Bob", "Alice"})
print(users)
users = set(users)
print(users)
# # можна використовувати всі функції звичайного set, крім тих, що модифікують значення


############################################

print()
#Task1_lists:
# removing duplicated from the list using set()

# initializing list
initial_list = [8, 10, 35, 29, 35, 10, 11, 8, 46]
print ("Initial list: " + str(initial_list))

# to remove duplicated from list
initial_list = list(set(initial_list))

# printing list after removal
# ordering distorted
print ("List without duplicates: " + str(initial_list))

print()

############################################
print()
#Task2_lists:

my_nums1 = {"18", "6", "9", "85", "102"}
my_nums2 = {"6", "49", "85", "18", "50"}
#
# # функція symmetric_difference дозволяє отримати унікальні значення з обох списків множин,
# і з першої, і з другої, отримати значення які не дублюються
#це є протилежність функціі intersection
# #v1
my_nums3 = my_nums1.symmetric_difference(my_nums2)  # унікальні значення першої та другої множин
print(my_nums3)

############################################
print()
#Task3_lists:

text = "34 is my house address. my house is located in this city. i like this house"
number = ""
counter = 0
for symbol in text:
    if symbol.isnumeric():
        number +=symbol
        counter += 1
    else:
        break
number = int(number)
print(number)
text = text[counter + 1:]
print(text)

# list of unique words
unique_words = list(set(text.split()))
print(unique_words)

#порахуємо кількість унікальних слів у рядку - зараз 12, але має бути 10, бо 2 з них числа
print(len(unique_words))

############################################

#це приклад гри про угадування слів
import random

words = ["Cat", "Apple", "Dog", "Letter", "Helicopter"]

secret_word = words[random.randint(0, len(words) - 1)]
# print(secret_word)

user_word = ["_"] * len(secret_word) #таким чином ми виводимо на екран нижні підкреслювання, щоб юзер міг вгадати слово
# print(user_word)
print(" ".join(user_word)) #так ми виводимо нижні підкреслювання, які юзер буде бачити 

attempts_counter = 0

while True:
    # v1
    if "".join(user_word).find("_") == -1:
        print(f"\nYou guessed a word!\nWord: {secret_word}\nAttempts: {attempts_counter}")
        break
    # v2
    # if "".join(user_word).lower() == secret_word.lower():
    #     print(f"\nYou guessed a word!\nWord: {secret_word}\nAttempts: {attempts_counter}")
    #     break
    print(" ".join(user_word))

    letter = input("Enter letter: ").strip().lower()

    if not letter.isalpha() or len(letter) != 1:
        print("Please enter only one letter!")
        continue
        # или
        # raise Exception("Please enter only one letter!")

    attempts_counter += 1
    for i in range(len(secret_word)):
        if letter == secret_word[i].lower():
            user_word[i] = letter

# добавить:
# - два уровня сложности
# легкий уровень: кол-во попыток равно длина слова * 2 -> если не угадал - вывести сообщение об этом
# сложный уровень: кол-во попыток равно длина слова * 1.5 -> если не угадал - вывести сообщение об этом
# показывать сколько попыток осталось
# - обработку исключений