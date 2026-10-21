l = [3,2,54,65,89]

# for item in l:
#     index += l
#     print(f"The item number at index {index} is {item}")


# This can be simplified using enumerate function

for index , item in enumerate(l):
 print(f"The item number at index {index} is {item}")