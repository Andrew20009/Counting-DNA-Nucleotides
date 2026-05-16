def read_dna_from_txt(file_path: str) -> str: 
    # Function that reads nucleotide sequence from txt file
    sequence = "" # Initialize empty variable for the sequence
    
    with open(file_path) as f: # Open the file for reading
        for line in f: 
            cleaned = line.strip().upper() # Remove whitespace and convert to uppercase
            sequence += cleaned 
    
    return sequence 


def count_nucleotides(sequence: str) -> dict: # Count occurrences of each nucleotide in the sequence
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0} # Counter for each nucleotide
    for nucleotide in sequence:
        if nucleotide in counts: # Only count valid nucleotides (A, C, G, T)
            counts[nucleotide] += 1 # Increment count for specific nucleotide
    return counts 


if __name__ == "__main__": # Entry point of the code
    file = "rosalind_dna.txt" # Assign the filename to the variable
    
    # Simple verification that txt file is present
    try:
        seq = read_dna_from_txt(file)
        counts = count_nucleotides(seq)
        
        print(counts['A'], counts['C'], counts['G'], counts['T'])
        
    except FileNotFoundError:
        print(f"Error: File'{file}' not found!")
        print("Put file rosalind_dna.txt in the same folder as code.")
    except Exception as e:
        print(f"Error Occured: {e}")
