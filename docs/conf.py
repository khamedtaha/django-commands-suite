# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------
project = "django-commands-suite"
author = "Mohammed Taha Khamed"
version = "0.2"
release = "0.2.5"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",          # optional
    "sphinx_autodoc_typehints", # optional
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "titles_only": False,
}

# -- Language -------------------------------------------------
language = "en"  # change to "ar" if you want Arabic UI

# -- Custom CSS (for fonts like Tajawal) -------------------------------------
def setup(app):
    app.add_css_file("custom.css")
