# 📊 Avance 4 — Evaluación completa
**Fecha:** 12/06/2026

## Esencial para el docente
- `avance_4.md` — reporte completo + análisis
- 📓 **Notebook con evaluación:** [`../../notebook.ipynb`](../../notebook.ipynb) (sección 5)
- 📊 **Figuras:** [`../../reports/figures/`](../../reports/figures/)
  - `02_matriz_confusion.png` — matriz 9×9
  - `03_curva_roc.png` — ROC One-vs-Rest
  - `06_accuracy_por_clase.png` — performance por clase
  - `07_vs_baseline.png` — comparación con random
  - `09_analisis_errores.png` — heatmap de confusiones
  - `08_heatmap_probabilidades.png` — 12 ejemplos
  - `10_predicciones_ejemplos.png` — 1 por clase

## Métricas finales
- Accuracy: ~50% · F1 macro: ~0,46 · AUC promedio: > 0,75
- Mejor clase: Food Organics
- Más difíciles: Vegetation, Paper, Cardboard

## Análisis de errores
- Cardboard ↔ Paper (similares visualmente)
- Glass ↔ Misc Trash (vidrios pequeños ambiguos)
- Vegetation ↔ Misc Trash (orgánicos secos)
