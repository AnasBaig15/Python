from functools import reduce
# l = ["apple", "mango", "banana"]
# result = ", and, ".join(l)
# print(result)

# Format Method

# l = ["apple", "mango", "banana"]
# result = ", and, ".join(l)
# print(result)


# Map filter

# l = [1,2,3,4,5,]

# square = lambda x: x*x

# sqList = map(square,1)
# print(list(sqList))


# Filter EExample

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even,1)
print(list(onlyEven))

# Reduce Function

def sum(a,b):
    return a + b

mul = lambda x,y:x*y
print(reduce(sum,1))