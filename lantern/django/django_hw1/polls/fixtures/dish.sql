CREATE TABLE Dish (
    DishId SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    recipe VARCHAR NOT NULL,
    weight DECIMAL NOT NULL,
    price DECIMAL NOT NULL,
    MenuId INT REFERENCES Menu(MenuId),
    );
