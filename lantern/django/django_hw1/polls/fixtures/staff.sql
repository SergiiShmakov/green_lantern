CREATE TABLE Staff (
    StaffId SERIAL PRIMARY KEY,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL,
    birth_date DATE,
    email VARCHAR(254) UNIQUE,
    phone_number INT UNIQUE,
    salary INT,
    job_position  VARCHAR(32) NOT NULL,
    RestaurantId INT REFERENCES Restaurant(RestaurantId),
    );
