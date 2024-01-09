import random

value = random.random()    #random number between 0 and 1
print(value)

print()

value = random.uniform(1, 10)    #random number between 1 and 10
print(value)

print()

value = random.randint(1, 6)    #random number between 1 and 6 (inclusive)
print(value)

print()

greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)    #random string in list
print(value + ', Corey!')

print()

colors = ['Red', 'Black', 'Green']
results = random.choices(colors, k=10)    #multiple random strings in list determined by the k value
print(results)

print()

colors = ['Red', 'Black', 'Green']
results = random.choices(colors, weights=[18, 18, 2], k=10)    #multiple random strings in list determined by the k value while adjusting the chances of certain strings to be drawn (green has a 2/38 chance)
print(results)

print()

deck = list(range(1, 53))    #non-inclusive
random.shuffle(deck)    #randomizes list
print(deck)
ran_deck = random.sample(deck, k=5)    #randomly picks from the list
print(ran_deck)

print()

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)


print("\n---------------------------------------\n")


random.seed()
def print_random():
    for i in range(5):
        print(random.randint(0, 100), end=' ')
print_random()

print()

random.seed(2)
def print_random():
    for i in range(5):
        print(random.randint(0, 100), end=' ')
print_random()


print("\n---------------------------------------\n")


# Using randint
print(random.randint(0, 10))  # Returns a random integer from 0 to 10 (inclusive)

# Using randrange
print(random.randrange(0, 10))  # Returns a random integer from 0 to 9 (10 is not included)
print(random.randrange(0, 10, 2))  # Returns a random even number from 0 to 8