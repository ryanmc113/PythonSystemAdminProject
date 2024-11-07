# PythonSystemAdminProject
For backup remote PostgresSQL database either locally or to S3


Prepareing the Development
------------------------------
1. Ensure ``pip`` and ``pipenv`` are installed.

Usage
------------------------------

Pass in a full database URL, the storage driver, and the diestination.

S3 Example w/ bucket name:

:: 
    $pgback up postgress://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

:: 

    $pgbackup postgress://bob@example.com:5432/db_one -- driver local /var/local/db_one/backups/dump.sql


Running Tests
------------------------------

run tests locall ysing ``make`` if virtualenv is active:

:; 
    $make

if virtualenv isn't active then use:

::

    $pipenv run make