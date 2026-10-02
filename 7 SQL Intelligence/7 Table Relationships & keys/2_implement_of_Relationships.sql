CREATE TABLE salesreport (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    location_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    discount NUMERIC(5,2) DEFAULT 0,
    total_amount NUMERIC(12,2) NOT NULL,

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    CONSTRAINT fk_location
        FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);

alter table 
 salesreport rename to sales;

INSERT INTO sales
(sale_date, customer_id, product_id, location_id, quantity, discount, total_amount)
VALUES
('2026-09-01', 1, 1, 1, 2, 5.00, 123500.00),
('2026-09-02', 2, 2, 2, 1, 10.00, 27000.00),
('2026-09-03', 3, 3, 3, 3, 5.00, 7125.00),
('2026-09-04', 4, 4, 4, 2, 0.00, 3600.00),
('2026-09-05', 5, 5, 5, 4, 10.00, 3240.00),
('2026-09-06', 6, 6, 6, 1, 5.00, 8075.00),
('2026-09-07', 7, 7, 7, 2, 0.00, 3600.00),
('2026-09-08', 8, 8, 8, 1, 10.00, 4050.00),
('2026-09-09', 9, 9, 9, 3, 5.00, 3420.00),
('2026-09-10', 10, 10, 10, 2, 0.00, 1400.00),

('2026-09-11', 1, 2, 3, 2, 5.00, 57000.00),
('2026-09-12', 2, 3, 4, 1, 0.00, 2500.00),
('2026-09-13', 3, 4, 5, 3, 10.00, 4860.00),
('2026-09-14', 4, 5, 6, 5, 5.00, 4275.00),
('2026-09-15', 5, 6, 7, 2, 10.00, 15300.00),
('2026-09-16', 6, 7, 8, 4, 5.00, 6840.00),
('2026-09-17', 7, 8, 9, 2, 0.00, 9000.00),
('2026-09-18', 8, 9, 10, 3, 5.00, 3420.00),
('2026-09-19', 9, 10, 1, 5, 10.00, 3150.00),
('2026-09-20', 10, 1, 2, 1, 5.00, 61750.00);

select * from sales;