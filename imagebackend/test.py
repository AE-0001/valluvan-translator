import enchant

dictionary = enchant.Dict("en_US")

misspelled_word = "wandow"
if not dictionary.check(misspelled_word):
    suggestions = dictionary.suggest(misspelled_word)
    if suggestions:
        corrected_word = suggestions[0]
        print(f"Corrected word: {corrected_word}")
    else:
        print("No suggestions available.")
