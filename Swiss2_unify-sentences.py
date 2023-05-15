with open(f"data-Swiss/all/Antonis.txt", "r") as r:
    lines = r.read().splitlines()

id = 1
with open(f"data-Swiss/all/blank-dialect.txt", "w") as w:
    typ = False
    for line in lines:
        elements = line.split("\t")
        if elements[3] == "do":
            template = elements[2]
            typ = False
            continue
        elif elements[2] == "as is":
            typ = True
        else:
            if not typ:
                sentence = template.replace("[]", elements[4])
                sentence = sentence.replace("...", "")
                sentence = sentence.replace("…", "")
                sentence = sentence.replace(" ,", ",")
                sentence = sentence.replace(",,", ",")
                sentence = sentence.replace("  ", " ")
                w.write(f"{elements[0]}\t{elements[1]}\t{sentence}\n")
            if typ:
                w.write(f"{elements[0]}\t{elements[1]}\t{elements[4]}\n")
