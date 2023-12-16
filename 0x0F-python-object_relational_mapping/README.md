# 0x0F. Python - Object-relational mapping

## Task 0: [Get all states](0-select_states.py)

### Requirements:
- List all states from the `hbtn_0e_0_usa` database.
- Use MySQLdb module.
- Connect to MySQL server running on localhost at port 3306.
- Sort results in ascending order by `states.id`.

## Task 1: [Filter states](1-filter_states.py)

### Requirements:
- List states starting with 'N' (uppercase) from the `hbtn_0e_0_usa` database.
- Use MySQLdb module.
- Connect to MySQL server running on localhost at port 3306.
- Sort results in ascending order by `states.id`.

## Task 2: [Filter states by user input](2-my_filter_states.py)

### Requirements:
- Display states matching a user-provided name from the `states` table in the `hbtn_0e_0_usa` database.
- Use MySQLdb module.
- Connect to MySQL server running on localhost at port 3306.
- Sort results in ascending order by `states.id`.

## Task 3: [SQL Injection](3-my_safe_filter_states.py)

### Requirements:
- Retrieve states safely by avoiding SQL injection vulnerabilities from user input.
- Use MySQLdb module.
- Connect to MySQL server running on localhost at port 3306.
- Sort results in ascending order by `states.id`.

## Task 4: [Cities by states](4-cities_by_state.py)

### Requirements:
- List all cities from the `hbtn_0e_4_usa` database.
- Use MySQLdb module.
- Connect to MySQL server running on localhost at port 3306.
- Sort results in ascending order by `cities.id`.

## Task 5: [All cities by state](5-filter_cities.py)

### Requirements:
- List all cities of a specified state from the `hbtn_0e_4_usa` database.
- Use MySQLdb module.
- Connect to MySQL server running on localhost at port 3306.
- Sort results in ascending order by `cities.id`.

## Task 6: [First state model](model_state.py)

### Requirements:
- Define a State class inheriting from declarative_base() for the `hbtn_0e_6_usa` database.
- Represent columns for `id` and `name`.
- Use SQLAlchemy module.
- Connect to MySQL server running on localhost at port 3306.

## Task 7: [All states via SQLAlchemy](7-model_state_fetch_all.py)

### Requirements:
- Retrieve all State objects from the `hbtn_0e_6_usa` database using SQLAlchemy.
- Sort results in ascending order by `states.id`.

## Task 8: [First state](8-model_state_fetch_first.py)

### Requirements:
- Retrieve and print the first State object from the `hbtn_0e_6_usa` database using SQLAlchemy.
- Display results as specified or 'Nothing' if the table is empty.

## Task 9: [Contains `a`](9-model_state_filter_a.py)

### Requirements:
- Retrieve all State objects containing the letter 'a' from the `hbtn_0e_6_usa` database using SQLAlchemy.
- Sort results in ascending order by `states.id`.

## Task 10: [Get a state](10-model_state_my_get.py)

### Requirements:
- Retrieve and print the State object by name from the `hbtn_0e_6_usa` database using SQLAlchemy.
- Display the states.id or 'Not found' if no state matches.

## Task 11: [Add a new state](11-model_state_insert.py)

### Requirements:
- Add the State object "Louisiana" to the `hbtn_0e_6_usa` database using SQLAlchemy.
- Print the newly added states.id after creation.

## Task 12: [Update a state](12-model_state_update_id_2.py)

### Requirements:
- Change the name of a State object from the `hbtn_0e_6_usa` database using SQLAlchemy.
- Update the State where id = 2 to "New Mexico".

## Task 13: [Delete states](13-model_state_delete_a.py)

### Requirements:
- Delete all State objects containing the letter 'a' from the `hbtn_0e_6_usa` database using SQLAlchemy.

## Task 14: [Cities in state](model_city.py, 14-model_city_fetch_by_state.py)

### Requirements:
- Define a City class linked to the `hbtn_0e_14_usa` database.
- Represent columns for `id`, `name`, and `state_id`.
- Retrieve and print all City objects from the database using SQLAlchemy.
