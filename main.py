#Кортежі, Діапазони, Словники, Множини
###########

#Task1 - dictionaries:

countries_list = [
    ("Ukraine", ["Kyiv", "Dnipro", "Lviv", "Mykolayiv"]),
    ("USA", ["Los Angeles", "New York", "Detroit", "Nashvill"]),
    ("Germany", ["Hamburg", "Munich", "Dusseldorf", "Stuttgart"]),
    ("Netherlands", ["Rotterdam", "Maastricht", "Utrecht", "Vollendam"])
]

countries_dict = dict(countries_list)
print(countries_dict)
######

#Task2 - dictionaries:

dictionary = {'vehicles': ["bus", "truck"], 'animals': ["rat", "spider"], 'games': ["cards", "dice"]}
print(dictionary['animals'])

##

print()
#Task1_lists:

initial_list = [8, 10, 35, 29, 35, 10, 11, 8, 46]
print ("Initial list: " + str(initial_list))

initial_list = list(set(initial_list))
print ("List without duplicates: " + str(initial_list))

print()

############################################
print()
#Task2_lists:

my_nums1 = {"18", "6", "9", "85", "102"}
my_nums2 = {"6", "49", "85", "18", "50"}
#

my_nums3 = my_nums1.symmetric_difference(my_nums2)  
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

unique_words = list(set(text.split()))
print(unique_words)

print(len(unique_words))
