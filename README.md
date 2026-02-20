#Analisi Dataset JSON con Python

Progetto di analisi di un dataset JSON della classe quarta superiore del corso informatico dell'istituto tecnico I.T.I.S. Castelli. <br>
Lo scopo è analizzare il dataset scelto attraverso programmazione in linguaggio Python, ad esempio per esplorarne la struttura o per filtrarne i dati. Il dataset è composto da dizionari di cui la key è il link al Playstation Store di ogni gioco, mentre la value è il dizionario degli attributi di ogni gioco. I campi di questo dizionario sono: la stringa title, la lista platforms, il float rating, l'intero votes, la stringa developer, la stringa indicante una data release_date, il float price e la lista di stringhe generi.
<br>
Il dataset JSON scelto è il catalogo di giochi Playstation 4 e Playstation 5 ed è stato ricavato da: "https://www.kaggle.com/datasets/evgeny1928/playstation-games-info/data?select=output.json".
<br>
In base ai requisiti all'analisi del dataset, sono stati sviluppati diversi blocchi di codice in linguaggio Python:
- Visualizza la classifica dei 20 giochi col rating più alto con minimo 10.000 voti
- Visualizza la classifica dei 20 più popolari in base al numero di voti
- Visualizza il numero di giochi rilasciato ogni anno
- Visualizza il numero di giochi per genere
- Visualizza il numero di giochi disponibili per piattaforma
- Visualizza il numero di giochi rilasciati dalla top 20 sviluppatori
- Visualizza il grafico a barre del rating medio a ogni range di prezzo
- Visualizza il grafico a linee del rating medio dei giochi rilasciati per ogni anno
- Visualizzare il grafico a barre del rating medio per genere
- Visualizzare il grafico del rating medio per sviluppatore con minimo 20 giochi
