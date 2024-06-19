-- A SQL script that lists all bands with Glam rock as
-- their main style, ranked by their longevity
SELECT band_name,
  FLOOR(2022 - formed) AS lifespan
FROM metal_bands
WHERE split is NULL OR split > 2022
  AND FIND_IN_SET('Glam rock', style) = 1
ORDER BY lifespan DESC;
