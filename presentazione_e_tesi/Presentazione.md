#### **Slide 1: Titolo**
"Buon pomeriggio a tutti, sono Cristian Porzio. Oggi vi presento il mio lavoro di tirocinio e tesi. 

---

#### **Slide 2: La Scoperta di un Buon Libro (Problemi e Obiettivi)**
Il punto di partenza del mio progetto sono due problemi concreti. 

Il primo è che il **mercato editoriale è vastissimo** ed in continua crescita. 

Il secondo, più specifico per chi fa ricerca e sviluppo come noi, è che spesso i **dataset accademici pubblici sono datati** o con informazioni mancanti.

Per affrontare queste sfide, mi sono posto quattro obiettivi principali:
1.  **Progettare un'architettura flessibile** per integrare dati sempre **attuali**.
2.  Costruire un sistema di raccomandazione scalabile, capace di gestire **milioni di libri**.
3.  Assicurarmi che fosse performante anche su **hardware modesto**.
4.  E infine, **validare l'efficacia** della soluzione proposta."

---

#### **Slide 3: Panoramica Fasi Individuate**
Il progetto si è articolato in tre macro-fasi.
1.  La prima è stata la **Ricerca e l'analisi del Dataset** di partenza, con conseguente pulizia.
2.  Il cuore del lavoro è stato lo **Sviluppo dei Sistemi**: ovvero modulo di **Data Augmentation** per arricchire i dati, e poi il vero e proprio motore di **Raccomandazione**, con una WebApp per l'interagire con esso.
3.  L'ultima fase è stata il **Benchmarking**, per validare quantitativamente e qualitativamente l'intero sistema."

---

#### **Slide 4: Data-Augmentation (Fase 1: Recupero)**
"Analizziamo la pipeline del sistema di arricchimento dati. Quando inseriamo un nuovo libro, il sistema attiva un **Aggregatore** che interroga una serie di **Provider modulari**. 

Possiamo usare sia **API web** tradizionali, sia integrare **tool esterni a riga di comando**, come  Goodreads Scraper. In questo modo, il sistema recupera un insieme di metadati grezzi da più fonti."

---

#### **Slide 5: Data-Augmentation (Fase 2 & 3: Normalizzazione e Salvataggio)**
"Ma i dati grezzi sono spesso caotici e inconsistenti. È stato usato un **LLM**, che analizza i generi letterari, titolo e descrizione e li **normalizza**, mappandoli sulla tassonomia standard del dataset di partenza. Solo a questo punto i dati, finalmente puliti e arricchiti, vengono salvati nel nostro database, pronti per essere utilizzati."

---

#### **Slide 6: Validazione (Coerenza dei Generi)**
"Per verificare che l'LLM funzionasse correttamente e coerentemente, ho raccolto un campione di **libri recenti**, pubblicati nell'ultimo semestre 2024. Per ogni libro, ho recuperato le informazioni da due canali separati:

1. Da un lato, usando lo **scraper di Goodreads**, che mi ha fornito dati "grezzi"
    
2. Dall'altro, ho recuperato gli stessi libri usando i provider di **Google Books e OpenLibrary**, che tendono ad avere meno informazioni e descrizioni differenti.
    
L'obiettivo era vedere se, partendo da input così diversi, il sistema sarebbe arrivato alla **stessa conclusione**, mappando i generi sullo stesso insieme predefinito.

Il risultato, è stato positivo. La stragrande maggioranza dei libri ha ottenuto una classificazione di genere quasi identica, con una mediana di **0.80** con l'Indice di Jaccard.

Quindi l'approccio basato su LLM è in grado di **comprendere il contenuto semantico di un libro**, ed etichettarlo in maniera consistente.

---

#### **Slide 7: Sistema di Raccomandazione**
"Una volta ottenuto un catalogo ricco e coerente, entra in gioco il sistema di raccomandazione.
Il processo parte dalla **profilazione dell'utente** passato in input.
Questo profilo viene poi usato in due strategie parallele:
1.  Il **Content-Based** cerca libri simili a quelli che l'utente ha già amato.
2.  Il **Collaborative Filtering** trova utenti con gusti simili e suggerisce i libri che a loro sono piaciuti.
Le due liste di candidati vengono infine unite e raffinate da un modulo di **Re-Ranking**, prima di produrre la lista finale."

---

#### **Slide 8: Validazione (Metriche Quantitative)**
"Ho valutato il sistema di raccomandazione con un campione di 1000 utenti, ho 'nascosto' alcuni libri e chiesto al sistema di provare ad indovinarli.  
Notiamo che il **Collaborative Filtering** è più efficace del **Content-Based** su Precision e Recall, anche se i valori restano molto bassi: questo dipende dal metodo di Holdout, che considera validi solo i libri presenti nel test set di ciascun utente.

Per l'analisi dei generi, i risultati sono molto interessanti:

- Il **Genre Overlap** è intorno al 45%, segno di buon equilibrio tra coerenza e scoperta.
    
- La **Genre Diversity** supera i 220 generi, evitando l’iperspecializzazione.
    
- Il **Genre Match Score** è quasi al 100%, quindi anche i generi nuovi proposti sono quasi sempre in linea con le preferenze dell’utente."
---

#### **Slide 9: Questionario (Familiarità e Interesse)**
Conoscendo i limiti delle metriche, ho condotto un **beta-testing con 27 utenti reali**.
I risultati sono stati molto incoraggianti. Il sistema ha un'ottima capacità di **scoperta**: 

infatti **95%** delle raccomandazioni riguardava libri che gli utenti non avevano ancora letto, di cui un terzo erano titoli **completamente sconosciuti**.

Ancora più importante, l'**interesse** delle raccomandazioni è stato molto alto, con una forte concentrazione sui punteggi 4 e 5.

---

#### **Slide 10: Questionario (Soddisfazione Generale)**
Infine, la soddisfazione complessiva degli utenti è stata positiva. 

I grafici mostrano un buon livello di **soddisfazione generale**, 

una percezione della **diversità** dei suggerimenti nella media.

e, soprattutto, non si sono sbilanciati sulla possibilità di **utilizzare il sistema in futuro**.

---

#### **Slide 11: Grazie per l'Attenzione**
Grazie per l'attenzione. Il mio intero lavoro è disponibile a questo indirizzo."
