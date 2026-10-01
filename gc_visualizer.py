import matplotlib.pyplot as plt
DNA = "ATGCAATGCATGCCC"
gc_count = 0
for base in DNA:
  if base == "G" or base == "C":
    gc_count += 1

gc_percentage = (gc_count / len(DNA)) * 100
at_content = 100 - gc_percentage
print("DNA length: ",len(DNA))
print("GC percentage: ",round(gc_percentage,2),"%")
print("AT content: ",round(at_content,2),"%")

labels = ["GC content", "AT content"]
values = [gc_content, at_content]

plt.bar(labels,values, color=["green","orange"])

plt.title("GC vs AT content")
plt.ylabel("Percentage")
plt.show()
