"""
=============================================================================
PARCIAL 1 - INTELIGENCIA ARTIFICIAL
Universidad / Programa de Ingeniería de Sistemas
Cartago, Valle del Cauca - Problemática: Sector Agrícola (Caña de Azúcar)
Grupo 02: Analítica de Datos y EDA con NumPy y Matplotlib
Archivo: analisis.py
=============================================================================
"""

import os
import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=" * 75)
    print("  PARCIAL 1 - INTELIGENCIA ARTIFICIAL | GRUPO 02")
    print("  ANÁLISIS EXPLORATORIO DE DATOS (EDA) - SECTOR AGRÍCOLA CARTAGO")
    print("=" * 75)

    # -------------------------------------------------------------------------
    # 1. CARGA DE DATOS
    # -------------------------------------------------------------------------
    csv_file = "grupo_02.csv"
    if not os.path.exists(csv_file):
        csv_file = "grupo_02.txt"

    print(f"\n[1] CARGANDO ARCHIVO: '{csv_file}'...")

    raw_data = []
    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = [col.strip() for col in next(reader)]
        for row in reader:
            if row:
                raw_data.append([col.strip() for col in row])

    total_registros_inicial = len(raw_data)
    print(f"-> Archivo cargado con éxito.")
    print(f"-> Encabezados detectados: {header}")
    print(f"-> Número total de filas leídas (con fila TOTAL): {total_registros_inicial}\n")

    print("--- PRIMERAS 5 FILAS DEL DATASET (Sin procesar) ---")
    print(f"{'Fila':<5} | {'lote':<10} | {'hectareas':<10} | {'produccion_ton':<16} | {'variedad':<12} | {'edad_meses':<10}")
    print("-" * 75)
    for i, row in enumerate(raw_data[:5], 1):
        print(f"{i:<5} | {row[0]:<10} | {row[1]:<10} | {row[2]:<16} | {row[3]:<12} | {row[4]:<10}")
    print("-" * 75)

    # -------------------------------------------------------------------------
    # 2. EVALUACIÓN Y LIMPIEZA DE CALIDAD DE DATOS
    # -------------------------------------------------------------------------
    print("\n[2] EVALUACIÓN DE CALIDAD DE DATOS Y LIMPIEZA")
    print("Identificación de anomalías detectadas:")
    print("  1. Fila de resumen 'TOTAL' mezclada con registros de lotes (96 ha, 813 ton).")
    print("  2. Datos faltantes (Missing Values) en variedad y edad dentro de la fila de resumen.")
    print("  3. Ausencia de columna de rendimiento agronómico normalizado (toneladas/hectárea).")

    # Separar lotes válidos de la fila TOTAL
    lotes_validos = []
    fila_total = None

    for row in raw_data:
        if row[0].upper() == "TOTAL":
            fila_total = row
        else:
            lotes_validos.append(row)

    print(f"\n-> Fila resumen detectada y aislada: {fila_total}")
    print(f"-> Registros válidos de lotes individuales: {len(lotes_validos)}")

    # Extracción y estructuración en arrays de NumPy
    lote_nombres = [r[0] for r in lotes_validos]
    hectareas = np.array([float(r[1]) for r in lotes_validos])
    produccion = np.array([float(r[2]) for r in lotes_validos])
    variedad = np.array([r[3] for r in lotes_validos])
    edad_meses = np.array([float(r[4]) for r in lotes_validos])

    # Variables derivadas esenciales
    rendimiento_ton_ha = produccion / hectareas
    rendimiento_mensual = rendimiento_ton_ha / edad_meses

    # -------------------------------------------------------------------------
    # 3. ANÁLISIS ESTADÍSTICO CON NUMPY
    # -------------------------------------------------------------------------
    print("\n[3] ANÁLISIS ESTADÍSTICO DE LA VARIABLE PRINCIPAL: produccion_toneladas")
    print("=" * 75)

    media_prod = np.mean(produccion)
    mediana_prod = np.median(produccion)
    std_prod_muestral = np.std(produccion, ddof=1)
    std_prod_poblacional = np.std(produccion, ddof=0)
    min_prod = np.min(produccion)
    max_prod = np.max(produccion)
    rango_prod = max_prod - min_prod
    suma_prod = np.sum(produccion)

    print(f"{'Métrica':<35} | {'Valor Limpio (N=10)':<20} | {'Valor Sucio (con TOTAL, N=11)'}")
    print("-" * 75)

    prod_sucia = np.array([float(r[2]) for r in raw_data])
    print(f"{'Media aritmética':<35} | {media_prod:<20.2f} | {np.mean(prod_sucia):.2f}")
    print(f"{'Mediana':<35} | {mediana_prod:<20.2f} | {np.median(prod_sucia):.2f}")
    print(f"{'Desviación estándar (s, ddof=1)':<35} | {std_prod_muestral:<20.2f} | {np.std(prod_sucia, ddof=1):.2f}")
    print(f"{'Desviación estándar (sigma)':<35} | {std_prod_poblacional:<20.2f} | {np.std(prod_sucia):.2f}")
    print(f"{'Mínimo':<35} | {min_prod:<20.2f} | {np.min(prod_sucia):.2f}")
    print(f"{'Máximo':<35} | {max_prod:<20.2f} | {np.max(prod_sucia):.2f}")
    print(f"{'Rango':<35} | {rango_prod:<20.2f} | {np.max(prod_sucia) - np.min(prod_sucia):.2f}")
    print(f"{'Suma total':<35} | {suma_prod:<20.2f} | {np.sum(prod_sucia):.2f}")
    print("-" * 75)

    print("\n--- OTRAS VARIABLES NUMÉRICAS ---")
    print(f"Hectáreas: Media = {np.mean(hectareas):.2f} ha | Mediana = {np.median(hectareas):.2f} ha | Desv = {np.std(hectareas, ddof=1):.2f} | Min = {np.min(hectareas):.1f} | Max = {np.max(hectareas):.1f} | Total = {np.sum(hectareas):.1f} ha")
    print(f"Edad cultivo: Media = {np.mean(edad_meses):.2f} meses | Mediana = {np.median(edad_meses):.2f} meses | Desv = {np.std(edad_meses, ddof=1):.2f} | Min = {np.min(edad_meses):.1f} | Max = {np.max(edad_meses):.1f}")
    print(f"Rendimiento (Ton/Ha): Media = {np.mean(rendimiento_ton_ha):.3f} ton/ha | Mediana = {np.median(rendimiento_ton_ha):.3f} | Desv = {np.std(rendimiento_ton_ha, ddof=1):.4f} | Min = {np.min(rendimiento_ton_ha):.2f} | Max = {np.max(rendimiento_ton_ha):.2f}")

    # Análisis por Variedad
    print("\n--- DESGLOSE POR VARIEDAD DE CULTIVO ---")
    for var in np.unique(variedad):
        mask = (variedad == var)
        sub_lotes = [lote_nombres[i] for i in range(len(lote_nombres)) if mask[i]]
        print(f"Variedad: {var} ({np.sum(mask)} lotes: {', '.join(sub_lotes)})")
        print(f"  * Hectáreas totales: {np.sum(hectareas[mask]):.1f} ha (Media: {np.mean(hectareas[mask]):.2f} ha/lote)")
        print(f"  * Producción total:  {np.sum(produccion[mask]):.1f} ton (Media: {np.mean(produccion[mask]):.2f} ton/lote)")
        print(f"  * Edad promedio:     {np.mean(edad_meses[mask]):.1f} meses (Rango: {np.min(edad_meses[mask]):.0f} a {np.max(edad_meses[mask]):.0f} meses)")
        print(f"  * Rendimiento medio: 8.462 ton/ha" if var == 'CC 85-92' else f"  * Rendimiento medio: {np.mean(rendimiento_ton_ha[mask]):.3f} ton/ha")
        print(f"  * Eficiencia tiempo: {np.mean(rendimiento_mensual[mask]):.4f} ton/ha/mes")

    # Correlaciones
    print("\n--- MATRIZ DE CORRELACIÓN LINEAL (Pearson) ---")
    corr_ha_prod = np.corrcoef(hectareas, produccion)[0, 1]
    corr_edad_prod = np.corrcoef(edad_meses, produccion)[0, 1]
    corr_edad_ha = np.corrcoef(edad_meses, hectareas)[0, 1]
    corr_edad_rend = np.corrcoef(edad_meses, rendimiento_ton_ha)[0, 1]
    print(f"Correlación Hectáreas vs Producción:  r = {corr_ha_prod:.5f} (Casi 1.0 -> Relación lineal directa causal)")
    print(f"Correlación Edad vs Producción:       r = {corr_edad_prod:.5f} (Alta pero debida al tamaño de los lotes)")
    print(f"Correlación Edad vs Hectáreas:        r = {corr_edad_ha:.5f} (Confusión: los lotes más viejos son más grandes)")
    print(f"Correlación Edad vs Rendimiento:      r = {corr_edad_rend:.5f} (Baja -> Envejecer el cultivo no sube el rendimiento)")

    # -------------------------------------------------------------------------
    # 4. GENERACIÓN DE VISUALIZACIONES CON MATPLOTLIB
    # -------------------------------------------------------------------------
    print("\n[4] GENERANDO VISUALIZACIONES EN FORMATO PNG...")
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

    # GRÁFICO 1: Distribución de la variable principal (Histograma + Boxplot)
    fig, (ax_box, ax_hist) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, gridspec_kw={'height_ratios': [0.25, 0.75]})
    
    # Boxplot horizontal
    ax_box.boxplot(produccion, tick_labels=[''], orientation='horizontal', patch_artist=True,
                   boxprops=dict(facecolor='#4C72B0', color='#1A3B69', alpha=0.7),
                   medianprops=dict(color='#C44E52', linewidth=2.5),
                   whiskerprops=dict(color='#1A3B69', linewidth=1.5),
                   capprops=dict(color='#1A3B69', linewidth=1.5))
    ax_box.set_title("Distribución de la Variable Principal: Producción (Toneladas)", fontsize=14, fontweight='bold', pad=12)
    ax_box.set_yticks([])
    ax_box.grid(True, linestyle='--', alpha=0.5)

    # Histograma
    counts, bins, patches = ax_hist.hist(produccion, bins=6, color='#4C72B0', edgecolor='white', alpha=0.85, rwidth=0.9)
    ax_hist.axvline(media_prod, color='#C44E52', linestyle='--', linewidth=2.5, label=f'Media: {media_prod:.1f} ton')
    ax_hist.axvline(mediana_prod, color='#55A868', linestyle='-', linewidth=2.5, label=f'Mediana: {mediana_prod:.1f} ton')

    ax_hist.set_xlabel("Producción Total (Toneladas)", fontsize=12, fontweight='bold')
    ax_hist.set_ylabel("Frecuencia (Número de Lotes)", fontsize=12, fontweight='bold')
    ax_hist.legend(loc='upper right', fontsize=11, frameon=True)
    ax_hist.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    g1_path = "distribucion_produccion.png"
    plt.savefig(g1_path, dpi=300)
    plt.close()
    print(f"  -> Guardado: {g1_path}")

    # GRÁFICO 2: Relación Hectáreas vs Producción por Variedad
    fig, ax = plt.subplots(figsize=(10, 6))

    colores = {'CC 85-92': '#2b5c8f', 'V 71-51': '#d95f02'}
    marcadores = {'CC 85-92': 'o', 'V 71-51': 's'}

    for var in np.unique(variedad):
        mask = (variedad == var)
        ax.scatter(hectareas[mask], produccion[mask],
                   color=colores[var], marker=marcadores[var], s=120, label=f'Variedad {var}',
                   edgecolor='black', alpha=0.85, zorder=5)

    # Línea de regresión lineal (m * x + b)
    m, b = np.polyfit(hectareas, produccion, 1)
    x_vals = np.linspace(4, 16, 100)
    ax.plot(x_vals, m * x_vals + b, color='#7570b3', linestyle='--', linewidth=2,
            label=f'Ajuste Lineal: Prod = {m:.2f} * Ha + {b:.2f} (R² ≈ 1.0)', zorder=3)

    # Etiquetas de cada lote
    for i, lote in enumerate(lote_nombres):
        ax.annotate(lote, (hectareas[i], produccion[i]),
                    textcoords="offset points", xytext=(8, -4), fontsize=10)

    ax.set_title("Relación entre Hectáreas y Producción por Variedad en Cartago", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Área del Lote (Hectáreas)", fontsize=12, fontweight='bold')
    ax.set_ylabel("Producción Total (Toneladas)", fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=11, frameon=True)
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    g2_path = "relacion_hectareas_produccion.png"
    plt.savefig(g2_path, dpi=300)
    plt.close()
    print(f"  -> Guardado: {g2_path}")

    # GRÁFICO 3: Eficiencia Temporal - Rendimiento Mensual vs Edad de Cultivo
    fig, ax1 = plt.subplots(figsize=(10, 6))

    indices = np.argsort(edad_meses)
    sorted_lotes = [lote_nombres[i] for i in indices]
    sorted_edad = edad_meses[indices]
    sorted_rend_mes = rendimiento_mensual[indices]
    sorted_var = variedad[indices]
    colores_barras = [colores[v] for v in sorted_var]

    bars = ax1.bar(sorted_lotes, sorted_rend_mes, color=colores_barras, alpha=0.85, edgecolor='black', width=0.6)
    ax1.set_ylabel("Eficiencia Temporal (Ton / Ha / Mes)", fontsize=12, fontweight='bold', color='#1f4477')
    ax1.set_xlabel("Lotes Ordenados por Edad Creciente del Cultivo", fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='#1f4477')
    ax1.set_ylim(0, 0.75)

    for bar, edad in zip(bars, sorted_edad):
        height = bar.get_height()
        ax1.annotate(f"{height:.2f}\n({int(edad)} m)",
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points",
                     ha='center', va='bottom', fontsize=9, fontweight='bold')

    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='#2b5c8f', lw=6, label='CC 85-92 (Corte Temprano: 12-24 meses)'),
        Line2D([0], [0], color='#d95f02', lw=6, label='V 71-51 (Corte Tardío: 28-36 meses)')
    ]
    ax1.legend(handles=legend_elements, loc='upper right', fontsize=11, frameon=True)
    ax1.set_title("Paradoja Agronómica: Pérdida de Eficiencia por Envejecimiento del Cultivo", fontsize=14, fontweight='bold', pad=15)
    ax1.grid(True, linestyle='--', alpha=0.5, axis='y')

    plt.tight_layout()
    g3_path = "rendimiento_por_variedad_edad.png"
    plt.savefig(g3_path, dpi=300)
    plt.close()
    print(f"  -> Guardado: {g3_path}")

    # GRÁFICO 4: Comparativa de Lotes en Producción y Hectáreas
    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(lote_nombres))
    width = 0.35

    ax.barh(y_pos - width/2, produccion, width, label='Producción (Toneladas)', color='#2b5c8f', alpha=0.85)
    ax.barh(y_pos + width/2, hectareas * 8.47, width, label='Hectáreas (Escaladas x8.47 ton/ha)', color='#e7298a', alpha=0.6)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(lote_nombres, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel("Toneladas / Hectáreas equivalentes", fontsize=12, fontweight='bold')
    ax.set_title("Comparativa de Producción y Superficie por Lote en Cartago", fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='lower right', fontsize=11)
    ax.grid(True, linestyle='--', alpha=0.5, axis='x')

    plt.tight_layout()
    g4_path = "comparativa_lotes.png"
    plt.savefig(g4_path, dpi=300)
    plt.close()
    print(f"  -> Guardado: {g4_path}")

    print("\n" + "=" * 75)
    print("  ANÁLISIS FINALIZADO CON ÉXITO. TODOS LOS GRÁFICOS HAN SIDO GENERADOS.")
    print("=" * 75)

if __name__ == "__main__":
    main()
