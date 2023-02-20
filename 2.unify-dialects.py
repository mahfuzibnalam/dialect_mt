import glob

filenames = glob.glob(f"data/tsv_files/*.tsv")

dialectlines = []
with open("data/all/dialect.txt", "w") as w:
    for filename in filenames:
        with open(filename, "r") as r:
            lines = r.read().splitlines()
            for line in lines[1:]:
                elements = line.split("\t")
                if len(elements) >= 6 and elements[0] == "" and elements[1] == "":
                    if elements[3] not in dialectlines:
                        w.write(f"{elements[3]}\t{elements[4]}\t{elements[5]}\n")
                        dialectlines.append(elements[3])
