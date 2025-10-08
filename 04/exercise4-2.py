# Banker Roulette - Who will pay the bill?

import random

friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']

# Option 1
print(random.choice(friends) + " will pay the bill.")

# Option 2
random_friend = random.randint(0, 4)
print(friends[random_friend] + " will pay the bill.")