from views.utils import leer_numero


class MainView:

    @staticmethod
    def mostrar_menu(usuario) -> int:
        print("\n" + "=" * 40)
        print("      CLÍNICA - MENÚ PRINCIPAL")
        print("=" * 40)
        print(f"Usuario: {usuario.username} | Rol: {usuario.rol}")
        print("=" * 40)
        print("1.- Gestión de Pacientes")
        print("2.- Gestión de Departamentos")
        print("3.- Gestión de Farmacia")
        print("4.- Administración de Usuarios")
        print("9.- Cerrar Sesión")
        print("0.- Salir")
        print("=" * 40)

        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[SISTEMA] {mensaje}")
