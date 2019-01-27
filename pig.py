#get sentence from the user
original = input("What is your word or sentence you would like us to translate? ").strip().lower()
print()

#split up the sentence into words
words = original.split()

#loop through the words and conver to pig latin

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        cons = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)



#stick words back together
output = " ".join(new_words)

#output the final string
print("Piglatin Translation = " + output)
