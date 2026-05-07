# Arquitectura del Sistema

## Pipeline general

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  Imagen residuo  │ →  │  Preprocesamiento │ →  │  MobileNetV2     │
│  (foto del user) │    │  resize 64×64     │    │  (Transfer Learn)│
└──────────────────┘    └──────────────────┘    └──────────────────┘
                                                          │
                                                          ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  App Streamlit   │ ←  │  9 probabilidades│ ←  │  Classifier head │
└──────────────────┘    └──────────────────┘    └──────────────────┘
```

## Modelo

```python
MobileNetV2(
  features:           # 2.2M params, FROZEN
    - 18 inverted residual blocks
    - Output: 1280-channel feature map
  classifier (custom): # 82k params, ENTRENABLES
    - Dropout(0.3)
    - Linear(1280, 64) + ReLU
    - Linear(64, 9)  ← 9 categorías
)
```

## Estrategia de entrenamiento

- **Fase 1:** features congeladas, 2 épocas, LR=1e-3.
- **Fase 2:** descongelar últimas 30 capas, 2 épocas, LR=1e-4.

## Decisiones

| Decisión | Motivo |
|---|---|
| MobileNetV2 vs ResNet | Más liviano (2.4M vs 11M+) |
| 64×64 vs 224×224 | Más rápido en CPU |
| Transfer learning | Pocas imágenes (570) |
| Sampler balanceado | Train ligeramente desbalanceado |
