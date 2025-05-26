# indexing and slicing
word = "Programming"
print(word[0])
print(word[-1])
gram = word[3:7]
print(gram)

# extracting first five and last five characters
first_five = word[:5]
last_five = word[-5:]
print(first_five)
print(last_five)

# reversing
word="Programming"
print(word[::-1])

# extracting
print(word[::2])

word= "Hello, World!"

#lowercase
print(word.lower())

#uppercase
print(word.upper())

#whitespace
text = "Hello, World!" 
print(text.strip()) 

# replacing world with python
replaced_string = word.replace("World", "Python")
print("Replaced string:", replaced_string)

#occurrences of 'o'
o_count = word.count("o")
print("Number of occurrences of 'o':", o_count)

# Check start and end of string
print(word.startswith("Hello"))
print(word.endswith("!"))

# string manipulation
sentence= "The quick brown fox jumps over the lazy dog"

# Count words
word_count = len(sentence.split())
print(word_count)

# finding where fox is in the sentence
fox_position = sentence.find("fox")
print(fox_position)

# replacing lazy with active
changed_sentence = sentence.replace("lazy", "active")
print(changed_sentence)

#capitalizing
print(sentence.title())

# numeric string
num_string = "12345"

# Check if numeric
yesnumeric=num_string.isdigit()
print("Is numeric:", yesnumeric)

# Convert to integer and add 10
num_int = int(num_string) + 10
print("Integer plus 10:", num_int)

# Convert back to string
final_string = str(num_int) + " is the result"
print("Final string:", final_string)