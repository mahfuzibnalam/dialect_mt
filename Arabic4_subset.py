import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--lang", help="echo the string you use here", default="Arabic")
parser.add_argument("--lang_code", help="echo the string you use here", default="arb")
args = parser.parse_args()

dialects = "Alexandria;Baghdad;Doha;Benghazi;Khartoum;Sfax;Muscat;Mosul;Riyadh;Sanaa;Aswan;\
Algiers;Tripoli;Jeddah;Rabat;Cairo;Jerusalem;Beirut;Basra;Tunis;Damascus;Salt;Fes;Aleppo;Amman"

final_indexes = []
for i, dialect in enumerate(dialects.split(";")):
    dialect = dialect.replace(" ", "_")
    filename = f"data-{args.lang}/dialects_clean/{dialect}.{args.lang_code}"
    with open(filename, "r") as r:
        lines = r.read().splitlines()

    indexes = []
    for id, line in enumerate(lines):
        if line != "":
            indexes.append(id)

    if i == 0 :
        final_indexes = indexes
    else:
        final_indexes = list(set(indexes) & set(final_indexes))

for mtmodel in ["nllb-200-distilled-600M", "nllb-200-distilled-1.3B", "nllb-200-1.3B", "nllb-200-3.3B"]:
    with open(f"scores/{args.lang}/BLEU_dialects_avg_{mtmodel}.txt", "w") as ww:
        for dialect in dialects.split(";"):
            dialect = dialect.replace(" ", "_")
            filename = f"data-{args.lang}/dialects_{mtmodel}_translation/{dialect}.eng"
            filename = filename.replace(f"data-{args.lang}", f"scores/{args.lang}/BLEU")
            filename = filename.replace(f".{args.lang_code}", ".eng")
            with open(f"{filename}", "r") as r:
                lines = r.read().splitlines()

            average = 0.0
            for id in final_indexes:
                score = (float)(lines[id])
                average += score
            cnt = len(final_indexes)
            ww.write(f"{average/cnt}\n")