# Diccionario de Datos

## Fuente

**RealWaste Dataset** — UCI Machine Learning Repository · ID 908
- **URL:** https://archive.ics.uci.edu/dataset/908/realwaste
- **Mirror HF:** https://huggingface.co/datasets/shahzaibvohra/realwaste
- **Licencia:** Creative Commons Attribution 4.0
- **Origen:** Whyte's Gully Waste and Resource Recovery facility (Wollongong, NSW, Australia)
- **Resolución original:** 524×524 píxeles

## Estructura

```
datos/raw/
├── train/  (435 imágenes)
│   ├── Cardboard/        50
│   ├── Food_Organics/    50
│   ├── Glass/            50
│   ├── Metal/            50
│   ├── Miscellaneous_Trash/ 50
│   ├── Paper/            50
│   ├── Plastic/          65
│   ├── Textile_Trash/    35
│   └── Vegetation/       35
└── test/   (135 imágenes - 15 por clase)
    ├── Cardboard/        15
    ├── ...
    └── Vegetation/       15
```

**Total: 570 imágenes** (>200 mín. TIF).

## Clases (target)

| Clase | Descripción |
|---|---|
| **Cardboard** | Cartón corrugado, cajas de cartón |
| **Food Organics** | Restos de comida, frutas y vegetales descartados |
| **Glass** | Botellas, vidrios rotos, frascos |
| **Metal** | Latas, hojalata, aluminio |
| **Miscellaneous Trash** | Residuos no clasificables o multiclase |
| **Paper** | Hojas, periódicos, papel impreso |
| **Plastic** | Botellas plásticas, envases, films |
| **Textile Trash** | Telas, ropa, géneros textiles |
| **Vegetation** | Hojas, ramas, restos de jardín |

## Características

| Atributo | Valor |
|---|---|
| Formato | JPG |
| Canales | RGB (3) |
| Tamaño usado | 64×64 (resize) |
| Encoding | sRGB |

## Calidad de los datos

| Dimensión | Evaluación |
|---|---|
| Exactitud | Alta — etiquetas verificadas |
| Completitud | Total |
| Consistencia | Alta — mismo formato |
| Validez | Alta — clases bien definidas |
| Unicidad | Verificada |

## Limitaciones

1. **Imágenes con fondo controlado** — generalización a fotos de campo puede degradar.
2. **Solo 9 clases** — residuos raros (RAEE, peligrosos) no detectados.
3. **Subset reducido (570)** — con dataset completo (4.752) los resultados serían mejores.
