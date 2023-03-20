

from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="Spreadinator",
  url="https://github.com/ComfortableSoftware/spreadinator",
  version="0.3.0",
  package_dir={"spreadinator": "spreadinator"},
  package_data={
      "spreadinator": [
          "../doc/*",
      ],
  },
  packages=find_packages(),
  install_requires=[
      "CSCF",
  ],
  scripts=[
      "scripts/copyonly",
      "scripts/currentspread",
      "scripts/respread",
      "scripts/spread",
      "scripts/spreadinator",
  ],
)


#
