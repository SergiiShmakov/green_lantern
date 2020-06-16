CREATE TABLE Menu (
    MenuId SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    DishId INT REFERENCES Dish(DishId),
    );
