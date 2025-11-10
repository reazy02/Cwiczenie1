# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Automotive - Jak działa samochód'
copyright = '2025, Posłuszny'
author = 'Posłuszny'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'pl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'classoptions': ',oneside',
    'babel': r'\usepackage[polish]{babel}',
    'preamble': r'''
\usepackage{float}
\floatplacement{figure}{H}
\usepackage{titlesec}
\titleformat{\section}{\normalfont\Large\bfseries}{\thesection}{1em}{}
''',
}

latex_documents = [
    ('index', 'automotive_jakdzialasamochod.tex', 'Automotive - Jak działa samochód', 'Bartłomiej Posłuszny', 'report'),
]

