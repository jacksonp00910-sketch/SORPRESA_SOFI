import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Nuestra Historia ❤️", page_icon="🌹", layout="centered")

# Estilos visuales con contraste alto para la caja de texto y diseño limpio
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    h1, h2, h3, p {
        text-align: center;
        color: #333333;
    }
    /* Estilo para que la caja de texto resalte claramente */
    .stTextInput input {
        background-color: #ffffff !important;
        color: #2c3e50 !important;
        border: 2px solid #ff6b81 !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        text-align: center !important;
    }
    .stButton button {
        border-radius: 20px;
        font-weight: bold;
    }
    .mensaje-final {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
        text-align: left;
        line-height: 1.6;
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar variables de estado
if "fase" not in st.session_state:
    st.session_state.fase = 1
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "intentos_no" not in st.session_state:
    st.session_state.intentos_no = 0

# --- FASE 1: INGRESAR EL NOMBRE ---
if st.session_state.fase == 1:
    st.markdown("# ¡Hola! ❤️")
    st.markdown("### Por favor, ingresa tu nombre:")
    
    nombre_input = st.text_input("Tu nombre aquí...", label_visibility="collapsed")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Continuar ✨", use_container_width=True):
            if nombre_input.strip() == "":
                st.warning("¡Tienes que escribir tu nombre primero, preciosa!")
            else:
                st.session_state.nombre = nombre_input.strip()
                st.session_state.fase = 2
                st.rerun()

# --- FASE 2: PREGUNTA INTERACTIVA ---
elif st.session_state.fase == 2:
    st.markdown(f"# ¡Hola, {st.session_state.nombre}! ❤️")
    st.markdown("### Tengo una pregunta muy importante para ti...")
    st.markdown("## ¿Quieres ser mi novia?")
    
    st.write("")
    
    textos_no = [
        "No 🙈", 
        "¿Segura? 🧐", 
        "Piénsalo bien... 🤔", 
        "¿Me rompes el corazón? 🥺", 
        "Dale otra oportunidad al amor 💖", 
        "El sistema dice que no te creo 🤖", 
        "¡Error 404: Respuesta inválida!", 
        "Ok, ya te estás poniendo terca 😂",
        "¡Última oportunidad!"
    ]
    
    no_agotado = st.session_state.intentos_no >= len(textos_no)
    
    if no_agotado:
        st.info("¡El botón 'No' ha decidido retirarse de la pantalla! Solo te queda una opción. 🥰")
        col_centro = st.columns([1, 2, 1])[1]
        with col_centro:
            if st.button("¡SÍ! 🥰", use_container_width=True):
                st.session_state.fase = 3
                st.rerun()
    else:
        col_si, col_no = st.columns(2)
        with col_si:
            if st.button("¡SÍ! 🥰", use_container_width=True):
                st.session_state.fase = 3
                st.rerun()
                
        with col_no:
            texto_actual = textos_no[st.session_state.intentos_no]
            if st.button(texto_actual, use_container_width=True):
                st.session_state.intentos_no += 1
                st.rerun()

# --- FASE 3: EL MENSAJE FINAL (SOLO SI DICE SÍ) ---
elif st.session_state.fase == 3:
    st.markdown("# ✨ ¡Y así comienza nuestra historia! ✨")
    
    # Reproductor de música limpio usando iframe
    musica_url = "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3"
    st.markdown(
        f'<iframe src="{musica_url}" allow="autoplay" style="display:none"></iframe>',
        unsafe_allow_html=True
    )
    
    st.markdown("""
    <div class="mensaje-final">
        <p>Si llegaste hasta aquí, es porque decidiste darme una oportunidad para escribir una nueva historia juntos. ❤️</p>
        <p>No te prometo que todos los días serán perfectos, pero sí que quiero hacer de cada uno de ellos un motivo para sonreír. Quiero seguir conociéndote, escucharte, apoyarte en tus sueños, sorprenderte con tus postres favoritos y crear recuerdos que algún día podamos mirar con una sonrisa.</p>
        <p>Quiero ser esa persona con la que puedas contar, con quien puedas ser vos misma y con quien los días sencillos se conviertan en momentos especiales.</p>
        <p>Porque si algo tengo claro, es que no quiero una historia perfecta; quiero una historia real, bonita y nuestra, que construyamos juntos, paso a paso, con cariño, confianza y muchas ganas de elegirnos cada día.</p>
        <p>Así que preparate, porque todavía nos quedan muchísimas aventuras, risas, abrazos, citas bonitas y recuerdos por crear. 🌹✨</p>
        <p style="text-align: center; font-weight: bold; font-size: 1.1em; color: #e74c3c;">
            ❤️ Te quiero muchísimo, Sofi. Gracias por darme la oportunidad de intentarlo contigo. ❤️
        </p>
        <p style="text-align: center; font-weight: bold; font-size: 1.2em;">
            Y ahora sí… ¡que comience nuestra aventura! 💫
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.balloons()