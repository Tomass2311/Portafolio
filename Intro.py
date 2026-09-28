import streamlit as st
from PIL import Image
st.title("Portafolio de Actividades en Clase.")

with st.sidebar:
    st.subheader("Portafolio de Actividades")

    st.write(
        "En este portafolio se presentan las diferentes actividades y "
        "proyectos realizados durante las clases."
    )

    st.markdown("---")

    st.write("### Información personal")

    st.write("**Nombre:** Tomás Stiven Urrego Llanos")
    st.write("**Programa:** Ingeniería de Software")
    st.write("**Materia:** Programacion Avanzada")
    st.write("**Institución:** I.U. Pascual Bravo")

    st.markdown("---")

    st.write("### Objetivo")

    st.write(
        "Mostrar de manera organizada las actividades, ejercicios y "
        "proyectos desarrollados durante el curso, junto con una breve "
        "descripción de cada uno."
    )

st.subheader("Actividades realizadas en clase")

st.write(
    "En este portafolio se presentan las diferentes actividades y "
    "ejercicios desarrollados durante las sesiones de clase, junto "
    "con una breve descripción y el enlace a cada aplicación."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sesión 2: Vectores y matrices")
    image = Image.open("txt_to_audio2.png")
    st.image(image, width=190)
    st.write(
        "Actividad enfocada en el uso de vectores y matrices mediante "
        "una aplicación en Streamlit. Se agregó una nueva fruta "
        "definiendo características como peso, diámetro y dulzor, "
        "y se calculó la distancia entre sus características." )
    url = "https://clase2fruta.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col2:
    st.subheader("Sesión 3: Cálculo aplicado, gradiente")
    image = Image.open("txt_to_audio.png")
    st.image(image, width=190)
    st.write(
        "Actividad sobre derivadas, gradiente y descenso de gradiente. "
        "Se modificó la función objetivo de la aplicación y su "
        "gradiente para observar cómo estos conceptos permiten "
        "encontrar mínimos mediante un proceso de optimización." )
    url = "https://clase3tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col3:
    st.subheader("Sesión 4: Lógica, Big-O y vectorización")
    image = Image.open("OIG5.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad enfocada en la relación entre la lógica de "
        "programación, la complejidad algorítmica y la vectorización. "
        "Se resolvió un ejercicio práctico y se incorporaron los "
        "resultados junto con el enlace de la aplicación." )
    url = "https://clase4tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sesión 5: Preparación de datos")
    image = Image.open("data_analisis.png")
    st.image(image, width=190)
    st.write(
        "Actividad práctica sobre preparación y análisis de datos. "
        "Se trabajaron conceptos como tipos de datos, valores "
        "faltantes, outliers, normalización, estandarización, "
        "división de datos, covarianza y correlación." )
    url = "https://clase5tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col2:
    st.subheader("Sesión 6: Aplicación preparación de datos")
    image = Image.open("OIG3.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad realizada con datos ambientales reales obtenidos "
        "mediante APIs de la plataforma MARCO de Cornare. Se "
        "exploraron y prepararon los datos de una estación de "
        "monitoreo y se modificó la aplicación para trabajar con "
        "una estación seleccionada." )
    url = "https://clase6tsur.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col3:
    st.subheader("Sesión 7: Regresión lineal")
    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)
    st.write(
        "Actividad sobre regresión lineal simple y múltiple, enfocada "
        "en la predicción de valores numéricos. Se trabajaron "
        "conceptos como función de costo, gradiente, descenso de "
        "gradiente y métricas de evaluación como R², MAE y RMSE." )
    url = "https://clase7tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sesión 8: Series de tiempo")
    image = Image.open("OIG6.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre el análisis y pronóstico de series de tiempo. "
        "Se exploraron conceptos como tendencia, estacionalidad y "
        "ruido, además de modelos como ARIMA y Suavizado Exponencial "
        "para la predicción de la calidad del aire." )
    url = "https://clase8tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col2:
    st.subheader("Sesión 9: Predicción de calidad del aire")
    image = Image.open("OIG4.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad enfocada en la predicción de contaminantes del "
        "aire mediante series de tiempo. Se trabajaron modelos como "
        "ARIMA, SARIMA y Holt-Winters, además del uso de ventanas "
        "deslizantes para generar predicciones." )
    url = "https://clase9tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col3:
    st.subheader("Sesión 10: Sistema de IoT")
    image = Image.open("OIG6.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre sistemas de Internet de las Cosas (IoT), "
        "enfocada en la captura y procesamiento de datos obtenidos "
        "mediante tecnologías de IoT." )
    url = "https://clase10tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sesión 11: De la regresión lineal a la logística")
    image = Image.open("OIG8.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad enfocada en el paso de la regresión lineal a la "
        "regresión logística, comprendiendo cómo pasar de predecir "
        "un valor numérico a realizar una clasificación por clases." )
    url = "https://clase11tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col2:
    st.subheader("Sesión 12: Clasificación KNN")
    image = Image.open("OIG4.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre el algoritmo K vecinos más cercanos (KNN), "
        "un método utilizado para clasificación y regresión. Se "
        "exploró su aplicación para trabajar con fronteras no "
        "lineales y problemas basados en similitud." )
    url = "https://appknntsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

