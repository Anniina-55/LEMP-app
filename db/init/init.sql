CREATE DATABASE IF NOT EXISTS appdb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
  
CREATE USER IF NOT EXISTS 'appuser'@'%';
GRANT ALL PRIVILEGES ON appdb.* TO 'appuser'@'%';
FLUSH PRIVILEGES;

USE appdb;

CREATE TABLE IF NOT EXISTS quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quote_text VARCHAR(255) CHARACTER SET utf8mb4 NOT NULL
);

INSERT INTO quotes (quote_text) VALUES
('Life is what happens when you’re busy making other plans'),
('Learning never exhausts the mind'),
('Every step forward, no matter how small is progress'),
('Mistakes are proof that you are trying'),
('Harjoitus tekee mestarin'),
('Parempi myöhään kuin ei milloinkaan'),
('Opiskelu on kivaa');