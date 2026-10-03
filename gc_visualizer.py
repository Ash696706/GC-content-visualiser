import matplotlib.pyplot as plt
# DNA Validation
def validate_dna(dna):
    valid_bases = set("ATGC")
    for base in dna:
        if base not in valid_bases:
            return False
    return True
# Nucleotide Count
def nucleotide_count(dna):
    return {
        "A": dna.count("A"),
        "T": dna.count("T"),
        "G": dna.count("G"),
        "C": dna.count("C")
    }
# GC Content
def gc_content(dna):
    gc_count = dna.count("G") + dna.count("C")
    return (gc_count / len(dna)) * 100
# AT Content
def at_content(dna):
    return 100 - gc_content(dna)
# Sliding Window GC Analysis
def sliding_window_gc(dna, window_size):

    gc_percentages = []

    for i in range(len(dna) - window_size + 1):

        window = dna[i:i + window_size]

        gc_count = window.count("G") + window.count("C")

        gc_percentage = (gc_count / window_size) * 100

        gc_percentages.append(gc_percentage)

        print(
            "Window:",
            window,
            "→ GC:",
            round(gc_percentage, 2),
            "%"
        )

    return gc_percentages
# Main Program
dna = input("Enter DNA sequence: ").upper()

# Validate DNA
if not validate_dna(dna):

    print("Invalid DNA sequence!")
    print("Only A, T, G and C are allowed.")

else:

    print("\nDNA sequence is valid.")

    # DNA length
    print("DNA length:", len(dna))

    # Nucleotide counts
    counts = nucleotide_count(dna)

    print("\nNucleotide Counts:")

    print("A:", counts["A"])
    print("T:", counts["T"])
    print("G:", counts["G"])
    print("C:", counts["C"])

    # GC and AT content
    gc = gc_content(dna)
    at = at_content(dna)

    print("\nOverall Composition:")

    print("GC percentage:", round(gc, 2), "%")
    print("AT percentage:", round(at, 2), "%")

    # Classification
    if gc >= 50:
        print("Sequence classification: GC-rich")
    else:
        print("Sequence classification: AT-rich")

    # Window size
    window_size = int(input("\nEnter sliding window size: "))

    if window_size <= 0:
        print("Window size must be greater than 0.")

    elif window_size > len(dna):
        print("Window size cannot be larger than DNA sequence.")

    else:

        print("\nSliding Window GC Analysis:")

        gc_percentages = sliding_window_gc(
            dna,
            window_size
        )
        # GC Profile Graph
        
        positions = range(
            1,
            len(gc_percentages) + 1
        )
        plt.plot(
            positions,
            gc_percentages,
            marker="o"
        )
        plt.title("Sliding Window GC Content")
        plt.xlabel("Window Starting Position")
        plt.ylabel("GC Content (%)")
        plt.ylim(0, 100)
        plt.grid(True)
        plt.show()
