# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.abspath("."))
sys.path.insert(0, '../..')

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "renpydoc",
]

templates_path = ["_templates"]
html_static_path = ["_static"]

source_suffix = ".rst"

project = u"TODO"
copyright = u"TODO, Elckarow"
author = "Elckarow"
release = "TODO"
version = release

exclude_patterns = [ ]

pygments_style = "default"

html_title = "TODO"
html_logo = "images/logo.png"

html_theme = "sphinx_rtd_theme"
html_theme_options = { "sticky_navigation" :  False }

html_css_files = [
    "custom.css",
]

html_context = {
  "display_github": True,
  "github_user": "Elckarow",
  "github_repo": "TODO",
}

html_show_sourcelink = False
html_show_copyright = False

html_permalinks = True
html_permalinks_icon = " link"

epub_title = u"TODO"
epub_author = u""
epub_publisher = u""
epub_copyright = copyright

highlight_language = "renpy"
master_doc = "index"