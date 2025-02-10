def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_sentence = " ".join(iter_words_reversed(words))
    return reversed_sentence

def iter_words_reversed(words):
    result = []
    for i in range(len(words) - 1, -1, -1):  # Iterate backwards using a loop
        result.append(words[i])
    return result

# Example usage
input_str = "Python is great"
output_str = reverse_words(input_str)
print(output_str)  # Output: "great is Python"
