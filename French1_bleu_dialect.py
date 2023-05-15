import os
import argparse
from sacrebleu.metrics import BLEU

parser = argparse.ArgumentParser()
parser.add_argument("--lang", help="echo the string you use here", default="French")
parser.add_argument("--lang_code", help="echo the string you use here", default="fra")
args = parser.parse_args()

dialects = "Occitan"

os.system(f"mkdir scores/{args.lang}")
os.system(f"mkdir scores/{args.lang}/BLEU")

bleu = BLEU()
for model in ["nllb-200-distilled-600M", "nllb-200-distilled-1.3B", "nllb-200-1.3B", "nllb-200-3.3B"]:
    os.system(f"mkdir scores/{args.lang}/BLEU/dialects_{model}_translation")
    with open(f"data-{args.lang}/dialects_{model}_translation/ref.eng", "r") as r:
        rlines = r.read().splitlines()
    with open(f"scores/{args.lang}/BLEU_dialects_avg_{model}.txt", "w") as ww:
        for dialect in dialects.split(";"):
            dialect = dialect.replace(" ", "_")
            filename = f"data-{args.lang}/dialects_{model}_translation/{dialect}.eng"
            with open(filename, "r") as r:
                lines = r.read().splitlines()

            filename = filename.replace(f"data-{args.lang}", f"scores/{args.lang}/BLEU")
            filename = filename.replace(f".{args.lang_code}", ".eng")
            avg = 0.0
            cnt = 0
            with open(filename, "w") as w:
                for id, line in enumerate(lines):
                    if line != "" and line != ". . .":
                        score = bleu.corpus_score([line], [[rlines[id]]])
                        avg += score.score
                        cnt += 1
                        w.write(f"{score.score}\n")
                    else:
                        w.write("\n")
            print(cnt)
            ww.write(f"{avg/cnt}\n")