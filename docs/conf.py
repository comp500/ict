# -*- coding: utf-8 -*-

from recommonmark.parser import CommonMarkParser

extensions = []
templates_path = ['/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx', 'templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']		
source_parsers = {		
            '.md': CommonMarkParser,		
        }
master_doc = 'index'
project = u'ict.infra.link'
copyright = u'2016'
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'ict-igcse-infralink'
html_theme = 'sphinx_rtd_theme'
file_insertion_enabled = False
latex_documents = [
  ('index', 'ict-igcse-infralink.tex', u'ict.infra.link Documentation',
   u'', 'manual'),
]

def setup(app):
   app.add_stylesheet("theme_overrides.css")
