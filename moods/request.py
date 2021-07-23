import sqlite3
import json
from models import Moods

def get_single_mood(id):
    """Getting single mood from SQL by mood id"""
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute(
            """
        SELECT
            m.id,
            m.label
        FROM moods m
        WHERE m.id = ?
        """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        mood = Moods(
            data["id"],
            data["label"],
        )

        return json.dumps(mood.__dict__)

def get_all_moods():
    """Joining moods with entries in SQL"""
    # Open a connection to the database, save it as conn
    with sqlite3.connect("./dailyjournal.db") as conn:

        # The type of rows returned when we fetch
        conn.row_factory = sqlite3.Row
        # What let's us execute queries
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            m.id,
            m.label
        FROM moods m
        """
        )

        # Initialize an empty list to hold all entrie representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entrie instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entrie class above.
            mood = Moods(
                row["id"],
                row["label"],
            )
            moods.append(mood.__dict__)
            # Use `json` package to properly serialize list as JSON
        return json.dumps(moods)

def delete_mood(id):
    """deleting from SQL database"""
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM moods
        WHERE id = ?
        """,
            (id,),
        )