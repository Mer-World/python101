print("=== Simple Word Counter ===")
text = input("Enter a sentence or paragraph: ")

# Count total words
words = text.split()  # Split the text into words
total_words = len(words)
print("\nTotal words:", total_words)

# Count how many times each word appears
word_counts = {}  # Create an empty dictionary to store counts

for word in words:
    # Make words lowercase for consistent counting
    word = word.lower()
    
    # If we've seen this word before, add 1 to its count
    if word in word_counts:
        word_counts[word] += 1
    # If this is the first time seeing this word, set count to 1
    else:
        word_counts[word] = 1

# Print each word and its count
print("\nWord counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Find the most frequent word
most_common_word = ""
highest_count = 0

for word, count in word_counts.items():
    if count > highest_count:
        most_common_word = word
        highest_count = count

print("\nMost frequent word:")
print(f"'{most_common_word}' appears {highest_count} times")