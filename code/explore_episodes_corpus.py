import pandas as pd
import os
import matplotlib.pyplot as plt

# Use these lines with your project path in case of error message "No module named 'preprocessing.corpus'"
# import sys
# sys.path.insert(1, <your_project_path>)

from preprocessing.corpus import DocFeatureMatrix
from preprocessing.presetting import global_corpus_representation_directory, vocab_lists_dicts_directory, load_stoplist, \
    global_corpus_raw_dtm_directory, local_temp_directory
from preprocessing.metadata_transformation import full_genre_labels, years_to_periods


# set your lokal path to your 19CproseCorpus path
project_path = '/home/julian/git/19CproseCorpus'

figures_path = os.path.join(project_path,"figures" )
data_path = os.path.join(project_path,"data" )
tables_path = os.path.join(project_path,"tables" )


metadata_filepath= os.path.join(data_path, "Bibliographie.tsv")


df = pd.read_csv(metadata_filepath, index_col=0, sep="\t")
df = df.reset_index()
df["isEpisode"] = df.loc[:, "Dokument_ID"].apply(lambda x: x[6:])
df = df[df["isEpisode"] != "00"]
print(df)

period_var = "Perioden"


replace_dict = {"Gattungslabel_ED_normalisiert": {"N": "Novelle", "E": "Erzählung", "0P":"other journal content",
                                                  "0E": "other prose fiction",
                                                  "0":"other prose fiction",
                                    "(unbekannt)":"other prose fiction",
                                    "0PE":"other prose fiction",
                                    "R": "Roman (novel)", "M": "Märchen (fairy tale)", "E_N_Rubrik":"Rubrik: Erzählungen und Novellen" ,
                                    "XE": "other prose fiction",
                                                  "0X": "other journal content"}}
df = full_genre_labels(df, replace_dict=replace_dict)

# for convenenince different media types are normalized to a smaller set of types
replace_dict = {"Medientyp_ED": {"Zeitschrift": "Journal", "Zeitung": "Journal", "Kalender": "Journal",
                                 "Rundschau" : "Rundschau", "Werke":"Buch", "Monatsschrift":"Journal",
                                 "Zyklus" : "Anthologie", "Roman" : "Buch", "(unbekannt)" : "Buch",
                                    "Illustrierte": "Journal", "Sammlung": "Anthologie",
                                 "Kolportage":"Kolportage",
                                 "Nachlass": "Buch", "Jahrbuch":"Taschenbuch", "Monographie": "Buch", "Deutsche Romanzeitung":"Journal"}}

df = full_genre_labels(df, replace_dict=replace_dict)

df = years_to_periods(input_df=df, category_name="Jahr_ED", start_year=1780, end_year=2000, epoch_length=70,
                      new_periods_column_name=period_var)

start_df = df.copy()

corpus_statistics = df.groupby([period_var, "Gattungslabel_ED_normalisiert"]).size()

df_corpus_statistics_genre = pd.DataFrame(corpus_statistics)

df = df_corpus_statistics_genre
df = df.unstack().reset_index()
df.set_index("Perioden",inplace=True)
df.columns = df.columns.droplevel()

title_en = "Corpus Size for Genres and Periods for episodes"
df.plot(kind='bar', stacked=False, title= title_en,
        color={"Erzählung": "green", "other prose fiction": "cyan",
               "Novelle": "red", "Roman (novel)": "blue", "Kolportage":"brown",
                "Rubrik: Erzählungen und Novellen":"lightgrey",
               "kein Label": "lightgrey", "Märchen (fairy tale)":"orange",
               "other journal content": "darkgrey"})
plt.xticks(rotation=45)
plt.ylim(0,1000)
plt.xlabel("periods") # if en
plt.ylabel("number of episodes")
plt.tight_layout()
plt.savefig(os.path.join(project_path, "figures", "en_episodes_Corpus_Size_for_Genres_and_Periods.svg"))
plt.show()

df = start_df.copy()
corpus_statistics = df.groupby([period_var, "Medientyp_ED"]).size()
df_corpus_statistics_media = pd.DataFrame(corpus_statistics)

title_en = "Corpus Size for Media and Periods for episodes"
title_de = "Zusammensetzung des Korpus nach Perioden und Medienformaten"

df = df_corpus_statistics_media
df = df.unstack().reset_index()
df.set_index("Perioden",inplace=True)
df.columns = df.columns.droplevel()

df.plot(kind='bar', stacked=False, title= title_en,
                                    color={"Anthologie":"yellow", "Kolportage":"brown",
                                           "Taschenbuch": "purple", "Familienblatt":"lightgreen", "Rundschau":"grey", "Buch":"darkgreen", "Journal":"lightblue"})
plt.xticks(rotation=45)
plt.ylim(0,1000)
plt.tight_layout()
plt.savefig(os.path.join(figures_path, "en_episodes_Corpus_Size_for_Media_types_and_Periods.svg"))
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
genre_df.to_csv(os.path.join(tables_path, "episodes_corpus_size_genre.csv"))

media_df = df_corpus_statistics_media_nontemporal
media_df.loc["Total"] = media_df.sum()
media_df["Proportion"] = media_df[0].apply(lambda x: x / media_df.loc["Total"])
media_df = media_df.rename(columns={0:"Count"})
print(media_df)
media_df.to_csv(os.path.join(tables_path, "episodes_corpus_size_media.csv"))