# AA_Project_Numberlink

Este proyecto implementa un solucionador para el rompecabezas lógico **Numberlink**, un problema NP-completo. Utiliza el algoritmo de **Fuerza bruta** optimizado con una **heurística** basada en el razonamiento humano.

-----

### Uso

Asegúrate de tener **Python 3.x** instalado.

#### 1\. Formato de Entrada

El programa requiere un archivo de texto (`.txt`).

  * **Línea 1:** Dimensiones (`Filas Columnas`).
  * **Resto:** La cuadrícula, donde el **espacio (` `)** es una celda vacía.

#### 2\. Ejecución

Ejecuta el script principal (`numberlinkPlayer.py`) pasando el archivo del tablero como argumento:

```bash
python numberlinkPlayer.py <ruta/a/archivo_tablero.txt>
```

**Ejemplo:**

```bash
python numberlinkPlayer.py tests/test_01.txt
```

-----

### 📌 Salida

| Resultado | Mensaje | Descripción |
| :--- | :--- | :--- |
| **Éxito** | `Solution found:` | Tablero resuelto, todos los pares conectados y la **cuadrícula está completamente llena**. |
| **Fallo** | `There is not solution for this board.` | No se pudo encontrar una solución válida dentro de las restricciones. |
