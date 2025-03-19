import os
import sys
from pathlib import Path
from django.conf import settings
from django.core.wsgi import get_wsgi_application
import django


sys.path.insert(0, os.path.abspath(os.path.join('..', '..', 'djangotutorial')))
# sys.path.insert(0, str(Path('..', 'djangotutorial/polls').resolve()))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
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
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',  # для автогенерации подсказок типов
    'sphinxcontrib_django',  # для поддержки Django
]
autodoc_member_order = 'bysource'  # Порядок следования членов по исходному коду
autodoc_default_options = {
    'members': True,  # Включает все члены класса
    'undoc-members': True,  # Включает даже не задокументированные члены
    'show-inheritance': True,  # Показывает наследование классов
}

# autodoc_mock_imports = ["djangotutorial"]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_static_path = ['_static']


