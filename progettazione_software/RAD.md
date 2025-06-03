
# Introduzione
## Obiettivo del Sistema
Questo progetto di tirocinio ha l'obiettivo di sviluppare un **tool per la manutenzione di dataset librari**, finalizzato a supportare la creazione di **sistemi di raccomandazione**. 

Nello specifico, sarà proposto un sistema che **incentiva la lettura di generi inesplorati**, arricchendo al contempo i **metadati librari** con una struttura aggiornata e innovativa.
## Ambito del Sistema
Contribuire attivamente allo sviluppo della **ricerca nel campo**, fornendo sia strumenti pratici che spunti teorici
## Obiettivi e Criteri di Successo del Sistema
- **Funzionalità Base del Tool e del Sistema di Raccomandazione:**
    - **Sviluppo del Tool:** Il tool per i manutentori di dataset deve essere funzionante e capace di eseguire le operazioni principali per cui è stato concepito (caricamento dati, visualizzazione, modifica, estensione di metadati).
- **Miglioramento e Estensione dei Metadati Librari:**
    - **Struttura Aggiornata:** Definizione e implementazione di una struttura di metadati che sia considerata "al passo coi tempi".
    - **Applicazione Efficace:** Dimostrare come il tool permetta di "impreziosire" o "estendere" i metadati in modo concreto e utile per il sistema di raccomandazione o per future analisi.
- **Valutazione e Sperimentazione Iniziale:**
    - **Valutazione della Diversificazione:** Se possibile, una prima, anche qualitativa o su piccola scala, valutazione della capacità del sistema di raccomandazione di proporre generi diversi dai gusti predefiniti dell'utente.

# Sistema Attuale
Sono presenti numerosi siti web gratuiti dove ad oggi è possibile creare le proprie librerie digitali, lasciare recensioni, partecipare alle discussioni o gruppi di scambio/vendita, leggere news e ricevere avvisi sulle nuove uscite, come:

### 1. **Goodreads**

* **Descrizione**: Social network per lettori, permette di catalogare libri, scrivere recensioni, partecipare a gruppi di discussione e ricevere consigli basati sulle letture precedenti.
* **Proprietà**: Acquisito da Amazon nel 2013.
* **Funzionalità chiave**:

  * Creazione di scaffali personalizzati.
  * Algoritmi di raccomandazione basati su valutazioni e generi preferiti.
  * Ampia comunità di lettori con discussioni e gruppi tematici.
* **Note**: Alcuni utenti segnalano limitazioni nell'interfaccia e nella gestione delle recensioni .

### 2. **The StoryGraph**

* **Descrizione**: Piattaforma indipendente focalizzata su statistiche di lettura dettagliate e raccomandazioni personalizzate.
* **Funzionalità chiave**:

  * Analisi delle abitudini di lettura (es. ritmo, temi, emozioni).
  * Raccomandazioni basate su preferenze specifiche.
  * Interfaccia moderna e priva di pubblicità.
* **Note**: Apprezzata per l'indipendenza da Amazon e l'attenzione alla privacy.

### 3. **LibraryThing**

* **Descrizione**: Strumento di catalogazione personale con un focus sulla precisione bibliografica e l'organizzazione dettagliata.
* **Funzionalità chiave**:

  * Importazione di dati da fonti come Amazon e Library of Congress.
  * Utilizzo esteso di tag e metadati per l'organizzazione.
  * Sistema di raccomandazione basato su librerie simili.
* **Note**: Preferito da utenti con collezioni ampie e interesse per la catalogazione dettagliata.

### 4. **Anobii**

* **Descrizione**: Piattaforma con forte presenza in Italia, permette di catalogare libri, scrivere recensioni e interagire con altri lettori.
* **Funzionalità chiave**:

  * Calcolo della compatibilità tra librerie degli utenti.
  * Possibilità di scambiare e vendere libri tra utenti.
  * App mobile per la gestione della libreria personale.
* **Note**: Focalizzata sul mercato italiano con una comunità attiva.

### 5. **Babelio**

* **Descrizione**: Social network letterario francese che consente di creare e condividere librerie personali.
* **Funzionalità chiave**:

  * Recensioni, citazioni e discussioni su libri.
  * Partecipazione a premi letterari come il Prix Babelio.
  * Classificazione tematica tramite tag e nuvole di parole chiave.
* **Note**: Particolarmente popolare nei paesi francofoni.



# Sistema Proposto
Partendo da un dataset librario dato in input (nel formato atteso), il sistema si occuperà di produrre un database (con Apache Ignite) così composto e successivamente arricchito:
## Tabella Libro
Le informazioni minime per l'identificazione di un libro sono:

| Campo              | Tipo        | Descrizione                                    |
| ------------------ | ----------- | ---------------------------------------------- |
| `book_id`          | string/int  | ID univoco nel sistema o nel dataset originale |
| `title`            | string      | Titolo del libro                               |
| `authors`          | list/string | Autori (possibilmente normalizzati)            |
| `isbn` / `isbn13`  | string      | Codici identificativi standard                 |
| `publisher`        | string      | Casa editrice                                  |
| `publication_date` | date        | Data di pubblicazione                          |
| `language_code`    | string      | Codice lingua (ISO 639-1)                      |
| `series_name`      | string/null | Nome della collana/saga se presente            |
| `series_position`  | int/null    | Numero del libro nella serie                   |
### Data Augmentation
La Data Augmentation è incentrata sul retrieval di metadati quali:

| Campo              | Tipo         | Note                                                |                |
| ------------------ | ------------ | --------------------------------------------------- | -------------- |
| `description`      | string       | Sinossi o abstract                                  |                |
| `page_count`       | int          | Numero di pagine                                    |                |
| `average_rating`   | float        | Media dei voti                                      | Se mancassero? |
| `ratings_count`    | int          | Numero totale di voti                               |                |
| `genres_primary`   | string       | Genere principale (es. Giallo)                      |                |
| `genres_secondary` | list[string] | Generi secondari o sfumature (es. Horror, Thriller) |                |
| `cover_url`        | string       | URL copertina                                       | Evitabile      |
| `updated_at`       | datetime     | Timestamp ultimo aggiornamento automatico           |                |

Risultato di elaborazioni NLP o LLM:

| Campo                   | Tipo               | Note                                                        |
| ----------------------- | ------------------ | ----------------------------------------------------------- |
| `extracted_keywords`    | list[string]       | Keyword estratte dalla sinossi                              |
| `themes`                | list[string]       | Temi narrativi dominanti (es. distopia, crescita personale) |
| `readability_score`     | float              | Indicatore di leggibilità                                   |
| `emotion_profile`       | dict[string,float] | Profili emozionali (es. tristezza: 0.7, gioia: 0.2)         |
| `bridging_genres_score` | dict[string,float] | Punteggio di “ponte” tra generi                             |
## Tabella Metadati-Utenti
Attraverso l'analisi delle recensioni lasciate sul sistema, è possibile profilare gli utenti. Questi dati sono utili per filtrare e personalizzare, oltre che per fini statistici.

| Campo                  | Tipo           | Descrizione                                             |
| ---------------------- | -------------- | ------------------------------------------------------- |
| `user_books`           | list[book_id]  | Libri recensiti inseriti dall’utente                    |
| `preferred_page_range` | tuple[int,int] | Range tipico di pagine letto                            |
| `preferred_genres`     | list[string]   | Generi predominanti dell’utente                         |
| `reading_history`      | list[dict]     | Cronologia delle preferenze (data, libro, voto, genere) |
## Requisiti Funzionali

| ID  | Nome                     | Descrizione                                                                                                       | Attori   | Priorità |
| --- | ------------------------ | ----------------------------------------------------------------------------------------------------------------- | -------- | -------- |
| 1   | Caricamento Dataset      | Il sistema dovrà uniformare i dati in ingresso per lavorare con dataset librari differenti, a scelta dell'utente. | Curatore | Elevata  |
| 2   | Data Augmentation        | Il sistema si occupa di etichettare con ulteriori attributi utili i singoli libri caricati nel dataset.           | Curatore | Elevata  |
| 3   | Raccolta Libri Personale | Il sistema permette di tenere traccia e recensire i libri dell'utilizzatore                                       | Curatore | Elevata  |
| 4   | Raccomandazioni          | Il sistema genera dei nuovi libri come suggerimenti per la lettura                                                | Curatore | Elevata  |


## Requisiti Non Funzionali

| ID  | Nome                                    | Descrizione                                                                                                                                                                                                                                                                     | Priorità | Difficoltà |
| --- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------- |
| 1   | Gestione Errori Esplicativa             | Il sistema deve prevedere una<br>gestione degli errori che fornisca<br>messaggi chiari agli utenti per gli<br>specifici problemi legati o meno<br>al sistema, specificandone la<br>causa.                                                                                       | Media    | Media      |
| 2   | Indipendenza<br>hardware /<br>software  | Il sistema deve essere utilizzabile<br>nella sua interezza<br>indipendentemente<br>dall’architettura hardware e<br>software dell’utente.                                                                                                                                        | Alta     | Bassa      |
| 3   | Modifiche /<br>Estensioni<br>Facilitate | Il sistema deve essere progettato in<br>modo da consentire modifiche ed<br>estensioni facili ed efficienti alla code-base per<br>migliorare la sua utilità. Questo<br>richiede una documentazione<br>completa e chiara del codice<br>sorgente ed un design di tipo<br>modulare. | Alta     |            |
| 4   | Legalità dei Dati                       |                                                                                                                                                                                                                                                                                 | Alta     | Alta       |


![[Pasted image 20250603135150.png]]