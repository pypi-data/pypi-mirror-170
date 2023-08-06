
Check
[`CHANGELOG`](https://github.com/kr-g/smog/blob/main/CHANGELOG.md)
for latest ongoing, or upcoming news.


# BACKLOG

<del>
- XMP evaluation
  
  - https://pypi.org/project/python-xmp-toolkit/
  
    - https://github.com/python-xmp-toolkit/python-xmp-toolkit
  
      - https://libopenraw.freedesktop.org/exempi/
</del>

<del>
- database schema migration

  - https://github.com/sqlalchemy/alembic
</del>

- automatic tests 

<del>
- configuration of alembic paths via smog cmd-line

  - auto migrate smog.db
</del>

- find by media name 
- support for MySQL
- support for PostgreSql
- rework cmd-line interface
- processed-files handling (cmd-line `-proc`). move already scanned media to separate folder
- filter on gps location
  - theory
    - https://en.wikipedia.org/wiki/Haversine_formula
      - https://en.wikipedia.org/wiki/Versine#Haversine
        - https://en.wikipedia.org/wiki/Versor
          - https://upload.wikimedia.org/wikipedia/commons/7/73/ECEF_ENU_Longitude_Latitude_relationships.svg
  - impl
    - https://en.wikipedia.org/wiki/SpatiaLite
      - https://www.gaia-gis.it/fossil/libspatialite/home
      - others hilbert or z -curve, r-tree ...
        - https://en.wikipedia.org/wiki/Geohash
      - https://en.wikipedia.org/wiki/Military_Grid_Reference_System
    - 
- outbound processing
  - ~~watermark~~
  - ~~resize~~
  - ~~thumbnails~~
  - convert to different pic formats
  - word press integration (?)
  - pdf ~~watermark~~, preview, encrypt
    - [pypdf2 github](https://github.com/py-pdf/PyPDF2)
    - [pypdf2 readthedocs](https://pypdf2.readthedocs.io/en/latest/)
- syncronize data from different devices
- 


# OPEN ISSUES

refer to [issues](https://github.com/kr-g/smog/issues)


# LIMITATIONS

- 

