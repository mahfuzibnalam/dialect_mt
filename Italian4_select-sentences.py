import glob

filenames = glob.glob(f"data-Italian/tsv_files/*.tsv")

with open("data-Italian/all/raw.txt", "r") as r:
    rawlines = r.read().splitlines()

with open("data-Italian/all/raw-dialect.txt", "w") as w:
    for rawline in rawlines:
        dialectlines = []
        for filename in filenames:
            with open(filename, "r") as r:
                lines = r.read().splitlines()
                for line in lines[1:]:
                    elements = line.split("\t")
                    if len(elements) >= 3 and elements[0] != "" and elements[1] != "":
                        if elements[2] == rawline:
                            found = True
                        else:
                            found = False
                        continue

                    if found:
                        if len(elements) >= 4 and elements[0] == "" and elements[1] == "":
                            if elements[3] not in dialectlines:
                                w.write(f"{rawline}\t{elements[2]}\t{elements[3]}\n")
                                dialectlines.append(elements[3])
