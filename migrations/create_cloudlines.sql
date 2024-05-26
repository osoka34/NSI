-- CREATE table cloudlines
CREATE table cloudlines (
    id serial primary key,
    Synoptic_index_of_thу_station integer not null default 0,
    Year integer not null default 0,
    Type_of_cloudiness integer not null default 0,
    Average_cloudiness_in_January varchar(40) not null default '',
    Average_cloudiness_in_February varchar(40) not null default '',
    Average_cloudiness_in_March varchar(40) not null default '',
    Average_cloudiness_in_April varchar(40) not null default '',
    Average_cloudiness_in_May varchar(40) not null default '',
    Average_cloudiness_in_June varchar(40) not null default '',
    Average_cloudiness_in_July varchar(40) not null default '',
    Average_cloudiness_in_August varchar(40) not null default '',
    Average_cloudiness_in_September varchar(40) not null default '',
    Average_cloudiness_in_October varchar(40) not null default '',
    Average_cloudiness_in_November varchar(40) not null default '',
    Average_cloudiness_in_December varchar(40) not null default ''
);