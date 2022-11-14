-- Script that lists all cities contained in the database hbtn_0d_usa.
-- SELECT cities.id, cities.name, states.name FROM cities NATURAL JOIN states ORDER BY cities.id;
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states WHERE states.id = cities.id  ORDER BY cities.id;