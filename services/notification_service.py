class NotificationService:
    def send_welcome_notification(self, user):
        """Enviar notificación de bienvenida"""
        message = f"Bienvenido, {user['name']}! Tu cuenta ha sido creada exitosamente."
        return {
            "status": "sent",
            "message": message,
            "user_email": user.get('email')
        }

    def send_password_reset(self, user):
        """Enviar notificación de restablecimiento de contraseña"""
        message = f"Se ha solicitado un restablecimiento de contraseña para {user['name']}"
        return {
            "status": "sent",
            "message": message
        }