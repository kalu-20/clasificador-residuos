# ♻️ Clasificador de Residuos para Reciclaje

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kalu-20/clasificador-residuos/blob/main/notebook.ipynb)
[![View on GitHub Pages](https://img.shields.io/badge/View-GitHub%20Pages-blue)](https://kalu-20.github.io/clasificador-residuos/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Sistema de Inteligencia Artificial Aplicada para clasificación automática de residuos mediante visión por computadora.**

> **Trabajo Integrador Final** · Modelado de Sistemas de IA Aplicada · UPATecO Salta · Ciclo lectivo 2026

---

## 👥 Equipo

| Integrante | Rol |
|---|---|
| **María Claudia Fabián** | Líder · Análisis · Modelado |
| _Integrante 2_ | _por completar_ |
| _Integrante 3_ | _por completar_ |

**Formador:** Lic. Walter Gabriel Ramirez

---

## 🎯 Problema

La gestión inadecuada de residuos es un problema ambiental crítico. La separación correcta requiere educación ciudadana o sistemas automatizados. Este proyecto desarrolla un **clasificador CNN** que, dada una foto de un residuo, predice a cuál de **9 categorías** pertenece:

📦 Cardboard · 🍎 Food Organics · 🍾 Glass · 🥫 Metal · 🗑️ Misc Trash · 📄 Paper · 🥤 Plastic · 👕 Textile Trash · 🌿 Vegetation

## 🛠️ Stack tecnológico

- **Modelo:** MobileNetV2 + Transfer Learning (PyTorch)
- **Dataset:** [RealWaste · UCI ML Repository (ID 908)](https://archive.ics.uci.edu/dataset/908/realwaste)
- **App local:** Streamlit
- **Notebook:** Jupyter / Google Colab

## 📂 Estructura del repositorio

```
clasificador-residuos/
├── notebook.ipynb           ← Notebook principal (Colab-ready)
├── index.html               ← Versión HTML para GitHub Pages
├── data/                    ← Dataset (480 imágenes en 9 clases)
│   ├── Cardboard/
│   ├── Food_Organics/
│   ├── Glass/
│   ├── Metal/
│   ├── Miscellaneous_Trash/
│   ├── Paper/
│   ├── Plastic/
│   ├── Textile_Trash/
│   └── Vegetation/
├── app/streamlit_app.py     ← App local con uploader
├── models/                  ← Modelo entrenado .pt
├── reports/
│   ├── figures/             ← 12 figuras del análisis
│   ├── Informe_APA_TIF_Residuos.pdf
│   └── Presentacion_Final_TIF_Residuos.pptx
├── docs/                    ← Documentación
└── entregas/                ← Avances 1-5 con archivos esenciales
```

## 🚀 Cómo correr el proyecto

### Opción 1 · En Google Colab (recomendado)

Click en el badge "Open in Colab" arriba ⬆️. El notebook se abre y al apretar **Ejecutar todas** (`Ctrl+F9`):
1. Clona este repo (incluye dataset).
2. Entrena el modelo (~3-4 min en CPU de Colab).
3. Genera visualizaciones, matriz de confusión, ROC y predicciones.

### Opción 2 · En GitHub Pages (solo lectura)

Andá a **[kalu-20.github.io/clasificador-residuos](https://kalu-20.github.io/clasificador-residuos/)** y vas a ver el notebook completo con todas las figuras y resultados, sin necesidad de ejecutarlo.

### Opción 3 · Local

```bash
git clone https://github.com/kalu-20/clasificador-residuos.git
cd clasificador-residuos
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

### Opción 4 · App Streamlit local (con uploader de imagen)

```bash
streamlit run app/streamlit_app.py
# Abre en http://localhost:8501
```

## 📊 Resultados

| Métrica | Valor |
|---|---|
| Modelo | MobileNetV2 + Transfer Learning |
| Accuracy en test | ~50 % |
| F1 macro | ~0,46 |
| Random baseline | 11,1 % (1/9) |
| Mejora vs random | × 4+ |

## 📅 Cronograma de entregas (TIF)

🌐 **Índice web de entregas:** [kalu-20.github.io/clasificador-residuos/entregas/](https://kalu-20.github.io/clasificador-residuos/entregas/)

| Avance | Fecha | Página web | Carpeta |
|---|---|---|---|
| Avance 1 — Problema y plan | 24/04/2026 | [📄 ver online](https://kalu-20.github.io/clasificador-residuos/entregas/avance_1/) | [`entregas/avance_1/`](entregas/avance_1/) |
| Avance 2 — Núcleo técnico | 08/05/2026 | [📄 ver online](https://kalu-20.github.io/clasificador-residuos/entregas/avance_2/) | [`entregas/avance_2/`](entregas/avance_2/) |
| Avance 3 — App local | 29/05/2026 | [📄 ver online](https://kalu-20.github.io/clasificador-residuos/entregas/avance_3/) | [`entregas/avance_3/`](entregas/avance_3/) |
| Avance 4 — Evaluación completa | 12/06/2026 | [📄 ver online](https://kalu-20.github.io/clasificador-residuos/entregas/avance_4/) | [`entregas/avance_4/`](entregas/avance_4/) |
| Presentación final | 23-30/06/2026 | [📄 ver online](https://kalu-20.github.io/clasificador-residuos/entregas/avance_5/) | [`entregas/avance_5/`](entregas/avance_5/) |

## 📜 Licencia

- **Código:** MIT License
- **Dataset RealWaste:** Creative Commons Attribution 4.0 (UCI ML Repository)

## 🙏 Agradecimientos

- Dataset original: Single, S. & Quinn, E. (2023). RealWaste. *Information*, 14(12), 633.
- Arquitectura: Sandler, M., et al. (2018). MobileNetV2. *CVPR*.
- Mirror del dataset: [shahzaibvohra/realwaste · Hugging Face](https://huggingface.co/datasets/shahzaibvohra/realwaste).
