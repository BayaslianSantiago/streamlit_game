import streamlit as st
import textwrap
import os 

# --- Configuración de la página ---
st.set_page_config(
    page_title="La Gran Aventura de Valen",
    page_icon="🐱",
    layout="centered"
)

# --- CSS Personalizado (Pastel Edition) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Fredoka', sans-serif;
    }

    h1 {
        color: #8A6FA3 !important;
        text-align: center;
        font-weight: 600;
    }
    h2, h3 {
        color: #9E8FB2 !important;
        text-align: center;
        margin-top: 20px !important;
    }

    .main-text {
        font-size: 20px;
        line-height: 1.8;
        color: #5D4E6D;
        padding: 30px;
        background-color: #FFFFFF;
        border: 4px solid #C9A7EB;
        border-radius: 25px;
        box-shadow: 8px 8px 20px rgba(201, 167, 235, 0.25);
        margin-top: 20px;
        margin-bottom: 30px;
        text-align: center;
    }

    .cat-name { color: #FF8FAB; font-weight: 600; font-size: 1.1em; }
    .valen-name { color: #89CFF0; font-weight: 600; font-size: 1.1em; }
    .villain-name { color: #708090; font-weight: 600; font-size: 1.1em; }
    .magic-text { color: #9370DB; font-weight: bold; }

    div.stButton > button {
        border-radius: 20px;
        border: 2px solid #C9A7EB;
        background-color: #E0BBE4;
        color: white !important;
        font-weight: 600;
        font-size: 18px;
        padding: 10px 20px;
        transition: all 0.3s ease;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
    }

    div.stButton > button:hover {
        background-color: #FF8FAB;
        border-color: #FFC1CC;
        transform: translateY(-3px);
    }

    hr { border-color: #C9A7EB !important; opacity: 0.5; }

    img {
        border-radius: 20px;
        border: 3px solid #E0BBE4;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- Funciones Auxiliares ---
def formatear_texto(texto):
    texto = textwrap.dedent(texto).strip()
    texto = texto.replace("Valentina", '<span class="valen-name">Valentina</span>')
    texto = texto.replace("Nala", '<span class="cat-name">Nala</span>')
    texto = texto.replace("Kiara", '<span class="cat-name">Kiara</span>')
    texto = texto.replace("Rey Esqueleto", '<span class="villain-name">Rey Esqueleto</span>')
    return f'<div class="main-text">{texto}</div>'

# --- DEFINICIÓN DE LA HISTORIA COMPLETA ---
historia = {
    # --- ESCENA 1: INICIO (Modificada) ---
    "inicio": {
        "titulo": "Una tarde tranquila... ¿o no?",
        "imagen": "inicio_habitacion.jpg", # Nombre cambiado para ser más genérico
        "texto": """
        Todo comenzó una tarde de domingo. Valen estaba haciendo tiempo hasta que Santi salga de trabajar, viendo memes, tranquila y feliz, pero algo no iba bien.

        Valentina pensó "hoy voy a salir como duendecillo porque vamos al Parque Navideño" . De repente, mientras se terminaba de preprar para la salida, escuchó un ruido extraño. *Woshh... ¡MIAU!*

        Al asomarse, vio a Nala y Kiara frente a **Un Portal Dimensional**. era un **remolino de luz azulada y brillante** girando ahí mismo!

        Nala parecía hipnotizada por la luz y estaba con una patita levantada, lista para cruzar el umbral. Kiara te miraba con sus ojos enormes y azulitos, como diciendo "¡Mamá, esto no es normal!".
        """,
        "opciones": [
            {"texto": "🏃‍♀️ Correr para agarrar a Nala", "destino": "nala_salta"},
            {"texto": "🐾 Acercarse cautelosamente con Kiara", "destino": "investigacion_cauta"},
        ]
    },

    # --- ESCENA 2A (Modificada) ---
    "nala_salta": {
        "titulo": "¡El salto al vacío!",
        "imagen": "nala_salta_puerta.jpg", # Nombre cambiado: armario -> puerta
        "texto": """
        Valentina corre, pero Nala fue más rápida. Con un maullido emocionado, Nala corre hacia la puerta y salta directamente hacia el remolino de luz ¡y desaparece!

        Un torbellino de colores pastel aparece en medio de la habitación. Kiara se frota contra tus piernas, maullando bajito, mirando el umbral con desconfianza. No puedes dejar a Nala sola del otro lado.
        """,
        "opciones": [
            {"texto": "✨ ¡Cruzar el umbral por Nala!", "destino": "mundo_gatuno"},
            {"texto": "🧸 Intentar atraer a Nala con un juguetito desde aquí", "destino": "final_aburrido_escoba"},
        ]
    },

    # --- ESCENA 2B (Modificada) ---
    "investigacion_cauta": {
        "titulo": "Precaución ante todo",
        "imagen": "kiara_asustada_puerta.jpg", # Nombre cambiado: armario -> puerta
        "texto": """
        Decides que no es buena idea correr hacia portales mágicos. Te agachas junto a Kiara y avanzan despacio hacia el portal, como dos agentes secretos.

        Cuando llegan al umbral, Nala ya está del otro lado, asomando solo la cabeza entre las luces. Al sentirte cerca, Nala se gira, te mira con cara de travesura máxima, ¡y se lanza de cabeza hacia el nuevo mundo!

        Ahora solo quedáis tú y Kiara frente al portal en medio de la habitación.
        """,
        "opciones": [
            {"texto": "😥 Suspirar y cruzar tras ella", "destino": "mundo_gatuno"},
            {"texto": "🚪 Fingir demencia", "destino": "final_cobarde"},
        ]
    },

    # --- ESCENA 3: MUNDO GATUNO ---
    "mundo_gatuno": {
        "titulo": "El Reino bajo Amenaza",
        "imagen": "mundo_gatuno_alerta.jpg",
        "texto": """
        Cruzas la puerta y caes sobre una montaña de almohadones suaves. El cielo es violeta, pero hay humo oscuro a lo lejos.
        
        Nala está persiguiendo mariposas, pero Kiara se eriza. Dos Gatos Guardias Siameses armados os bloquean el paso. Se ven tensos y cansados.

        "¡Alto ahí! Nadie pasa hacia el Castillo Real. Estamos en Alerta Roja por la invasión de los Huesudos", gruñe uno.
        
        Te das cuenta de que llevas en el bolsillo esas **abejitas de crochet** que compraste en la feria hippie el otro día.
        """,
        "opciones": [
            {"texto": "🐝 Usar las abejitas para distraerlos", "destino": "soborno_abejitas"},
            {"texto": "🌳 Escabullirse por el Bosque de Rascadores", "destino": "bosque_rascadores"},
        ]
    },

    # --- RAMA: LAS ABEJITAS ---
    "soborno_abejitas": {
        "titulo": "La Estrategia del Crochet",
        "imagen": "guardias_jugando.jpg",
        "texto": """
        Sacas las abejitas de crochet y las mueves un poco. Los ojos de los guardias se dilatan al instante. Su disciplina militar se derrumba.

        "¡Es... es artesanía del reino humano!", grita uno.

        Lanzas las abejitas lejos. Los guardias salen corriendo tras ellas, rodando felices por el suelo. El camino está libre. Nala, Kiara y tú corréis hacia el Castillo.
        """,
        "opciones": [
            {"texto": "🏰 Entrar al Castillo de la Reina", "destino": "revelacion_reina"},
        ]
    },

    # --- RAMA: EL BOSQUE ---
    "bosque_rascadores": {
        "titulo": "Sigilo Felino",
        "imagen": "bosque_rascadores.jpg",
        "texto": """
        Deciden rodear a los guardias por el bosque. Los árboles son rascadores gigantes. Kiara guía el camino con sigilo experto, mientras tú tienes que cargar a Nala para que no haga ruido.

        Desde la espesura, ves el Castillo. No hay tiempo que perder, algo oscuro se acerca desde el norte.
        """,
        "opciones": [
            {"texto": "🏰 Colarse en el Castillo", "destino": "revelacion_reina"},
        ]
    },

    # --- LA REVELACIÓN ---
    "revelacion_reina": {
        "titulo": "La Profecía de la Karen",
        "imagen": "reina_gata.jpg",
        "texto": """
        Entráis al Salón del Trono. La Reina Gata (una persa blanca muy elegante) no parece sorprendida.

        "Te estábamos esperando, Valentina", dice la Reina. "No entraste por accidente. Nala y Kiara abrieron el portal de tu habitación porque tú eres la Única."

        "El **Rey Esqueleto** ha abierto una grieta desde el Inframundo. Quiere robar nuestra reserva infinita de hierba gatera y usar a nuestros michis como soldados zombies. Solo una Humana puede detenerlo."
        """,
        "opciones": [
            {"texto": "⚔️ ¡Acepto mi destino! ¡Por los michis!", "destino": "ataque_esqueleto"},
        ]
    },

    # --- EL CLÍMAX (Elección de Clase) ---
    "ataque_esqueleto": {
        "titulo": "Elige tu Destino",
        "imagen": "rey_esqueleto.jpg",
        "texto": """
        ¡BOOOM! La pared explota. El **Rey Esqueleto** entra con su ejército de huesos. "¡Entregadme a los gatitos!", ruge.

        El tiempo se congela. La Reina Gata te toca la frente con su pata.
        "Valentina, el poder del Reino responde a tu alma. ¿Qué forma tomarás para defendernos?"
        """,
        "opciones": [
            {"texto": "🔮 Maga Guerrera Gatita", "destino": "batalla_maga"},
            {"texto": "⚔️ Espadachín Guerrera Gatuna", "destino": "batalla_espadachin"},
            {"texto": "🧚‍♀️ Hada de la Naturaleza", "destino": "batalla_hada"},
        ]
    },

    # --- BATALLA: MAGA ---
    "batalla_maga": {
        "titulo": "La Maga Suprema",
        "imagen": "valen_maga_accion.jpg",
        "texto": """
        ¡FUUUSH! Una túnica violeta con estrellas brillantes te envuelve. En tu mano aparece un Báculo con una joya en forma de patita.

        Cargas tu magia y lanzas el hechizo: **"¡Lluvia de Meteoritos de Lana!"**.

        Bolas de fuego rosa caen del cielo hacia el **Rey Esqueleto**. ¡Sus huesos empiezan a brillar y a bailar sin control!
        """,
        "opciones": [
            {"texto": "✨ ¡Ver el resultado de tu magia!", "destino": "victoria_maga"},
        ]
    },
    
    # --- VICTORIA: MAGA ---
    "victoria_maga": {
        "titulo": "Victoria Mágica",
        "imagen": "victoria_maga_esqueleto.jpg",
        "texto": """
        El **Rey Esqueleto** no puede soportar el ritmo del hechizo bailongo. 
        
        ¡CRACK! ¡PUM! Explota en una nube de purpurina, confeti y huesitos inofensivos que caen al suelo. ¡La magia ha triunfado! Los gatos del reino maúllan tu nombre.
        """,
        "opciones": [
            {"texto": "💤 La misión ha terminado...", "destino": "despertar_real"},
        ]
    },

    # --- BATALLA: ESPADACHÍN ---
    "batalla_espadachin": {
        "titulo": "La Espadachín Veloz",
        "imagen": "valen_espadachin_accion.jpg",
        "texto": """
        ¡ZAS! Apareces con una armadura ligera y plateada con orejas de gato en el casco. Empuñas la **Katana del Ronroneo Eterno**.

        Te mueves más rápido que Nala persiguiendo un puntero láser. Te lanzas hacia el **Rey Esqueleto** para dar el golpe de gracia a su corona.
        """,
        "opciones": [
            {"texto": "⚔️ ¡Ver el golpe final!", "destino": "victoria_espadachin"},
        ]
    },

    # --- VICTORIA: ESPADACHÍN ---
    "victoria_espadachin": {
        "titulo": "Corte Perfecto",
        "imagen": "victoria_espada_esqueleto.jpg",
        "texto": """
        Con una precisión increíble, tu katana corta la corona de huesos del Rey. Sin su corona, su poder se desvanece.
        
        El **Rey Esqueleto** se desarma y cae al suelo, convirtiéndose en una pila de huesos tristes. ¡Tu velocidad salvó el reino!
        """,
        "opciones": [
            {"texto": "💤 La misión ha terminado...", "destino": "despertar_real"},
        ]
    },

    # --- BATALLA: HADA ---
    "batalla_hada": {
        "titulo": "El Hada del Bosque Gatuno",
        "imagen": "valen_hada_accion.jpg",
        "texto": """
        ¡PLING! Te crecen unas alas transparentes y brillantes. Tu ropa se convierte en pétalos de flores silvestres.

        Alzas las manos y el suelo tiembla. Invocas el poder de la naturaleza para atrapar al **Rey Esqueleto**.
        """,
        "opciones": [
            {"texto": "🌿 ¡Ver el poder de la naturaleza!", "destino": "victoria_hada"},
        ]
    },

     # --- VICTORIA: HADA ---
    "victoria_hada": {
        "titulo": "La Prisión Floral",
        "imagen": "victoria_hada_esqueleto.jpg",
        "texto": """
        **Enredaderas de Hierba Gatera Gigante** brotan del suelo y atrapan al Rey.

        "¡Noooo, soy alérgico al polen del amor!", grita mientras las flores lo envuelven completamente, purificando su maldad y convirtiéndolo en un arbusto decorativo muy bonito.
        """,
        "opciones": [
            {"texto": "💤 La misión ha terminado...", "destino": "despertar_real"},
        ]
    },

    # --- EL FINAL ---
    "despertar_real": {
        "titulo": "Un Despertar... ¿Mágico?",
        "imagen": "despertar_cama.jpg",
        "texto": """
        Con el enemigo derrotado, todo se vuelve blanco. Abres los ojos. Estás en tu cama. Es lunes por la mañana.

        "¿Fue todo un sueño?", piensas. Nala y Kiara duermen a tus pies, ronroneando tranquilas.

        Te levantas y sacudes la almohada. Algo cae al suelo. Es una de las **abejitas de crochet**... pero tiene un pequeño mordisco de gato y brilla con una luz tenue y rosada.

        Sonríes. El reino está a salvo gracias a ti.
        """,
        "es_final": True
    },

    # --- FINALES FALLIDOS (Modificados) ---
    "final_aburrido_escoba": {
        "titulo": "Final: La Realidad Decepcionante",
        "imagen": "final_escoba.jpg",
        "texto": """
        Intentas pescar a Nala lanzando un juguete a través del umbral, pero rebota. La luz se apaga de golpe y el portal desaparece. 
        
        Nala aparece caminando desde el baño como si nada. Todo fue una alucinación por ver TikToks hasta tan tarde.
        """,
        "es_final": True
    },
    "final_cobarde": {
        "titulo": "Final: La Duda Eterna",
        "imagen": "final_te_sofa.jpg",
        "texto": """
        Elegis ignorar todo pensando que es un mal viaje y nada mas. El corazón a mil pero decidis ir a pedir ayuda alguien en tu casa. 
        
        Mejor no saber qué había del otro lado. Te vas a dormir, pero siempre te preguntarás por qué tus gatas te miran a veces como si fueras una reina que renunció a su corona.
        """,
        "es_final": True
    },
}

# --- LÓGICA DEL JUEGO ---
if 'escena_actual' not in st.session_state:
    st.session_state['escena_actual'] = 'inicio'

def cambiar_escena(nueva_escena):
    st.session_state['escena_actual'] = nueva_escena

escena_id = st.session_state['escena_actual']
# Manejo de errores
escena_datos = historia.get(escena_id, {
    "titulo": "Error en la Matrix Gatuna", 
    "texto": "¡Ups! Esta parte de la historia se perdió en el limbo.", 
    "es_final": True
})

# --- RENDERIZADO EN PANTALLA ---

st.title(f"{escena_datos['titulo']}")

# --- CÓDIGO DE IMÁGENES ---
image_path = escena_datos.get("imagen")
if image_path:
    if os.path.exists(image_path):
        st.image(image_path, use_column_width=True)
    else:
        # Mensaje de ayuda discreto
        st.info(f"📸 Falta la imagen: {image_path}")

st.markdown(formatear_texto(escena_datos['texto']), unsafe_allow_html=True)

st.divider()

if escena_datos.get("es_final"):
    st.subheader("🌸 Fin de la Aventura 🌸")
    if st.button("🔄 Volver a soñar"):
        cambiar_escena("inicio")
        st.rerun()
else:
    # Títulos especiales
    if escena_id == "ataque_esqueleto":
        st.subheader("✨ ¡ELIGE TU PODER! ✨")
    elif "batalla_" in escena_id:
        st.subheader("💥 ¡AL ATAQUE! 💥")
    else:
        st.subheader("¿Qué hará Valentina?")
        
    cols = st.columns(len(escena_datos['opciones']))
    for i, opcion in enumerate(escena_datos['opciones']):
        cols[i].button(
            opcion["texto"],
            on_click=cambiar_escena,
            args=(opcion["destino"],),
            use_container_width=True
        )
