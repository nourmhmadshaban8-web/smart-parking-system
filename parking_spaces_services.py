import sqlite3

class ParkingSpacesService:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    
    def get_space(self, space_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM parking_spaces WHERE space_id = ?", (space_id,))
        space = cursor.fetchone()
        conn.close()
        return space

    def get_all_spaces(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM parking_spaces")
        spaces = cursor.fetchall()
        conn.close()
        return spaces

    def get_available_spaces(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM parking_spaces WHERE status = 'available'")
        spaces = cursor.fetchall()
        conn.close()
        return spaces

    def recommend_space(self):
        available_spaces = self.get_available_spaces()
        if available_spaces:
            return available_spaces[0] 
        return "Sorry, no parking spaces available right now."

    def update_space_status(self, space_id, new_status):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE parking_spaces SET status = ? WHERE space_id = ?", (new_status, space_id))
        conn.commit()
        conn.close()
        return f"Space {space_id} status updated to {new_status}"