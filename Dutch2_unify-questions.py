dialects = {}

with open(f"data-Dutch/tsv_files/meetpunt.tsv", "r") as r:
    lines  = r.read().splitlines()

    for line in lines[1:]:
        elements = line.split("\t")
        dialects[elements[0]] = elements[2].replace("'", "")

files = {}
with open(f"data-Dutch/tsv_files/file.tsv", "r") as r:
    lines  = r.read().splitlines()

    for line in lines[1:]:
        elements = line.split("\t")
        if elements[1] not in files:
            files[elements[1]] = [elements[0]]
        else:
            files[elements[1]].append(elements[0])

tiers = {}
with open(f"data-Dutch/tsv_files/tier.tsv", "r") as r:
    lines  = r.read().splitlines()

    for line in lines[1:]:
        elements = line.split("\t")
        if elements[1] not in tiers:
            tiers[elements[1]] = [elements[0]]
        else:
            tiers[elements[1]].append(elements[0])

intervals = {}
questions = []
with open(f"data-Dutch/tsv_files/interval.tsv", "r") as r:
    lines  = r.read().splitlines()

    for id, line in enumerate(lines[1:]):
        elements = line.split("\t")
        if len(elements) >=8 and elements[7] not in questions and elements[7] != "":
            questions.append(elements[7])
        if elements[1] not in intervals:
            intervals[elements[1]] = [id+1]
        else:
            intervals[elements[1]].append(id+1)

with open(f"data-Dutch/tsv_files/interval.tsv", "r") as r:
    lines  = r.read().splitlines()
    for question in questions[0:10]:
        with open(f"data-Dutch/questions_raw/{question}.nld", "w") as wv:
            for dialect in dialects:
                if dialect in files:
                    for file in files[dialect]:
                        if file in tiers:
                            for tier in tiers[file]:
                                if tier in intervals:
                                    found = False
                                    sent = ""
                                    for interval in intervals[tier]:
                                        elements = lines[(int)(interval)].split("\t")
                                        if elements[7] == question and not found:
                                            found = True
                                            sent += f"{dialects[dialect]}\t{elements[5]}\n"
                                            continue
                                        if elements[7] == question and found:
                                            found = True
                                            sent += f"{dialects[dialect]}\t{elements[5]}\n"
                                            continue
                                        if elements[7] == "''" and found:
                                            found = True
                                            sent += f"{dialects[dialect]}\t{elements[5]}\n"
                                            continue
                                        if elements[7] != "''" and elements[7] != question:
                                            found = False
                                            continue
                                    wv.write(sent)