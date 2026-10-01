DNA = "ATCGATGCATGCAACCAA"
 gc_count = 0
for base in DNA:
  if base == "G" or base == "C"
gc_count += 1
gc_content = (gc_count / len(DNA)) * 100
print("DNA length: ", len(DNA))
print("GC percentage: ", round(gc_content, 2), "%")
