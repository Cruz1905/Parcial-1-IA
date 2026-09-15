# Parcial 1 - Inteligencia Artificial: Análisis de Datos Agrícolas en Cartago

**Asignatura:** Inteligencia Artificial  
**Docente:** Jhon James Cano Sánchez  
**Grupo Asignado:** Grupo 02  
**Repositorio:** [`Parcial-1-IA`](https://github.com/Cruz1905/Parcial-1-IA)  
**Ubicación de Estudio:** Cartago, Valle del Cauca, Colombia  
**Sector:** Agricultura (Cultivo de Caña de Azúcar)  

---

## 1. Configuración del Entorno y Reproducibilidad

El proyecto se encuentra configurado para ejecutarse en contenedores Docker o en entornos locales/WSL con Python 3.12.

### Requisitos Previos
- Docker Desktop / WSL
- Python 3.12
- Git

### Ejecución con Docker
```bash
docker compose up --build
```

### Ejecución en Entorno Local / WSL
```bash
python -m venv .venv
# En Linux/WSL:
source .venv/bin/activate
# En Windows:
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## 2. Dataset Asignado (Grupo 02)
El archivo `grupo_02.csv` contiene los registros de 10 lotes agrícolas en Cartago (Valle del Cauca), con variables de superficie (hectáreas), producción en toneladas, variedad de caña y edad del cultivo en meses.

---

## 3. Carga y Calidad de Datos

Se implementó el script `analisis.py` para cargar el archivo `grupo_02.csv` y realizar la auditoría de calidad de datos.

### Problemas detectados:
1. **Fila de resumen `TOTAL`**: Mezclada en la tabla transaccional (96 ha, 813 ton). Se procede a aislar y filtrar esta fila para no distorsionar las métricas estadísticas.
2. **Datos faltantes**: La fila TOTAL posee campos nulos en variedad y edad (`,,`).
3. **Ausencia de variables normalizadas**: Se calcularon mediante NumPy el rendimiento unitario (`ton/ha`) y la eficiencia temporal (`ton/ha/mes`).

---

## 4. Análisis Estadístico con NumPy (Variable Principal: produccion_toneladas)
- **Media:** 81.30 ton
- **Mediana:** 80.50 ton
- **Desviación Estándar (s):** 27.19 ton
- **Mínimo:** 42.00 ton
- **Máximo:** 127.00 ton
- **Rango:** 85.00 ton
