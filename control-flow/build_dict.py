# Building Dictionaries

# Using a for loop to create a set of counters
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
        
print(word_counter)

# Using the get method
word_counter_new = {}
for word in book_title:
    word_counter_new[word] = word_counter_new.get(word, 0) + 1
print(word_counter_new)
