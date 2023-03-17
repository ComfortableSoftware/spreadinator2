

from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="Spreadinator2",
  url="https://github.com/ComfortableSoftware/spreadinator",
  version="2!0.2.1-2",
  package_dir={"spreadinator2": "spreadinator2"},
  package_data={
      "spreadinator2": [
          "../doc/*",
      ],
  },
  packages=find_packages(),
  install_requires=[
      "CS-CF2",
  ],
  scripts=[
      "scripts/copyonly2",
      "scripts/currentspread2",
      "scripts/respread2",
      "scripts/spread2",
      "scripts/spreadinator2",
  ],
)


#
