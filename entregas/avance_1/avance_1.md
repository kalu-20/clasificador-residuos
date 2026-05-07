# Avance 1 — Problema, solución y plan

**Fecha:** 24/04/2026 · **Estado:** ✅ Completo

## Resumen

Definimos el problema (clasificación automática de residuos), elegimos Ciclo 3 (Visión por computadora), identificamos el dataset (RealWaste UCI, 4.752 imágenes en 9 clases) y armamos el plan.

## Checklist
- [x] Ficha de inicio (7 bloques) → [`docs/01_ficha_inicio.md`](../docs/01_ficha_inicio.md)
- [x] Problema y solución definidos
- [x] Arquitectura → [`docs/02_arquitectura.md`](../docs/02_arquitectura.md)
- [x] Comentarios sobre los pasos del ciclo
- [x] Dataset identificado (570 imgs > 200 min)
- [x] Repositorio creado
- [x] Tablero activo

## Información clave

- **Problema:** clasificación multiclase 9-way de imágenes de residuos.
- **Métrica:** F1 macro.
- **Stack:** PyTorch + MobileNetV2 + Streamlit.
