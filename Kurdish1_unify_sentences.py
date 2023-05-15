with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Kurdish/tsv_files/KurdishDialectsMT.tsv", "r") as r:
    lines = r.read().splitlines()

with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Kurdish/dialects_clean/Silêmanî.ckb", "w") as w:
    for line in lines[1:]:
        sent = line.split("\t")[0]
        w.write(f"{sent}\n")

with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Kurdish/dialects_clean/Sine.ckb", "w") as w:
    for line in lines[1:]:
        sent = line.split("\t")[1]
        w.write(f"{sent}\n")

with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Kurdish/dialects_clean/Mehabad.ckb", "w") as w:
    for line in lines[1:]:
        sent = line.split("\t")[2]
        w.write(f"{sent}\n")