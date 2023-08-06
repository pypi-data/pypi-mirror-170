<!---
[![Build Status](https://travis-ci.com/OSGeo/grass.svg?branch=main)](https://travis-ci.com/OSGeo/grass)
[![GCC C/C++ standards check](https://github.com/OSGeo/grass/workflows/GCC%20C/C++%20standards%20check/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3A%22GCC+C%2FC%2B%2B+standards+check%22)
[![Python code quality check](https://github.com/OSGeo/grass/workflows/Python%20code%20quality%20check/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3A%22Python+code+quality+check%22)
[![General linting](https://github.com/OSGeo/grass/workflows/General%20linting/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3A%22General+linting%22)
[![Ubuntu](https://github.com/OSGeo/grass/workflows/Ubuntu/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3AUbuntu)
[![OSGeo4W](https://github.com/OSGeo/grass/workflows/OSGeo4W/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3AOSGeo4W)
[![CentOS](https://github.com/OSGeo/grass/workflows/CentOS/badge.svg)](https://github.com/OSGeo/grass/actions?query=workflow%3ACentOS)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5176030.svg)](https://doi.org/10.5281/zenodo.5176030)
--->

![Latest Release](https://img.shields.io/pypi/v/osgeonorge.svg)
![Package Status](https://img.shields.io/pypi/status/osgeonorge.svg)
![License](https://img.shields.io/pypi/l/osgeonorge.svg)
![Build Status](https://img.shields.io/pypi/status/osgeonorge.svg)
![Coverage](https://gitlab.com/ninsbl/osgeonorge/badges/main/coverage.svg)
[![Build Status](https://gitlab.com/ninsbl/osgeonorge/badges/main/pipeline.svg)](https://gitlab.com/ninsbl/osgeonorge/pipelines)
[![Documentation](https://readthedocs.org/projects/pip/badge/)](https://osgeonorge.readthedocs.io/en/latest/)

# OSGeonorge

OSGeonorge is a collection of tools and functions for ETL
or ELT tasks with data from Geonorge.no using 
[OSGeo](https://www.osgeo.org/) software. It aims
at simplifying data warehousing or inclusion of data from
geonorge (https://www.geonorge.no) in maintenance or analysis pipelines.

## Documentation
Please visit the [documentation](https://ninsbl.gitlab.io/osgeonorge)
for details on installation, usage and API reference.

## Requirements

Required Python packages:
- requests
- psycopg2
- numpy
- GDAL (>=3.4.2)

Other required librariies:
- openfyba

## Contributing

All contributions, bug reports, bug fixes, documentation improvements,
enhancements and ideas are welcome. These should be submitted at the
[Gitlab repository](https://gitlab.com/ninsbl/osgeonorge).

## License

OSGeonorge is Free and Open Source Software with a
GPL >= 3 license.

## Credits

The layout and content of the OSGeonorge package is based on the
[PyPi package template](https://gitlab.com/costrouc/python-package-template) by
[Christopher Ostrouchov](https://gitlab.com/costrouc). Kudos to him for a very
helpful instruction on creating Python packages.
