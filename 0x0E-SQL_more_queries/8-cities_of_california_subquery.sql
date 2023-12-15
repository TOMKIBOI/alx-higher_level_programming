-- Script that lists all registered cities in the california DB
SELECT id, name -- Query to list all the cities from California
FROM cities
WHERE state_id = ( -- Query to get the id of California
      SELECT id
      FROM states
      WHERE name = "California");
