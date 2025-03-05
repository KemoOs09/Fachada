class AuthenticationService:
    def __init__(self):
        self._valid_credentials = {
            "admin": "secret123",
            "user": "pass456"
        }

    def authenticate(self, username, password):
        """Validar credenciales"""
        return self._valid_credentials.get(username) == password

    def generate_token(self, username):
        """Generar token de autenticación (simulado)"""
        return f"token_{username}_123456"