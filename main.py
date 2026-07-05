import streamlit as st
import random

st.set_page_config(page_title="Benteler Quiz", page_icon="🔧", layout="centered")

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = [
        {"question": "1. Benennen Sie die in der Zeichnung gekennzeichneten Groessen. (Alpha, Beta, Gamma, 1, 2, 3)", "choices": ["Freiwinkel, Keilwinkel, Spanwinkel, Spanflaeche, Freiflaeche, Schnittflaeche", "Spanwinkel, Keilwinkel, Freiwinkel, Freiflaeche, Spanflaeche, Schnittflaeche", "Keilwinkel, Freiwinkel, Spanwinkel, Schnittflaeche, Freiflaeche, Spanflaeche"], "correct": ["Freiwinkel, Keilwinkel, Spanwinkel, Spanflaeche, Freiflaeche, Schnittflaeche"]},
        {"question": "2. Welche drei Arten von Spanen koennen beim Spanen entstehen?", "choices": ["Fliessspan, Scherspan, Reissspan", "Langespan, Kurzespan, Reissspan", "Grobspan, Feinspan, Mittelspan"], "correct": ["Fliessspan, Scherspan, Reissspan"]},
        {"question": "3. Durch welchen Winkel wird die Art des Spanes beeinflusst?", "choices": ["Spanwinkel - Gamma", "Freiwinkel - Alpha", "Keilwinkel - Beta"], "correct": ["Spanwinkel - Gamma"]},
        {"question": "4. Was ist die Grundform aller Werkzeugschneiden?", "choices": ["Der Keil", "Der Freiwinkel", "Der Spanwinkel", "Der Keilwinkel"], "correct": ["Der Keil"]},
        {"question": "5. Kreuzen Sie die zwei richtigen Aussagen an. Beim Anreissen...", "choices": ["a) wird die Anreissnadel immer am Stahlmass entlang geschoben.", "b) muss die Reissnadel mindestens zweimal am Lineal entlang gezogen werden.", "c) muss die Reissnadel moeglichst tief in den Werkstoff eindringen.", "d) richtet sich der Druck auf die Reissnadelspitze nach dem Werkstoff.", "e) wird die Reissnadel an der Unterkante des Lineals entlanggefuehrt.", "f) is die Reissnadel gegen die Ziehrichtung geneigt."], "correct": ["a) wird die Anreissnadel immer am Stahlmass entlang geschoben.", "f) is die Reissnadel gegen die Ziehrichtung geneigt."]},
        {"question": "6. In was fuer einer Einheit werden die Zaehnezahl und die Zahnteilung angegeben?", "choices": ["Zaehnezahl auf 1 Zoll -> Zaehne gezaehlt / Zahnteilung in mm", "Zaehnezahl in mm / Zahnteilung in Zoll", "Zaehnezahl pro cm / Zahnteilung in Grad"], "correct": ["Zaehnezahl auf 1 Zoll -> Zaehne gezaehlt / Zahnteilung in mm"]},
        {"question": "7. Der Saegeschlitz beim Saegen mit der Handsaege wird stets breiter als das Saegeblatt dick ist. Zweck des Freischnitts:", "choices": ["a) Der Saegeschnitt muss breiter sein, damit das Saegeblatt не klemmt.", "b) Zweck ist es, die Druckkraft на Saegeblatt verringern zu koennen.", "c) Der breitere Saegeschlitz entsteht durch schraeges Fuehren.", "d) Der breitere Saegeschlitz wird durch das gewellte bzw. geschraenkte Saegeblatt автоматически erzeugt."], "correct": ["a) Der Saegeschnitt muss breiter sein, damit das Saegeblatt не klemmt.", "d) Der breitere Saegeschlitz wird durch das gewellte bzw. geschraenkte Saegeblatt автоматически erzeugt."]},
        {"question": "8. In welcher Antwort (eine) sind ausschliesslich Anreisswerkzeuge aufgefuehrt?", "choices": ["Anreissnadel, Bogenmass, Anreissplatte", "Hoehenreisser, Anreisszirkel, Hammer", "Koerner, Anschlagwinkel, Hoehenreisser", "Anreissnadel, Stangenzirkel, Hoehenreisser"], "correct": ["Anreissnadel, Stangenzirkel, Hoehenreisser"]},
        {"question": "9. Kreuzen Sie die richtige Aussage (eine) ueber die Anreissplatte an!", "choices": ["Die Anreissplatte wird vorzugsweise zum Richten von Halbzeugen benutzt.", "Die Anreissplatte dient zum Koernen und Meisseln.", "Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."], "correct": ["Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."]},
        {"question": "10. Warum muss bei den letzten Hueben vor dem Durchsaegen der Druck verringert werden?", "choices": ["weil andernfalls das Werkstueck zu Boden faellt.", "damit der Schnitt не am Ende verlaeuft.", "damit Handverletzungen durch ein ploetzliches Abrutschen vermieden werden."], "correct": ["damit Handverletzungen durch ein ploetzliches Abrutschen vermieden werden."]},
        {"question": "11. Wie wird ein Saegeschnitt am Werkstueck zweckmaessig angesaegt?", "choices": ["a) Damit die Saege не seitlich verrutscht, kein Anstellwinkel.", "b) Das Feilen einer Fuehrungskerbe erleichtert das Ansaegen.", "c) Anreisslinie rechts vom Saegeblatt.", "d) Das Einhalten eines kleinen Anstellwinkels traegt zu sicherem Ansaegen bei."], "correct": ["b) Das Feilen einer Fuehrungskerbe erleichtert das Ansaegen.", "d) Das Einhalten одного kleinen Anstellwinkels traegt zu sicherem Ansaegen bei."]},
        {"question": "12. Welche drei Aussagen sind zutreffend? Anreissen / Stahlmassstab / Reissnadel.", "choices": ["b) Der Stahlmassstab soll не verdreht und verbogen werden.", "c) Das Stahllineal dient als Fuehrung der Reissnadel beim Anreissen.", "f) Zum Anreissen von harten Werkstoffen werden Reissnadeln mit gehaerteten Spitzen verwendet.", "g) Spitzen не для Koerner."], "correct": ["b) Der Stahlmassstab soll не verdreht und verbogen werden.", "c) Das Stahllineal dient als Fuehrung der Reissnadel beim Anreissen.", "f) Zum Anreissen von harten Werkstoffen werden Reissnadeln mit gehaerteten Spitzen verwendet."]},
        {"question": "13. Welches Bild zeigt ein Saegeblatt mit geschraenkten Zaehnen?", "choices": ["Bild 1", "Bild 2", "Bild 3 (Zaehne abwechselnd nach links und rechts gebogen)", "Bild 4"], "correct": ["Bild 3 (Zaehne abwechselnd nach links und rechts gebogen)"]},
        {"question": "14. Welche drei Behauptungen ueber das Koernen sind zutreffend?", "choices": ["b) Die Handkante wird beim Aufsetzen на Werkstueck gelegt, fuer sichere Fuehrung.", "c) Der Koerner wird nach dem Aufsetzen aufgerichtet. Er muss senkrecht stehen.", "e) Der Schlag mit dem Hammer muss genau in Richtung der Koernerachse erfolgen."], "correct": ["b) Die Handkante wird beim Aufsetzen на Werkstueck gelegt, fuer sichere Fuehrung.", "c) Der Koerner wird nach dem Aufsetzen aufgerichtet. Er muss senkrecht stehen.", "e) Der Schlag mit dem Hammer muss genau in Richtung der Koernerachse erfolgen."]},
        {"question": "15. Saegeblaetter werden aus unlegiertem Werkzeugstahl oder aus HSS hergestellt. Was bedeutet HSS?", "choices": ["Hochleistungsschnellarbeitsstahl (Hochleistungsschnellschnittstahl)", "Harter Spezial Stahl", "High Speed System"], "correct": ["Hochleistungsschnellarbeitsstahl (Hochleistungsschnellschnittstahl)"]},
        {"question": "16. Warum muessen duenne Werkstuecke flach und не hochkant eingespant werden?", "choices": ["Damit es не federt, die Saege не einhakt und die Saegezaehne не abbrechen.", "Um Material zu sparen.", "Damit der Schnitt schneller geht."], "correct": ["Damit es не federt, die Saege не einhakt und die Saegezaehne не abbrechen."]},
        {"question": "17. Welche zwei Arten von mechanischen Trennverfahren gibt es im Allgemeinen?", "choices": ["Spanen und Zerteilen", "Schneiden und Schmelzen", "Brechen und Saegen"], "correct": ["Spanen und Zerteilen"]},
        {"question": "18. Benenne die abgebildeten Trennverfahren (Reihenfolge laut Bild).", "choices": ["Saegen, Feilen, Bohren, Senken, Reiben, Innengewindeschneiden, Aussengewindeschneiden", "Feilen, Saegen, Senken, Bohren, Reiben", "Saegen, Feilen, Fraesen, Bohren"], "correct": ["Saegen, Feilen, Bohren, Senken, Reiben, Innengewindeschneiden, Aussengewindeschneiden"]}
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
st.write("Полный тренажёр из 18 вопросов.")
st.markdown("---")

if st.session_state.current_idx < len(st.session_state.shuffled):
    q = st.session_state.shuffled[st.session_state.current_idx]
    st.subheader(f"Frage {st.session_state.current_idx + 1} von {len(st.session_state.shuffled)}")
    st.info(q["question"])
    
    is_multiple = len(q["correct"]) > 1
    user_answers = []
    
    if is_multiple:
        st.caption("ℹ️ Выберите НЕСКОЛЬКО вариантов:")
        for choice in q["choices"]:
            if st.checkbox(choice, key=f"c_{st.session_state.current_idx}_{choice}"):
                user_answers.append(choice)
    else:
        st.caption("ℹ️ Выберите ОДИН вариант:")
        selected_radio = st.radio("Варианты:", q["choices"], index=None, key=f"r_{st.session_state.current_idx}", label_visibility="collapsed")
        user_answers = [selected_radio] if selected_radio else []

    if not st.session_state.answered:
        if st.button("Antworten (Ответить)", type="primary", use_container_width=True):
            if not user_answers:
                st.warning("Пожалуйста, выберите ответ!")
            else:
                st.session_state.answered = True
                st.session_state.selected = user_answers
                st.rerun()
    else:
        correct_set = set(q["correct"])
        user_set = set(st.session_state.selected)
        
        if user_set == correct_set:
            st.success("🟢 Richtig! (Верно)")
            if f"sc_{st.session_state.current_idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"sc_{st.session_state.current_idx}"] = True
        else:
            st.error("🔴 Falsch! (Неверно)")
            st.write("**Правильный ответ:**")
            for c in q["correct"]:
                st.write(f"✔️ {c}")
                
        if st.button("Nächste Frage (Дальше) ➡️", use_container_width=True):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.selected = []
            st.rerun()
else:
    st.success(f"🏁 Отлично! Результат: {st.session_state.score} из {len(st.session_state.shuffled)} правильных.")
    if st.button("Запустить заново 🔄", use_container_width=True):
        del st.session_state.shuffled
        st.rerun()
