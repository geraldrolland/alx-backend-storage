-- Lists all bands with Glam rock as their main style, ranked by their longevity.
-- SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
SELECT band_name,
IF(split IS NOT NULL, split - formed, 2022 - formed) AS lifespan
FROM holberton.metal_bands;
