import matplotlib.pyplot as plt

dna = "ATGCCATCCGATCGATTACGGGA"

gc_count = 0

for base in dna:
    if base == "G" or base == "C":
        gc_count += 1

gc_content = (gc_count / len(dna)) * 100
at_content = 100 - gc_content

print("DNA length:", len(dna))
print("GC percentage:", round(gc_content, 2), "%")
print("AT percentage:", round(at_content, 2), "%")


# Sliding window analysis
window_size = 5
gc_percentages = []

for i in range(len(dna) - window_size + 1):
    window = dna[i:i + window_size]

    gc_count_window = window.count("G") + window.count("C")
    gc_percentage_window = (gc_count_window / window_size) * 100

    gc_percentages.append(gc_percentage_window)

    print(window, "→ GC:", round(gc_percentage_window, 2), "%")


# GC profile graph
positions = range(1, len(gc_percentages) + 1)

plt.plot(positions, gc_percentages, marker="o")

plt.title("GC Content Across DNA Sequence")
plt.xlabel("Window Position")
plt.ylabel("GC Percentage")

plt.show()
