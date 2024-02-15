-- a script that lists all cities contained in the database hbtn_0d_usa
SELECT id,name FROM cities
LEFT JOIN states ON state_id=id ORDER BY id;
