def count_words_in_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        content = input_file.read()
        words = content.split()
        num_words = len(words)

    with open(output_filename, 'w') as output_file:
        output_file.write(f"Number of words: {num_words}")

# Test
count_words_in_file("input.txt", "output.txt")
