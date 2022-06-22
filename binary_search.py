binary_counter = 0
simple_counter = 0

def binary_search(list, value):
    low = 0
    high = len(list) - 1
    
    global binary_counter
    while low <= high:
        binary_counter += 1
        middle = int((low + high) / 2) + 1
        if list[middle] == value:
            return list[middle]

        if list[middle] > value:
            high = middle - 1
        else:
            low = middle + 1
            

def simple_search(list, value):
    global simple_counter 
    for i in list:
        simple_counter += 1
        if i == value:
            return value


binary_search([i for i in range(100000)], 25678)
simple_search([i for i in range(100000)], 25678)

print(simple_counter)
print(binary_counter)