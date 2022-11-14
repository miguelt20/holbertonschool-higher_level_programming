-- Script that lists all cities contained in the database hbtn_0d_usa.
-- SELECT cities.id, cities.name, states.name FROM cities NATURAL JOIN states ORDER BY cities.id;
SELECT cities.id, cities.name, states.name FROM cities JOIN states WHERE states.id = cities.state_id  ORDER BY cities.id;