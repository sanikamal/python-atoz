# Extract First Names

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

# Output:
# ['rick', 'morty', 'summer', 'jerry', 'beth']

# Multiples of Three

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

# Output:

# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

# Filter Names by Scores

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)

# Output:
# ['Beth Smith', 'Summer Smith', 'Rick Sanchez']

