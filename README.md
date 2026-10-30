# Pronti a Tutto: Il Manuale Moderno di Sopravvivenza

Questo è un libro open source, sviluppato collaborativamente dalla community. Chiunque può leggerlo, condividerlo, segnalare errori e contribuire al suo miglioramento.

Non serve essere esperti per contribuire. Anche una correzione, un esempio, una spiegazione più chiara o una segnalazione possono fare la differenza.

## Come leggere

Questo manuale può essere letto dall'inizio alla fine oppure consultato per argomento, in base alle proprie esigenze. Ogni capitolo affronta temi specifici e può essere utilizzato autonomamente come riferimento.

- clona il progetto:
  ```sh
  git clone https://github.com/alphacvps/book.git
  ```

- Il progetto utilizza [Pandoc](https://pandoc.org/) per convertire i contenuti nei diversi formati. La compilazione è gestita dallo script Python `scripts/build.py`:
  ```sh
  python3 scripts/build.py --format pdf # per conoscere gli altri formati: python3 scripts/build.py --help
  ```

- Il libro si troverà all'interno della cartella `dist/`.
