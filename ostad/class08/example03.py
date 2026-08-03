# # for loop enumurate korbo

# fruits = ["apple", "banana", "cherry", "Lichi", "Watermelon"]

# # for index, fruit in enumerate(fruits, start=1): # for each fruit in the bucket of fruits, with index starting from 1
# for index, fruit in enumerate(fruits): # for each fruit in the bucket of fruits, with index starting from 0
#     print(f"Index: {index}, Fruit: {fruit}")




fruits = ["apple", "banana", "cherry", "Lichi", "Watermelon"]


for index, fruit in enumerate(fruits): # for each fruit in the bucket of fruits, with index starting from 0

    if fruits[index] == "cherry": # if the fruit is cherry
         
        break # exit the loop
    print(f"Index: {index}, Fruit: {fruit} - Found!")# print the index and fruit with Found!
