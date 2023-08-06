
see [`BACKLOG`](https://github.com/kr-g/smog/blob/main/BACKLOG.md)
for open development tasks and limitations.


# CHANGELOG


## version v0.0.4 - 20221009

- `colman` sub-cmd `-rename` to rename a collection
  - a literal "%d" in the name will be expanded to the first/ last date(s) of the collection media items
- converter
 - image 
   - strip metadata
   - thumbnail
   - resize
   - watermark   
 - pdf 
   - watermark   
- `scan` BUG-FIX: raise StopIteration removed when file is renamed in repo folder
- `check` sub-cmd
  - db and repo integrity
  - source path against db-index path integrity
- pagination opt `-page` for `find` sub-cmd
- list hashtags with show-tags opt for `find` sub-cmd
- list where media is used in collections with show-cols opt for `find` sub-cmd
- find and remove media confirmation prompt 
- converter pipe enhancements
  - added `tee` support for writing the produced output to a different folder/ filename
  - added `pipeio` support what produces the original input as output again
    - this is supposed to be used together with tee, see `run_converter.py` 
      so that the input can be reused by the next pipe stage 
- `colman` sub-cmd `-add-media` and `-rm-media` media read media-id from stdin 
  with cmd-line parameter given as '-'
- `cat` sub-cmd prints a media from repo to stdout
  - converter `getmedia` for getting a media from smog repo to converter pipe
- cmd-line tool `smogconvert` added
- 


## version v0.0.3 - 20220725

- new for `colman`
  - `-add-media`, adding media to a collection
  - `-rm-media`, removing media from a collection
  - `touch`, sets the first/last timestamps fresh 
    - resolves BUG in `scan` with `-col`
- sub-cmd `tag` for hashtag and media handling
- database schema revision check during startup
- `find` filter on collection id
- license change
- 


## version v0.0.2 - 20220712

- support of xmp metadata added
  - support of various file types containing xmp metadata
    - `xmp -types` will list all file extensions
  - cmd-line `xmp` sub-command for query xmp metadata
- [`sqlalchemy`](https://www.sqlalchemy.org/) orm integration for media database
- introduced pipe style processing of media items
- enhanced cmd-line with `scan` sub-command
- cmd-line `find` sub-command 
- cmd-line `scan` hashtag 
- cmd-line `scan` collection 
- added `alembic` database migration
- added `config` sub-command with `-db-init` and `-db-migrate`
- `find` filter on hashtag(s)
- `find` filter on collection name
- `find` short display option showing column `media.id`
- `find` with `-remove` for deleting from db-index and repo (file-system)
- `col` for inspecting collections
- `colman` with `remove` for deleting a collection from the db-index
- 


## version v0.0.1 - 20220626

- first release
- 
