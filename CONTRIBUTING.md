# Contributing

**Grazie per il tuo interesse nel contribuire a questo progetto!**

Questo documento descrive il processo ufficiale per proporre modifiche, migliorare i contenuti e collaborare allo sviluppo del libro.

Puoi contribuire in diversi modi.
- correzioni grammaticali e ortografiche
- miglioramento dei contenuti esistenti
- creazione di nuovi capitoli
- aggiunta di esempi pratici
- traduzione dei contenuti
- ricerca e verifica delle informazioni
- miglioramento della documentazione
- segnalazioni e suggerimenti

Non è necessario contribuire con grandi modifiche: anche piccoli miglioramenti sono preziosi.

## Prima di iniziare

Prima di lavorare a una modifica:
- Controlla le Issue aperte.
- Verifica che nessuno stia già lavorando sulla stessa modifica.
Se la modifica è significativa, apri una Issue per discuterla.

Per modifiche semplici, come refusi o errori grammaticali, puoi procedere direttamente con una Pull Request.

## Configurazione dell'ambiente

- Clona il repository:
    ```bash
    git clone https://github.com/alphacvps/book.git
    cd book
    ```

- Crea una nuova branch:
    ```bash
    git checkout -b tipo/nome-modifica
    ```

## Linee guida

Ogni contributo deve rispettare alcuni principi fondamentali:
- Chiarezza
- Scrivi in modo semplice e comprensibile.
- Spiega i termini tecnici quando vengono introdotti.
- Non dare per scontate conoscenze non ancora trattate.
- Qualità
- Verifica le informazioni prima di inserirle.
- Utilizza fonti affidabili.
- Inserisci riferimenti bibliografici quando necessario.
- Preferisci esempi concreti e verificabili.
- Coerenza
- Rispetta la struttura dei capitoli esistenti.
- Utilizza correttamente titoli e sottotitoli Markdown.
- Mantieni uno stile uniforme.
- Evita ripetizioni e contenuti duplicati.
- Copyright
- Non copiare contenuti protetti da copyright senza autorizzazione.
- Cita le fonti utilizzate.
- Non inserire immagini o materiali senza verificarne la licenza.

## Commit e Pull Request

1. Utilizziamo commit descrittivi per facilitare la revisione della cronologia.
    ```text
    tipo: descrizione breve
    ```

2. Creare una Pull Request dopo aver completato le modifiche:
    ```bash
    git add .
    git commit -m "titolo: descrizione breve"
    git push origin nome-della-branch
    ```

3. Apri una Pull Request verso il branch principale (main) e spiega brevemente cosa hai modificato.

4. Checklist:
    - [ ] Ho verificato le informazioni inserite.
    - [ ] Ho controllato grammatica e ortografia.
    - [ ] Ho rispettato le linee guida editoriali.
    - [ ] Ho verificato che non ci siano contenuti duplicati.
    - [ ] Ho controllato la formattazione Markdown.

5. Closes #[NUMERO ISSUE]

Non esitare a chiedere aiuto: siamo felici di accogliere nuovi contributori.

Grazie per contribuire alla crescita di questo progetto!
