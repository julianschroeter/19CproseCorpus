import pandas as pd
import os
import matplotlib.pyplot as plt
import pathlib

# Define path for preprocessing import
import sys
sys.path.insert(1, str(pathlib.Path().resolve()))

from preprocessing.corpus import DocFeatureMatrix
from preprocessing.metadata_transformation import full_genre_labels, years_to_periods

# set lokal path to 19CproseCorpus repository
project_path = pathlib.Path().resolve()


figures_path = os.path.join(project_path,"figures" )
data_path = os.path.join(project_path,"data" )
tables_path = os.path.join(project_path,"tables" )


infile_name = os.path.join(data_path, "raw_dtm_l1__use_idf_False500mfw.csv" ) # read the corpus as a document term matrix
metadata_filepath= os.path.join(data_path, "Bibliographie.tsv")

dtm_obj = DocFeatureMatrix(data_matrix_filepath=infile_name, metadata_csv_filepath= metadata_filepath) # combine corpus with metadata information using the DocFEatureMatrix class and its methods

df0 = dtm_obj.data_matrix_df
print(df0)
dtm_obj = dtm_obj.add_metadata(["Gattungslabel_ED_normalisiert", "Nachname", "Titel", "Medientyp_ED", "Jahr_ED"])

df1 = dtm_obj.data_matrix_df
print(df1)

cat_labels = ["N", "E", "0E", "0PE", "XE", "M", "R", "0", "E_N_Rubrik", "(unbekannt)", "Kolportage"]
dtm_obj = dtm_obj.reduce_to_categories("Gattungslabel_ED_normalisiert", cat_labels)


df = dtm_obj.data_matrix_df
df2 = df.copy()
print(df)

period_var = "Perioden"

df = years_to_periods(input_df=df, category_name="Jahr_ED", start_year=1760, end_year=2000, epoch_length=30,
                      new_periods_column_name=period_var)



replace_dict = {"Gattungslabel_ED_normalisiert": {"N": "Novelle", "E": "Erzählung",
                                                  "0E": "other prose fiction",
                                                  "0":"other prose fiction",
                                   # "(unbekannt)":"other prose fiction",
                                    "0PE":"other prose fiction (novella #3)",
                                    "R": "Roman (novel)", "M": "Märchen (fairy tale)",
                                                  "E_N_Rubrik":"Rubrik: Erzählungen und Novellen" , #"prose fiction with unknown label (novella #4)"
                                    "XE": "other prose fiction"}}
df = full_genre_labels(df, replace_dict=replace_dict)


# for convenenince different media types are normalized to a smaller set of types
replace_dict = {"Medientyp_ED": {"Zeitschrift": "Journal", "Zeitung": "Journal", "Kalender": "Journal",
                                 "Rundschau" : "Rundschau", "Werke":"Buch", "Monatsschrift":"Journal",
                                 "Zyklus" : "Anthologie", "Roman" : "Buch", "Roman/Monographie" : "Buch",
                                    "Illustrierte": "Journal", "Sammlung": "Anthologie",
                                 "Kolportage":"Kolportage", "(unbekannt)":"unknown",
                                 "Nachlass": "Buch", "Jahrbuch":"Taschenbuch", "Monographie": "Buch", "Deutsche Romanzeitung":"Journal"}}

df = full_genre_labels(df, replace_dict=replace_dict)
start_df = df.copy()

title_en = "Corpus Size for Genres and Periods"
title_de = "Zusammensetzung des Korpus nach Perioden und Genres"
corpus_statistics = df.groupby([period_var, "Gattungslabel_ED_normalisiert"]).size()

df_corpus_statistics_genre = pd.DataFrame(corpus_statistics)

df = df_corpus_statistics_genre
df = df.unstack().reset_index()
df.set_index("Perioden",inplace=True)
df.columns = df.columns.droplevel()

df.plot(kind='bar', stacked=False, title= title_en,
        color={"Erzählung": "green", "other prose fiction": "cyan",
               "Novelle": "red", "Roman (novel)": "blue", "Kolportage":"brown",
                "Rubrik: Erzählungen und Novellen":"lightgrey",
               "kein Label": "lightgrey", "Märchen (fairy tale)":"orange"})

plt.xticks(rotation=45)
plt.xlabel("periods") # if en
plt.ylabel("number of works")
plt.tight_layout()
plt.savefig(os.path.join(figures_path, "en_Corpus_Size_for_Genres_and_Periods.svg"))
plt.show()

df = start_df.copy()
corpus_statistics = df.groupby([period_var, "Medientyp_ED"]).size()
df_corpus_statistics_media = pd.DataFrame(corpus_statistics)

title_en = "Corpus Size for Media and Periods"
title_de = "Zusammensetzung des Korpus nach Perioden und Medienformaten"

df = df_corpus_statistics_media
df = df.unstack().reset_index()
df.set_index("Perioden",inplace=True)
df.columns = df.columns.droplevel()

df.plot(kind='bar', stacked=False, title= title_en,
                                    color={"Anthologie":"yellow", "Kolportage":"brown", "unknown":"black",
                                           "Taschenbuch": "purple", "Familienblatt":"lightgreen", "Rundschau":"grey", "Buch":"darkgreen", "Journal":"lightblue"})
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(figures_path, "en_Corpus_Size_for_Media_types_and_Periods.svg"))
plt.show()

df = start_df.copy()
print(df)
corpus_statistics = df.groupby(["Medientyp_ED"]).size()
df_corpus_statistics_media_nontemporal = pd.DataFrame(corpus_statistics)
corpus_statistics = df.groupby(["Gattungslabel_ED_normalisiert"]).size()
df_corpus_statistics_genre_nontemporal = pd.DataFrame(corpus_statistics)

genre_df = df_corpus_statistics_genre_nontemporal
genre_df.loc["Total"] = genre_df.sum()
genre_df["Proportion"] = genre_df[0].apply(lambda x: x / genre_df.loc["Total"])
genre_df = genre_df.rename(columns={0:"Count"})
print(genre_df)
genre_df.to_csv(os.path.join(tables_path, "corpus_size_genre.csv"))


fig, ax = plt.subplots(figsize=(12,8))
df = genre_df.copy()
df = df[:-1] # drop last row with totals
ax.pie(df.iloc[:,1], labels=df.index,autopct='%1.1f%%',
       colors=["green", "brown", "orange","red", "blue", "grey", "cyan"])
plt.title("Korpus nach Gattungen")
plt.title("Corpus: Shares of Genres") # if en
plt.tight_layout()
plt.savefig(os.path.join(figures_path, "pie_chart_corpus_size_genre.svg"))
plt.show()



media_df = df_corpus_statistics_media_nontemporal
media_df.loc["Total"] = media_df.sum()
media_df["Proportion"] = media_df[0].apply(lambda x: x / media_df.loc["Total"])
media_df = media_df.rename(columns={0:"Count"})
print(media_df)
media_df.to_csv(os.path.join(tables_path, "corpus_size_media.csv"))



fig, ax = plt.subplots()
df = media_df.copy()
df = df[:-1] # drop last row with totals
ax.pie(df.iloc[:,1], labels=df.index,autopct='%1.1f%%',
       colors=["yellow", "darkgreen", "lightgreen", "lightblue", "brown", "grey", "purple", "black"])
plt.title("Korpus nach Medienformaten")
plt.tight_layout()
plt.savefig(os.path.join(figures_path, "pie_chart_corpus_size_media_formats.svg"))
plt.show()

# explore canonicity and gender

dtm_obj = DocFeatureMatrix(data_matrix_filepath=infile_name, metadata_csv_filepath= metadata_filepath) # combine corpus with metadata information using the DocFEatureMatrix class and its methods

rel_metadata = ["Gattungslabel_ED_normalisiert", "Jahr_ED", "Medientyp_ED", "Gender", "Kanon_Status", "seriell"]


dtm_obj = dtm_obj.add_metadata(rel_metadata)
dtm_obj = dtm_obj.reduce_to(rel_metadata, return_eliminated_terms_list=False)

df = dtm_obj.data_matrix_df

# for convenience, abbrieviations can be replaced by meaningful genre names
replace_dict = {"Gattungslabel_ED_normalisiert": {"N": "Novelle", "E": "Erzählung", "0E": "sonstige Prosaerzählung", "0R" : "sonstige Journalinhalte", "0PE" : "sonstige Prosaerzählung", "0X_Essay" : "sonstige Journalinhalte", "0PB" : "sonstige Journalinhalte", "Lyrik" : "sonstige Journalinhalte", "Drama" : "sonstige Journalinhalte",
                                    "R": "Roman", "M": "Märchen", "XE": "sonstige Prosaerzählung", "V": "sonstige Journalinhalte", "V ": "sonstige Journalinhalte", "0P": "sonstige Journalinhalte", "0": "sonstige Journalinhalte"}}
df = full_genre_labels(df, replace_dict=replace_dict)

# fpr convenenince different media types are normalized to a smaller set of types
replace_dict = {"Medientyp_ED": {"Zeitschrift": "Journal", "Zeitung": "Journal", "Kalender": "Journal", "Rundschau" : "Journal", "Zyklus" : "Anthologie", "Roman" : "Werke", "(unbekannt)" : "selbst. Roman Buchdrucke",
                                    "Illustrierte": "Journal", "Sammlung": "Anthologie", "Nachlass": "Werke", "Jahrbuch":"Taschenbuch", "Monographie": "Werke"}}


df = full_genre_labels(df, replace_dict=replace_dict)

replace_dict = {"Gender": {"m": "Male", "f": "Female", "unbekannt": "unknown"}}


df = full_genre_labels(df, replace_dict=replace_dict)


replace_dict = {"Kanon_Status": {0: "very low", 1: "low", 2: "mid", 3:"high"}}


df = full_genre_labels(df, replace_dict=replace_dict)


replace_dict = {"seriell": {"True": "Serie", "TRUE": "Serie", "vermutlich": "Serie", "(unbekannt)":"unbekannt",
                                                  "False": "nicht-seriell", "FALSE":"nicht-seriell"}}


df = full_genre_labels(df, replace_dict=replace_dict)

metadata_dfs = []
rel_metadata = ["Gender", "Kanon_Status", "seriell"]
for metadata in rel_metadata:
    column0 = str("distrubtion of " + metadata)
    column1 = str("distribution of "+ metadata + " (relative share)")
    new_df = pd.concat([df[metadata].value_counts(), df[metadata].value_counts(normalize=True)], axis=1)
    new_df.columns = [column0, column1]
    print(new_df)
    metadata_dfs.append(new_df)

gender_df = metadata_dfs[0]
canon_df = metadata_dfs[1]
seriell_df =metadata_dfs[2]


gender_df.to_csv(os.path.join(tables_path, "corpus_gender_distribution.csv"))
canon_df.to_csv(os.path.join(tables_path, "corpus_canonicity_distribution.csv"))
seriell_df.to_csv(os.path.join(tables_path, "corpus_serial_bool_distribution.csv"))

fig, ax = plt.subplots(figsize=(12,8))
df = gender_df.copy()
#df = df[:-1] # drop last row with totals
ax.pie(df.iloc[:,1], labels=df.index,autopct='%1.1f%%',
       colors=["blue", "Red", "grey"])
plt.title("Gender distribution")

plt.tight_layout()
plt.savefig(os.path.join(figures_path, "pie_chart_corpus_gender_distribution.svg"))
plt.show()



fig, ax = plt.subplots(figsize=(12,8))
df = canon_df.copy()
#df = df[:-1] # drop last row with totals
ax.pie(df.iloc[:,1], labels=df.index,autopct='%1.1f%%',
       colors=["blue", "red", "grey", "green"])
plt.title("Canonicity distribution")

plt.tight_layout()
plt.savefig(os.path.join(figures_path, "pie_chart_corpus_canonicity_distribution.svg"))
plt.show()