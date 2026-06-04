Counting DNA Nucleotides

OVERVIEW

This program reads a DNA sequence from a text file and counts the occurrences of its four nucleotides: Adenine (A), Cytosine (C), Guanine (G), and Thymine (T).
It is a solution to the "Counting DNA Nucleotides" Rosalind problem (ID: DNA). The tool is simple, efficient, and ideal for practicing file handling and string processing in Python.

FEATURES

Reads DNA sequence from a file (rosalind_dna.txt)
Automatically converts input to uppercase
Counts occurrences of A, C, G, and T
Ignores any non-nucleotide characters
Fast and memory-efficient — works well with long sequences
Clean, well-commented code with proper functions and docstrings

IMPORTANT NOTE

!!!Please put the Input txt with name rosalind_dna.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!


EXAMPLE
Input (rosalind_dna.txt):AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Output:20 12 17 21
Numbers are in sequence A, C, G, T

HOW IT WORKS

The program reads the DNA sequence from the file.
It cleans the input (removes whitespace and converts to uppercase).
It iterates through each character and counts only valid nucleotides (A, C, G, T).
Finally, it prints the counts in the order: A C G T.


TECHNOLOGIES USED

Python
File txt
