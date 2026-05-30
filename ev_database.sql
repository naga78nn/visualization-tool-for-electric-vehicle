CREATE DATABASE EVProject;

USE EVProject;

CREATE TABLE ElectricCarData (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Brand VARCHAR(100),
    Model VARCHAR(100),
    Efficiency_WhKm FLOAT,
    Range_Km INT,
    PriceEuro FLOAT
);

CREATE TABLE ChargingStations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    region VARCHAR(100)
);

INSERT INTO ElectricCarData
(Brand, Model, Efficiency_WhKm, Range_Km, PriceEuro)
VALUES
('Tesla', 'Model 3', 150, 500, 45000),
('Hyundai', 'Kona Electric', 140, 450, 35000),
('BMW', 'i4', 180, 480, 55000),
('Nissan', 'Leaf', 160, 350, 30000),
('Kia', 'EV6', 155, 510, 47000);

INSERT INTO ChargingStations(region)
VALUES
('North'),
('South'),
('North'),
('East'),
('West'),
('South');