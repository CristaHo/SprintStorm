from src.db.user import get_user_id_by_username, delete_user

class UserLibrary:
    def delete_user_by_username(self, username):
        user_id = get_user_id_by_username(username)
        if user_id:
            delete_user(user_id)
