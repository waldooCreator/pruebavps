# Calculadora básica (interfaz gráfica)

Pequeña calculadora escrita en Python usando `tkinter`.

Requisitos:
- Python 3 (incluye `tkinter` en la mayoría de distribuciones).

Ejecutar:

```bash
python3 calculator.py
```

Controles:
- Botones numéricos y de operaciones (+, -, *, /).
- `.` para decimal, `=` para evaluar.
- `C` limpia la pantalla, `⌫` borra el último carácter.
- También puedes usar el teclado: números, operadores, `Enter` para evaluar, `Backspace` y `Esc`.

Versión web (Django)

También hay una versión web incluida. Para usarla en un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:2000
```

Abre `http://127.0.0.1:2000/` en tu navegador.
