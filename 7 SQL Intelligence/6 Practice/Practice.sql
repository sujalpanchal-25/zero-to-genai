-- ============================================================
-- SQL INTELLIGENCE PRACTICE DATABASE
-- PostgreSQL
-- Topics covered from your uploaded practice files:
-- WHERE, ORDER BY, LIMIT/OFFSET, DISTINCT, BETWEEN, IN, ILIKE,
-- GROUP BY, HAVING, AND/NOT, ALTER TABLE, UPDATE, aggregates,
-- CASE, date/time functions, math functions, string functions.
-- ============================================================

-- STEP 1: Run this line separately if the database does not exist:


-- STEP 2: Connect to "sql_intelligence_practice" in pgAdmin/psql
-- and run everything below.

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(50) NOT NULL,
    email       VARCHAR(100) UNIQUE NOT NULL,
    age         INT NOT NULL,
    create_at   TIMESTAMP NOT NULL
);

INSERT INTO customers (name, email, age, create_at) VALUES
('Aarav',  'aarav@gmail.com', 19, '2025-01-15 10:30:00'),
('Aanya',  'aanya@gmail.com', 22, '2025-02-20 11:15:00'),
('Rahul',  'rahul@gmail.com', 27, '2025-03-12 09:45:00'),
('Riya',   'riya@gmail.com', 31, '2025-03-25 14:20:00'),
('Karan',  'karan@gmail.com', 24, '2025-04-05 16:10:00'),
('Kashish','kashish@gmail.com', 20, '2025-04-18 12:40:00'),
('Amit',   'amit@gmail.com', 35, '2025-05-02 08:30:00'),
('Anjali', 'anjali@gmail.com', 28, '2025-05-19 17:25:00'),
('Bhavya', 'bhavya@gmail.com', 19, '2025-06-07 10:05:00'),
('Chetan', 'chetan@gmail.com', 42, '2025-06-21 13:50:00'),
('Dev',    'dev@gmail.com', 30, '2025-07-03 15:15:00'),
('Diya',   'diya@gmail.com', 18, '2025-07-14 09:10:00'),
('Esha',   'esha@gmail.com', 26, '2025-08-01 11:35:00'),
('Harsh',  'harsh@gmail.com', 33, '2025-08-16 18:00:00'),
('Isha',   'isha@gmail.com', 25, '2025-08-29 14:45:00'),
('Jay',    'jay@gmail.com', 21, '2025-09-10 10:55:00'),
('Kunal',  'kunal@gmail.com', 37, '2025-09-22 16:35:00'),
('Meera',  'meera@gmail.com', 29, '2025-10-05 12:20:00'),
('Neha',   'neha@gmail.com', 32, '2025-10-19 09:40:00'),
('Om',     'om@gmail.com', 23, '2025-11-02 17:10:00');

-- Check the initial table
SELECT * FROM customers ORDER BY id;


-- ============================================================
-- ALTER TABLE PRACTICE AREA
-- Do these after the basic SELECT practice.
-- ============================================================

-- Add a phone column.
-- ALTER TABLE customers ADD COLUMN phone VARCHAR(15);

-- Add an active-status column with a default.
-- ALTER TABLE customers ADD COLUMN is_active BOOLEAN DEFAULT TRUE;

-- Add country with a default value.
-- ALTER TABLE customers
-- ADD COLUMN country VARCHAR(20) DEFAULT 'India' NOT NULL;

-- Rename create_at to admission.
-- ALTER TABLE customers RENAME COLUMN create_at TO admission;

-- Change age type.
-- ALTER TABLE customers ALTER COLUMN age TYPE INT;

-- Set a default for phone.
-- ALTER TABLE customers ALTER COLUMN phone SET DEFAULT 'N/A';

-- Remove the phone default.
-- ALTER TABLE customers ALTER COLUMN phone DROP DEFAULT;

-- Add a UNIQUE constraint to phone.
-- ALTER TABLE customers ADD CONSTRAINT phone_unique UNIQUE(phone);

-- Drop the constraint.
-- ALTER TABLE customers DROP CONSTRAINT phone_unique;

-- Drop a column when you are ready.
-- ALTER TABLE customers DROP COLUMN phone;


-- ============================================================
-- OPTIONAL RESET
-- If ALTER practice changes your table too much, run:
-- DROP TABLE IF EXISTS customers;
-- Then rerun CREATE TABLE + INSERT statements above.
-- ============================================================
