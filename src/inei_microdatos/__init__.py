"""Programmatic access to INEI Peru's microdata portal."""

from inei_microdatos.catalog import (
    build_catalog,
    catalog_age,
    load_catalog,
    save_catalog,
)
from inei_microdatos.client import INEIClient
from inei_microdatos.download import LAYOUTS, download_docs, download_modules
from inei_microdatos.geography import select_census_geography
from inei_microdatos.reader import list_tables, read_catalog_entry, read_module
from inei_microdatos.survey_geography import geography_capabilities, select_geography
from inei_microdatos.variables import search as search_variables
from inei_microdatos.variables import search_across_years

__version__ = "0.5.0"
__all__ = [
    "INEIClient",
    "build_catalog",
    "load_catalog",
    "catalog_age",
    "save_catalog",
    "download_modules",
    "download_docs",
    "read_module",
    "read_catalog_entry",
    "list_tables",
    "LAYOUTS",
    "select_census_geography",
    "select_geography",
    "geography_capabilities",
    "search_across_years",
    "search_variables",
]
