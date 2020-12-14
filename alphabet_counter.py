def alphabet_counter(word):
    import string
    alphabet_list = list(string.ascii_lowercase)
    vowel = ['a', 'e', 'i', 'o', 'u']
    alphabet_dict = {}
    for i in alphabet_list:
        alphabet_dict[i] = 0

    non_alphabet = 0
    vowels = 0
    word_s = word
    word = list(word.lower())
    for i in word:
        if i in alphabet_list:
             alphabet_dict[i] += 1
        else:
            non_alphabet += 1
        if i in vowel:
            vowels += 1

    print("\n░░░ Results ░░░\nShowing Results for:  '" + word_s + "'\n")
    print("🔵 Total characters:  " + str(len(word)) + "\n")
    for key, value in alphabet_dict.items():
        if value != 0:
            print("❍ " + key + " = " + str(value))

    if vowels != 0:
        print("\n🔘 Vowels = " + str(vowels))

    if non_alphabet != 0:
        print("\n⭕ Not an alphabet = " + str(non_alphabet))

x = input("Throw in some characters:  ")
alphabet_counter(x)