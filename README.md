# Parcial 3 – Lenguajes de Programación

Implementación de dos lenguajes usando ANTLR y Python:

- **Punto 1**: Lenguaje SQL-like con operaciones CRUD (CREATE, SELECT, UPDATE, DELETE) y validación semántica mediante gramática de atributos.
- **Punto 2 y Punto 3**: Lenguaje para declaración y multiplicación de matrices con validación de dimensiones (A(m×n) × B(n×p)).

---

## Estructura

```bash
Parcial3/
├── Punto1/
│ ├── CrudLang.g4 → Gramática ANTLR (SQL-like)
│ ├── sql_visitor.py → Visitor con validación semántica (tablas, columnas)
│ ├── main.py → Ejecutable. Contiene generar_gramatica_atributos()
│ └── ejemplo.sql → Ejemplo de programa
│
└── Punto2_y_Punto3/
├── Matrices.g4 → Gramática ANTLR (matrices)
├── visitor.py → Visitor con validación de dimensiones
├── main.py → Ejecutable. Contiene generar_gramatica_atributos()
└── test.m → Ejemplo de programa
```


## Ejecución

### Requisitos
- Python 3.8+
- ANTLR4 instalado
- Entorno virtual (recomendado)

### Punto 1 (SQL)
```bash
cd Punto1
python3 -m venv venv
source venv/bin/activate
pip install antlr4-python3-runtime
antlr4 -Dlanguage=Python3 -visitor CrudLang.g4
python3 main.py ejemplo.sql
```

### Punto 2 y Punto 3 (Matrices)

```bash
cd Punto2
python3 -m venv venv
source venv/bin/activate
pip install antlr4-python3-runtime
antlr4 -Dlanguage=Python3 -visitor Matrices.g4
python3 main.py test.m
```

## Salidas esperadas
### Punto 1
```bash
 CREATE TABLE users → ['id', 'name']
 SELECT ['id', 'name'] FROM users
 UPDATE users
 DELETE FROM users
 ¡Gramática de atributos generada y aplicada correctamente!
```

### Punto 2 y Punto 3
```bash
2x3 × 3x2 = 2x2
¡Listo!
```
## 7. Autor

Paula Alejandra Ortiz Salon



