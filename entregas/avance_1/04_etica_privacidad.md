# Consideraciones Éticas y de Privacidad

## 1. Privacidad

El dataset solo contiene **fotografías de residuos**. No hay PII. **No aplica la Ley 25.326**.

## 2. Sesgos identificados

### Sesgo geográfico
Dataset proviene de Australia. Residuos argentinos pueden tener empaques distintos (ej. envases sachet típicos del país).

### Sesgo de fondo
Imágenes capturadas en condiciones estandarizadas (fondo plano). Generalización a fotos de campo limitada.

### Desbalance de clases en train
Plastic 65, Textile_Trash 35, Vegetation 35 → mitigado con WeightedRandomSampler.

## 3. Riesgos

| Riesgo | Prob | Impacto | Mitigación |
|---|---|---|---|
| Falso reciclaje (item al contenedor equivocado) | Media | Bajo a medio | Mostrar probabilidad, sugerir consultar etiqueta del envase |
| Sobre-confianza del usuario | Alta | Bajo | Caveat permanente |
| Mal uso para fines comerciales sin licencia | Baja | Bajo | Citación obligatoria de la fuente |

## 4. Caveat en la app

> ⚠️ **Aviso:** Esta herramienta es de apoyo educativo y experimental. Su clasificación tiene un margen de error y NO debería usarse como única fuente de verdad para reciclaje a escala industrial. Para decisiones críticas, verificar manualmente.

## 5. Sostenibilidad

El modelo MobileNetV2 está diseñado para correr en dispositivos modestos. **No requiere GPU ni cloud** — alineado con criterios de IA de bajo impacto ambiental.
