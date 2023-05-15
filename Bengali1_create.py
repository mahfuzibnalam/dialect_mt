with open(f"dialect-Bengali/tsv_files/corpus.train.bn", "r") as r:
    blines = r.read().splitlines()
with open(f"dialect-Bengali/tsv_files/corpus.train.en", "r") as r:
    elines = r.read().splitlines()

with open(f"dialect-Bengali/tsv_files/selected.bn", "w") as wb:
    with open(f"dialect-Bengali/tsv_files/selected.en", "w") as we:
        for id, bline in enumerate(blines):
            words = bline.split(" ")
            if len(words) >= 6 and len(words) <= 7:
                wb.write(f"{bline}\n")
                we.write(f"{elines[id]}\n")
