# 📱 Avance 3 — App local funcionando
**Fecha:** 29/05/2026

## Esencial para el docente
- `avance_3.md` — documento del avance
- 💻 **App:** [`../../app/streamlit_app.py`](../../app/streamlit_app.py)
- 📸 **Screenshots reales:**
  - `app_screenshot_inicio.png` — vista inicial
  - `app_screenshot_prediccion.png` — predicción real con probabilidades

## Cómo correrla
```bash
git clone https://github.com/kalu-20/clasificador-residuos.git
cd clasificador-residuos
pip install -r requirements.txt
streamlit run app/streamlit_app.py
# Abre en http://localhost:8501
```

## Funcionalidad
1. Upload imagen JPG/PNG
2. Predicción + probabilidad
3. Bar chart con 9 clases
4. Recomendación contextual de reciclaje
5. Caveat ético siempre visible
