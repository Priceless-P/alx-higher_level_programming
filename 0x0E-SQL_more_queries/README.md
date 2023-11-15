# SQL - More Queries

This repository contains scripts for various SQL tasks. Each task is outlined below with its respective script file linked.

## Tasks and Associated Files

1. **[My privileges!](0-privileges.sql)**
   - Lists privileges for MySQL users 'user_0d_1' and 'user_0d_2' on the server.

2. **[Root user](1-create_user.sql)**
   - Creates the MySQL server user 'user_0d_1' with all privileges.

3. **[Read user](2-create_read_user.sql)**
   - Creates the database 'hbtn_0d_2' and the user 'user_0d_2' with SELECT privilege.

4. **[Always a name](3-force_name.sql)**
   - Creates the 'force_name' table with 'id' and 'name' fields.

5. **[ID can't be null](4-never_empty.sql)**
   - Creates the 'id_not_null' table with 'id' and 'name' fields, setting default value for 'id'.

6. **[Unique ID](5-unique_id.sql)**
   - Creates the 'unique_id' table with 'id' (unique) and 'name' fields.

7. **[States table](6-states.sql)**
   - Creates the 'hbtn_0d_usa' database and 'states' table with 'id' (unique, primary key) and 'name' fields.

8. **[Cities table](7-cities.sql)**
   - Creates the 'cities' table in 'hbtn_0d_usa' database with 'id', 'state_id' (foreign key), and 'name' fields.

9. **[Cities of California](8-cities_of_california_subquery.sql)**
   - Lists all cities in California from the 'hbtn_0d_usa' database.

10. **[Cities by States](9-cities_by_state_join.sql)**
    - Lists all cities with their respective states from 'hbtn_0d_usa' database.

11. **[Genre ID by show](10-genre_id_by_show.sql)**
    - Lists shows from 'hbtn_0d_tvshows' with at least one genre linked.

12. **[Genre ID for all shows](11-genre_id_all_shows.sql)**
    - Lists shows from 'hbtn_0d_tvshows' with respective genre IDs.

13. **[No genre](12-no_genre.sql)**
    - Lists shows from 'hbtn_0d_tvshows' without a linked genre.

14. **[Number of shows by genre](13-count_shows_by_genre.sql)**
    - Displays the number of shows linked to each genre from 'hbtn_0d_tvshows'.

15. **[My genres](14-my_genres.sql)**
    - Lists all genres of the show 'Dexter' from 'hbtn_0d_tvshows'.

16. **[Only Comedy](15-comedy_only.sql)**
    - Lists all Comedy shows in 'hbtn_0d_tvshows'.

17. **[List shows and genres](16-shows_by_genre.sql)**
    - Lists all shows and linked genres from 'hbtn_0d_tvshows'.

