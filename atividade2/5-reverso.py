def reverseWords(phrase):
    words = phrase.split()  # Split the phrase into a list of words
    reversedWords = [word[::-1] for word in words]  # Reverse each word
    newPhrase = " ".join(reversedWords)  # Join the reversed words into a new phrase
    return newPhrase

# Example usage
originalPhrase = input("Digite a frase: ")
reversedPhrase = reverseWords(originalPhrase)
print("Reverso:", reversedPhrase)
