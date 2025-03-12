import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application



sys.path.insert(0, os.path.abspath('/workspaces/new1'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotutorial.mysite.settings")
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'djangoapp'
copyright = '2025, Зубов Александр'
author = 'Зубов Александр'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    ]

# autodoc_mock_imports = ["djangotutorial"]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_static_path = ['_static']


