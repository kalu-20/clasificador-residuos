# 🤖 Avance 2 — Núcleo técnico funcionando
**Fecha:** 08/05/2026

## Esencial para el docente
- `avance_2.md` — resumen + decisiones técnicas
- 📓 **Notebook principal:** [`../../notebook.ipynb`](../../notebook.ipynb) — pipeline completo
- 🤖 **Modelo entrenado:** [`../../models/best_model_waste.pt`](../../models/best_model_waste.pt)

## Resultados
- Accuracy: ~50% · F1 macro: ~0,46
- × 4+ mejor que random (1/9 = 11,1%)
- 9 clases · 480 imágenes (~80/20 split)

## Estrategia de entrenamiento
1. **Frozen** — features de MobileNetV2 congeladas (LR=1e-3)
2. **Fine-tuning** — últimas 30 capas descongeladas (LR=1e-4)
3. **WeightedRandomSampler** para balancear clases
