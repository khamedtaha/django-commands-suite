# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
project = "django-commands-suite"
copyright = '2025, Mohammed Taha Khamed'
author = "Mohammed Taha Khamed"
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


language=en