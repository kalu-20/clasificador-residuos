# Ficha de Inicio — Avance 1

**TIF · Modelado de Sistemas de IA Aplicada · UPATecO Salta · 2026**
**Formador:** Lic. Walter Gabriel Ramirez

---

## Bloque 1 · Identificación

| Campo | Valor |
|---|---|
| **Nombre** | Clasificación de Residuos para Reciclaje — Sistema de IA Aplicada |
| **Integrantes** | María Claudia Fabián · _Integrante 2_ · _Integrante 3_ |
| **Ciclo técnico** | Ciclo 3 — Visión por computadora |
| **Fecha de inicio** | 10/04/2026 |
| **Avance 1** | 24/04/2026 |

## Bloque 2 · Problema

### Contexto

La gestión inadecuada de residuos es un problema ambiental crítico. La separación correcta requiere educación o sistemas automatizados. Una **planta de recuperación** o un **contenedor inteligente** puede beneficiarse mucho de un sistema que identifique automáticamente el tipo de residuo.

### Pregunta

> **Dada una foto de un residuo, ¿podemos predecir automáticamente a cuál de 9 categorías pertenece (Cardboard, Food Organics, Glass, Metal, Misc Trash, Paper, Plastic, Textile Trash, Vegetation)?**

### Tipo de IA

- **Tarea:** Clasificación de imágenes multiclase (9 clases).
- **Métrica principal:** F1 macro (queremos balance entre clases).
- **Métricas secundarias:** Accuracy, ROC-AUC por clase, matriz de confusión.

### ¿Por qué IA?

- **Escalabilidad:** procesa miles de items por minuto.
- **Disponibilidad:** funciona 24/7 sin operador.
- **Consistencia:** no se cansa ni se distrae.
- **Trazabilidad:** cada predicción se puede explicar.

## Bloque 3 · Solución propuesta

### Sistema completo

App local en Streamlit donde:
1. Usuario sube foto del residuo.
2. La app procesa y devuelve la **predicción** + probabilidades por categoría.
3. Muestra recomendación: "Este residuo pertenece al contenedor X" o consejo de reciclaje.

### Stack tecnológico

| Capa | Tecnología | Por qué |
|---|---|---|
| Modelo | MobileNetV2 + Transfer Learning | Liviano, corre en CPU, suficiente accuracy |
| Framework | PyTorch + torchvision | Estándar industria |
| App | Streamlit | El más simple |
| Lenguaje | Python 3.10+ | Estándar |

## Bloque 4 · Arquitectura

```
[Foto residuo] → resize 64×64 → normalización ImageNet
              → MobileNetV2 features (frozen)
              → classifier custom (Dropout + 64-FC + ReLU + 9-FC)
              → softmax → predicción + probabilidades
```

## Bloque 5 · Comentarios sobre los pasos del ciclo

### a) Datos
- 570 imágenes (435 train + 135 test) de RealWaste (UCI/HuggingFace).
- 9 clases bien definidas, balanceadas en test.

### b) Preprocesamiento
- Resize 64×64.
- Normalización con stats ImageNet.
- Data augmentation: HorizontalFlip, RandomRotation, ColorJitter.

### c) Modelado
- MobileNetV2 (2.4M params, 82k entrenables).
- Optimizer: Adam, LR=1e-3 (frozen) y 1e-4 (fine-tuning).

### d) Evaluación
- Métricas globales y por clase.
- Matriz de confusión 9×9.
- ROC-AUC por clase.

### e) Despliegue
- App Streamlit local con upload, predicción y caveat.

## Bloque 6 · Dataset

| Campo | Valor |
|---|---|
| **Nombre** | RealWaste |
| **Fuente** | UCI ML Repository (ID 908) |
| **Mirror** | shahzaibvohra/realwaste (HuggingFace) |
| **Tamaño total** | 4.752 imágenes |
| **Subset usado** | 570 imágenes (>200 mín. TIF) |
| **Clases** | 9 |
| **Licencia** | CC BY 4.0 |

## Bloque 7 · Repositorio y tablero

- Estructura ya creada (ver `README.md`).
- Tablero: ver `tablero_gestion.md`.
