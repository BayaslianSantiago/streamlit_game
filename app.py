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
        "titulo": "Una tarde cualquiera",
        "imagen": "inicio_habitacion.jpg", # Nombre cambiado para ser más genérico
        "texto": """
        Todo comenzó una tarde de domingo. Valen estaba haciendo tiempo hasta que Santi salga de trabajar, viendo memes, tranquila y feliz, pero algo no iba bien.

        Valentina pensó "hoy voy a salir como duendecillo porque vamos al Parque Navideño" . De repente, mientras se terminaba de preparar para la salida, escuchó un ruido extraño. *Woshh... ¡MIAU!*

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
        Valentina corre, pero Nala fue más rápida. Con un maullido emocionado, Nala corre hacia el portal, salta directamente hacia el remolino de luz y desaparece!!

        Kiara se frota contra tus piernas, maullando bajito, mirando el umbral con desconfianza. No puedes dejar a Nala sola del otro lado, ni a Kiara sin saber que puede aparecer del otro lado.
        """,
        "opciones": [
            {"texto": "✨ ¡Ir a buscar a Nala! *Agarras fuerte a Kiara y se meten al portal*", "destino": "mundo_gatuno"},
            {"texto": "🧸 Intentar atraer a Nala con un juguetito desde aquí", "destino": "final_aburrido_escoba"},
        ]
    },

    # --- ESCENA 2B (Modificada) ---
    "investigacion_cauta": {
        "titulo": "Precaución ante todo",
        "imagen": "kiara_asustada_puerta.jpg", # Nombre cambiado: armario -> puerta
        "texto": """
        Decides que no es buena idea correr hacia portales mágicos. Vas despacio junto a Kiara y avanzan despacio hacia el portal, como dos agentes secretos.

        Estás muy cerca del portal, tenes que tomar una decision 
        """,
        "opciones": [
            {"texto": "😥 Tomar aire e ir por Nalita", "destino": "mundo_gatuno"},
            {"texto": "🚪 Fingir demencia", "destino": "final_cobarde"},
        ]
    },

    # --- ESCENA 3: MUNDO GATUNO ---
    "mundo_gatuno": {
        "titulo": "El Reino bajo Amenaza",
        "imagen": "mundo_gatuno_alerta.jpg",
        "texto": """
        Pasas por el portal y apareces en un mundo de fantasía, con estructuras medievales y bosques llenos de vida. El cielo es precioso, y ves un castillo a lo lejos.
        
        Nala está persiguiendo mariposas, pero Kiara está mas atenta, sobre todo a Tres Gatos Guardias Siameses armados que estan bloqueando el paso. Se ven tensos y cansados.

        "¡Alto ahí! Nadie pasa hacia el Castillo Real. Estamos en Alerta Roja por la invasión de los muertos vivientes", gruñe uno.
        Otro guardia agrega: "No les digas asi! Me asusta! :("
        el tercer guardia agrega: "no puede ser que nos hagan trabajar turnos de 2hs, solo nos dejan 8hs de siesta desde que está la alerta roja"

        
        Te acordas que llevas en el bolsillo las **abejitas de crochet** que compraste en la feria hippie.
        Pensas ''Menos mal que llevo todo encima por las dudas''
        Pero tambien ves un Bosque y la posibilidad de eludir a los guardias.
        """,
        "opciones": [
            {"texto": "🐝 Usar las abejitas para distraerlos", "destino": "soborno_abejitas"},
            {"texto": "🌳 Escabullirse por el Bosque", "destino": "bosque_rascadores"},
        ]
    },

    # --- RAMA: LAS ABEJITAS ---
    "soborno_abejitas": {
        "titulo": "La Estrategia del Crochet",
        "imagen": "guardias_jugando.jpg",
        "texto": """
        Sacas las abejitas de crochet y las mueves un poco. Los ojos de los guardias se dilatan al instante. Su disciplina militar se derrumba.

        "¡Es... es artesanía del reino humano!", grita el primer guardia que hace un rato estaba enojado.
        "Hace milenios que no hay una abeja en estos reinos, es una recreación muy valiosa! y suave!" agrega el que estaba cansado
        "Lo necesito!" grita el tercer guardia

        Lanzas las abejitas lejos. Los guardias salen corriendo tras ellas, rodando felices por el suelo. El camino está libre. Nala, Kiara y vos corren hacia el Castillo.
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
        Deciden rodear a los guardias por el bosque(sus armaduras parecen algo pesadas y no se les ve con muchas ganas de perseguilos). Los árboles son gigantes. Kiara guía el camino con sigilo experto, mientras vos tenes que cargar a Nala para que no haga quilombo.

        Desde la espesura, ves el Castillo. Necesitas una explicación para todo esto.
        """,
        "opciones": [
            {"texto": "🏰 Colarse en el Castillo", "destino": "revelacion_reina"},
        ]
    },

    # --- LA REVELACIÓN ---
    "revelacion_reina": {
        "titulo": "La Profecía",
        "imagen": "reina_gata.jpg",
        "texto": """
        Entráis al Salón del Trono. La Reina Michi no parece sorprendida.

        "Te estábamos esperando, Valentina", dice la Reina. "No entraste por accidente. Nala y Kiara abrieron el portal de tu habitación porque vos sos la elegída."

        "El **Rey Esqueleto** ha abierto una grieta desde el Inframundo. Quiere robar nuestra reserva infinita de hierba gatera y usar a nuestros michis como soldados zombies. Solo vos podes puede detenerlo."

        "El anillo de Gatitos que conseguiste en el Mundo Humano te eligio para esta cruzada, los gatos vemos todo lo que hacen por nosotros los humanos y vos
        sos la unica persona con el coraje y la voluntad de ayudarnos, con la fuerza suficiente en su espiritu para manejar el poder de los gatitos.
        Tu alma está conectada con este mundo por lo buena que fuiste con tus gatas y con todos gatos que se cruzaron en tu camino."

        No dudas ni un segundo, tu alma ya tomó una decisión antes de llegar a tu mente.
        
        """,
        "opciones": [
            {"texto": "⚔️ ¡Acepto mi destino! ¡Por los michis!", "destino": "ataque_esqueleto"},
        ]
    },

    # --- EL CLÍMAX (Elección de Clase) ---
    "ataque_esqueleto": {
        "titulo": "La forma de tu Alma",
        "imagen": "rey_esqueleto.jpg",
        "texto": """
        Un sonido que parece salido del mismo infierno emerge de un portal que estaba cerca, un portal que rompe totalmente con la apariencia amigable y espiritual del castillo y del reino.
        El **Rey Esqueleto** entra con su armadura de caballero negro y su espada consechadora de incontables vidas, hoy viene por los michis. 
        "ⵅⴹⵔⵛⵁⵃⵜⵣⵎⴿ" Ruge en un idioma extraño mas antiguo que cualquier reino.
        Pero no hay que entender lo que dice para saber lo que quiere; conquistar y destruir.

        El tiempo se congela. La Reina Gata se acerca flotando, te mira a los ojos y te toca la frente con su patita.
        "Valentina, el poder del Reino responde a tu alma, y este se va a manifestar en la forma que vos le des."
        """,
        "opciones": [
            {"texto": "🔮 Hechicera inmortal", "destino": "batalla_maga"},
            {"texto": "⚔️ Guerrera Defensora de los Michis", "destino": "batalla_espadachin"},
            {"texto": "🧚‍♀️ Hada de la Naturaleza del Reino", "destino": "batalla_hada"},
        ]
    },

    # --- BATALLA: MAGA ---
    "batalla_maga": {
        "titulo": "La aparición de la Hechicera",
        "imagen": "valen_maga_accion.jpg",
        "texto": """
        ¡FUUUSH! Una túnica roja con runas antiguas te envuelve. Tus manos sienten el poder de los hechizos, de la creacion y de la destrucción.

        Cargas con toda tu magia y lanzas el hechizo: **"¡Aniquilación total de los no-muertos!"**.

        De tus manos salen fuegos antiguos y runas que van hacia el **Rey Esqueleto**. ¡Sus huesos se empiezan a incendiar para despues desvanecerse!
        """,
        "opciones": [
            {"texto": "✨ ¡Se terminó tu reinado, maldito zombie esqueleto!", "destino": "victoria_maga"},
        ]
    },
    
    # --- VICTORIA: MAGA ---
    "victoria_maga": {
        "titulo": "La Hechicera Suprema",
        "imagen": "victoria_maga_esqueleto.jpg",
        "texto": """
        El **Rey Esqueleto** no fue rival contra la hechiceria y la magia que ya llevabas en tu alma, potenciado por el reino Michi. 
        
        Los gatos del reino maúllan tu nombre.

        Nala y Kiara te miran con orgullo, sabiendo que nunca dudaron ni un segundo que ibas a salvar a su reino.
        
        """,
        "opciones": [
            {"texto": "💤 La misión ha terminado...", "destino": "despertar_real"},
        ]
    },

    # --- BATALLA: ESPADACHÍN ---
    "batalla_espadachin": {
        "titulo": "La Espada que lucha por la Justicia",
        "imagen": "valen_espadachin_accion.jpg",
        "texto": """
        Apareces con una armadura plateada. Empuñas la **Espada de la Justicia Eterna**.

        Sentis tu fueza y destreza potenciada por el anillo gatito, en tu corazón estas segura de la victoria ya que el universo va a guiar cada paso y cada golpe.
        Te lanzas hacia el **Rey Esqueleto** para defender al Mundo Michi y a todos los Mundos de los animales que cuentan con vos en la batalla.
        """,
        "opciones": [
            {"texto": "⚔️ ¡Ataque Combinado Definitivo!", "destino": "victoria_espadachin"},
        ]
    },

    # --- VICTORIA: ESPADACHÍN ---
    "victoria_espadachin": {
        "titulo": "Corte Perfecto",
        "imagen": "victoria_espada_esqueleto.jpg",
        "texto": """
        Con una precisión increíble y una fuerza divina, tu espada rompe cada hueso del **Rey Esqueleto**. y purifica la maldida pura que hay cada trozo de sus huesos.
        
        Salvaste al Reino, y los Michis cuentan con la Guerrera mas fuerte y Elegante de todos los Mundos.
        """,
        "opciones": [
            {"texto": "💤 La misión ha terminado...", "destino": "despertar_real"},
        ]
    },

    # --- BATALLA: HADA ---
    "batalla_hada": {
        "titulo": "Hada del Bosque",
        "imagen": "valen_hada_accion.jpg",
        "texto": """
        Te crecen unas alas transparentes y brillantes. Tu ropa se convierte en pétalos de flores.

        Tu amor por la naturaleza y lo que representa en el universo; se unió junto a la fuerza del anillo gatito.

        Alzas las manos y el suelo tiembla. Invocas el poder de la naturaleza para atrapar al **Rey Esqueleto**.
        """,
        "opciones": [
            {"texto": "🌿 Acabemos con esto, quiero ir a merendar con mis hijas", "destino": "victoria_hada"},
        ]
    },

     # --- VICTORIA: HADA ---
    "victoria_hada": {
        "titulo": "Prisión Floral!",
        "imagen": "victoria_hada_esqueleto.jpg",
        "texto": """
        **Enredaderas con espinas** brotan del suelo y atrapan al Rey.

        El grita mientras las enredaderas lo envuelven completamente, destruyendo su maldad y convirtiéndolo en un bonito cactus.
        """,
        "opciones": [
            {"texto": "💤 La misión ha terminado...", "destino": "despertar_real"},
        ]
    },

    # --- EL FINAL ---
    "despertar_real": {
        "titulo": "Un Despertar...",
        "imagen": "despertar_cama.jpg",
        "texto": """
        Con el enemigo derrotado, todo se vuelve blanco. Abres los ojos. Estás en tu cama, Aun no te levantaste y Santi sale del trabajo en unas horas.

        "¿Fue todo un sueño?", piensas. Nala y Kiara duermen a tus pies, ronroneando tranquilas.

        Te levantas y sacudes la almohada. Algo cae al suelo. Es una bolsa de Hierva gatuna de alta calidad, con tu anillo de gatito que al caer refleja la luz del sol y brilla por un momento,
        Sonreis porque sabes que el reino está a salvo.

        Agarras tu celular y le mandas un audio a Santi contandole todo tu sueño con gran detalle.
        
        """,
        "es_final": True
    },

    # --- FINALES FALLIDOS (Modificados) ---
    "final_aburrido_escoba": {
        "titulo": "Final: La Realidad",
        "imagen": "final_escoba.jpg",
        "texto": """
        Intentas sacar a Nala lanzando un juguete a través del portal, pero rebota. La luz se apaga de golpe y el portal desaparece. 
        
        Nala aparece caminando desde el baño como si nada. Todo fue una alucinación por ver tantos memes hasta tan tarde.
        """,
        "es_final": True
    },
    "final_cobarde": {
        "titulo": "Final: raro",
        "imagen": "final_te_sofa.jpg",
        "texto": """
        Elegis ignorar todo pensando que es un mal viaje y nada mas. que estas mareada o que imaginas cosas. 
        Ves a Nala salir del baño y te quedas tranquila, volves a ver el portal y ya no hay nada. solo fue un momento raro.
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
