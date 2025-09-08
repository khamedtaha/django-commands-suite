# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
project = "django-commands-suite"
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
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
