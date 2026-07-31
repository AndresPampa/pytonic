# Python Expert

Repositorio de práctica para reforzar las bases de Python. El contenido se va actualizando a medida que avanza el curso.

## Objetivo

Repasar y consolidar fundamentos de Python con ejemplos cortos y ejercicios prácticos, sin depender solo de la memoria de proyectos anteriores.

## Requisitos

- Python **3.12+**
- [uv](https://docs.astral.sh/uv/) (gestor de entorno y dependencias del proyecto)

## Cómo empezar

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd "python expert"

# Crear/sincronizar el entorno virtual
uv sync

# Activar el entorno (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Ejecutar el script principal
uv run main.py
```

Para correr cualquier práctica:

```bash
uv run practica_datetime.py
uv run practica_timestamp.py
uv run poo/car-sample.py
```

## Estructura del proyecto

```
python expert/
├── main.py                 # Punto de entrada básico
├── practica_datetime.py    # Fechas y horas (datetime, locale)
├── practica_timestamp.py   # Timestamps (time / datetime)
├── poo/
│   └── car-sample.py       # Clases, constructor y atributos
├── pyproject.toml          # Configuración del proyecto
└── README.md
```

## Temas cubiertos

| Tema | Estado | Archivos |
|------|--------|----------|
| Fechas y horas (`datetime`) | En curso | `practica_datetime.py` |
| Timestamps | En curso | `practica_timestamp.py` |
| POO — clases y `__init__` | En curso | `poo/car-sample.py` |

> Esta tabla se irá ampliando con nuevos temas del curso (estructuras de datos, funciones, excepciones, módulos, etc.).

## Convenciones

- Cada práctica suele ser un script independiente y fácil de ejecutar.
- Los temas más grandes pueden agruparse en carpetas (por ejemplo `poo/`).
- Se prioriza código claro y comentado para el aprendizaje, no para producción.

## Notas

Proyecto gestionado con **uv**. La versión de Python está fijada en `.python-version` (3.12).
