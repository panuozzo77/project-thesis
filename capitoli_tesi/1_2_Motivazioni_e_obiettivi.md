La presente tesi non si propone di sviluppare un sistema di raccomandazione completamente innovativo o rivoluzionario dal punto di vista algoritmico, soprattutto considerando le limitazioni di potenza computazionale a disposizione. L’obiettivo principale, infatti, è piuttosto quello di affrontare una problematica spesso trascurata ma cruciale: **l’aggiornamento continuo e automatico dei dataset di libri utilizzati nei sistemi di raccomandazione**.

Attualmente, molte ricerche accademiche e modelli si basano su dataset statici o poco aggiornati, come ad esempio quelli derivanti da Goodreads, che pur essendo molto ricchi, presentano un ritardo significativo nell’inclusione di nuove pubblicazioni e una categorizzazione spesso troppo semplificata. Questo limita la capacità dei sistemi di raccomandazione di proporre titoli recenti o poco conosciuti ma potenzialmente rilevanti per l’utente.

- **Integrare dati aggiornati provenienti da fonti legali e ufficiali**, senza ricorrere a tecniche di scraping non autorizzate;
    
- **Applicare filtri configurabili dall’utente**, per selezionare quali nuovi libri includere nel dataset in base a parametri quali anno di pubblicazione, genere, rating, numero di pagine e altri attributi significativi;
    
- **Mantenere e arricchire il dataset esistente**, evitando di dover ricostruire da zero l’intero archivio di libri;