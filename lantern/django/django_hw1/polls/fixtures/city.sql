CREATE TABLE City (
    CityId SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    CountryId INT REFERENCES Country(CountryId),
    );