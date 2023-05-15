import glob

filenames = glob.glob(f"data-Basque/tsv_files/*.txt")

with open("data-Basque/all/raw.txt", "r") as r:
    rawsents = r.read().splitlines()
for filename in filenames:
    data = {}
    with open(filename, "r") as r:
        lines = r.read().splitlines()
        for id, line in enumerate(lines):
            if "Galderaren erantzuna" in line:
                oid = id
            if oid + 3 == id and line != "\tBai" and line != "\tEz.":
                data[lines[id-2].strip()] = line.strip()
    
    filename = filename.replace("tsv_files", "dialects_clean")
    filename = filename.replace("txt", "eus")
    with open(filename, "w") as w:
        for sent in rawsents:
            if sent in data:
                w.write(f"{data[sent]}\n")
            else:
                w.write(f"\n")  
