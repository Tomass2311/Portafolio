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

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

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

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


