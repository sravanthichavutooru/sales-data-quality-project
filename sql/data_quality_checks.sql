-- Sales data quality checks
-- These queries require a table named sales containing the CSV data.
-- Adding this file alone does not run the queries.

-- 1. Find duplicate order IDs.
SELECT order_id, COUNT(*) AS record_count
FROM sales
GROUP BY order_id
HAVING COUNT(*) > 1;

-- 2. Find missing customer IDs.
SELECT *
FROM sales
WHERE customer_id IS NULL
   OR TRIM(customer_id) = '';

-- 3. Find zero or negative quantities.
SELECT *
FROM sales
WHERE quantity <= 0;

-- 4. Find negative unit prices.
SELECT *
FROM sales
WHERE unit_price < 0;

-- 5. Find incorrect totals.
-- Compare rounded amounts to two decimal places.
SELECT
    order_id,
    quantity,
    unit_price,
    total_amount,
    ROUND(quantity * unit_price, 2) AS expected_total
FROM sales
WHERE ROUND(total_amount, 2)
   <> ROUND(quantity * unit_price, 2);
