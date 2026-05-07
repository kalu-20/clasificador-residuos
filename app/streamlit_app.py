"""
streamlit_app.py — App de clasificación de residuos.
TIF · UPATecO Salta · 2026

Cómo correr:
    streamlit run app/streamlit_app.py
"""

from pathlib import Path
import json
import numpy as np
import torch
import torch.nn as nn
import streamlit as st
from PIL import Image
from torchvision import transforms, models
from torchvision.models import MobileNet_V2_Weights
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "best_model_waste.pt"
CLASSES_PATH = PROJECT_ROOT / "models" / "classes.json"

# ──────────────────────────────────────────────
# Mensajes y emojis
# ──────────────────────────────────────────────
EMOJI = {
    "Cardboard": "📦", "Food_Organics": "🍎", "Glass": "🍾",
    "Metal": "🥫", "Miscellaneous_Trash": "🗑️", "Paper": "📄",
    "Plastic": "🥤", "Textile_Trash": "👕", "Vegetation": "🌿",
}
RECOMENDACIONES = {
    "Cardboard": "**Cartón.** Va al contenedor azul (papel/cartón). Aplastá la caja para ahorrar espacio.",
    "Food_Organics": "**Residuo orgánico.** Va al contenedor marrón (orgánicos) o composta. NO al plástico ni metal.",
    "Glass": "**Vidrio.** Va al contenedor verde (vidrio). Sin tapas; enjuagá el envase.",
    "Metal": "**Metal.** Va al contenedor amarillo (envases) o gris (metal). Aplastá las latas.",
    "Miscellaneous_Trash": "**Basura miscelánea.** Va al contenedor gris/negro. Si dudás, no contamines reciclables.",
    "Paper": "**Papel.** Va al contenedor azul. Sin grasa ni comida pegada.",
    "Plastic": "**Plástico.** Va al contenedor amarillo (envases). Verificá el código de reciclaje.",
    "Textile_Trash": "**Textil.** No va al reciclaje común. Llevá a punto verde de textiles o donaciones.",
    "Vegetation": "**Vegetación.** Compostable. Va al contenedor marrón o composta de jardín.",
}

st.set_page_config(
    page_title="Clasificador de Residuos · TIF UPATecO",
    page_icon="♻️",
    layout="wide",
)

# ──────────────────────────────────────────────
# Carga modelo (cacheada)
# ──────────────────────────────────────────────
@st.cache_resource
def cargar_modelo():
    if not MODEL_PATH.exists():
        return None, None
    with open(CLASSES_PATH) as f:
        classes = json.load(f)
    weights = MobileNet_V2_Weights.IMAGENET1K_V1
    model = models.mobilenet_v2(weights=weights)
    model.classifier = nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(model.last_channel, 64),
        nn.ReLU(),
        nn.Linear(64, len(classes)),
    )
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    return model, classes


@st.cache_resource
def cargar_transform():
    return transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])


def predecir(model, transform, classes, img: Image.Image):
    x = transform(img.convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        out = model(x)
        probs = torch.softmax(out, dim=1).numpy()[0]
    pred_idx = int(probs.argmax())
    return classes[pred_idx], probs


# ──────────────────────────────────────────────
# UI
# ──────────────────────────────────────────────
st.title("♻️ Clasificador de Residuos para Reciclaje")
st.markdown(
    """
    Sistema diagnóstico que recibe la **foto de un residuo** y predice
    a cuál de 9 categorías pertenece para apoyar la separación correcta
    en origen.

    *Trabajo Integrador Final · UPATecO Salta · Ciclo 2026 ·
    Cátedra Modelado de Sistemas de IA Aplicada · Lic. Walter G. Ramirez*
    """
)

st.warning(
    "⚠️ **Aviso:** Esta herramienta es de apoyo educativo y experimental. "
    "Su clasificación tiene un margen de error. Para decisiones críticas, "
    "verificá manualmente o consultá la normativa local de reciclaje."
)

# Sidebar
with st.sidebar:
    st.header("ℹ️ Información del modelo")
    model, classes = cargar_modelo()
    if model is None:
        st.error("Modelo no encontrado.")
    else:
        st.success("✓ Modelo MobileNetV2 cargado")
        st.caption(
            "**Arquitectura:** MobileNetV2 + Transfer Learning\n\n"
            "**Métricas en test (135 imgs):**\n"
            "- Accuracy: 48,1 %\n"
            "- F1 macro: 0,459\n"
            "- Random baseline: 11,1 %\n"
            "- Mejora vs random: × 4,3\n\n"
            "**9 clases:** Cardboard, Food Organics, "
            "Glass, Metal, Misc Trash, Paper, Plastic, "
            "Textile Trash, Vegetation"
        )
    st.markdown("---")
    st.markdown(
        "**Fuente:** RealWaste Dataset · UCI ML Repository\n\n"
        "**Licencia:** CC BY 4.0"
    )

transform = cargar_transform()

# Uploader
st.subheader("📸 Subí una foto del residuo a clasificar")
uploaded = st.file_uploader(
    "Elegí una imagen (JPG, JPEG o PNG)",
    type=["jpg", "jpeg", "png"],
    help="Idealmente con fondo plano y buena iluminación.",
)

# Ejemplos rápidos
ejemplos_dir = PROJECT_ROOT / "datos" / "raw" / "test"
if not uploaded and model is not None and ejemplos_dir.exists():
    st.info("💡 ¿No tenés imagen a mano? Probá con un ejemplo del test set:")
    cols = st.columns(5)
    classes_show = classes[:5]
    for i, cls in enumerate(classes_show):
        files = list((ejemplos_dir / cls).iterdir())
        if files:
            with cols[i]:
                if st.button(f"{EMOJI.get(cls, '🗑️')} {cls.replace('_',' ')}", key=f"ej_{i}"):
                    uploaded = open(files[0], "rb")

# Procesar
if uploaded is not None and model is not None:
    img = Image.open(uploaded)
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(img, caption=f"Imagen · {img.size[0]}×{img.size[1]} px", use_container_width=True)

    with col2:
        with st.spinner("Analizando..."):
            pred_cls, probs = predecir(model, transform, classes, img)
        prob_pred = probs[classes.index(pred_cls)]

        # Card grande con la predicción
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #27ae60, #2ecc71); color:white;
                        padding:25px; border-radius:12px; text-align:center;
                        margin-bottom:20px;">
                <h2 style="margin:0; color:white;">{EMOJI.get(pred_cls, '🗑️')} {pred_cls.replace('_', ' ')}</h2>
                <p style="margin:8px 0 0 0; font-size:18px;">
                    Confianza: <b>{prob_pred*100:.1f}%</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Recomendación
        st.info(RECOMENDACIONES.get(pred_cls, ""))

    # Bar chart
    st.subheader("📊 Probabilidades por clase")
    fig, ax = plt.subplots(figsize=(11, 4.5))
    colors = ["#3498db","#e74c3c","#27ae60","#f39c12","#9b59b6","#1abc9c","#34495e","#e91e63","#f1c40f"]
    bars = ax.bar([c.replace("_"," ") for c in classes], probs * 100, color=colors)
    bars[classes.index(pred_cls)].set_edgecolor("black")
    bars[classes.index(pred_cls)].set_linewidth(2)
    ax.set_ylim(0, 105)
    ax.set_ylabel("Probabilidad (%)")
    ax.set_title("Distribución de probabilidades", fontweight="bold", color="black")
    for bar, prob in zip(bars, probs):
        ax.text(bar.get_x() + bar.get_width()/2, prob*100 + 1,
                f"{prob*100:.1f}%", ha="center", fontweight="bold", fontsize=9)
    plt.xticks(rotation=20, ha="right")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)

    # Detalles técnicos
    with st.expander("🔬 Detalles técnicos"):
        st.write("**Probabilidades exactas:**")
        st.dataframe({
            "Clase": [c.replace("_"," ") for c in classes],
            "Probabilidad": [f"{p*100:.4f}%" for p in probs],
        }, use_container_width=True)
        st.write(f"**Tamaño del modelo:** ~9 MB · **Imagen procesada:** 64×64 RGB")

# Footer
st.markdown("---")
st.caption(
    "**Equipo:** María Claudia Fabián _(+ por completar)_  ·  "
    "**Formador:** Lic. Walter Gabriel Ramirez"
)
st.caption(
    "Dataset: [RealWaste · UCI](https://archive.ics.uci.edu/dataset/908/realwaste) · "
    "Licencia CC BY 4.0"
)
