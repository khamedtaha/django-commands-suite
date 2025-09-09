# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------
project = "django-commands-suite"
copyright = '2025, Mohammed taha Khamed '
author = "Mohammed taha Khamed"
version = "0.2"
release = "0.2.5"
# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",        
    "sphinx.ext.viewcode",       
    "sphinx.ext.napoleon",     
]
templates_path = ["_templates"]
exclude_patterns = []
# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]


sys.path.insert(0, os.path.abspath(".."))


