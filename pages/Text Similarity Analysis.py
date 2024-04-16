import streamlit as st
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re

st.write("# Text Analysis")
st.write("")
st.write("")
st.write("")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
df = st.session_state.df
df = df[:50]
st.subheader("Review Text")
st.write(df["Review Text"])

df["Preprocessed Review"] = df["Review Text"]
df["Preprocessed Review"] = df["Preprocessed Review"].apply(word_tokenize)

df["Preprocessed Review"] = df["Preprocessed Review"].apply(
    lambda x: [word.lower() for word in x]
)

stop_words = set(stopwords.words("english"))
df["Preprocessed Review"] = df["Preprocessed Review"].apply(
    lambda x: [word for word in x if word.lower() not in stop_words]
)

df["Preprocessed Review"] = df["Preprocessed Review"].apply(
    lambda x: [re.sub(r"[^\w\s]", "", token) for token in " ".join(x).split()]
)

st.write("")
st.write("")
st.write("")
st.subheader("Preprocessed Reviews")
st.write(df["Preprocessed Review"])

stemmer = PorterStemmer()
df["Preprocessed Review"] = df["Preprocessed Review"].apply(
    lambda x: [stemmer.stem(word) for word in x]
)

# lemmatizer = WordNetLemmatizer()
# df["Preprocessed Review"] = df["Preprocessed Review"].apply(
#     lambda x: [lemmatizer.lemmatize(word) for word in x]
# )

st.write("")
st.write("")
st.write("")
st.subheader("Reviews after Stemming")
st.write(df["Preprocessed Review"])

general = word_tokenize(df[df["Division Name"] == "General"].to_string())
general_petite = word_tokenize(df[df["Division Name"] == "General Petite"].to_string())
initmates = word_tokenize(df[df["Division Name"] == "Initmates"].to_string())


def jaccard_similarity(set1, set2):
    set1 = set(set1)
    set2 = set(set2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    return intersection / union


st.write("")
st.write("")
st.write("")
st.subheader("Jaccard Similarity")
st.write(
    f"Similarity Score between reviews of General and General Petite:  {jaccard_similarity(general, general_petite)}"
)
st.write(
    f"Similarity Score between reviews of General and Initmates:  {jaccard_similarity(general, initmates)}"
)
st.write(
    f"Similarity Score between reviews of General Petite and Initmates:  {jaccard_similarity(initmates, general_petite)}"
)
