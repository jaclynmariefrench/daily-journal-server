import sqlite3
import json
from models import Entries
from models import Moods

def get_all_entries():
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
            e.id,
            e.time,
            e.concept,
            e.entry,
            e.mood_id,
            m.id mood_id
        FROM journal_entries e
        JOIN moods m ON m.id = e.mood_id
        """
        )

        # Initialize an empty list to hold all entrie representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entrie instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entrie class above.
            entry = Entries(
                row["id"],
                row["time"],
                row["concept"],
                row["entry"],
                row["mood_id"],
            )

            # Create a Location instance from the current row
            mood = Moods(
                row["mood_id"], row["mood_label"]
            )

            # Add the dictionary representation of the location to the entrie
            entry.mood = mood.__dict__

            # Create a Location instance from the current row

            # Converting an object into a dictionary
            entries.append(entry.__dict__)

            # Use `json` package to properly serialize list as JSON
        return json.dumps(entries)