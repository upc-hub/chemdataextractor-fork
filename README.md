
# chemdataextractor-fork

A fork of [ChemdataExtractor v2.3.2](https://github.com/CambridgeMolecularEngineering/ChemDataExtractor) modified for use in the [FuelCell-IE-Pipeline](https://github.com/upc-hub/FuelCell-IE-Pipeline).

## Modifications

All changes are confined to `chemdataextractor/scrape/pub/rsc.py` (`perform_search` method):

| Change | Description |
|--------|-------------|
| Headless Chrome | Switched from Firefox to headless Chrome (`--headless`, `--no-sandbox`) |
| ChromeDriver | Uses `chromedriver-autoinstaller` — no manual driver download needed |
| Search filters | Added date range (2010–2024) and Open Access filters to RSC search URL |

Two additional compatibility patches for `allennlp==1.1.0`:
- `nlp/__init__.py` and `nlp/new_cem.py` — graceful import fallback for `CemTagger`
- `doc/text.py` — graceful import fallback for `CemTagger`

## Usage

This fork is used as a local dependency. Clone it inside the pipeline directory:

```bash
cd FuelCell-IE-Pipeline
git clone https://github.com/upc-hub/chemdataextractor-fork.git cde_n
```

See [FuelCell-IE-Pipeline](https://github.com/upc-hub/FuelCell-IE-Pipeline) for full setup instructions.

## Original

Based on [ChemdataExtractor](https://github.com/CambridgeMolecularEngineering/ChemDataExtractor) by the Cambridge Molecular Engineering group. Please cite the original work if you use this:

```bibtex
@article{swain2016chemdataextractor,
  title   = {ChemDataExtractor: A Toolkit for Automated Chemical Information
             Extraction from the Scientific Literature},
  author  = {Swain, Matthew C. and Cole, Jacqueline M.},
  journal = {Journal of Chemical Information and Modeling},
  volume  = {56},
  number  = {10},
  pages   = {1894--1904},
  year    = {2016}
}
```
