class ParkingSpacesServices:
    def __init__(self, db_connection):
        self.db = db_connection
        self.cursor = self.db.cursor()

    def get_space(self, space_id):
        query = "SELECT * FROM parking_spaces WHERE space_id = ?"
        self.cursor.execute(query, (space_id,))
        return self.cursor.fetchone()

    def get_all_spaces(self):
        query = "SELECT * FROM parking_spaces"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_available_spaces(self):
        query = "SELECT * FROM parking_spaces WHERE status = ?"
        self.cursor.execute(query, ("available",))
        return self.cursor.fetchall()

    def recommend_space(self):
        query = "SELECT * FROM parking_spaces WHERE status = ? LIMIT 1"
        self.cursor.execute(query, ("available",))
        return self.cursor.fetchone()

    def update_space_status(self, space_id, new_status):
        query = "UPDATE parking_spaces SET status = ? WHERE space_id = ?"
        self.cursor.execute(query, (new_status, space_id))
        self.db.commit()  