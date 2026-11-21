# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# -*- coding: utf-8 -*-

from datetime import datetime


# -- Project information -----------------------------------------------------

project = 'lightning'
author = 'Mathieu Blondel'
copyright = '{}, {}'.format(datetime.now().year, author)

# The full version, including alpha/beta/rc tags.
try:
    from lightning import __version__
except (ImportError, ModuleNotFoundError) as e:
    raise ImportError(
        f"You must install '{project}' package itself to build docs for it"
    ) from e

release = __version__
version = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_gallery.gen_gallery',
]

# Objects of the projects lightning documents against. Without this, the
# docstrings lightning inherits from scikit-learn reference objects that
# cannot be resolved.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
}

# Generate autosummary pages.
autosummary_generate = ["references.rst"]

autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "undoc-members": True,
}

# The root document of the build.
root_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '_templates', '_themes', 'Thumbs.db', '.DS_Store']

sphinx_gallery_conf = {
    'examples_dirs': '../examples',
    'gallery_dirs': 'auto_examples',
    'filename_pattern': '.py',
    'plot_gallery': 'True',
    'min_reported_time': 5,
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["lightning.css"]
