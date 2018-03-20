DROP TABLE IF EXISTS wage;
CREATE TABLE wage (
    id				INTEGER,
    year			INTEGER,
    q1_wage			FLOAT,
    q2_wage			FLOAT,
    q3_wage			FLOAT,
    q4_wage			FLOAT
);

DROP TABLE IF EXISTS provider;
CREATE TABLE provider (
    id 				INTEGER PRIMARY KEY,
    name			VARCHAR,
    description			VARCHAR,
    email			VARCHAR,
    url				VARCHAR,
    year_incorporated		INTEGER
);

DROP TABLE IF EXISTS program_participant;
CREATE TABLE program_participant (
    id				INTEGER PRIMARY KEY,
    participant_id		INTEGER,
    program_code		INTEGER,
    provider_id			INTEGER REFERENCES provider(id),
    entry_date			DATE,
    exit_date			DATE,
    exit_type			VARCHAR,
    obtained_credentials	BOOLEAN,
    potential_credentials	VARCHAR,
    funding_sources		VARCHAR,
    program_name		VARCHAR,
    service_location		VARCHAR
);

