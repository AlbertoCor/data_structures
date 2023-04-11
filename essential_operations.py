
#use of lists basic commands

fruits = []                 # create a list
fruits.append("kiwwi")      # add ingredient
fruits.append("berry")      # add ingredient
fruits.append("melon")      # add ingredient
fruits.sort()               # function .sort() rearrage in order depend on data type str or int
fruits.pop()                # function .pop() remove last item in list

fruits.insert(0,"apple")            # add an element in specified place
fruits.insert(1, "strawberry")      # adding an element in specified place
fruits.pop(1)                       # remove an element in specified place
    
fruits.remove("apple")              # remove an element with specific name 

print(fruits)

def pyramid_sum(lower,upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower +1, upper, margin + 4)
        print(blanks, result)
        return result

pyramid_sum(1,4)

print("\n" "*" * 50, "\n\n")


# lists (general propouse, most used structure, dynamic size, sequential type)

print("\n"" Lists" "\n")

list1 = list()
list2 = ["t", 25 , " cat", 3.1416]
list3 = [number**2 for number in range(1, 100, 3)]

print(list1)
print(list2)
print(list3)


# tuples (inmutable list utils for constant data as coordinates, streets, they are faster than lists)

print("\n"  "Tuples" "\n")

tuple1 = ()
tuple2 = (1274, 1275, 1276)
tuple3 = "mulan", "percy", "pucca"

print(tuple1)
print(tuple2)
print(tuple3)


# sets store objects with no duplicated elements as cooking recipe, quick access, accept operation logics its disordered

print("\n"  "Sets" "\n")

set1 = {3,5,7,9}
set2 = set()
numbers = [1,2,3,4,5,6,6,7]
set3 = set(numbers)

print(set1)
print(set2)
print(set3)


# dictionaries are pairs key/values they are associative arrays (hash maps) they are disordered

print("\n" "Dictionaries" "\n")


cats1 = {
        "mulan": 2,
        "pucca": 1.2,
        "percy": 4,
        }
cats2 = dict([("mulan",2), ("pucca", 1.2), ("percy", 4)])
cats3 = dict(mulan=2, pucca=1.2, percy=4)

print(cats1)
print(cats2)
print(cats3)









