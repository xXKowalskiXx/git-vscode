# Integer sets
odds = {1,3,5,7,9}
evens = {2,4,6,8,10}
primes = {2,3,5,7}

# Union
print(odds.union(evens))
input()
print(evens.union(odds))
input()
# Do sets change?
print(odds)
print(evens)
# Intersection
print(odds.intersection(primes))
print(primes.intersection(evens))
print(evens.intersection(odds))
input()

# Value in set?
# print(2 in primes)
# print(6 in odds)
# print(9 not in evens)