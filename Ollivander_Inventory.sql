SELECT
    w.id, wp.age, w.coins_needed, w.power
FROM wands INNER JOIN wands_property wp ON w.code = wp.code
WHERE wp.is_evil = 0 AND w.coins_needed = (
        SELECT MIN(W2.coins_needed) FROM wands W2 INNER JOIN wands_property WP2 ON W2.code = WP2.code WHERE WP2.age = wp.age AND W2.power = w.power
    ) ORDER BY w.power DESC, wp.age DESC;