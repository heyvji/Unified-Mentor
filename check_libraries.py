import importlib

libs = [
    "pandas", "numpy", "matplotlib", "seaborn", "nltk", "textblob",
    "plotly", "scikit-learn", "gensim", "spacy", "wordcloud", "streamlit"
]

for lib in libs:
    try:
        importlib.import_module(lib)
        print(f"{lib}: ✅ Installed")
    except ImportError:
        print(f"{lib}: ❌ Not Installed")
