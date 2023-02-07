# School-Project-Data-Warehouse

SQL_queries.py is what processes the data brought it from the S3 repository, from there it's brought into the two staging tables from S3 and into the stgaging tables where it's broken into dimension tables.

Credntials for aws should ALWAYS be stored in the cfg and never hard coded anywhere. Credentials have been removed from the config file on this repo as it will be public facing.
