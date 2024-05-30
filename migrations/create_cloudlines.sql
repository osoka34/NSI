-- CREATE table cloudlines
CREATE table cloudlines (
    id serial primary key,
    synoptic_index_of_the_station integer not null default 0,
    year integer not null default 0,
    type_of_cloudiness integer not null default 0,
    average_cloudiness_in_january varchar(40) not null default '',
    average_cloudiness_in_february varchar(40) not null default '',
    average_cloudiness_in_march varchar(40) not null default '',
    average_cloudiness_in_april varchar(40) not null default '',
    average_cloudiness_in_may varchar(40) not null default '',
    average_cloudiness_in_june varchar(40) not null default '',
    average_cloudiness_in_july varchar(40) not null default '',
    average_cloudiness_in_august varchar(40) not null default '',
    average_cloudiness_in_september varchar(40) not null default '',
    average_cloudiness_in_october varchar(40) not null default '',
    average_cloudiness_in_november varchar(40) not null default '',
    average_cloudiness_in_december varchar(40) not null default ''
);