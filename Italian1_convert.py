import pandas as pd
import glob

filenames = glob.glob(f"data-Italian/xls_files/*.xls")

for filename in filenames:
    data_xlsx = pd.read_excel(filename, index_col=None)
    data_xlsx.columns = [c.replace(' ', '_') for c in data_xlsx.columns]
    df = data_xlsx.replace('\n', ' ',regex=True)
    filename = filename.replace("xls", "tsv")
    df.to_csv(filename, sep='\t', encoding='utf-8',  index=False, line_terminator='\r\n')