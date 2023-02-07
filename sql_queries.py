import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "IF EXISTS DROP TABLE staging_events_table_drop"
staging_songs_table_drop = "IF EXISTS DROP TABLE staging_songs_table_drop"
songplay_table_drop = "IF EXISTS DROP TABLE songplay_table_drop"
user_table_drop = "IF EXISTS DROP TABLE songplay_table_drop"
song_table_drop = "IF EXISTS DROP TABLE songplay_table_drop"
artist_table_drop = "IF EXISTS DROP TABLE songplay_table_drop"
time_table_drop = "IF EXISTS DROP TABLE songplay_table_drop"

# CREATE TABLES

staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS staging_events_table(
            artist varchar sortkey distkey, 
            auth varchar,
            firstName varchar, 
            gender char, 
            itemInSession int, 
            lastName varchar, 
            length int, 
            level varchar, 
            location varchar, 
            method varchar, 
            page varchar, 
            registration int, 
            sessionId int , 
            song varchar, 
            status int , 
            ts numeric , 
            userAgent, 
            userId int)
""")

 = ("""CREATE TABLE IF NOT EXISTS staging_songs_table(
            num_songs int, 
            artist_id char, 
            artist_latitude varchar, 
            artist_longitude varchar, 
            artist_location varchar, 
            artist_name varchar, 
            song_id char,
            title varchar, 
            duration numeric, 
            year int)
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id int not null identity(0,1) primary key, start_time int not null, user_id int not null, level int, song_id varchar, artist_id varchar, session_id int not null, location int, user_agent int)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int not null primary key, first_name varchar not null, last_name varchar not null, gender varchar, level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int not null primary key, first_name varchar not null, last_name varchar not null, gender varchar, level varchar)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS CREATE TABLE IF NOT EXISTS artists(artist_id text not null primary key, name varchar not null, location varchar, lattitude int, longitude int)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time int, hour int, day int, week int, month int, year int, weekday int)
""")

# STAGING TABLES

staging_events_copy = ("""   copy staging_songs from 's3://udacity-dend/song_data'
                             credentials 'aws_iam_role={}'
                             gzip delimiter ';' compupdate off region 'us-wewest-2';
""").format()

staging_songs_copy = ("""    copy staging_songs from 's3://udacity-dend/song_data'
                             credentials 'aws_iam_role={}'
                             gzip delimiter ';' compupdate off region 'us-wewest-2';
""").format()

# FINAL TABLES

songplay_table_insert = ("""Insert songplay_table(song_id, title, artist_id, year, duration) \
                            SELECT DISTINCT song_id, title, artist_id, year, duration from staging_songs_table
""")

user_table_insert = ("""INSERT  user_table(user_id, first_name, last_name, gender, level) \
                        SELECT DISTINCT user_id, first_name, last_name, gender, level from staging_events_table
""")

song_table_insert = ("""INSERT song_table(song_id, title, artist_id, year, duration) \
                        SELECT DISTINCT song_id, title, artist_id, year, duration from staging_songs_table
""")

artist_table_insert = ("""INSERT artist_table(artist_id, name, location, lattitude, longitude) \
                          SELECT DISTINCT artist_id, artist_name, artist_location, artist_lattitude, artist_longitude from staging_songs_table
""")

time_table_insert = (""" time_table(start_time, hour, day, week, month, year, weekday) \
                         SELECT DISTINCT EXTRACT(time from ts) as start_time, EXTRACT(Hour from ts) as hour, EXTRACT(Day from ts) as day, EXTRACT(Week from ts) as week, EXTRACT(Month from ts) as month, EXTRACT(year from ts) as year, EXTRACT(weekday from ts) as weekday from staging_songs_table
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]


