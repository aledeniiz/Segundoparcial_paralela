#  Sistema Distribuido de Noticias - Inter vs Barça

Este proyecto simula un sistema distribuido asincrónico para recolectar noticias sobre el partido **Inter vs Barça** usando nodos de adquisición y un servidor central.

---

##  Estructura del Proyecto

```
simplified_news_system/
├── central_server.py       # Servidor HTTP que recibe artículos
├── acquisition_node.py     # Nodo que envía artículos simulados
└── README.md               # Instrucciones y explicación
```

##  Cómo Ejecutar

### 1. Inicia el servidor central

```bash
python central_server.py
```

Verás:

```
Server running on http://localhost:8000
```

El servidor queda escuchando en:
[http://localhost:8000/articles](http://localhost:8000/articles)

---

### 2. En otra terminal, lanza el nodo de adquisición

```bash
python acquisition_node.py
```

Esto enviará automáticamente 3 noticias simuladas al servidor.

---

### 3. Ver noticias en tu navegador

Abre:
```
http://localhost:8000/articles
```

Verás un JSON con las noticias recibidas.

---

##  ¿Cómo Funciona?

### `central_server.py`
- Usa `http.server` (estándar de Python) para crear un servidor que:
  - Recibe artículos en `/submit_article` (método POST).
  - Devuelve todos los artículos en `/articles` (método GET).
- Almacena las noticias en memoria (`articles_db`).

### `acquisition_node.py`
- Usa `aiohttp` para enviar peticiones POST al servidor.
- Genera 3 artículos simulados con título, fecha y contenido.
- Los envía uno por uno al servidor.

---

##  Simulación de Nodos Distribuidos

Puedes lanzar múltiples veces `acquisition_node.py` (en terminales separadas) para simular varios nodos de diferentes ubicaciones (Madrid, Londres, São Paulo, etc.).

---

##  Mejores Futuras
- Obtener noticias reales desde sitios deportivos.
- Añadir base de datos real (SQLite o MongoDB).
- Crear interfaz web para ver noticias.

---

##  Autor
Alejandro Déniz Solana 
