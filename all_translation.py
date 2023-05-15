import os
import glob
import argparse
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

parser = argparse.ArgumentParser()
parser.add_argument("--model", help="echo the string you use here", default="nllb-200-distilled-600M")
parser.add_argument("--code", help="echo the string you use here", default="ben_Beng")
parser.add_argument("--lang", help="echo the string you use here", default="Bengali")
args = parser.parse_args()
access_token = "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"

tokenizer = AutoTokenizer.from_pretrained(f"facebook/{args.model}", use_auth_token=access_token, src_lang=args.code)
model = AutoModelForSeq2SeqLM.from_pretrained(f"facebook/{args.model}", use_auth_token=access_token)

filenames = glob.glob(f"data-{args.lang}/*")
model_name = args.model.split("/")[0]

os.system(f"mkdir data-{args.lang}/dialects_{model_name}_translation")
for filename in filenames:
    with open(filename, "r") as r:
        articles = r.read().splitlines()
    
    filename = filename.replace(f"data-{args.lang}/", f"data-{args.lang}/dialects_{model_name}_translation/")
    lang_code = args.code.split("_")[0]
    filename = filename.replace(lang_code, "eng")
    with open(filename, "w") as w:
        for article in articles:
            if article != "":
                inputs = tokenizer(article, return_tensors="pt")

                translated_tokens = model.generate(
                    **inputs, forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"], max_length=30
                )
                translation = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
                w.write(f"{translation}\n")
            else:
                w.write("\n")
