from pathlib import Path

import pytest

from inei_microdatos import download_modules, load_catalog, read_module
from inei_microdatos.catalog import filter_catalog


def test_quickstart(tmp_path):
    # Cargar el catálogo incluido (viene con el paquete, sin configuración)
    catalog = load_catalog()

    # Filtrar lo que necesitas
    endes_2024 = filter_catalog(catalog, survey="endes", year_min=2024)

    # Download
    download_modules(endes_2024, dest=tmp_path, fmt="CSV", workers=4, layout="default")

    # Read into DataFrames
    dfs = read_module(
        Path(tmp_path)
        / "ENCUESTA DEMOGRÁFICA Y DE SALUD FAMILIAR - ENDES/2024/Unico/968-Modulo1629.zip"
    )
    for name, df in dfs.items():
        print(f"{name}: {df.shape}")


def test_renamu(tmp_path):
    # Cargar el catálogo incluido (viene con el paquete, sin configuración)
    catalog = load_catalog()

    # Filtrar lo que necesitas
    renamu_2024 = filter_catalog(catalog, survey="renamu", year_min=2024, year_max=2025)

    # Descargar
    download_modules(renamu_2024, dest=tmp_path, fmt="CSV", layout="flat")
    renamu_dir = Path(tmp_path) / "REGISTRO NACIONAL DE MUNICIPALIDADES - RENAMU"
    assert renamu_dir.exists()
    downloaded_files = set(map(lambda x: x.name, renamu_dir.iterdir()))
    print(downloaded_files)
    assert downloaded_files == {
        "928-Modulo1814.zip",
        "984-Modulo1963.zip",
    }


# RECH0: (37390, 44)
# RECH1: (135045, 36)
# RECH4: (135045, 22)
# RECHM: (3002, 8)
