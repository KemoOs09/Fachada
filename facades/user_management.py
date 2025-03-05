from services.user_service import UserService
from services.auth_service import AuthenticationService
from services.notification_service import NotificationService

class UserManagementFacade:
    def __init__(self):
        self.user_service = UserService()
        self.auth_service = AuthenticationService()
        self.notification_service = NotificationService()

    def register_user(self, username, password, user_data):
        """
        Método unificado para registro de usuario
        Combina múltiples operaciones de subsistemas
        """
     
        if not self.auth_service.authenticate(username, password):
            return {"error": "Credenciales inválidas", "status": "failed"}

       
        user = self.user_service.create_user(user_data)

        
        token = self.auth_service.generate_token(username)

        
        notification = self.notification_service.send_welcome_notification(user)

        return {
            "user": user,
            "token": token,
            "notification": notification,
            "status": "success"
        }

    def get_user_profile(self, user_id):
        """
        Método para obtener perfil de usuario
        """
        user = self.user_service.get_user(user_id)
        if not user:
            return {"error": "Usuario no encontrado", "status": "failed"}
        
        return {
            "user": user,
            "status": "success"
        }