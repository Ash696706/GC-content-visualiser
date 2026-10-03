# 🧬 DNA GC Content Analyzer

A beginner-friendly bioinformatics project built with Python to analyze DNA sequences and study their nucleotide composition and GC content.

The project also performs **sliding-window GC analysis** to observe how GC content changes across different regions of a DNA sequence.

## 🔬 Features

* ✅ DNA sequence validation
* ✅ DNA length calculation
* ✅ Count of A, T, G and C nucleotides
* ✅ Overall GC content calculation
* ✅ Overall AT content calculation
* ✅ GC-rich / AT-rich classification
* ✅ Sliding-window GC analysis
* ✅ GC content visualization using Matplotlib
* ✅ User-defined sliding window size

## 🧪 Example DNA Sequence

```text
ATGCCATCCGATCGATTACGGGA
```

The program analyzes the sequence and reports its nucleotide composition and GC percentage.

## 📊 What is GC Content?

GC content is the percentage of guanine (G) and cytosine (C) bases present in a DNA sequence.

The formula used is:

```text
GC Content = (G + C) / Total DNA Length × 100
```

AT content is calculated as:

```text
AT Content = 100 - GC Content
```

## 🪟 Sliding Window Analysis

The program divides the DNA sequence into smaller windows of a user-defined size.

For example, with a window size of `5`:

```text
ATGCC
TGCCA
GCCAT
CCATC
...
```

The GC percentage is calculated separately for each window.

This helps visualize how GC composition changes across different regions of the sequence.

## 📈 Visualization

The project generates a line graph showing GC content across the DNA sequence.

* X-axis → Window starting position
* Y-axis → GC content (%)

The graph makes it easier to identify regions with relatively higher or lower GC content.

## 🛠️ Technologies Used

* Python
* Matplotlib

## 📂 Project Structure

```text
DNA-GC-Analyzer/
│
├── dna_analyzer.py
├── README.md
└── requirements.txt
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### 2. Install the required library

```bash
pip install matplotlib
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

### 3. Run the program

```bash
python dna_analyzer.py
```

### 4. Enter a DNA sequence

Example:

```text
ATGCCATCCGATCGATTACGGGA
```

### 5. Enter a sliding window size

Example:

```text
5
```

## 💻 Example Output

```text
Enter DNA sequence: ATGCCATCCGATCGATTACGGGA

DNA sequence is valid.
DNA length: 23

Nucleotide Counts:
A: 6
T: 4
G: 6
C: 7

Overall Composition:
GC percentage: 56.52 %
AT percentage: 43.48 %

Sequence classification: GC-rich

Enter sliding window size: 5

Sliding Window GC Analysis:

Window: ATGCC → GC: 60.0 %
Window: TGCCA → GC: 60.0 %
Window: GCCAT → GC: 60.0 %
...
```

## 🧠 Concepts Practiced

This project helped me practice:

* Python variables
* Strings
* `input()`
* `if/else`
* `for` loops
* Functions
* Lists
* Dictionaries
* String methods such as `.count()`
* String slicing
* Validation
* Basic data visualization
* Working with biological sequences

## 🚀 Future Improvements

Possible improvements for future versions:

* Add FASTA file input
* Analyze multiple DNA sequences
* Add nucleotide percentage calculations
* Add CSV report generation
* Add protein translation
* Add reverse complement analysis
* Add command-line arguments
* Add automated tests
* Create a simple web interface

## 👩‍💻 About the Project

This project was created as part of my journey to learn **Python and bioinformatics**, combining programming with biotechnology.

The goal is to gradually develop practical computational biology projects and build a stronger foundation in **Python, bioinformatics and data analysis**.
