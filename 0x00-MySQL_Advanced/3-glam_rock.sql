-- 3. Old school band
-- List glam rock bands by lifespan

SELECT band_name, 
       IF(split IS NULL, 2022 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
