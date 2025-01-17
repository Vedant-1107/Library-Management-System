sen = input("Enter the Sentence: ").lower().strip()
words = sen.split()
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        cons = word[:vowel_pos]
        new_word = word[vowel_pos:] + cons + "ay"
        new_words.append(new_word)

new_sen = " ".join(new_words).capitalize()
print(new_sen)