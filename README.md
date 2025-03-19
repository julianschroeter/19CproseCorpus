# 19CproseCorpus
## General remarks
This repository contains the `19CproseCorpus`, a collection of 19th century narrative prose and novellas that provides balanced samples of serially and non-serially published texts from all major contemporary media formats.  
The repository provides: 
- A description of the corpus (see section on `Corpus description` in this file below and additional visualizations and tables in the `figures` folder).
All figures can be reproduced based on the python scripts in the `code` folder provide a picture of the structure of the corpus with regard to the distribution of genres and media types over time.
The output_explore_corpus.txt file in the data folder records the actual output of the script ´explore_corpus.py` (date: XX.03.2025).
- Python scripts allowing for an exploratory overview of the corpus (in the `code` folder. The scripts use functions and classes from the ´preprocessing´ module. 
For using the scripts see section on `Usage` below. 
- Document-term matrices `dtm` of the corpus according to different corpus releases (in the `data/dtm` folder). 
- A metadata table including a wide range of media-historical context (`Bibliographie.csv`). 



## Corpus description

The project corpus was built up between 2018 and 2025. 
Since 2023, it has been supplemented by the systematically relevant dimension of seriality.
The corpus will facilitate the answering of three research questions:
- The historical change of genre 
- The historical change of media and its interference with genre. Both questions were addressed in Julian Schröter's habilitation thesis entitled "Gattung – Medium – Politik: Eine quantitative Geschichte der Novelle im 19. Jahrhundert" (to be published in 2025/26). The python code for this project is published in the `PyNovellaHistory` repository (https://github.com/julianschroeter/PyNovellaHistory). 
- The interdependence of specific writing techniques such as the suspense narrative with seriality in the form of the cliffhanger. This project is currently in preparation.

The corpus has been constructed in two major phases: 
1. A novella corpus: In the first phase (2018–2020), a corpus of roughly 700 novella texts (see release notes below) from the 19th century has been constructed. 
The digitization process  was funded by the research fund of the Philosophical Faculty of the University of Würzburg.
What is important and new to this corpus is that it consists up to 30 percent of journal prose fiction texts that have not yet been discussed in literary studies. 
In this phase, the data basis for the habilitation thesis (see above) was established. The construction of the corpus was preceded by sighting all research in the media market of the 19th century (Zuber 1955; Schröder 1970; Meyer 1987; Jäger 2003. Based on qualitative analysis, cluster samples, stratified samples and random samples from clusters have been drawn.
   See version v.1.0.0 in section `Release notes` below and Schröter/Leitgeb Valta (2023).
2. Seriality and the cliffhanger: In the second phase (2023–2025), the existing corpus has been extended in order to facilitate empirical studies on the interdependency between suspense and seriality.
During this phase, the phase the corpus expansion has been funded by the Vogel-Stiftung Würzburg (Schröter 2024b).
   See version v.2.0.0 in `Release notes` below. For this phase, it was essential to cover samples from the fields of popular suspenseful narration from the different market sectors and media formats including serial and non-serial publication.

The corpus includes information concerning genre, medial history and seriality. 
The corpus design meets criteria of balance and representativeness according to Biber et al. 1998, Wynne 2014, Percillier 2017, and Schöch 2017). 
It covers: 
1. Balanced samples of canonized texts as well as non-canonical works, 
2. Balanced samples of works that were serially and wroks that were non-serially published. 
3. Balanced samples of the main subperiods: 1820–1850 and 1850–1880; sufficiently large samples for the marginal subperiods 1790–1820 and 1880–1940.
4. Balanced samples of historical prose genres: The corpus meets – besides the requirements of balance and representativeness – an important further requirement that was developed in Schröter (2019), 
namely that genre assignments shall be representative of the historical situation in the media market. This entails that each text can have different genre assignments in different historical situations. Based on this structure of metadata collection, semantic change of genre concepts as well as historical processes of canonization can be investigated. 

The corpus composition is outlined and visualized in more detail in the subsection on `Corpus composition` below with regard to sample size balance.


### Release notes 

Corpus data and feature representation: When the project (Habilitation) is being completed and when all metadata and annotations are collected, all texts that are not affected by copyright restrictions will be published as plain texts in this repository. Until then, only abstract feature representations such as document term matrices of the current state are accessible. Metadata: When the corpus is completed, all metadata will be publisehd. Until then, only anonymous metadata with informations about genre and medial context are accessible.
The corpus representation as a document matrix is recorded with three development states: 
- v.2.0.0 (March 2025): Current release
  - n (works) ~ 1000 manifestation of individual works, based on an expasion through the `GartenlaubeExtractor`
    (https://github.com/jecGrimm/GartenlaubeExtractor by Jana Grimm)
  - n (episodes) ~ 500 documents. This is the number of episodes for the works published serially (see table 1 below). 
- v.1.2.0 (May 2024):   n = 778 manifestations of individual works. This release relates to the submitted paper Julian Schröter: Love, Canon, and Gender (to be published 2025)
- v.1.1.0 (April 2024, with backdating to the status of May 2022): n = 693 manifestations. This release relates to the data basis of the habilitation thesis "Gattung – Medium – Politik" (see above)) 
- v.1.0.0 (April 2023): n = 721 manifestations of individual works. This release relates to the data basis for the paper Schröter (2024) 

The corpus has been constructed by Julian Schröter (project lead), Theresa Valta (student assistant from 2018 through 2022), 
Johannes Leitgeb (student assistant from 2018 through 2023, 
Martin Ruhl (student assistant since 2022), 
Franziska Danner (student assistant since 2023), 
and Jana Grimm (student assistant since 2024).

### Citation Suggestion
For the current release, see `CITATION.cff` file.

For a more comprehensive description of the corpus (phase 1), see:
Schröter, Julian, Johannes Leitgeb, and Theresa Valta (2023): "Ein digitales Korpus der Novellen und Journalprosa des 19. Jahrhunderts: Herausforderungen der Metadatenerschließung." DARIAH-DE Working Papers 46. https://doi.org/10.47952/gro-publ-131. 


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
A significant expansion of the corpus compared to existing collections lies on the one hand in the inclusion of representative samples from the then popular but now forgotten market segments 
(see criteria for balanced samples above), and on the other hand in the collection of a broader basis of media-historical metadata.

All metadata on the level of the documents are stored in the Bibliographie.csv (in the `data` folder). The following metadata were collected for all texts:
- `Nachname` (last name): The author's surname (`o.N` if unknown).
- `Vorname` (first name): The author's name (`o.N.` if unknown).
- `Pseudonym` (alias): if given, indicated as in the accessed manifestation of the work. 
- `Gender`: The author's known gender (`f`=female, `m`=male, `unbekannt`= unknown).
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
- `Jahr_Zweitdruck` (Year of second publication); empty if not given.
- `Label_Zweitdruck` (Genre label of the second publication); empty if not given.
- `Medium_Drittdruck` (Medium of third publication)
- `Jahr_Drittdruck` (Year of third publication); empty if not given.
- `Label_Drittdruck` (Genre label of third publication); empty if not given.
- `ìn_Deutscher_Novellenschatz`: True if in the collection "Deutscher Novellenschatz", otherwise `False`.
- `in_Pantheon`: `True` if in the collection "Pantheon", otherwise `False`.
- `in_RUB_Sammlung`: `True` if in the Reclam collection "Novellen und Erzählungen des 19. Jahrhunderts", otherwise `False`.
- `in_B-v-Wiese`: `True` if in the collection "Die deutsche Novelle von Goethe bis Kafka" (ed. by B. v. Wiese), otherwise `False`

- Structural and administrative metadata:
  - `Dokument ID`: Identification number of each document. The first 6 digits (XXXXXX-00) refer to the work, the last two digits (000000-XX) refer to episode numbers. For the whole text, the last two digits are (-00).
  - `Verantwortlich_Erfassung`: Name of the processor of the data record
  - `Source repository`: Name of the source repository, empty if the text was not retrieved from an existing digital text collection
  - `Bearbeitungsqualität`: Quality of the digitized text: `normalisiert`, `unknown`, `niedrig_digital`, `original`, `niedrig_original`, otherwise empty.
  - `spätere_Fassung_von`: If there is a former variant ("Fassung") of the work in the corpus, the `Dokument ID` of the former work manifestation is given; otherwise empty.
  - `UrhGeschBis`: Year until the expiry of copyright protection under German copyright law.
  - `falls_Episode_als_Ganztext_erfasst`: `True`if a work that consists of several episodes could only be documented as a whole text, otherwise `False`.
 

## Corpus composition

The composition of the corpus regarding the size and proportions of the samples regarding the essential categories of genre, seriality, and mediality are 
shown in tables X-X:

![Basic_corpus_characteristcs](https://github.com/user-attachments/assets/6121af6b-92c8-4ca5-89b2-11d3fdd2cbec)

Figure 1 shows the subsample sizes for each media format across subperiods, with the main periods from 1820–1850 and 1850–1880.

![](/figures/former_releases/May2024/en_Corpus_Size_for_Media_types_and_Periods.svg "Media Types")

Figure 1

Figure 2 shows the sumsample sizes for serially and non-serially published prose fiction across subperiods as in Figure 1.

(Figure 2 to come)


Figure 3 shows the subsample sizes for each genre across subperiods as in Figure 1.

![Fig 1](/figures/former_releases/May2024/en_Corpus_Size_for_Genres_and_Periods.svg)

Figure 3

Table 4 shows the balance of authors gender in the corpus.
![corpus_characteristic_gender](https://github.com/user-attachments/assets/ea5b666b-2703-476d-8f18-f776ddc23371)


Table 5 shows the balance regarding the status of canonicity in the corpus.


Table 5: Canonicity

|canon status| absolute | relative | estimated population |
|:-:|---|---|---|
|0 (not part of the canon)| 452 | 0.66 | > 0.85 |
|1  (weakly canonized) | 71 |0.1 | ––– |
|2 (medium) | 83 | 0.12 | –––|
|3 (high canon) | 81 | 0,12 |–––|

# Usage: CLI
Here are the instructions for the CLI.

# References 

Biber, Douglas/Conrad, Susan/Reppen, Randi (1998): Introduction: Goals and Methods of the Corpus-based Approach (Chapter 1). In: Biber, Douglas/Conrad, Susan/Reppen, Randi (ed.): Corpus Linguistics. Investigating Language Structure and Use. Cambridge, S. 1–18.

Jäger, G. (2003). Geschichte des deutschen Buchhandels im 19. und 20. Jahrhundert. Frankfurt am Main.

Leonard Konle, Fotis Jannidis, Carolin Odebrecht, & Lou Burnard. (2021). German Novel Corpus (ELTeC-deu): April 2021 release (v.1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4662482.

Meyer, R. (1987). Novelle und Journal, I: Titel und Normen: Untersuchungen zur Terminologie der Journalprosa, zu ihren Tendenzen, Verhältnissen und Bedingungen. Stuttgart.

Schöch, Christof (2017): Aufbau von Datensammlungen. In: Jannidis, Fotis/Kohle, Hubertus/Rehbein, Malte (ed.): Digital Humanities: eine Einführung. Stuttgart: J.B. Metzler Verlag. 223–233.

Christof Schöch, Roxana Patraș, Diana Santos, Tomaž Erjavec (2021): "Creating the European Literary Text Collection (ELTeC): Challenges and Perspectives", in: Modern Languages Open 1/25. http://doi.org/10.3828/mlo.v0i0.364.

Schröder, R. (1970). Novelle und Novellentheorie in der frühen Biedermeierzeit. Tübingen.

Schröter, Julian (2019): Gattungsgeschichte und ihr Gattungsbegriff am Beispiel der Novellen. In: Journal of Literary Theory 13:2, 227–257.

Schröter, Julian (2024a): Machine Learning as a Measure of the Conceptual Looseness of Disordered Genres: Studies on German Novellen. In: Robert Hesselbach et al. (ed.): Digital Stylistics in Romance Studies and Beyond, Heidelberg, 173–195 (https://doi.org/10.17885/heiup.1157.c19371).

Schröter, Julian (2024b). Abstract (short proposal): Der Cliffhanger im seriellen Spannungserzählen. Zu einem repräsentativen Korpus populären Erzählens im 19. Jahrhundert Julian Schröter. Zenodo. https://doi.org/10.5281/zenodo.10789497.

Schröter, Julian, Johannes Leitgeb, and Theresa Valta (2023): "Ein digitales Korpus der Novellen und Journalprosa des 19. Jahrhunderts: Herausforderungen der Metadatenerschließung." DARIAH-DE Working Papers 46. https://doi.org/10.47952/gro-publ-131. 

Weitin, Thomas (Hrsg.): Volldigitalisiertes Korpus. Der Deutsche Novellenschatz. Darmstadt/Konstanz, 2016. In: Deutsches Textarchiv.

Wynne, Martin (ed.) (2004): Developing Linguistic Corpora: a Guide to Good Practice. Oxford.

Zuber, M. (1955). Die deutschen Musenalmanache und schöngeistigen Taschenbücher des Biedermeier. 1815 – 1848. München.

