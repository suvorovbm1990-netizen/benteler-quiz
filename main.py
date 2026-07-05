import streamlit as st
import random

# Настройка интерфейса под мобильный экран
st.set_page_config(page_title="Benteler Mechanics", page_icon="🔧", layout="centered")

# Полная база данных со всеми вашими вопросами
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = [
        {
            "question": "Was ist die Grundform aller Werkzeugschneiden?",
            "choices": ["Der Keil", "Der Freiwinkel", "Der Spanwinkel", "Der Keilwinkel"],
            "correct": ["Der Keil"]
        },
        {
            "question": "In welcher Antwort (eine) sind ausschliesslich Anreisswerkzeuge aufgefuehrt?",
            "choices": [
                "Anreissnadel, Bogenmass, Anreissplatte",
                "Hoehenreisser, Anreisszirkel, Hammer",
                "Koerner, Anschlagwinkel, Hoehenreisser",
                "Anreissnadel, Stangenzirkel, Hoehenreisser",
                "Messschieber, Hoehenreisser, Stahlmassstab"
            ],
            "correct": ["Anreissnadel, Stangenzirkel, Hoehenreisser"]
        },
        {
            "question": "Kreuzen Sie die richtige Aussage (eine) ueber die Anreissplatte an!",
            "choices": [
                "Die Anreissplatte wird wegen ihrer ebenen Oberflaeche vorzugsweise zum Richten von Halbzeugen benutzt.",
                "Die Anreissplatte dient zum Koernen und Meisseln duenner Werkstuecke.",
                "Weil die Anreissplatte stets sauber zu halten ist, ist sie die geeignete Unterlage zum Einstauchen der Feilenangel...",
                "Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."
            ],
            "correct": ["Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."]
        },
        {
            "question": "Warum muss bei den letzten Hueben vor dem Durchsaegen des Werkstuecks der Druck auf das Saegeblatt verringert werden?",
            "choices": [
                "weil andernfalls das getrennte Werkstueck zu Boden faellt.",
                "damit der Schnitt nicht am Ende verlaeuft.",
                "damit das Saegeblatt nicht zu warm wird.",
                "damit Handverletzungen durch ein ploetzliches Abrutschen der Saege nach dem Durchsaegen vermieden werden."
            ],
            "correct": ["damit Handverletzungen durch ein ploetzliches Abrutschen der Saege nach dem Durchsaegen vermieden werden."]
        },
        {
            "question": "Der Saegeschlitz beim Saegen mit der Handsaege wird stets breiter als das Saegeblatt dick ist. Kreuzen Sie die beiden richtigen Aussagen ueber den Zweck des Freischnitts an.",
            "choices": [
                "Der breitere Saegeschlitz wird durch das gewellte bzw. geschraenkte Saegeblatt automatisch erzeugt.",
                "Der breitere Saegeschlitz entsteht ausschliesslich durch falsche Fuehrung der Saege.",
                "Zweck des breiteren Saegeschlitzes ist es, die Druckkraft auf das Saegeblatt verringern zu koennen.",
                "Der breitere Saegeschlitz verhindert das Klemmen des Saegeblattes im Saegeschlitz."
            ],
            "correct": [
                "Der breitere Saegeschlitz wird durch das gewellte bzw. geschraenkte Saegeblatt automatisch erzeugt.",
                "Der breitere Saegeschlitz verhindert das Klemmen des Saegeblattes im Saegeschlitz."
            ]
        }
    ]

# Инициализация состояний викторины
if "shuffled" not in st.session_state:
    q_list = list(st.session_state.quiz_data)
    random.shuffle(q_list)
    st.session_state.shuffled = q_list
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = []

st.title("🔧 Benteler Mechanics Trainer")
st.write("Полный тренажёр тестов.")
st.markdown("---")

if st.session_state.current_idx < len(st.session_state.shuffled):
    q = st.session_state.shuffled[st.session_state.current_idx]
    st.subheader(f"Frage {st.session_state.current_idx + 1} von {len(st.session_state.shuffled)}")
    st.info(q["question"])
    
    # Проверяем тип вопроса (один правильный или несколько)
    is_multiple = len(q["correct"]) > 1
    
    if is_multiple:
        st.caption("ℹ️ Выберите НЕСКОЛЬКО вариантов ответа:")
        user_answers = []
        for choice in q["choices"]:
            if st.checkbox(choice, key=f"ch_{st.session_state.current_idx}_{choice}"):
                user_answers.append(choice)
    else:
        st.caption("ℹ️ Выберите ОДИН вариант ответа:")
        selected_radio = st.radio("Варианты:", q["choices"], index=None, key=f"rd_{st.session_state.current_idx}", label_visibility="collapsed")
        user_answers = [selected_radio] if selected_radio else []

    # Кнопка проверки
    if not st.session_state.answered:
        if st.button("Antworten (Ответить)", type="primary", use_container_width=True):
            if not user_answers:
                st.warning("Пожалуйста, выберите хотя бы один ответ!")
            else:
                st.session_state.answered = True
                st.session_state.selected = user_answers
                st.rerun()
    else:
        # Проверка результатов
        correct_set = set(q["correct"])
        user_set = set(st.session_state.selected)
        
        if user_set == correct_set:
            st.success("🟢 Richtig! (Верно)")
            if f"score_added_{st.session_state.current_idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"score_added_{st.session_state.current_idx}"] = True
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
    st.balloons()
    st.success(f"🏁 Тест полностью завершен! Ваш итоговый результат: {st.session_state.score} из {len(st.session_state.shuffled)} правильных ответов.")
    if st.button("Пройти заново 🔄", use_container_width=True):
        del st.session_state.shuffled
        st.rerun()
