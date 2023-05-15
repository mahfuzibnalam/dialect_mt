import glob

filenames = glob.glob(f"data-Italian/tsv_files/*.tsv")

rawlines = []
with open("data-Italian/all/raw.txt", "w") as w:
    for filename in filenames:
        with open(filename, "r") as r:
            lines = r.read().splitlines()
            for line in lines[1:]:
                elements = line.split("\t")
                if len(elements) >= 3 and elements[0] != "" and elements[1] != "":
                    if elements[2] not in rawlines:
                        w.write(f"{elements[2]}\n")
                        rawlines.append(elements[2])
