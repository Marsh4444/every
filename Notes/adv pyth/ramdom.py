#python defines a set of functions that are used to generate or manipulate
# random numbers
# what we are going to learn .
# --the random module
# -- reproduce numbers with random.seed()
# -- create cryptographically strong random numbers with the secrets modul
# -- create random nd arrays with numpy.random


#----------------------------------------------------------------------
#--------------------#THE RANDOM MODULE--------------------------------
# This module implements pseudo-random number generators for various distributions
# it uses the mersenne Ywister algorithm
# (https://en.wikipedia.org/wiki/Mersenne_Twister) as its core generator. It is called
# pseudo-random, because the numbers seem random, but are reproducable.

import random

# #random float in (0,1)
# a = random.random()
# print(a)
#
# #produces a random float in range[a,b]
# a = random.uniform(1,10)
# print(a)
#
# #produces a random integer in range [a,b]. b is excluded
# a = random.randint(2,7)
# print(a)

#produces a random integer in range(a,b). b is excluded
# a = random.randrange(1,10)
# print(a)
#
# #produces a random element from a sequence
# a = random.normalvariate(0,1)
# print(a)
#
# #choses a random element from a sequence
# my_list = list("abcdefgh")
# a = random.choice(my_list)
# print(a)

#choses k unique random elements from a sequence
# my_list = list("abcdefgh")
# a = random.sample(my_list, 5)
# print(a)

#chooses k elements wit replacement, and return k sized list
# my_list = list("abcdefgh")
# a = random.choices(my_list, k=3)
# print(a)
#
# #shuffle list in place
# random.shuffle(my_list)
# print(my_list)

# The seed generator
# With random.seed(), you can make results reproducible, and the chain of
# calls after random.seed() will produce the same trail of data. The sequence
# of random numbers becomes deterministic, or completely determined by the seed value.

# print('seeding with 1...\n')
# my_list = list("abcdefgh")
# random.seed(1)
# print(random.random())
# print(random.uniform(1,10))
# print(random.choice(my_list))
#
# print('\nRe-seeding with 42...\n')
# random.seed(42)  # Re-seed
# print(random.random())
# print(random.uniform(1,10))
# print(random.choice(my_list))
#
# print('\nRe-seeding with 1...\n')
# random.seed(1)  # Re-seed
#
# print(random.random())
# print(random.uniform(1,10))
# print(random.choice(my_list))
#
# print('\nRe-seeding with 42...\n')
# random.seed(42)  # Re-seed
#
# print(random.random())
# print(random.uniform(1,10))
# print(random.choice(my_list))

#The secrets module¶
# The secrets module is used for generating
# cryptographically strong random numbers suitable for
# managing data such as passwords, account authentication, security
# tokens, and related secrets. In particularly, secrets should be used in preference
# to the default pseudo-random number generator in the random module, which is designed for modelling and simulation,
# not security or cryptography.
#the secrets module only as 3 fuctions

# import secrets
#
# #produces a random integer in range (0, n)
# a = secrets.randbelow(10)
# print(a)
#
# #returns an integer with k random bits.
# a = secrets.randbits(3)
# print(a)
#
# #chooses a random element from a sequence
# my_list = list("abcdefgh")
# a = secrets.choice(my_list)
# print(a)

# Random numbers with NumPy¶
# Create random numbers for nd arrays. The NumPy pseudorandom number generator is different from the Python standard
# library pseudorandom number generator. Importantly, seeding the Python pseudorandom number generator does not impact
# the NumPy pseudorandom number generator. It must be seeded and used separately.

import numpy as np
# #print(np.__version__)
# # generates an array with random floats, arrays has size (d0,d1,…,dn)
# a = np.random.rand(3)#produces a 1D array with 3 elements
# print(a)
# a = np.random.rand(3,3)#produces a 1D array with 3 elements
# print(a)

## generate nd array with random integers in range [a,b) with size n
#a = np.random.randint(0,10,(4,3))
#print(a)

# randomly shuffle a nd array.
# only shuffles the array along the first axis of a multi-dimensional array
# arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# np.random.shuffle(arr)
# print(arr)

np.random.seed(1)
# rand(d0,d1,…,dn)
# generate nd array with random floats, arrays has size (d0,d1,…,dn)
print(np.random.rand(3,3))
# reset the seed
np.random.seed(1)
print(np.random.rand(3,3))





































































































