-- =====================================================
-- KPI QUERIES
-- =====================================================

SELECT
    category,
    COUNT(*) AS total_products,
    AVG(price) AS average_price
FROM products
GROUP BY category;



-- =====================================================
-- PRODUCT PERFORMANCE
-- =====================================================

SELECT
    title,
    category,
    rating,
    price
FROM products
ORDER BY rating DESC
LIMIT 10;



-- =====================================================
-- INVENTORY MONITORING
-- =====================================================

SELECT
    title,
    stock,
    category
FROM products
WHERE stock < 20
ORDER BY stock ASC;



-- =====================================================
-- ALERT QUERIES
-- =====================================================

SELECT
    category,
    SUM(price * stock) AS inventory_value
FROM products
GROUP BY category
ORDER BY inventory_value DESC;