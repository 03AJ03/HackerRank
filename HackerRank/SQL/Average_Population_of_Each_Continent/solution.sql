SELECT COUNTRY.Continent,
       FLOOR(AVG(CITY.Population)) AS AvgCityPopulation
FROM CITY
JOIN COUNTRY
  ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;
