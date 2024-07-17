# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
from resilient_sdk.util import package_file_helpers
import os

sys.path.insert(0, os.path.abspath("."))

##################################
## HELPER FUNCTIONS FOR CONF.PY ##
##################################

def get_function_content(packages, base_dir, object_label, display_name_lambda, description_lambda):
    """
    Load object content base on list of all package names
    and the object label and a lambda function to get its display name
    and description.

    Generates a markdown table of the package's desired objects listed in the table
    and then builds up the whole page, stringing together tables for each app

    Example:

        ### My App
        [Full app documentation](/fn_my_app/README.md)

        |Functions     |Description                       |
        |--------------|----------------------------------|
        |App Function  |This is the function's description|
        |App Function 2|This is the function's description|


    :param packages: list of package names (to append to base_dir path)
    :type packages: list[str]
    :param base_dir: base directory of all the apps
    :type base_dir: str
    :param object_label: functions, playbooks, etc...
    :type object_label: str
    :param display_name_lambda: lambda function to get the display name of the object
    :type display_name_lambda: func
    :param description_lambda: lambda function to get the description of the object
    :type description_lambda: func
    :return: markdown page with tables of the object for every app that has them
    :rtype: str
    """
    details = ""

    # loop through
    for package_name in packages:
        path_package = os.path.join(base_dir, package_name)
        path_setup_py = os.path.join(path_package, "setup.py")
        path_customize = os.path.join(path_package, package_name, "util", "customize.py")

        try:
            # load the setup.py file so we can get the display name
            setup_py = package_file_helpers.parse_setup_py(path_setup_py, package_file_helpers.SUPPORTED_SETUP_PY_ATTRIBUTE_NAMES)
        except:
            # skip any apps with setup py files not properly formatted
            print(f"Skipping {package_name} because setup.py is not readable")
            continue
        display_name = setup_py.get("display_name") or setup_py.get("name")

        try:
            # load the export.res
            customization = package_file_helpers.get_import_definition_from_customize_py(path_customize)
        except:
            # skip any apps with customize files not properly formatted or located
            print(f"Skipping {package_name} because customize.py or export.res is not readable")
            continue


        # if object exists for app's customizations, then build table
        if customization.get(object_label):
            details += f"\n### {display_name}\n[Full app documentation](/{setup_py.get('name')}/README.md)"
            details += f"\n\n|{object_label.capitalize()}|Description|\n|---|---|"
            for o in customization.get(object_label):
                o_display_name = display_name_lambda(o)
                o_description = description_lambda(o)
                o_description = o_description.replace("\n", " ")
                details += f"\n|{o_display_name}|{o_description}|"
            details += "\n"# "\n\n</details>\n"

    return details


project = "IBM Security QRadar SOAR Apps"
author = "IBM Security QRadar SOAR"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ # pip install sphinx sphinx-autobuild furo sphinx_copybutton myst_parser sphinx-design
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_design"
]
myst_enable_extensions = [
    "substitution", # needed for substitutions in markdown. see myst_substitutions for uses
    "colon_fence"
]
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

templates_path = ["docs/_templates"]
# these include and exclude patterns are very important to this
# the excluded items are items that shouldn't be included in the pages
# the included items are the explicit files that we will build our pages off of
include_patterns = ["index.rst", "**/README.md", "fn_service_now/docs/**", "docs/python_api.md"]# CHANGE_HERE when ready to have all objects, add "docs/all_objects/**" to this list and remove from below
exclude_patterns = ["docs/_build", "Thumbs.db", ".DS_Store", "**/doc", "**/data", "**/tests", "docs/all_objects/**"]



# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "QRadar SOAR Apps"
html_favicon = "docs/_static/IBM_Security_Shield.ico"
html_theme_options = {
    "light_logo": "IBM_Security_Light.png",
    "dark_logo": "IBM_Security_Dark.png",
    # "announcement": "<em>This site is still in development and some links may be broken. Please be patient as we work to make things perfect.</em>" # option here to add site-wide banner; use with caution
}
html_use_index = False
html_show_sourcelink = False
html_domain_indices = False
# Add path to logos
html_static_path = ["docs/_static"]
html_css_files = [
    'css/custom.css',
]
html_js_files = [
    'js/custom.js',
]


#######################
# Create dynamic content from code to use in future .rst and .md files
#######################
# open ALLOW_IMAGE_NAMES to get list of images to include
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
path_allow_images = os.path.join(base_dir, ".scripts", "ALLOW_IMAGE_NAMES.txt")
all_packages = []
with open(path_allow_images, "r", encoding="utf-8") as allowed_images:
    for line in allowed_images.readlines():
        line = line.strip()
        if line and not line.startswith("#"):
            all_packages.append(line)


# for MVP this list was removed from the TOC but may be replaced eventually
# see /docs/all_objects/index in this repo for details
# to bring this back into being, search this file for CHANGE_HERE and update
myst_substitutions = {
    "all_functions": get_function_content(all_packages, base_dir, "functions", lambda o: o.get("display_name"), lambda o: o.get("description", {}).get("content", "") or ""),
    "all_playbooks": get_function_content(all_packages, base_dir, "playbooks", lambda o: o.get("display_name"), lambda o: o.get("description", {}).get("content", "") or ""),
    "all_workflows": get_function_content(all_packages, base_dir, "workflows", lambda o: o.get("name"), lambda o: o.get("description", "") or "")
}

# generate list of recently updated apps which will be removed from the "all apps" side bar and placed at the top
recently_updated_names = ["fn_service_now", "fn_remedy", "fn_siemplify", "fn_vmware_cbc", "fn_aws_iam", "fn_symantec_dlp", "rc_data_feed_plugin_resilientfeed", "fn_wiz"]
# generate paths to each readme for the TOC/sidebar
all_readmes = "\n    ".join([f"/{p}/README.md" for p in all_packages if p not in recently_updated_names])
recently_updated = "\n    ".join([f"/{p}/README.md" for p in recently_updated_names])


# create root table of contents; this determines the main page (index.rst)
# as well as the left side bar contents
TOC = f"""
**New and Recently Updated Apps**

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :caption: New and Recently Updated Apps

    {recently_updated}

**App Development**

.. toctree::
    :maxdepth: 1
    :caption: App Development

    /docs/python_api.md

**All Apps**

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :caption: All Apps

    {all_readmes}
"""

# add dynamically generated toc to the index page
rst_epilog = f"""
.. |toc| replace:: {TOC}
"""
