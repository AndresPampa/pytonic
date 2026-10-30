# El patrón Singleton garantiza que una clase tenga una sola instancia y ofrece
# un punto de acceso compartido a ella. Esto permite que distintas partes de un
# programa utilicen el mismo estado o recurso sin crear copias independientes.
#
# Algunos usos habituales son compartir una conexión a una base de datos, la
# configuración global de una aplicación, un sistema de registro (logger) o una
# caché. Conviene usarlo con moderación, ya que el estado global compartido puede
# dificultar las pruebas y aumentar el acoplamiento entre componentes.

class ConexionBD:
    """Conexión a una base de datos simulada con una única instancia."""

    _instancia = None

    #maneja la creacion de la instancia única
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        # Evita la re-inicialización de la instancia única
        if getattr(self, "_inicializada", False):
            return

        self.conectada = False
        self._inicializada = True

    def conectar(self):
        if not self.conectada:
            self.conectada = True
            print("Conexión simulada establecida.")

    def consultar(self, consulta: str) -> str:
        if not self.conectada:
            raise RuntimeError("Primero debes establecer la conexión.")
        return f"Resultado simulado para: {consulta}"


if __name__ == "__main__":
    conexion1 = ConexionBD()
    conexion2 = ConexionBD()

    conexion1.conectar()
    print(conexion2.consultar("SELECT * FROM usuarios"))
    print(f"¿Es la misma instancia? {conexion1 is conexion2}")