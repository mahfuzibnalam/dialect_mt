with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Tigrinya/tsv_files/all.en-ti_ER.tmx", "r") as r:
    lines = r.read().splitlines()
    with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Tigrinya/dialects_clean/Eritrean.tir", "w") as w:
        for line in lines:
            if '<tuv xml:lang="ti-ER"><seg>' in line:
                sent = line.replace('<tuv xml:lang="ti-ER"><seg>', "")
                sent = sent.replace("</seg></tuv>", "")
                w.write(f"{sent}\n")

with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Tigrinya/tsv_files/all.en-ti_ET.tmx", "r") as r:
    lines = r.read().splitlines()
    with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Tigrinya/dialects_clean/Ethiopian.tir", "w") as w:
        for line in lines:
            if '<tuv xml:lang="ti-ET"><seg>' in line:
                sent = line.replace('<tuv xml:lang="ti-ET"><seg>', "")
                sent = sent.replace("</seg></tuv>", "")
                w.write(f"{sent}\n")

with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Tigrinya/tsv_files/all.en-ti_ET.tmx", "r") as r:
    lines = r.read().splitlines()
    with open(f"/home/mahfuz/Research/MachineTranslation/Dialect/dialect/data-Tigrinya/all/raw.eng", "w") as w:
        for id, line in enumerate(lines):
            if '<tuv xml:lang="en">' in line:
                sent = lines[id + 1].replace('<seg>', "")
                sent = sent.replace("</seg></tuv>", "")
                w.write(f"{sent}\n")