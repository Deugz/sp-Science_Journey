# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Science Journey'
copyright = '2023, Vincent Deguin'
author = 'Vincent Deguin'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

comments_config = {
   "utterances": {
      "repo": "https://github.com/Deugz/sp-Science_Journey",
      "optional": "config",
   }
}

comments_config = {
   "hypothesis": True
}




extensions = [
  
  "myst_parser",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_new_tab_link",
  "sphinx_book_theme",
  "sphinx_togglebutton",
  "sphinx_thebe",
]

myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2



templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Logo/logo_SFTP.png"
html_favicon = "_static/Logo/logo_SFTP.png"
html_static_path = ['_static']

html_theme_options = {
    "external_links": [
        {
            "url": "https://deugz.github.io/nb-profile/_build/html/intro.html",
            "name": " &nbsp 👽 Profile",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-sbfp/_build/html/intro.html",
            "name": " &nbsp ✊ Projects",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-notes/_build/html/intro.html",
            "name": "&nbsp ✏️ Research notes",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-publi/_build/html/intro.html",
            "name": "&nbsp 💫 Publications",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-teaching/_build/html/intro.html",
            "name": "&nbsp 🎓 Teaching ",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/nb-blog/_build/html/intro.html",
            "name": "&nbsp 💥 Blog &nbsp",
            "attributes": {"target": "_blank"},
        },
        {
            "url": " https://deugz.github.io/nb-tools/_build/html/intro.html",
            "name": "&nbsp 🔧 Tools &nbsp",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "",
            "name": "&nbsp 🗨️ Forum ",
            "attributes": {"target": "_blank"},
        },
    ],
    "header_links_before_dropdown": 10,    
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/pydata/pydata-sphinx-theme",
            "icon": "fa-brands fa-github",
        },
    ],
    

    "logo": {
        "text": "V. Deguin",
        "image_dark": "_static/Logo/logo_SFTP.png",
        "alt_text": "V. Deguin",
    },
    
    
    "navbar_start": ["navbar-logo"],
    
}


html_css_files = ["css/custom_style.css", "css/Cube.css", "css/coffee_cup.css", "css/kittons.css", "css/style_book_shell.css", "css/style_flipping_card.css", "css/style_wheel.css"]
html_js_files = ["assets/script/kittons.js", "assets/script/script_flipping_card.js", "assets/script/script_wheel.js", "assets/script/scriptvideo.js", "assets/script/slideshow.js"]

    
