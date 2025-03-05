class UserService:
    def __init__(self):
        self._users = {
            1: {"id": 1, "name": "Juan Pérez", "email": "juan@example.com"},
            2: {"id": 2, "name": "María García", "email": "maria@example.com"}
        }

    def get_user(self, user_id):
        """Obtener usuario por ID"""
        return self._users.get(user_id)

    def create_user(self, user_data):
        """Crear nuevo usuario"""
        user_id = max(self._users.keys()) + 1
        user_data['id'] = user_id
        self._users[user_id] = user_data
        return user_data