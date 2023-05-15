import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--lang", help="echo the string you use here", default="Italian")
parser.add_argument("--lang_code", help="echo the string you use here", default="ita")
args = parser.parse_args()

communes = "Albosaggia;Aldeno;Altare;Arcola;Arenzano;Ne;Bergantino;Bologna;Bondeno;Borgofranco d'Ivrea;Borgomanero;Calizzano;Casalmaggiore;\
Casarza Ligure;Villa Lagarina;Cencenighe Agordino;Cesena;Cicagna;Cividale del Friuli;Colle di Val d'Elsa;Comano;Farra di Soligo;\
Favale di Malvaro;Finale Ligure;Firenze;Forlì;La Spezia;Lecco;Longare;Malonno;Mantova;Venezia;Milano;Moimacco;Moncalieri;Mondovì;\
Monno;Sover;Motta di Livenza;Novi Ligure;Imperia;Padova;Palazzolo dello Stella;Palmanova;Poirino;Pontinvrea;Pramaggiore;Chiomonte;\
Fontanigorda;Remanzacco;Rimini;Riomaggiore;Chieri;Rivarossa;Prali;Rovereto;Salzano;San Michele al Tagliamento;Scorzè;\
Selva di Val Gardena/Wolkenstein in Groeden;Tezze sul Brenta;Torino;Trecate;Treviso;Trieste;Trissino;Vallecrosia;Vaprio d'Adda;Vione;\
Alassio;Alba;Altavilla Vicentina;Montecchio Maggiore;Amblar;Andreis;Aquileia;Arsiero;Bagnolo San Vito;Barcis;Biancavilla;Borghetto di Vara;\
Corte Franca;Borgo San Martino;Bormio;Bovolone;Noale;Brione;Cairo Montenotte;Calalzo di Cadore;Calcinate;Caldogno;Asti;Camisano Vicentino;\
Brugine;Carcare;Carmignano di Brenta;Carpi;Carrara;Campitello di Fassa;Cesiomaggiore;Chiavari;Chies d'Alpago;Chioggia;Cimolais;Belluno;\
Claut;Forni Avoltri;Colognola ai Colli;Cordenons;Corvara in Badia/Corvara;Due Carrare;Erto e Casso;Cittadella;Falcade;\
Sernaglia della Battaglia;Ferrara;Sondalo;Galliera Veneta;Gazzo;Arcole;Montegaldella;Gorizia;Gradara;Grosio;Illasi;Iseo;Jesolo;Lamon;\
Rocca Pietore;Albignasego;Livigno;Lonato del Garda;Sandrigo;Luzzara;Marostica;Maserà di Padova;Mason Vicentino;Arsiè;Mirano;Monselice;\
Montecchio Precalcino;Montereale Valcellina;Nimis;Tassullo;Ortisei/St. Ulrich;Osimo;Comelico Superiore;Vodo Cadore;Pianiga;Piove di Sacco;\
Pozza di Fassa;Pieve di Cadore;Angrogna;Puos d'Alpago;Reana del Rojale;Quinto Vicentino;Redondesco;Revò;Romano d'Ezzelino;Ronzone;Rovigo;\
Rovolon;Badia/Abtei;San Martino di Lupari;San Pietro in Gu;Santa Maria di Sala;Savona;Samolaco;Schio;Selvazzano Dentro;Valdidentro;Solesino;\
Calasetta;Taggia;Taglio di Po;Teglio Veneto;Teolo;Pieve d'Alpago;Tollegno;Treia;Triggiano;Valdagno;Valfurva;Vallarsa;Verona;Vicenza;Vidor;\
Villa di Chiavenna;Stazzona;Villafranca Padovana;Villaverla;Villorba;Zero Branco;Correzzola;Agugliaro;Vittorio Veneto;Ariano Irpino;Avellino;\
Bari;Bitti;Castrignano del Capo;Catania;Corigliano d'Otranto;Corleone;Cosenza;Crotone;Gallipoli;Laino Castello;Locorotondo;Locri;Macerata;\
Marcianise;Melfi;Messina;Molfetta;Monasterace;Montella;Ortelle;Ossi;Paciano;Palermo;Papasidero;Pennapiedimonte;Posada;San Cesario di Lecce;\
San Marco in Lamis;San Martino in Pensilis;Sciacca;Terravecchia;Trepuzzi;Trevico;Troina;Venosa;Santa Cesarea Terme;Termoli;Tricase;Capurso;\
Lesina;Bagnoregio;Campi Salentina;Campobasso;Cardito;Carosino;Castiglione Messer Marino;Copertino;Cutrofiano;Faggiano;Francavilla Fontana;\
Gragnano;Grottaglie;Iglesias;Lanciano;L'Aquila;Lecce;Liscia;Lubriano;Maglie;Civitanova Marche;Martina Franca;Martinsicuro;Massafra;\
Mazara del Vallo;Monteiasi;Monteroni di Lecce;Monterotondo;Morolo;Mussomeli;Napoli;Nardò;Orvieto;Pescara;Pianella;Ragusa;Roma;Salerno;\
San Valentino in Abruzzo Citeriore;Sinagra;Soleto;Squinzano;Taranto;Torre del Greco;Villacidro;Sutrio;Lizzano;Abano Terme;Udine;\
Selva di Progno;Luserna;Palù del Fersina;Casale sul Sile"

provinces = "Sondrio;Trento;Savona;La Spezia;Genova;Rovigo;Bologna;Ferrara;Torino;Novara;Cremona;Belluno;Forlì-Cesena;Udine;Siena;\
Massa-Carrara;Treviso;Firenze;Lecco;Vicenza;Brescia;Mantova;Venezia;Milano;Cuneo;Alessandria;Imperia;Padova;Rimini;Bolzano/Bozen;\
Trieste;Pordenone;Catania;Verona;Bergamo;Asti;Modena;Gorizia;Pesaro Urbino;Reggio nell'Emilia;Ancona;Carbonia-Iglesias;Biella;Macerata;\
Bari;Como;Avellino;Nuoro;Lecce;Palermo;Cosenza;Crotone;Reggio di Calabria;Caserta;Potenza;Messina;Sassari;Perugia;Chieti;Foggia;\
Campobasso;Agrigento;Enna;Viterbo;Napoli;Taranto;Brindisi;L'Aquila;Teramo;Trapani;Roma;Frosinone;Caltanissetta;Terni;Pescara;Ragusa;\
Salerno;Medio Campidano"

regions = "Lombardia;Trentino Alto Adige;Liguria;Veneto;Emilia Romagna;Piemonte;Friuli Venezia Giulia;Toscana;Sicilia;Marche;Sardegna;\
Puglia;Campania;Calabria;Basilicata;Umbria;Abruzzo;Molise;Lazio"

numbers = {}
with open(f"data-Italian/all/numbers.txt", "r") as r:
    lines = r.read().splitlines()
    for line in lines:
        numbers[line.split("\t")[0]] = int(line.split("\t")[1])

##  Bucket Code
# final_indexes = [i for i in range(0,792)]
# for dialect in numbers:
#     dialect = dialect.replace(" ", "_")
#     filename = f"data-{args.lang}/dialects_clean/{dialect}.{args.lang_code}"
#     with open(filename, "r") as r:
#         lines = r.read().splitlines()

#     indexes = []
#     for id, line in enumerate(lines):
#         if line != "":
#             indexes.append(id)

#     final_indexes = list(set(indexes) & set(final_indexes))
#     if len(final_indexes) == 0:
#         print(1)

for scoretyp in ["BLEU", "COMET"]:
    for typ in ["commune"]:
        if typ == "dialect":
            for mtmodel in ["DeltaLM", "nllb-200-distilled-600M", "nllb-200-distilled-1.3B", "nllb-200-1.3B", "nllb-200-3.3B"]:
                with open(f"scores/{args.lang}/{scoretyp}_dialects_avg_{mtmodel}.txt", "w") as ww:
                    for dialect in numbers:
                        if numbers[dialect] >= 50 :
                            avg = 0.0
                            with open(f"scores/{args.lang}/{scoretyp}/dialects_{mtmodel}_translation/{dialect}.eng", "r") as r:
                                lines = r.read().splitlines()
                            scores = []
                            for line in lines:
                                if line != "":
                                    scores.append(float(line))
                            for seed in range(1,101):
                                random.seed(seed)
                                randscores = random.choices(scores, k=50)
                                avg += sum(randscores) / 50
                            
                            ww.write(f"{avg / 100}\n")
        else:
            if typ == "region":
                alls = regions
                id = -1
            if typ == "province":
                alls = provinces
                id = -2
            if typ == "commune":
                alls = communes
                id = -3
            alltodialect = {}
            for all in alls.split(';'):
                alltodialect[all] = []

            with open(f"data-Italian/all/dialects.txt", "r") as r:
                lines = r.read().splitlines()

            for line in lines:
                all = line.split("\t")[1].split(",")[id]
                dialect = line.split("\t")[0]
                dialect = dialect.replace(" ", "_")
                dialect = dialect.replace("'", "")
                if dialect not in alltodialect[all]:
                    alltodialect[all].append(dialect)
            for mtmodel in ["DeltaLM", "nllb-200-distilled-600M", "nllb-200-distilled-1.3B", "nllb-200-1.3B", "nllb-200-3.3B"]:
                with open(f"scores/{args.lang}/{scoretyp}_{typ}s_avg_{mtmodel}.txt", "w") as ww:
                    for all in alltodialect:
                        bigavg = 0.0
                        cnt = 0
                        for dialect in alltodialect[all]:
                            if numbers[dialect] >= 50 :
                                with open(f"scores/{args.lang}/{scoretyp}/dialects_{mtmodel}_translation/{dialect}.eng", "r") as r:
                                    lines = r.read().splitlines()
                                scores = []
                                for line in lines:
                                    if line != "":
                                        scores.append(float(line))
                                avg = 0.0
                                cnt += 1
                                for seed in range(1,101):
                                    random.seed(seed)
                                    randscores = random.choices(scores, k=50)
                                    avg += sum(randscores) / 50 
                                avg = avg / 100
                                bigavg += avg
                        if cnt > 0:
                            ww.write(f"{bigavg / cnt}\n")
                        else:
                            print(all)
                            ww.write(f"\n")