print("Word Counter")

text= input("Input your sentence: ")

words= text.split()
total_words= len(words)

#total words count
print("Total words: ", total_words)

word_counts={}

for word in words:
    word=word.lower()

    if word in word_counts:
        word_counts[word] +=1

    else:
        word_counts[word] =1

for word,count in word_counts.items():
    print(f"{word}: {count}")


most_common_word=" "
highest_count=0


for word,count in word_counts.items():
    if count> highest_count:
        most_common_word=word
        highest_count=count

print(f"{most_common_word} appears {highest_count} times")