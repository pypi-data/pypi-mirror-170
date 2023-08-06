[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# smog 

simple media organizer - smog organizes media files !

the most simplest thing what `smog` does is like
e.g. a file `20220202_093343.jpg`
is moved into a folder structure like 
`~/media-repo/2022/02/20220202/20220202_093343.jpg`.

if possible 
[`xmp/exif metadata`](https://en.wikipedia.org/wiki/Extensible_Metadata_Platform)
is used to determine the date,
otherwise it's extracted from the name (experimental).

internally `smog` calculates a SHA512 hash for each file for identification 
along with an UUID identifier. in case an identical file is scanned more than once,
e.g. if it exists in different locations (and also different file names) on a harddrive, 
it is added only once to the main database-index and the internal storage. 
anyway `smog` tracks the different file locations on the hard drive with the database-index.

for organizing different scan runs, or groups of related data, 
`smog` can add media files to `collections`. 
a media file can be grouped in more than one collection without
duplicating the used space on the harddrive since this is stored 
only in the database-index.
in addition it is also possible to `hashtag` media files.

if a media contains xmp exif data regarding `gps` location data; this is extracted to a
separate database index. (with v0.0.2 it is not possible to filter on that)


## what is a media ?

a media is a file what transports kind of information, such as:

- photo
- video
- pdf 
- ...

`smog` supports xmp metadata scanning for many file types/ mimes out-of-the-box.

get a list of automatic xmp scanned file extensions with:

    smog xmp -types


# what's new ?

check
[`CHANGELOG`](https://github.com/kr-g/smog/blob/main/CHANGELOG.md)
for latest ongoing, or upcoming news.


# limitations

check 
[`BACKLOG`](https://github.com/kr-g/smog/blob/main/BACKLOG.md)
for open development tasks and limitations.


# how to use 

todo: documentation


## is there a graphical user interface (GUI) ?

not yet (but probably later...)


## how to use with cmd-line

get cmd-line parameter with

    smog --help
    smogconvert --help
    
or for a sub-cmd

    phyton3 -m smog *sub-cmd* --help

all cmd-line options under:
- [`README_CMDLINE`](README_CMDLINE.md)
- [`README_smogconvert_CMDLINE`](README_smogconvert_CMDLINE.md)


# additional tools

## smogconvert (experimental, with version v0.0.4)

the `smogconvert` tool-chain provides media manipulation prio sharing media such as
- strip metadata
- set xmp metadata from file
- save xmp metadata to file
- resize image
- convert to different format
- create thumbnail
- watermark image
- support of custom defined converter pipelines ([example](./run_converter.json))
-

since marked as experimental this is an objective to change.

the basic idea is that a single converter can be called stand-alone as well as
running within a more complex transformation as part of a pipelined process.

the interface documentation is pending and so one has to figure out by reading 
the code  what feature is offered by each converter. 
the generall cmd-line interface is `converter in_file out_file opts`, where
`in_file` and `out_file` can be set to a single minus (`-`) for reading 
the input from `stdin`, and wrting the output to `stdout`.

all converter offer a [`tee`](https://en.wikipedia.org/wiki/Tee_(command)) 
mode by adding the parameter `out=dest_file` to specify the file for the output;
and an option `pipeio=yes` to bypass processing on stdout and preserve the orignal
input (for former converter) as input for the next coverter in the pipeline.

__IMPORTANT:__
all additional converter parameter are passed in the format `key=value` 
e.g. `pipeio=yes` at the end of cmd-line. 


# additional reference documentation

for expert reading 

- [xmp (wikipedia)](https://en.wikipedia.org/wiki/Extensible_Metadata_Platform)
  - [adobe xmp specfification](https://github.com/adobe/xmp-docs) 
- 


# platform

tested on python3, and linux


# installation

`smog` project dependencies: 

- [`SQLAlchemy`](https://www.sqlalchemy.org/)
  - [`alembic`](https://alembic.sqlalchemy.org)
- [`python-xmp-toolkit`](https://python-xmp-toolkit.readthedocs.io/en/latest/)  
  - [`Exempi`](https://libopenraw.freedesktop.org/exempi/)
- [`python-dateutil`](https://dateutil.readthedocs.io/en/latest/)
- [`pypdf2`](https://pypdf2.readthedocs.io/en/latest/index.html)
- [`reportlab`](https://docs.reportlab.com/)
- [`image-magick`](https://imagemagick.org/)
- 

__NOTE:__

1. on linux `Exempi` is mostlikely already installed. 
otherwise download binaries from Exempi site or build local 
from source package 

2. [`image-magick`](https://imagemagick.org/)
must be installed manually.
`smogconvert` based tools call `convert` under the hood.
make sure that `convert` is in the PATH.

it is recommended to install `smog` into a 
[`virtual environment`](https://docs.python.org/3/tutorial/venv.html).

use bash:

    mkdir smog
    cd $_
    python3 -m venv .venv
    source .venv/bin/activate

then `smog` itself can be installed with

    phyton3 -m pip install smog

IMPORTANT:

it is recommened to install `smog` into a 
[`venv`](https://docs.python.org/3/library/venv.html)


 
## initial configuration

after first installation of `smog` run

    smog config -db-init
    
to create an empty database `~/media-db/smog.db` 


## upgrade from older version

backup your database `~/media-db/smog.db` and migrate 
the database with  

    smog config -db-migrate


# internals

folloing folders are used:

| folder | description |
| --- | --- | 
| ~/Pictures or ~/Bilder | scan default folder. can be overwritten with cmd-line `-src`  | 
| ~/media-repo | media repo folder where all data is stored. dont manipulate content of this folder, or sub-folders, manually. use `smog` cmd-line for this. can be overwritten with cmd-line `-dest`  | 
| ~/media-db | folder for the database index. can be overwritten with cmd-line `-repo-db`  | 

__IMPORTANT NOTE:__

`smog` database-index is build with relative paths. 
so it is important to call `smog` always with the same set of base parameters,
otherwise the database-index points to invalid destinations on the harddrive.

to view the database-index use `smog find`, `smog col`, or `smog colman` from 
cmd-line, or e.g. [`sqlitebrowser`](https://sqlitebrowser.org/) for raw view.


## are different database backend engines supported?

at the present time only `SQLite` is supported as database backend.
but since `smog` uses `SQLAlchemy` as  
[`ORM`](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) 
mapper it might be implemented in the future for other 
[sql dialects](https://docs.sqlalchemy.org/en/14/dialects/)


# license

`smog` is dual licensed, and free only for `non-commercial` use. read properly.
[`LICENSE`](https://github.com/kr-g/smog/blob/main/LICENSE.md)


## other licenses

this is not a comprehensive list, 
refer to each project to find more information

- [`SQLAlchemy`](https://github.com/sqlalchemy/sqlalchemy)
  - [`alembic`](https://github.com/sqlalchemy/alembic)
- [`python-xmp-toolkit`](https://github.com/python-xmp-toolkit/python-xmp-toolkit)  
  - [`Exempi`](https://github.com/freedesktop/exempi)
- [`python-dateutil`](https://github.com/python-xmp-toolkit/python-xmp-toolkit)
- [`pypdf2`](https://github.com/py-pdf/PyPDF2)
- [`reportlab`](https://docs.reportlab.com/)
