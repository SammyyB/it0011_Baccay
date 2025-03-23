excluded_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

statement = input("Enter a string statement\n:").strip()

words = statement.split()
word_count = {}

def clean_word(word):
    return ''.join(filter(str.isalpha, word))

for word in words:
    cleaned_word = clean_word(word)
    if cleaned_word and cleaned_word.lower() not in excluded_words:
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

lowercase_words = sorted((w for w in word_count if w.islower()), key=str.lower)
uppercase_words = sorted((w for w in word_count if w[0].isupper()), key=str.lower)

total_filtered = sum(word_count.values())

print("\n\n")
for word in lowercase_words + uppercase_words:
    print(f"{word:10} - {word_count[word]}")

print(f"Total words filtered: {total_filtered}")