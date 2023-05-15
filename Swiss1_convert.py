chapters = ["i", "ii", "iii", "iv"]
numbers = [20, 32, 28, 38]

with open(f"data-Swiss/all/raw.txt") as r:
    rawlines = r.read().splitlines()

uid = 1
with open(f"data-Swiss/all/raw-dialect.txt", "w") as w:
    for id, chapter in enumerate(chapters):
        dialects = [{}]
        for number in range(1, numbers[id] + 1):
            filename = f"data-Swiss/tsv_files/{chapter}{number}.csv"
            with open(filename, "r") as r:
                lines = r.read().splitlines()
            
            w.write(f"{uid}\t{rawlines[uid - 1]}\n")
            for line in lines[1:]:
                elements = line.split(";")
                if elements[2] not in dialects:
                    dialects.append(elements[2])
                    w.write(f"{uid}\t{elements[2]}\n")
            uid += 1