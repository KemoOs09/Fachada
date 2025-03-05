import json
from facades.user_management import UserManagementFacade

def main():
    api = UserManagementFacade()

    
    print("Registrando usuario:")
    registro = api.register_user("admin", "secret123", {
        "name": "Carlos Rodríguez", 
        "email": "carlos@example.com"
    })
    print(json.dumps(registro, indent=2))

   
    print("\nObteniendo perfil de usuario:")
    perfil = api.get_user_profile(1)
    print(json.dumps(perfil, indent=2))

if __name__ == "__main__":
    main()