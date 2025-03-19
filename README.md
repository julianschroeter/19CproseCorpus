# 19CproseCorpus
## General remarks
This repository contains the "19CproseCorpus", a collection of 19th century narrative prose and novellas that provides balanced samples of serially and non-serially published texts from all major contemporary media formats.  
The repository provides: 
- a description of the corpus (see section on `Description` in this file below and the `figures_and_output` folder),
- document-term matrices of the corpus according to different corpus releases (in the `data` folder), 
- a set of metadata on the historical context (in the `Bibliographie.csv` file), 
- and python scripts allowing for an exploratory overview of the corpus (in the `scripts` folder.

## Corpus Description

The project corpus has been constructed between 2018 and 2025. 
Since 2023, it has been supplemented by the systematically relevant dimension of seriality. 
What is important and new to this corpus is that it consists up to 30 percent of journal prose fiction texts that have not yet been discussed in literary studies. 
The texts have been digitized during a preceding post-doctoral project (Habilitation) with the title 
“Gattung – Medium – Politik: Eine quantitative Geschichte der Novelle im 19. Jahrhundert"). 
The python code for this project is published in the `PyNovellaHistory` repository (https://github.com/julianschroeter/PyNovellaHistory). 
The digitization process (2018–2020) was funded by the research fund of the Philosophical Faculty of the University of Würzburg.
The corpus includes information concerning genre, medial history and seriality. 
The corpus design meets criteria of balance and representativeness according to Biber et al. 1998, Wynne 2014, Percillier 2017, and Schöch 2017). 
(1) Canonized texts are not over-represented, 
(2) serial and non-serial narrative texts are balanced. 
The corpus meets – besides the requirements of balance and representativeness – an important further requirement that was developed in Schröter (2019), 
namely that genre assignments shall be representative of the historical situation in the media market. This entails that each text can have different genre assignments in different historical situations. Based on this structure of metadata collection, semantic change of genre concepts as well as historical processes of canonization can be investigated. 
This design facilitates addressing research issues as historiographical questions more comprehensively than existing computational genre stylistics. 
The construction of the corpus was preceded by sighting all research in the media market of the 19th century (Zuber 1955; Schröder 1970; Meyer 1987; Jäger 2003. Based on qualitative analysis, cluster samples, stratified samples and random samples from clusters have been drawn. 

### Release Notes 

Corpus data and feature representation: When the project (Habilitation) is being completed and when all metadata and annotations are collected, all texts that are not affected by copyright restrictions will be published as plain texts in this repository. Until then, only abstract feature representations such as document term matrices of the current state are accessible. Metadata: When the corpus is completed, all metadata will be publisehd. Until then, only anonymous metadata with informations about genre and medial context are accessible.
The corpus representation as a document matrix is recorded with three development states: 
- v.2.0.0 (March 2025): Release for the project propposal EvoLT
  - n (works) ~ 1000 manifestation of individual works, based on an expasion through the `GartenlaubeExtractor`
    (https://github.com/jecGrimm/GartenlaubeExtractor by Jana Grimm)
  - n (episodes) = XXX documents. 
- v.1.2.0 (May 2024):   n = 778 manifestations of individual works
- v.1.1.0 (April 2024, with backdating to the status of May 2022): n = 693 manifestations as the Data basis of the habilitation thesis) 
- v.1.0.0 (April 2023): n = 721 manifestations of individual works 

The corpus has been constructed by Julian Schröter (project lead), Theresa Valta (student assistant from 2018 through 2022), 
Johannes Leitgeb (student assistant from 2018 through 2023, 
Martin Ruhl (student assistant since 2022), 
Franziska Danner (student assistant since 2023), 
and Jana Grimm (student assistant since 2024).

### Citation Suggestion
Schröter, Julian, Johannes Leitgeb, and Theresa Valta. "Ein digitales Korpus der Novellen und Journalprosa des 19. Jahrhunderts: Herausforderungen der Metadatenerschließung." DARIAH-DE Working Papers ​46, ​DARIAH-DE, ​Göttingen, 2023, doi: https://doi.org/10.47952/gro-publ-131. 

### Sources 
- Most of the texts, anthologies, journals, almanacs that were available only as scanned images without digital full texts, were retrieved from: https://digitale-sammlungen.de/en/
- The following two collections were fully included as digital full texts and extended with additional metadata (see below):
  - Deutscher Novellenschatz, DTA: https://www.deutschestextarchiv.de/sammlungen/novellenschatz (Weitin 2016). 
  - ELTEC deu: https://zenodo.org/records/4662482 (Schöch et al. 2021, Konle et al. 2021)
- Individual texts from the following collections were included as full texts: 
  - Textgridrepository: https://textgridrep.org/
  - Gutenberg.org: https://gutenberg.org/
  - Projekt Gutenberg: https://www.projekt-gutenberg.org/
  - Wikisource: https://de.wikisource.org
  - Karl-May-Gesellschaft: https://www.karl-may-gesellschaft.de


## Metadata
A significant expansion of the corpus compared to existing collections lies on the one hand in the inclusion of representative samples from the then popular but now forgotten market segments (such as paperbacks/almanacs before 1850 and family papers after 1850), and on the other hand in the collection of a broader basis of media-historical metadata.

All metadata on the level of the documents are stored in the Bibliographie.csv (in the `data` folder). The following metadata were collected for all texts:
- `Nachname` (last name): The author's surname ("o.N" if unknown).
- `Vorname` (first name): The author's name ("o.N." if unknown).
- `Pseudonym` (alias): if given, indicated as in the accessed manifestation of the work. 
- `Gender`: The author's known gender (f=female, m=male,unbekannt=unknown).
- `Titel` (title): Title as given in the accessed manifestation of the work.
- `Untertitel_im_Text` (subtitle in text): Subtitle as given in the accessed manifestation of the work (empty if not given).
- `Untertitel_im_Inhaltsverzeichnis` (subtitle in table of contents): Subtitle as given in the table of contents, if the work was published in an anthology or journal including a table (empty if not given).
- `Jahr_ED` (year of first publication): The year of first publication of the work.
- `entstanden` (year of creation): The year of creation;  only documented if it differs significantly from the year of first publication (e.g. in the case of posthumous publication).
- `Gattungslabe_ED` (genre label in the paratext): genre label in the paratext of the accessed manifestation of the work.
- `Gattungslabel_ED_normalisiert` (normalized genrelabel from paratext): Moderately normalized historical generic labels (from `Gattungslabel_ED`), according to the following rule:
`Novelle`:= `N`, `Erzählung`:= `E`, all mid-length prose fiction without genre label:= `0E`, all mid-length prose fiction with other genre labels (such as "Geschichte", "Begebenheit" := `XE)
`Roman` (novel) := `R´, `Märchen` (fairy tale) := `M`, nonfictional texts := `0X`, completely unknonw := `0`
- `Medium_ED` (media format of first publication): The media format of forst publication of the item
- `Medientyp_ED` (normalized type of the media format `Medium_ED`), with the following types: `Zeitschrift`, `Taschenbuch`, `Zeitung`, 
`Buch`, `Anthologie`, `Sammlung`, `Werke` (collected works), `Nachlass`, `Illustrierte`, `Kalender`, `Monatsschrift`, `Rundschau`(revue), `Familienblatt`, `Zyklus`, 
`Kolportage`.
- `Hg.` (editor): Editor of the `Medium_ED`.
- `Kanon_Status` (status of canonicity): The status of canonicity covers the values `0`(unknown/forgotten today), `1` (the author is still known today), 
`2` (well known work, which is, however not considered a very important instance of the genre). 
`3` (considered an important literary work of its genre; for novellas, if in one of the novella collections, see below) 
The exact criteria are described below. 
- `Nummer im Heft`: Position of the work or episode in the item of a magazine (empty if not given).
- `seriell`: `True` (Bool) if the manifestation of the work was published in at lease two episodes, `False` if published as a whole.
- `Seiten` (pages): Pages of the printed manifestation in the `Medium_ED`.
- `Medium_Zweitdruck` (Medium of second publication): Medium of a subsequent publication of the work; empty if not given.
- `Jahr_Zweidruck` (Year of second publication); empty if not given.
- `Label_Zweidruck` (Genre label of the second publication); empty if not given.
- `Medium_Drittdruck` (Medium of third publication)
- `Jahr_Drittdruck` (Year of third publication); empty if not given.
- `Label_Drittdruck` (Genre label of third publication); empty if not given.
- `ìn_Deutscher_Novellenschatz`: True if in the collection "Deutscher Novellenschatz", otherwise `False`.
- `in_Pantheon`: `True` if in the collection "Pantheon", otherwise `False`.
- `in_RUB_Sammlung`: `True` if in the Reclam collection "Novellen und Erzählungen des 19. Jahrhunderts", otherwise `False`.
- `in_B-v-Wiese`: `True` if in the collection "Die deutsche Novelle von Goethe bis Kafka" (ed. by B. v. Wiese), otherwise `False`

- Structural and administrative metadata:
  - `Dokument ID`: Identification number of each document. The first 6 digits (XXXXXX-00) refer to the work, the last two digits (000000-XX) refer to the episode. For the whole text, the last two digits are (-00).
  - `Verantwortlich_Erfassung`: Name of the processor of the data record
  - `Source repository`: Name of the source repository, empty if the text was not retrieved from an existing digital text collection
  - `Bearbeitungsqualität`: Quality of the digitized text: `normalisiert`, `unknown`, `niedrig_digital`, `original`, `niedrig_original`, otherwise empty.
  - `spätere_Fassung_von`: If there is a former variant ("Fassung") of the work in the corpus, the `Dokument ID` of the former work manifestation is given; otherwise empty.
  - `UrhGeschBis`: Year until the expiry of copyright protection under German copyright law.
  - `falls_Episode_als_Ganztext_erfasst`: `True`if a work that consists of several episodes could only be documented as a whole text, otherwise `False`.
  



 
## Structure of the repository
- Figures: 
  - Figures that can be reproduced based on the python scripts in the code folder provide a picture of the structure of the corpus with regard to the distribution of genres and media types over time.
  - The figures are stored in the `figures` folder. 
- Code: 
  - In the code folder, a smple and short python scripts for getting a quick overview over the corpus can be found. 
  - In this script functions and classes from the preprocessing module are used. 
  - The output_explore_corpus.txt file in the data folder records the properties of the corpus (date: Feb 13 2022).

Basic characteristics of the corpus (date: May 2023):
roughly 800 German manifestations of narrative prose fiction between 1770 and 1940 with a focus on the period between 1820 and 1880.

![Basic_corpus_characteristcs](https://github.com/user-attachments/assets/6121af6b-92c8-4ca5-89b2-11d3fdd2cbec)

![corpus_characteristic_gender](https://github.com/user-attachments/assets/ea5b666b-2703-476d-8f18-f776ddc23371)

Table 5: Canonicity

|canon status| absolute | relative | estimated population |
|---|---|---|---|
|0 (not part of the canon)| 452 | 0.66 | > 0.85 |
|1  (weakly canonized) | 71 |0.1 | ––– |
|2 (medium) | 83 | 0.12 | –––|
|3 (high canon) | 81 | 0,12 |–––|



References: 

Biber, Douglas/Conrad, Susan/Reppen, Randi (1998): Introduction: Goals and Methods of the Corpus-based Approach (Chapter 1). In: Biber, Douglas/Conrad, Susan/Reppen, Randi (ed.): Corpus Linguistics. Investigating Language Structure and Use. Cambridge, S. 1–18.

Jäger, G. (2003). Geschichte des deutschen Buchhandels im 19. und 20. Jahrhundert. Frankfurt am Main.

Leonard Konle, Fotis Jannidis, Carolin Odebrecht, & Lou Burnard. (2021). German Novel Corpus (ELTeC-deu): April 2021 release (v.1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4662482.

Meyer, R. (1987). Novelle und Journal, I: Titel und Normen: Untersuchungen zur Terminologie der Journalprosa, zu ihren Tendenzen, Verhältnissen und Bedingungen. Stuttgart.

Schöch, Christof (2017): Aufbau von Datensammlungen. In: Jannidis, Fotis/Kohle, Hubertus/Rehbein, Malte (ed.): Digital Humanities: eine Einführung. Stuttgart: J.B. Metzler Verlag. S. 223–233.

Christof Schöch, Roxana Patraș, Diana Santos, Tomaž Erjavec (2021): "Creating the European Literary Text Collection (ELTeC): Challenges and Perspectives", in: Modern Languages Open 1/25. DOI: http://doi.org/10.3828/mlo.v0i0.364.

Schröder, R. (1970). Novelle und Novellentheorie in der frühen Biedermeierzeit. Tübingen.

Schröter, Julian (2019): Gattungsgeschichte und ihr Gattungsbegriff am Beispiel der Novellen. In: Journal of Literary Theory 13:2, S. 227–257.

Weitin, Thomas (Hrsg.): Volldigitalisiertes Korpus. Der Deutsche Novellenschatz. Darmstadt/Konstanz, 2016. In: Deutsches Textarchiv.

Wynne, Martin (ed.) (2004): Developing Linguistic Corpora: a Guide to Good Practice. Oxford.

Zuber, M. (1955). Die deutschen Musenalmanache und schöngeistigen Taschenbücher des Biedermeier. 1815 – 1848. München.

