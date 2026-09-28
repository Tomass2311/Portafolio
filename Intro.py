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
        "Actividad sobre vectores y matrices en Streamlit. "
        "Se agregó una nueva fruta con características de peso, "
        "diámetro y dulzor, y se calculó la distancia entre frutas."
    )
    url = "https://clase2fruta.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col2:
    st.subheader("Sesión 3: Cálculo aplicado, gradiente")
    image = Image.open("txt_to_audio.png")
    st.image(image, width=190)
    st.write(
        "Actividad sobre derivadas, gradiente y descenso de gradiente. "
        "Se modificó la función objetivo y su gradiente para realizar "
        "un proceso de optimización."
    )
    url = "https://clase3tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col3:
    st.subheader("Sesión 4: Lógica, Big-O y vectorización")
    image = Image.open("OIG5.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre lógica, complejidad algorítmica y vectorización. "
        "Se resolvió un ejercicio práctico relacionado con la eficiencia "
        "de los procesos computacionales."
    )
    url = "https://clase4tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sesión 5: Preparación de datos")
    image = Image.open("data_analisis.png")
    st.image(image, width=190)
    st.write(
        "Actividad sobre preparación y análisis de datos. "
        "Se trabajaron tipos de datos, outliers, normalización, "
        "estandarización, división de datos y correlación."
    )
    url = "https://clase5tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col2:
    st.subheader("Sesión 6: Aplicación preparación de datos")
    image = Image.open("OIG3.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad con datos ambientales reales de MARCO de Cornare. "
        "Se consultaron datos de una estación y se modificó la aplicación "
        "para trabajar con información propia."
    )
    url = "https://clase6tsur.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col3:
    st.subheader("Sesión 7: Regresión lineal")
    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)
    st.write(
        "Actividad sobre regresión lineal simple y múltiple para realizar "
        "predicciones numéricas, trabajando gradiente, descenso de gradiente "
        "y métricas de evaluación."
    )
    url = "https://clase7tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sesión 8: Series de tiempo")
    image = Image.open("OIG6.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre análisis y pronóstico de series de tiempo. "
        "Se exploraron tendencia, estacionalidad y modelos como "
        "ARIMA y Suavizado Exponencial."
    )
    url = "https://clase8tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col2:
    st.subheader("Sesión 9: Predicción de calidad del aire")
    image = Image.open("OIG4.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre predicción de contaminantes del aire mediante "
        "series de tiempo. Se trabajaron modelos ARIMA, SARIMA, "
        "Holt-Winters y ventanas deslizantes."
    )
    url = "https://clase9tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col3:
    st.subheader("Sesión 10: Sistema de IoT")
    image = Image.open("OIG6.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre Internet de las Cosas (IoT), enfocada en "
        "la captura y procesamiento de datos obtenidos mediante "
        "tecnologías de IoT."
    )
    url = "https://clase10tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Sesión 11: De la regresión lineal a la logística")
    image = Image.open("OIG8.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre regresión logística y clasificación. "
        "Se exploró el paso de predecir valores numéricos a "
        "clasificar datos en diferentes clases."
    )
    url = "https://clase11tsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")

with col2:
    st.subheader("Sesión 12: Clasificación KNN")
    image = Image.open("OIG4.jpg")
    st.image(image, width=190)
    st.write(
        "Actividad sobre el algoritmo K vecinos más cercanos (KNN). "
        "Se exploró su uso para clasificación y regresión mediante "
        "la similitud entre los datos."
    )
    url = "https://appknntsul.streamlit.app/"
    st.write(f"Aplicación: [Ver actividad]({url})")
