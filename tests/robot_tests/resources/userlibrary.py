from src.app import app
with app.app_context():
            from src.utils.database import reset_database
            reset_database()

"""
class UserLibrary:
    def delete_user_by_username(self, username):
        user_id = get_user_id_by_username(username)
        if user_id:
            delete_user(user_id)
"""
