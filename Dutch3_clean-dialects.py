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
with open(f"data-Dutch/tsv_files/interval.tsv", "r") as r:
    lines  = r.read().splitlines()

    for id, line in enumerate(lines[1:]):
        elements = line.split("\t")
        if elements[1] not in intervals:
            intervals[elements[1]] = [id+1]
        else:
            intervals[elements[1]].append(id+1)

with open(f"data-Dutch/tsv_files/interval.tsv", "r") as r:
    lines  = r.read().splitlines()
    for dialect in dialects:
        if dialect in files:
            with open(f"data-Dutch/dialects_raw/{dialects[dialect]}.nld", "w") as wv:
                    for file in files[dialect]:
                        if file in tiers:
                            for tier in tiers[file]:
                                if tier in intervals:
                                    for interval in intervals[tier]:
                                        elements = lines[(int)(interval)].split("\t")
                                        wv.write(f"{elements[5]}\t{elements[7]}\n")