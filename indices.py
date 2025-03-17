def find_word_indices(sentence, word):
    start_index = sentence.find(word)
    if start_index == -1:
        return None, None  # Word not found in the sentence
    end_index = start_index + len(word)
    return start_index, end_index

# Example usage
sentence = "Make sure the environments are configured correctly"
word = "environments"
start_index, end_index = find_word_indices(sentence, word)
print(f"Word: {word}, Start Index: {start_index}, End Index: {end_index}")