# Counting DNA Nucleotides

## OVERVIEW
This program reads a DNA sequence from a text file and counts the occurrences of its four nucleotides: Adenine (A), Cytosine (C), Guanine (G), and Thymine (T).
It is a solution to the **"Counting DNA Nucleotides"** Rosalind problem **(ID: DNA)**. The tool is simple, efficient, and ideal for practicing file handling and string processing in Python.

---

## FEATURES
- Reads DNA sequence from a file <u>(rosalind_dna.txt)</u>
- Automatically converts input to uppercase
- Counts occurrences of <u>A, C, G, and T</u>
- Ignores any non-nucleotide characters
- Fast and memory-efficient — works well with long sequences
- Clean, well-commented code with proper functions and docstrings

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the Input txt with name rosalind_dna.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_dna.txt):
```
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```
**Output:**
```
20 12 17 21
```
> Numbers are in sequence: <u>A, C, G, T</u>

---

## HOW IT WORKS
1. The program reads the DNA sequence from the file
2. It cleans the input (removes whitespace and converts to uppercase)
3. It iterates through each character and counts only <u>valid nucleotides (A, C, G, T)</u>
4. Finally, it prints the counts in the order: A C G T

---

## TECHNOLOGIES USED
- **Python**
- **TXT File**
