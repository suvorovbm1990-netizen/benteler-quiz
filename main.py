import streamlit as st
import random

st.set_page_config(page_title="Benteler Quiz", page_icon="🔧", layout="centered")

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = [
        {
            "question": "1. Benennen Sie die in der Zeichnung gekennzeichneten Groessen. (Alpha, Beta, Gamma, 1, 2, 3)",
            "choices": [
                "Freiwinkel, Keilwinkel, Spanwinkel, Spanflaeche, Freiflaeche, Schnittflaeche",
                "Spanwinkel, Keilwinkel, Freiwinkel, Freiflaeche, Spanflaeche, Schnittflaeche",
                "Keilwinkel, Freiwinkel, Spanwinkel, Schnittflaeche, Freiflaeche, Spanflaeche"
            ],
            "correct": ["Freiwinkel, Keilwinkel, Spanwinkel, Spanflaeche, Freiflaeche, Schnittflaeche"]
        },
        {
            "question": "2. Welche drei Arten von Spanen koennen beim Spanen entstehen?",
            "choices": ["Fliessspan, Scherspan, Reissspan", "Langespan, Kurzespan, Reissspan", "Grobspan, Feinspan, Mittelspan"],
            "correct": ["Fliessspan, Scherspan, Reissspan"]
        },
        {
            "question": "3. Durch welchen Winkel wird die Art des Spanes beeinflusst?",
            "choices": ["Spanwinkel - Gamma", "Freiwinkel - Alpha", "Keilwinkel - Beta"],
            "correct": ["Spanwinkel - Gamma"]
        },
        {
            "question": "4. Was ist die Grundform aller Werkzeugschneiden?",
            "choices": ["Der Keil", "Der Freiwinkel", "Der Spanwinkel", "Der Keilwinkel"],
            "correct": ["Der Keil"]
        },
        {
            "question": "5. Kreuzen Sie die zwei richtigen Aussagen an. Beim Anreissen...",
            "choices": [
                "a) wird die Anreissnadel immer am Stahlmass entlang geschoben.",
                "b) muss die Reissnadel mindestens zweimal am Lineal entlang gezogen werden.",
                "c) muss die Reissnadel moeglichst tief in den Werkstoff eindringen.",
                "d) richtet sich der Druck auf die Reissnadelspitze nach dem Werkstoff.",
                "e) wird die Reissnadel an der Unterkante des Lineals entlanggefuehrt.",
                "f) ist die Reissnadel gegen die Ziehrichtung geneigt."
            ],
            "correct": [
                "a) wird die Anreissnadel immer am Stahlmass entlang geschoben.",
                "f) ist die Reissnadel gegen die Ziehrichtung geneigt."
            ]
        },
        {
            "question": "6. In was fuer einer Einheit werden die Zaehnezahl und die Zahnteilung angegeben?",
            "choices": [
                "Zaehnezahl auf 1 Zoll -> Zaehne gezaehlt / Zahnteilung in mm",
                "Zaehnezahl in mm / Zahnteilung in Zoll",
                "Zaehnezahl pro cm / Zahnteilung in Grad"
            ],
            "correct": ["Zaehnezahl auf 1 Zoll -> Zaehne gezaehlt / Zahnteilung in mm"]
        },
        {
            "question": "7. Der Saegeschlitz beim Saegen mit der Handsaege wird stets breiter als das Saegeblatt dick ist. Kreuzen Sie die beiden richtigen Aussagen ueber den Zweck des Freischnitts an.",
            "choices": [
                "a) Der Saegeschnitt muss breiter als die Dicke des Saegeblatts sein, damit das Saegeblatt im Schlitz nicht klemmt.",
                "b) Zweck des breiteren Saegeschlitzes ist es, die Druckkraft auf das Saegeblatt verringern zu koennen.",
                "c) Der breitere Saegeschlitz entsteht durch geuebtes, schraeges Fuehren der Saege.",
                "d) Der breitere Saegeschlitz wird durch das gewellte bzw. geschraenkte Saegeblatt automatisch erzeugt."
            ],
            "correct": [
                "a) Der Saegeschnitt muss breiter als die Dicke des Saegeblatts sein, damit das Saegeblatt im Schlitz nicht klemmt.",
                "d) Der breitere Saegeschlitz wird durch das gewellte bzw. geschraenkte Saegeblatt automatisch erzeugt."
            ]
        },
        {
            "question": "8. In welcher Antwort (eine) sind ausschliesslich Anreisswerkzeuge aufgefuehrt?",
            "choices": [
                "Anreissnadel, Bogenmass, Anreissplatte",
                "Hoehenreisser, Anreisszirkel, Hammer",
                "Koerner, Anschlagwinkel, Hoehenreisser",
                "Anreissnadel, Stangenzirkel, Hoehenreisser"
            ],
            "correct": ["Anreissnadel, Stangenzirkel, Hoehenreisser"]
        },
        {
            "question": "9. Kreuzen Sie die richtige Aussage (eine) ueber die Anreissplatte an!",
            "choices": [
                "Die Anreissplatte wird wegen ihrer ebenen Oberflaeche vorzugsweise zum Richten von Halbzeugen benutzt.",
                "Die Anreissplatte dient zum Koernen und Meisseln duenner Werkstuecke.",
                "Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."
            ],
            "correct": ["Die Anreissplatte darf nur zum Anreissen and Messen benutzt werden."]
        },
        {
            "question": "10. Warum muss bei den letzten Hueben vor dem Durchsaegen des Werkstuecks der Druck auf das Saegeblatt verringert werden?",
            "choices": [
                "weil andernfalls das getrennte Werkstueck zu Boden faellt.",
                "damit der Schnitt nicht am Ende verlaeuft.",
                "damit Handverletzungen durch ein ploetzliches Abrutschen der Saege nach dem Durchsaegen vermieden werden."
            ],
            "correct": ["damit Handverletzungen durch ein ploetzliches Abrutschen der Saege nach dem Durchsaegen vermieden werden."]
        },
        {
            "question": "11. Wie wird ein Saegeschnitt am Werkstueck zweckmaessig angesaegt? Kreuzen Sie die beiden richtigen Antworten an.",
            "choices": [
                "a) Damit die Saege nicht seitlich verrutscht, wird die Saege beim Ansaegen so gefuehrt, dass kein Anstellwinkel entsteht.",
                "b) Das Feilen einer Fuehrungskerbe an der Schnittstelle vor dem Saegevorgang erleichtert das Ansaegen.",
                "c) Zum Ansaegen ist das Werkstueck so zu spannen, dass die Anreisslinie rechts vom Saegeblatt liegt.",
                "d) Das Einhalten eines kleinen Anstellwinkels traegt ebenfalls zu einem sicheren Ansaegen des Saegeschnitts bei."
            ],
            "correct": [
                "b) Das Feilen einer Fuehrungskerbe an der Schnittstelle vor dem Saegevorgang erleichtert das Ansaegen.",
                "d) Das Einhalten eines kleinen Anstellwinkels traegt ebenfalls zu einem sicheren Ansaegen des Saegeschnitts bei."
            ]
        },
        {
            "question": "12. Welche drei Aussagen sind zutreffend? Anreissen / Stahlmassstab / Reissnadel.",
            "choices": [
                "b) Der Stahlmassstab soll nicht verdreht und verbogen werden.",
                "c) Das Stahllineal dient als Fuehrung der Reissnadel beim Anreissen.",
                "f) Zum Anreissen von harten Werkstoffen werden Stahlreissnadeln mit gehaerteten Spitzen verwendet.",
                "g) Die Spitzen der Reissnadeln werden so schlank gefertigt, damit die Reissnadeln nicht als Koerner verwendet werden."
            ],
            "correct": [
                "b) Der Stahlmassstab soll nicht verdreht und verbogen werden.",
                "c) Das Stahllineal dient als Fuehrung der Reissnadel beim Anreissen.",
                "f) Zum Anreissen von harten Werkstoffen werden Stahlreissnadeln mit gehaerteten Spitzen verwendet."
            ]
        },
        {
            "question": "13. Welches Bild zeigt ein Saegeblatt mit geschraenkten Zaehnen?",
            "choices": ["Bild 1", "Bild 2", "Bild 3 (Zaehne abwechselnd nach links und rechts gebogen)", "Bild 4"],
            "correct": ["Bild 3 (Zaehne abwechselnd nach links und rechts gebogen)"]
        },
        {
            "question": "14. Welche drei der nachstehenden Behauptungen ueber das Koernen sind zutreffend?",
            "choices": [
                "a) Der Koerner wird leicht neben dem Anreisspunkt aufgesetzt...",
                "b) Die Handkante wird beim Aufsetzen des Koerners auf das Werkstueck gelegt, damit der Koerner sicherer gefuehrt werden kann.",
                "c) Der Koerner wird nach dem Aufsetzen aufgerichtet. Er muss dann senkrecht zur Werkstueckoberflaeche stehen.",
                "d) Damit der Koerner nicht zu tief in das Werkstueck eindringt, ist seine Spitze nicht gehaertet.",
                "e) Der Schlag mit dem Hammer muss genau in Richtung der Koernerachse erfolgen.",
                "f) Der Koerner muss genau senkrecht aufgesetzt werden... Die Hand soll dabei das Werkstueck nicht beruehren."
            ],
            "correct": [
                "b) Die Handkante wird beim Aufsetzen des Koerners auf das Werkstueck gelegt, damit der Koerner sicherer gefuehrt werden kann.",
                "c) Der Koerner wird nach dem Aufsetzen aufgerichtet. Er muss dann senkrecht zur Werkstueckoberflaeche stehen.",
                "e) Der Schlag mit dem Hammer muss genau in Richtung der Koernerachse erfolgen."
            ]
        },
        {
            "question": "15. Saegeblaetter werden aus unlegiertem Werkzeugstahl oder aus HSS hergestellt. Was bedeutet HSS?",
            "choices": ["Hochleistungsschnellarbeitsstahl (Hochleistungsschnellschnittstahl)", "Harter Spezial Stahl", "High Speed System"],
            "correct": ["Hochleistungsschnellarbeitsstahl (Hochleistungsschnellschnittstahl)"]
        },
        {
            "question": "16. Warum muessen duenne Werkstuecke flach und nicht hochkant eingespant werden?",
            "choices": ["Damit es nicht federt, die Saege nicht einhakt und die Saegezaehne nicht abbrechen.", "Um Material zu sparen.", "Damit der Schnitt schneller geht."],
            "correct": ["Damit es nicht federt, die Saege nicht einhakt und die Saegezaehne nicht abbrechen."]
        },
        {
            "question": "17. Welche zwei Arten von mechanischen Trennverfahren gibt es im Allgemeinen?",
            "choices": ["Spanen und Zerteilen", "Schneiden und Schmelzen", "Brechen und Saegen"],
            "correct": ["Spanen und Zerteilen"]
        },
        {
            "question": "18. Benenne die abgebildeten Trennverfahren (Reihenfolge laut Bild).",
            "choices": [
                "Saegen, Feilen, Bohren, Senken, Reiben, Innengewindeschneiden, Aussengewindeschneiden",
                "Feilen, Saegen, Senken, Bohren, Reiben",
                "Saegen, Feilen, Fraesen, Bohren"
            ],
            "correct": ["Saegen, Feilen, Bohren, Senken, Reiben, Innengewindeschneiden, Aussengewindeschneiden"]
        }
    ]

if "shuffled" not in st.session_state:
    q_list = list(st.session_state.quiz_data)
    random.shuffle(q_list)
    st.session_state.shuffled = q_list
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = []

st.title("🔧 Benteler Mechanics Trainer")
st.write("Kompletter Test mit allen 18 Fragen.")
st.markdown("---")

if st.session_state.current_idx < len(st.session_state.shuffled):
    q = st.session_state.shuffled[st.session_state.current_idx]
    st.subheader(f"Frage {st.session_state.current_idx + 1} von {len(st.session_state.shuffled)}")
    st.info(q["question"])
    
    is_multiple = len(q["correct"]) > 1
    user_answers = []
    
    if is_multiple:
        st.caption("ℹ️ Mehrere Antworten auswaehlen:")
        for choice in q["choices"]:
            if st.checkbox(choice, key=f"c_{st.session_state.current_idx}_{choice}"):
                user_answers.append(choice)
    else:
        st.caption("ℹ️ Eine Antwort auswaehlen:")
        selected_radio = st.radio("Optionen:", q["choices"], index=None, key=f"r_{st.session_state.current_idx}", label_visibility="collapsed")
        user_answers = [selected_radio] if selected_radio else []

    if not st.session_state.answered:
        if st.button("Antworten", type="primary", use_container_width=True):
            if not user_answers:
                st.warning("Bitte waehlen Sie eine Antwort aus!")
            else:
                st.session_state.answered = True
                st.session_state.selected = user_answers
                st.rerun()
    else:
        correct_set = set(q["correct"])
        user_set = set(st.session_state.selected)
        
        if user_set == correct_set:
            st.success("🟢 Richtig!")
            if f"sc_{st.session_state.current_idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"sc_{st.session_state.current_idx}"] = True
        else:
            st.error("🔴 Falsch!")
            st.write("**Richtige Antwort:**")
            for c in q["correct"]:
                st.write(f"✔️ {c}")
                
        if st.button("Naechste Frage ➡️", use_container_width=True):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.selected = []
            st.rerun()
else:
    st.success(f"🏁 Test beendet! Ihr Ergebnis: {st.session_state.score} von {len(st.session_state.shuffled)} richtig.")
    if st.button("Neu starten 🔄", use_container_width=True):
        del st.session_state.shuffled
        st.rerun()
