import os
import argparse
from comet import load_from_checkpoint

parser = argparse.ArgumentParser()
parser.add_argument("--lang", help="echo the string you use here", default="Bengali")
parser.add_argument("--lang_code", help="echo the string you use here", default="ben")
args = parser.parse_args()

model = load_from_checkpoint(f"/home/mahfuz/Research/MachineTranslation/COMET/wmt22-comet-da/checkpoints/model.ckpt")

dialects = "Barisal;Dhakaiya;Jessore;Khulna;Kushtia"

os.system(f"mkdir scores/{args.lang}")
os.system(f"mkdir scores/{args.lang}/COMET")

for mtmodel in ["nllb-200-distilled-600M", "nllb-200-distilled-1.3B", "nllb-200-1.3B", "nllb-200-3.3B"]:
    os.system(f"mkdir scores/{args.lang}/COMET/dialects_{mtmodel}_translation")
    with open(f"scores/{args.lang}/COMET_dialects_avg_{mtmodel}.txt", "w") as ww:
        for dialect in dialects.split(";"):
            dialect = dialect.replace(" ", "_")
            filename = f"data-{args.lang}/dialects_{mtmodel}_translation/{dialect}.eng"
            with open(filename, "r") as r:
                lines = r.read().splitlines()
            with open(f"data-{args.lang}/dialects_clean/{dialect}.{args.lang_code}", "r") as r:
                slines = r.read().splitlines()
            with open(f"data-{args.lang}/all/raw.eng", "r") as r:
                rlines = r.read().splitlines()
            

            filename = filename.replace(f"data-{args.lang}", f"scores/{args.lang}/COMET")
            filename = filename.replace(f".{args.lang_code}", ".eng")

            datas = []
            for id, line in enumerate(lines):
                if line != "" and line != ". . .":
                    data = {
                            "src": "",
                            "mt": line,
                            "ref": rlines[id]
                        }
                    datas.append(data)
            model_output = model.predict(datas, batch_size=32, gpus=1)
            ww.write(f"{model_output[1]}\n")
            cnt = 0
            with open(f"{filename}", "w") as w:
                for id, line in enumerate(lines):
                    if line != "" and line != ". . .":
                        score = model_output[0][cnt]
                        cnt += 1
                        w.write(f"{score}\n")
                    else:
                        w.write("\n")