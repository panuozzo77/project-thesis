###  Vantaggi di usare Apache Ignite per il sistema:

1. **Velocità (In-Memory)** – Ottimo per query rapide di raccomandazione.
    
2. **Scalabilità** – Progettato per essere distribuito su più nodi.
    
3. **SQL Support** – Puoi interrogare le tabelle come in un RDBMS.
    
4. **Supporto per strutture complesse** – Come dizionari e liste (utile per `genres_secondary`, `emotion_profile`...).

è integrabile con Python tramite il modulo [PyIgnite](https://ignite.apache.org/docs/latest/binary-client-protocol/python-thin-client).