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
                "c) Der breitere Saegeschlitz entsteht durch geuebtes, schraeges Fuehren की Saege.",
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
            "correct": ["Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."]
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
                "f) Zum Anreissen von harten
