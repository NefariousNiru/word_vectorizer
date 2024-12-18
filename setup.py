from setuptools import setup

setup(
    name="wcc",  # Name of your package
    version="0.1",
    py_modules=["arguments", "util", "word_vectorizer"], # Modules in package
    install_requires=[
        "argparse",  # argparse is part of the standard library in Python 3
    ],
    entry_points={
        "console_scripts": [
            "wcc=word_vectorizer:main",  # Entry point to the main function in word_vectorizer.py
        ],
    },
)
