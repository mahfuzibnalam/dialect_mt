import glob

filenames = glob.glob(f"data-Basque/tsv_files/*.txt")

rawsents = []
with open("data-Basque/all/raw.txt", "w") as w:
    with open("data-Basque/all/ref.eng", "w") as wr:
        for filename in filenames:
            with open(filename, "r") as r:
                lines = r.read().splitlines()
                for id, line in enumerate(lines):
                    if "Galderaren erantzuna" in line:
                        oid = id
                    if oid + 3 == id and line != "\tBai" and line != "\tEz.":
                        if lines[id-2].strip() not in rawsents and lines[id-1].strip() != "":
                            rawsents.append(lines[id-2].strip())
                            w.write(f"{lines[id-2].strip()}\n")
                            wr.write(f"{lines[id-1].strip()}\n")