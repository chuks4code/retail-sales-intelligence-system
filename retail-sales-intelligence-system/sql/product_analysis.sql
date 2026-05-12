-- Top Rated Products

SELECT
    title,
    category,
    rating,
    price
FROM products
ORDER BY rating DESC
LIMIT 10;


-- Most Expensive Products

SELECT
    title,
    category,
    price
FROM products
ORDER BY price DESC
LIMIT 10;