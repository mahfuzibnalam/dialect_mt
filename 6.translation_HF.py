import glob
import argparse
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

parser = argparse.ArgumentParser()
parser.add_argument("--model", help="echo the string you use here", default="nllb-200-distilled-600M")
args = parser.parse_args()
access_token = "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"

tokenizer = AutoTokenizer.from_pretrained(f"facebook/{args.model}", use_auth_token=access_token, src_lang="ita_Latn")
model = AutoModelForSeq2SeqLM.from_pretrained(f"facebook/{args.model}", use_auth_token=access_token)

filenames = glob.glob(f"data/dialects_clean/*")

for filename in filenames:
    with open(filename, r) as r:
        articles = r.read().splitlines()
    with open(filename, r) as r:
        articles = r.read().splitlines()
    for article in articles:    
        article = "Şeful ONU spune că nu există o soluţie militară în Siria"
        inputs = tokenizer(article, return_tensors="pt")

        translated_tokens = model.generate(
            **inputs, forced_bos_token_id=tokenizer.lang_code_to_id["eng_Latn"], max_length=30
        )
        translation = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        print(translation)