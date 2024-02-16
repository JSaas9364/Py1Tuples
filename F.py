def decode_and_sort(input_file, output_file):
    # Create a list to store number-word pairs as tuples
    number_word_pairs = []
    
    # Open and read the input_file, use with to avoid data leaks
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Check each line to extract numbers and words
    for line in lines:
        parts = line.split()
        if len(parts) == 2:
            number = int(parts[0])
            word = parts[1]
            number_word_pairs.append((number, word))
    
    # Sort the list of tuples by numbers in ascending order, using lambda
    sorted_pairs = sorted(number_word_pairs, key=lambda x: x[0])
    filtered_pairs = [(number, word) for number, word in sorted_pairs if str(number)[-1] in {'1', '3', '6'}]

    
    # Write the sorted pairs to the output_file
    with open(output_file, 'w') as output:
        for number, word in filtered_pairs:
            output.write(f"{word}\n")
 
 
                  

# Input and output file paths
input_file = 'dec.txt'
output_file = 'filtered.txt'

# Call the function to decode, sort, and write to the output file
decode_and_sort(input_file, output_file)
