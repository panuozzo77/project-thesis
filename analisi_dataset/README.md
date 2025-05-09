I dataset sono stati presi qui
https://github.com/MengtingWan/goodreads/tree/master

questo è il sito ufficiale che rimanda a GitHub https://cseweb.ucsd.edu/~jmcauley/datasets/goodreads.html

Per trovare i nomi delle tabelle ho scaricato con Google Colab tutto il materiale (35 tabelle in totale) ed ho compreso quali tabelle possano essere utili per lo sviluppo, scrivendone le informazioni in output.txt, cleared_output.txt, tables_explanation. Infine ho provveduto alla creazione di uno Schema, evitando di inserire multiple tabelle in quanto sono dei sub-set di tabelle più grandi (vedasi ad esempio le recensioni)

in `output.txt` ![[output.txt]] ho estratto le colonne del file e stampato un record per comprendere la scrittura delle informazioni

in `cleared_output.txt` ![[cleared_output.txt]]
ho solo estratto le colonne

in `table_explanation.txt` ![[tables_explanation.txt]] una breve descrizione di ciascun file

in `schema` ho provveduto a darne una rappresentazione del database [[schema.svg]]