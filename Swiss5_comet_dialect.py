import os
import argparse
from comet import load_from_checkpoint

parser = argparse.ArgumentParser()
parser.add_argument("--lang", help="echo the string you use here", default="Swiss_German")
parser.add_argument("--lang_code", help="echo the string you use here", default="deu")
args = parser.parse_args()

model = load_from_checkpoint(f"/home/mahfuz/Research/MachineTranslation/COMET/wmt22-comet-da/checkpoints/model.ckpt")

dialects = "Aarau,AG;Aarberg,BE;Aarburg,AG;Adelboden,BE;Aedermannsdorf,SO;Aesch,BL;Aeschi,SO;Agarn,VS;Alpnach,OW;Alpthal,SZ;\
Altdorf,UR;Altstätten,SG;Amden,SG;Amriswil,TG;Andelfingen,ZH;Andermatt,UR;Andwil,SG;Appenzell,AI;Arosa,GR;Ausserberg,VS;\
Avers,GR;Bäretswil,ZH;Baldingen,AG;Basadingen-Schlattingen,TG;Basel,BS;Bassersdorf,ZH;Bauma,ZH;Belp,BE;Benken,SG;Bern,BE;\
Berneck,SG;Betten,VS;Bettingen,BS;Bettlach,SO;Bibern,SH;Binn,VS;Birmenstorf,AG;Birwinken,TG;Blatten,VS;Bleienbach,BE;\
Boltigen,BE;Boniswil,AG;Boswil,AG;Bottighofen,TG;Bremgarten,AG;Brienz,BE;Brig-Glis,VS;Rüte,AI;Brugg,AG;Brunnadern,SG;\
Ingenbohl,SZ;Buchberg,SH;Buckten,BL;Bühler,AR;Bülach,ZH;Bürchen,VS;Büren an der Aare,BE;Buochs,NW;Busswil bei Büren,BE;\
Chur,GR;Churwalden,GR;Dagmersellen,LU;Davos,GR;Degersheim,SG;Densbüren,AG;Diemtigen,BE;Diepoldsau,SG;Diessbach bei Büren,BE;\
Düdingen,FR;Ebnat-Kappel,SG;Egg,ZH;Eglisau,ZH;Einsiedeln,SZ;Elfingen,AG;Elgg,ZH;Ellikon an der Thur,ZH;Elm,GL;Engelberg,OW;Engi,GL;\
Entlebuch,LU;Erlach,BE;Ermatingen,TG;Erschwil,SO;Eschenbach,LU;Escholzmatt,LU;Ettingen,BL;Fällanden,ZH;Trub,BE;Spiez,BE;Ferden,VS;\
Fiesch,VS;Fischingen,TG;Flaach,ZH;Fläsch,GR;Flawil,SG;Flühli,LU;Flums,SG;Maur,ZH;Frauenfeld,TG;Frauenkappelen,BE;Fribourg,FR;Frick,AG;\
Frutigen,BE;Gadmen,BE;Gächlingen,SH;Gais,AR;Gelterkinden,BL;Giffers,FR;Giswil,OW;Glarus,GL;Göschenen,UR;Grabs,SG;Grafenried,BE;\
Grindelwald,BE;Grosswangen,LU;Gossau,ZH;Gsteig,BE;Guggisberg,BE;Gurmels,FR;Gurtnellen,UR;Guttannen,BE;Guttet-Feschel,VS;Habkern,BE;\
Hägglingen,AG;Hallau,SH;Schlatt-Haslen,AI;Hedingen,ZH;Heiden,AR;Heitenried,FR;Herisau,AR;Hölstein,BL;Homburg,TG;Horw,LU;Hünenberg,ZG;\
Hütten,ZH;Hüttwilen,TG;Huttwil,BE;Illnau-Effretikon,ZH;Inden,VS;Innerthal,SZ;Innertkirchen,BE;Ins,BE;Interlaken,BE;Iseltwald,BE;\
Isenthal,UR;Ittigen,BE;Jaun,FR;Jenins,GR;Kaiserstuhl,AG;Kaisten,AG;Kandersteg,BE;Kappel am Albis,ZH;Kesswil,TG;Reichenbach im Kandertal,BE;\
Kirchberg,SG;Kirchleerau,AG;Kleinlützel,SO;Klosters-Serneus,GR;Konolfingen,BE;Krauchthal,BE;Krinau,SG;Küblis,GR;Küsnacht,ZH;Küssnacht am Rigi,SZ;\
Lachen,SZ;Langenbruck,BL;Langenthal,BE;Langnau im Emmental,BE;Langnau am Albis,ZH;Langwies,GR;Laufen,BL;Laupen,BE;Lauterbrunnen,BE;Leibstadt,AG;\
Leissigen,BE;Lenk,BE;Lenzburg,AG;Liesberg,BL;Liestal,BL;Ligerz,BE;Linthal,GL;Luchsingen,GL;Lützelflüh,BE;Lungern,OW;Lupfig,AG;Thundorf,TG;\
Luzern,LU;Silenen,UR;Magden,AG;Maisprach,BL;Malans,GR;Malters,LU;Mammern,TG;Marbach,LU;Marthalen,ZH;St.Stephan,BE;Meikirch,BE;Meilen,ZH;\
Meiringen,BE;Melchnau,BE;Kerns,OW;Mels,SG;Brunegg,AG;Menzingen,ZG;Merenschwand,AG;Merishausen,SH;Metzerlen,SO;Möhlin,AG;Mörel,VS;Mörschwil,SG;\
Mollis,GL;Mosnang,SG;Mümliswil-Ramiswil,SO;Münchenbuchsee,BE;Muhen,AG;Muotathal,SZ;Murten,FR;Mutten,GR;Muttenz,BL;Näfels,GL;Uster,ZH;Neftenbach,ZH;\
Neuenegg,BE;Neuenkirch,LU;Kradolf-Schönenberg,TG;Niederbipp,BE;Niederrohrdorf,AG;Niederweningen,ZH;Nunningen,SO;Oberägeri,ZG;Oberhof,AG;Oberiberg,SZ;\
Oberriet,SG;Obersaxen,GR;Oberwald,VS;Oberwichtrach,BE;Obstalden,GL;Pfäfers,SG;Pfäffikon,ZH;Pfaffnau,LU;Pieterlen,BE;Plaffeien,FR;Pratteln,BL;\
Quarten,SG;Rafz,ZH;Ramsen,SH;Randa,VS;Rapperswil,BE;Reckingen,VS;Regensberg,ZH;Reutigen,BE;Rheineck,SG;Medels im Rheinwald,GR;Wattwil,SG;\
Rickenbach,SO;Rifferswil,ZH;Murgenthal,AG;Römerswil,LU;Röthenbach im Emmental,BE;Roggenburg,BL;Roggwil,TG;Romanshorn,TG;Rorbas,ZH;Risch,ZG;\
Rubigen,BE;Rüeggisberg,BE;Rümlang,ZH;Ruswil,LU;Saanen,BE;Saas Grund,VS;Safien,GR;Salgesch,VS;Sarnen,OW;Schänis,SG;Schaffhausen,SH;Schangnau,BE;\
Schiers,GR;Schleitheim,SH;Schnottwil,SO;Schönenbuch,BL;Schüpfheim,LU;Schwanden,GL;Wahlern,BE;Schwyz,SZ;Seftigen,BE;Sempach,LU;Sennwald,SG;Sevelen,SG;\
Siglistorf,AG;Signau,BE;Simplon,VS;Zihlschlacht-Sitterdorf,TG;Solothurn,SO;St.Antönien,GR;St.Gallen,SG;St.Niklaus,VS;Stadel,ZH;Stallikon,ZH;Stans,NW;\
Steffisburg,BE;Steg,VS;Stein,AG;Stein am Rhein,SH;Sternenberg,ZH;Stüsslingen,SO;Sumiswald,BE;Sursee,LU;Täuffelen,BE;Tafers,FR;Tamins,GR;Teufenthal,AG;\
Thalwil,ZH;Thun,BE;Thusis,GR;Triengen,LU;Trimmis,GR;Trogen,AR;Tüscherz-Alfermée,BE;Tuggen,SZ;Turbenthal,ZH;Ueberstorf,FR;Unterschächen,UR;\
Unterstammheim,ZH;Untervaz,GR;Urdorf,ZH;Urnäsch,AR;Ursenbach,BE;Utzenstorf,BE;Vals,GR;Villigen,AG;Visp,VS;Visperterminen,VS;Wädenswil,ZH;\
Wängi,TG;Walchwil,ZG;Wald,ZH;Waldstatt,AR;Walenstadt,SG;Wangen an der Aare,BE;Wartau,SG;Wegenstetten,AG;Weggis,LU;Weinfelden,TG;Welschenrohr,SO;\
Wengi,BE;Wiesen,GR;Wil,SG;Wilchingen,SH;Wildhaus,SG;Willisau Stadt,LU;Winterthur,ZH;Wolfenschiessen,NW;Wolhusen,LU;Wollerau,SZ;Worb,BE;Würenlos,AG;\
Wynigen,BE;Zell,LU;Zermatt,VS;Ziefen,BL;Zofingen,AG;Zürich,ZH;Zug,ZG;Zunzgen,BL;Zweisimmen,BE;Bibern,SO;Eschenbach,SG;Stein,SG"

regions = "AG;BE;SO;BL;VS;OW;SZ;UR;SG;TG;ZH;AI;GR;BS;SH;AR;NW;LU;FR;GL;ZG"

os.system(f"mkdir scores/{args.lang}")
os.system(f"mkdir scores/{args.lang}/COMET")

for mtmodel in ["nllb-200-distilled-600M", "nllb-200-distilled-1.3B", "nllb-200-1.3B", "nllb-200-3.3B"]:
    for typ in ["dialect", "region"]:
        if typ == "region":
            alls = regions
            alltodialect = {}
            for all in alls.split(';'):
                alltodialect[all] = []

            with open(f"data-{args.lang}/all/dialects.txt", "r") as r:
                lines = r.read().splitlines()

            for line in lines:
                region = line.split(",")[-1]
                alltodialect[region].append(line)
            
            with open(f"scores/{args.lang}/COMET_{typ}s_avg_{mtmodel}.txt", "w") as ww:
                for all in alltodialect:
                    avg = 0.0
                    cnt = 0
                    for dialect in alltodialect[all]:
                        with open(f"scores/{args.lang}/COMET/dialects_{mtmodel}/{dialect}.eng", "r") as r:
                            lines = r.read().splitlines()
                            for line in lines:
                                if line != "":
                                    avg += (float)(line)
                                    cnt +=1
                    print(cnt)
                    ww.write(f"{avg/cnt}\n")

        else:
            os.system(f"mkdir scores/{args.lang}/COMET/dialects_{mtmodel}")
            with open(f"scores/{args.lang}/COMET_dialects_avg_{mtmodel}.txt", "w") as ww:
                for dialect in dialects.split(";"):
                    filename = f"data-{args.lang}/dialects_{mtmodel}/{dialect}.eng"
                    with open(filename, "r") as r:
                        lines = r.read().splitlines()
                    with open(f"data-{args.lang}/dialects_{mtmodel}/{dialect}_standard.eng", "r") as r:
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