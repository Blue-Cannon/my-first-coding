# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute.
sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------
project = "My First Coding"
copyright = "BlueBixt 2026, All Rights Reserved."
author = "Rogge M. Ramos"

# The short X.Y version
version = "0.1.0"
# The full version, including alpha/beta/rc tags
release = "0.1.0"


# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",  # Core library for generating docs from docstrings
    "sphinx.ext.napoleon",  # Support for Google or NumPy styled docstrings
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.todo",  # Support for todo items
    "sphinx.ext.githubpages",  # Publish docs to GitHub Pages easily
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The master toctree document.
root_doc = "index"

# Language of the document
language = "en"


# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# Common choices: 'alabaster', 'furo', 'sphinx_rtd_theme'
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------
# If true, todo and todoList produce output, else they produce nothing.
todo_include_todos = True

# -- Options for napoleon extension ------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
