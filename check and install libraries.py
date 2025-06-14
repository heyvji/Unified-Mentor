import importlib
import subprocess
import sys

# List of libraries to check
libraries = [
    "pandas", "numpy", "matplotlib", "seaborn", "nltk", "textblob",
    "plotly", "scikit-learn", "gensim", "spacy", "wordcloud", "streamlit"
]

for lib in libraries:
    try:
        importlib.import_module(lib)
        print(f"{lib}: ✅ Already installed")
    except ImportError:
        print(f"{lib}: ❌ Not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
        print(f"{lib}: ✅ Successfully installed")
