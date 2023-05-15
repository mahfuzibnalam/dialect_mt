with open(f"data-Dutch/sand_data.sql", "r") as r:
    lines = r.read().splitlines()

def Convert(header, table_name, file_name):
    with open(f"data-Dutch/tsv_files/{file_name}.tsv", "w") as w:
        w.write(f"{header}")
        for line in lines:
            if table_name in line:
                found = False
                for char in line:
                    if char == "(":
                        found = True
                        sentence = ""
                        continue
                    if char == ")":
                        found = False
                        elements = sentence.split(",")
                        for element in elements:
                            w.write(f"{element}\t")
                        w.write("\n")
                        continue

                    if found:
                        sentence += char

Convert("interval_id\ttier_id\tinterval_nr\txmin\txmax\ttekst\ttype_zin\tvraag_nr\tkomt_voor\t\n", "INSERT INTO `praat_interval`", "interval")
Convert("tier_id\tfile_id\ttier_nr\tname\t\n", "INSERT INTO `praat_tier`", "tier")
Convert("file_id\tmeetpunt_id\txmin\txmax\tfilenaam\toffset\tdatum_toegevoegd\tdatum_opname\tsoundfile\tcd\t\n", "INSERT INTO `praat_file`", "file")
Convert("meetpunt_id\tkloeke_nr\tplaatsnaam\ttranscribent\t\n", "INSERT INTO `meetpunt`", "meetpunt")

