# 19CproseCorpus

This repository provides a description, abstract feature representations (data), anonymous metadata (data), and python scripts (scripts, based on functions and classes in the preprocessing module) for an exploratory overview of a literary corpus that is currently constructed.

If you want to cite or use this corpus, please refer to:
Schröter, Julian, Johannes Leitgeb, and Theresa Valta. "Ein digitales Korpus der Novellen und Journalprosa des 19. Jahrhunderts: Herausforderungen der Metadatenerschließung." DARIAH-DE Working Papers ​46, ​DARIAH-DE, ​Göttingen, 2023, doi: https://doi.org/10.47952/gro-publ-131. 



Description: 

The project corpus has been constructed between 2018 to 2022. It is currently supplemented by the systematically relevant dimension of seriality. What is important and new to this corpus is that it consists up to 30 percent of journal prose fiction texts that have not yet been discussed in literary studies. The texts have been digitized during a preceding post-doctoral project (Habilitation) with the title “Ästhetische und soziale Funktionen der Erzählungen und Novellen im 19. Jahrhundert ("Towards a functional history of nineteenth-century German novellas"). The python code for this project will soon be published in the PyNovellaHistory GitHub repository. The digitization process was funded by the research fund of the Philosophical Faculty of the University of Würzburg. The corpus includes information concerning genre, medial history and seriality. The corpus design meets criteria of balance and representativeness according to Biber et al 1998, Wynne 2014, Percillier 2017, and Schöch 2017). (1) Canonized texts are not over-represented, and (2) serial and non-serial narrative texts are balanced. The corpus meets – besides the requirements of balance and representativeness – an important further requirement that I developed in Schröter (2019), namely that genre assignments shall be representative of the historical situation in the media market. This design facilitates addressing research issues as historiographical questions more comprehensively than existing computational genre stylistics. The construction of the corpus was preceded by sighting all research in the media market of the 19th century (Zuber 1955; Schröder 1970; Meyer 1987; Jäger 2003. Based on qualitative analysis, cluster samples, stratified samples and random samples from clusters have been drawn. Besides the requirements of balance and representativeness, the corpus meets an important further requirement that I developed in (Gattungsgeschichte und ihr Gattungsbegriff am Beispiel der Novellen. In: Journal of Literary Theory 13:2 2019, 227–257). Genre assignments shall be representative of the historical situation in the media market. This entails that each text can have different genre assignments in different historical situations. Based on this structure of metadata collection, semantic change of genre concepts as well as historical processes of canonization can be investigated. 

The project has been constructed by Julian Schröter (project lead), Theresa Valta (student assistant from 2018 through 2022), Johannes Leitgeb (student assistant since 2018, Martin Ruhl (student assistant since 2022), Franziska Danner (student assistant since 2023), and Jana Grimm (student assistant since April 2024).

Data: 

Corpus data and feature representation: When the project (Habilitation) is being completed and when all metadata and annotations are collected, all texts that are not affected by copyright restrictions will be published as plain texts in this repository. Until then, only abstract feature representations such as document term matrices of the current state are accessible. Metadata: When the corpus is completed, all metadata will be publisehd. Until then, only anonymous metadata with informations about genre and medial context are accessible.
The corpus representation as a document matrix is recorded with two development states, May 2022 and May 2024.

Figures: 

Figures that can be reproduced based on the python scripts in the code folder provide a picture of the structure of the corpus with regard to the distribution of genres and media types over time.

Code: 

In the code folder, a smple and short python scripts for getting a quick overview over the corpus can be found. In this script functions and classes from the preprocessing module are used. The output_explore_corpus.txt file in the data folder records the properties of the corpus (date: Feb 13 2022).

Basic characteristics of the corpus (date: May 2023):
roughly 800 German manifestations of narrative prose fiction between 1770 and 1940 with a focus on the period between 1820 and 1880.

![Basic_corpus_characteristcs](https://github.com/user-attachments/assets/6121af6b-92c8-4ca5-89b2-11d3fdd2cbec)

![corpus_characteristic_gender](https://github.com/user-attachments/assets/ea5b666b-2703-476d-8f18-f776ddc23371)

Table 5: Canonicity:

|---| absolute | relative | estimated population |
|---|---|---|---|
|0 (not part of the canon)| 452 | 0.66 | > 0.85 |
|1  (weakly canonized) | 71 |0.1 | ––– |
|2 (medium) | 83 | 0.12 | –––|
|3 (high canon) | 81 | 0,12 |–––|



References: 

Biber, Douglas/Conrad, Susan/Reppen, Randi (1998): Introduction: Goals and Methods of the Corpus-based Approach (Chapter 1). In: Biber, Douglas/Conrad, Susan/Reppen, Randi (ed.): Corpus Linguistics. Investigating Language Structure and Use. Cambridge, S. 1–18.

Jäger, G. (2003). Geschichte des deutschen Buchhandels im 19. und 20. Jahrhundert. Frankfurt am Main.

Meyer, R. (1987). Novelle und Journal, I: Titel und Normen: Untersuchungen zur Terminologie der Journalprosa, zu ihren Tendenzen, Verhältnissen und Bedingungen. Stuttgart.

Schöch, Christof (2017): Aufbau von Datensammlungen. In: Jannidis, Fotis/Kohle, Hubertus/Rehbein, Malte (ed.): Digital Humanities: eine Einführung. Stuttgart: J.B. Metzler Verlag. S. 223–233.

Schröder, R. (1970). Novelle und Novellentheorie in der frühen Biedermeierzeit. Tübingen.

Schröter, Julian (2019): Gattungsgeschichte und ihr Gattungsbegriff am Beispiel der Novellen. In: Journal of Literary Theory 13:2, S. 227–257.

Wynne, Martin (ed.) (2004): Developing Linguistic Corpora: a Guide to Good Practice. Oxford.

Zuber, M. (1955). Die deutschen Musenalmanache und schöngeistigen Taschenbücher des Biedermeier. 1815 – 1848. München.
