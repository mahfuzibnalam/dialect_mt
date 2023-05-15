import os
import argparse
from sacrebleu.metrics import BLEU

parser = argparse.ArgumentParser()
parser.add_argument("--model", help="echo the string you use here", default="DeltaLM")
args = parser.parse_args()

dialects = "Padova6;Troina1;Calcinate;Vidor;Milano4;Vicenza;Motta di Livenza;Sinagra;Rovigo;Marcianise;Messina2;Galliera Veneta;\
Squinzano;Borghetto di Vara;Palermo10;Troina2;Longare;San Valentino in Abruzzo Citeriore;Melfi;Padova1;Osimo;Riomaggiore;\
San Valentino;Troina8;Civita di Bagnoregio 1;Monterotondo;Alba;Lesina;Bondeno;Poirino;Borgonato1;Orvietano;Illasi;\
Carmignano di Brenta;Termoli;Tollegno;Francavilla Fontana;Pianella8;Chiavari2;Zianigo;Arenzano;Vodo Di Cadore;Carpi;\
Marostica2;Granarola;San Marco in Lamis;Biancavilla;Pianella10;Cutrofiano;Palermo3;Lonato;Cividale;Capurso;Palermo6;\
Correzzola;Luzzara1;Livigno1;Iseo1;San Martino di Lupari 6;Ghizzole di Montegaldella;Piove di Sacco;Monteiasi;Troina7;\
Palermo4;Castiglione Messer Marino;Taglio di Po2;Rovereto;Torino5;Palermo8;Quinto Vicentino;Livigno2;Calitri;Cirvoi;\
Santa Maria di Sala 1;Bitti;Pianiga3;Nimis;Villacidro;Lamon;Carrara;Aquilano;Teolo;Macerata;Chies dAlpago;Soleto;Zianigo6;\
San Martino di Lupari2;Terranegra;Troina4;Nardò;Albosaggia;Mestre;Cicagna;Alassio;Bagnolo S. Vito;Padova100;Pianella5;Torino4;\
Borgoricco 1;Sciacca;Pontevigodarzere 3;Milano3;San Martino di Lupari 7;Scorzé;Aldeno2;Cencenighe Agordino;Venezia1;Vitigliano;\
Pianella1;Santa Maria di Sala 2;Gazzo;Pramaggiore;Roma;Lucanico;Bagnoli Irpino;San Pietro in Gu1;Amblar;Marchigiano;Vidor2;Salerno;\
Ariano Irpino;Tabarchino;Morolo;Arzeno;Riva presso Chieri;Mirano;Torino3;Iseo8;Bovolone;Copertino;Iseo5;Torino6;Vaprio dAdda;Chiavari1;\
Borgonato6;Monasterace2;Borgo San Martino;Troina3;Terravecchia;Frontale di Sondalo;Torino2;Venezia 6;Rivai di Arsiè;San Martino di Lupari 5;\
Troina9;Nones ;Ferrara1;Pennapiedimonte;Reisoni;Cardito1;Cosenza;Calliano;Castrignano del Capo;Due Carrare3;Papasidero;Ronzone 2;Arcola;\
Santa Maria di Sala;Tignes di Pieve dAlpago;Martina Franca;Borgonato3;Tai di Cadore;Altare;Massafra;Pozza di Fassa;Zianigo2;Pianiga;\
Rodoretto;Palermo2;Falzè di Piave;Monasterace1;padova2;Collina;Posada;Remanzacco;Mussomeli;Trissino;Triggiano;Taggia;Selvazzano Dentro;\
Palermo5;Liscia;San Pietro in Gu2;Trepuzzi;Marostica;Corigliano dOtranto;Montesover;San Martino in Pensilis;Padova8;Gazzolo;Pianella6;\
Vodo di Cadore;Casalmaggiore;Padova4;Pescara1;Veternigo;Taranto;Qualso;Mazara del Vallo;Ortisei;Pontinvrea;Aquileia;Torre del Greco1;\
Cardito3;Laino Castello;Casarza Ligure;Iseo3;Corleone;Caldogno;Zianigo5;Borgomanero;Monselice;Verona;Cesarolo2;Cimolais;Revò;Ortelle;\
Claut;Pianella4;Solesino;Rovolon;Valfurva2;Lupia di Sandrigo;Campobasso;Mondovì;Laste di Rocca Pietore;Noale;Piove di Sacco3;Lizzano;\
Colognola ai Colli;Locri;Taglio di Po1;Bari;Valdagno;Grosio;Cesena2;Cardito2;Semogo;Carife;Agugliaro;Pianella9;Napoli;Padova7;Romanesco;\
Jesolo;San Martino di Lupari;Martinsicuro;Pianiga2;Maserà di Padova;Ragusa;Villorba;Rivarossa Canavese;Mason Vicentino;Zianigo4;\
Altavilla Vicentina;Campi Salentina;Padova9;Molfetta6;Moncalieri;Villaverla;San Leonardo;Teglio Veneto;Montecchio Precalcino;Pianella2;\
Galliera Veneta1;Redondesco;Padola;Villa di Chiavenna;Carmignano di Brenta1;Savona;Zianigo3;Bormio;Farra di Soligo;Forlì;Milano2;Luserna;\
Crotone;Borgonato7;Ronzone;Grottaglie;Calizzano;San Cesario di Lecce;Cesarolo1;Calalzo di Cadore;Erto;Molfetta1;Montella;Zero Branco;\
Schenone;San Martino di Lupari1;Sutrio;Bagnoregio;San Pietro in Gu;Ceneda;Selva di Val Gardena;Santa Maria di Sala 5;Lion;Due Carrare2;\
Monno;Aldeno3;Mellame d’Arsiè;Cesesa1;Udine;Catania4;Salzano;Barcis;Troina10;Bologna1;San Michele al Tagliamento1;Treviso;LAquila;Cazet;\
Andreis;Schio;Lecce2;Faggiano;Lucinico;Torre del Greco;Catania3;Montecalvo Irpino;Romano DEzzelino;Iseo2;Rimini;Gragnano;Maglie;Pianiga1;\
Piove di Sacco2;Corvara;Cesiomaggiore;Molfetta2;Monteroni;Cardito;Lubriano;Palazzolo dello Stella ;Torino;Ramats;Molfetta3;Palermo7;\
Arsiero;Facca;Palermo9;Padova3;Treia;Lecco;Molfetta5;Finale Ligure;Borgonato4;Falcade;Campagnola;Lughignano;Briana;Pianella3;\
Santa Maria di Sala 4;Molfetta7;Comano;Tricase;Borgonato5;Troina5;Alte Ceccato;Trieste1;Villa di Tirano;Locorotondo;Brione;Rocca Pietore;\
Prà del Torno;Gallipoli1;Lanciano;Borgofranco dIvrea;Gorizia;Pontevigodarzere 1;Ossi;Ferrara2;Milano5;Pontevigodarzere 2;Trecate;\
Palù del Fersina;Valfurva1;Cairo Montenotte;Messina3;San Marco in Lamis2;Pozzale di cadore;Moimacco;Tezze sul Brenta;\
San Michele al Tagliamento2;Troina6;Aldeno1;Puos dAlpago;Iseo6;Molfetta4;Mantova;San Martino di Lupari 4;Monteiasi 2;Vicenza2;Milano1;\
Catania2;San martino di lupari 3;Trieste2;Vallecrosia;Santa Maria di Sala 3;Peaio;Messina1;Carcare;Favale di Malvaro;Iseo4;Bologna2;\
Pianella7;La Spezia;Bergantino;Cardito4;Iglesias;Valmorbia;Paciano;Lecce;Camisano Vicentino;Castellano;Venosa;Palmanova;Oneglia;\
Montereale Valcellina;Iseo7;Chioggia;Villafranca Padovana;Giazza;Due Carrare;Novi Ligure;Malonno;Trevico;Firenze;Scampitella;Torino1;\
Cordenons;Catania1;Colle Val dElsa;Borgonato2;Veneziano;Santa Croce Bigolina;Padova5;Carosino;Vione"

with open(f"data-Italian/dialects_{args.model}_translation/ref.eng", "r") as r:
    rlines = r.read().splitlines()

os.system(f"mkdir scores/Italian/BLEU/dialects_{args.model}_translation")

bleu = BLEU()
with open(f"scores/Italian/BLEU_dialects_avg_{args.model}.txt", "w") as ww:
    for dialect in dialects.split(";"):
        dialect = dialect.replace(" ", "_")
        filename = f"data-Italian/dialects_{args.model}_translation/{dialect}.eng"
        with open(filename, "r") as r:
            lines = r.read().splitlines()

        filename = filename.replace("data-Italian", "scores/Italian/BLEU")
        filename = filename.replace(".ita", ".eng")
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
        ww.write(f"{avg/cnt}\n")