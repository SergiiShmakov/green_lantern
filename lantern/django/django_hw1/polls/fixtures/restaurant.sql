CREATE TABLE Restaurant (
    RestaurantId SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL UNIQUE,
    CountryID INT REFERENCES Country(CountryID),
    CityID INT REFERENCES City(CityID),
    MenuId INT REFERENCES Menu(MenuId),
    );