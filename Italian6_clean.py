import glob 

# rawlines = []
# duplines = {}
# with open(f"data-Italian/all/raw-dialect.txt", "r") as r:
#     lines = r.read().splitlines()
#     for line in lines:
#         rawline = line.split("\t")[1]
#         if rawline in rawlines:
#             if rawline in duplines:
#                 duplines[rawline] += 1
#             else:
#                 duplines[rawline] = 2
#         else:
#             rawlines.append(rawline)
# duplines = dict(sorted(duplines.items(), key=lambda item: item[1], reverse = True))
# badlines = []
# for line in duplines:
#     if duplines[line] > 20:
#         badlines.append(line)

badlines = ['--> testo vuoto <---', '', 'non tradotta', 'omessa', '-', '---', 'Frase non tradotta']

filenames = glob.glob(f"data-Italian/dialects/ref.txt")

for filename in filenames:
    with open(filename, "r") as r:
        lines = r.read().splitlines()
    
    filename = filename.replace("dialects", "dialects_clean")
    filename = filename.replace("txt", "ita")
    filename = filename.replace(" ", "_")
    filename = filename.replace("'", "")
    with open(filename, "w") as w:
        for line in lines:
            if line in badlines:
                line = ""
            w.write(f"{line}\n")