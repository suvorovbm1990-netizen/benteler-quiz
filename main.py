import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Полная база данных тестов по промышленной механике (Benteler)
QUIZ_DATA = [
    {
        "question": "1. Benennen Sie die in der Zeichnung gekennzeichneten Groessen.\n(Alpha, Beta, Gamma, 1, 2, 3)",
        "choices": [
            "Freiwinkel, Keilwinkel, Spanwinkel, Spanflaeche, Freiflaeche, Schnittflaeche",
            "Spanwinkel, Keilwinkel, Freiwinkel, Freiflaeche, Spanflaeche, Schnittflaeche",
            "Keilwinkel, Freiwinkel, Spanwinkel, Schnittflaeche, Freiflaeche, Spanflaeche"
        ],
        "correct_choices": ["Freiwinkel, Keilwinkel, Spanwinkel, Spanflaeche, Freiflaeche, Schnittflaeche"]
    },
    {
        "question": "2. Welche drei Arten von Spanen koennen beim Spanen entstehen?",
        "choices": ["Fliessspan, Scherspan, Reissspan", "Langespan, Kurzespan, Reissspan", "Grobspan, Feinspan, Mittelspan"],
        "correct_choices": ["Fliessspan, Scherspan, Reissspan"]
    },
    {
        "question": "3. Durch welchen Winkel wird die Art des Spanes beeinflusst?",
        "choices": ["Spanwinkel - Gamma", "Freiwinkel - Alpha", "Keilwinkel - Beta"],
        "correct_choices": ["Spanwinkel - Gamma"]
    },
    {
        "question": "4. Was ist die Grundform aller Werkzeugschneiden?",
        "choices": ["Der Keil", "Der Freiwinkel", "Der Spanwinkel", "Der Keilwinkel"],
        "correct_choices": ["Der Keil"]
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
        "correct_choices": [
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
        "correct_choices": ["Zaehnezahl auf 1 Zoll -> Zaehne gezaehlt / Zahnteilung in mm"]
    },
    {
        "question": "7. Der Saegeschlitz beim Saegen mit der Handsaege wird stets breiter als das Saegeblatt dick ist. Kreuzen Sie die beiden richtigen Aussagen ueber den Zweck des Freischnitts an.",
        "choices": [
            "a) Der Saegeschnitt muss breiter als die Dicke des Saegeblatts sein, damit das Saegeblatt im Schlitz не klemmt.",
            "b) Zweck des breiteren Saegeschlitzes ist es, die Druckkraft auf das Saegeblatt verringern zu koennen.",
            "c) Der breitere Saegeschlitz entsteht durch geuebtes, schraeges Fuehren der Saege.",
            "d) Der breitere Saegeschlitz wird durch das gewellte bzw. geschraenkte Saegeblatt automatisch erzeugt.",
            "e) Der breitere Saegeschlitz entsteht ausschliesslich durch falsche Fuehrung."
        ],
        "correct_choices": [
            "a) Der Saegeschnitt muss breiter als die Dicke des Saegeblatts sein, damit das Saegeblatt im Schlitz не klemmt.",
            "d) Der breitere Saegeschlitz wird durch das gewellte bzw. geschraenkte Saegeblatt automatisch erzeugt."
        ]
    },
    {
        "question": "8. In welcher Antwort (eine) sind ausschliesslich Anreisswerkzeuge aufgefuehrt?",
        "choices": [
            "Anreissnadel, Bogenmass, Anreissplatte",
            "Hoehenreisser, Anreisszirkel, Hammer",
            "Koerner, Anschlagwinkel, Hoehenreisser",
            "Anreissnadel, Stangenzirkel, Hoehenreisser",
            "Messschieber, Hoehenreisser, Stahlmassstab"
        ],
        "correct_choices": ["Anreissnadel, Stangenzirkel, Hoehenreisser"]
    },
    {
        "question": "9. Kreuzen Sie die richtige Aussage (eine) ueber die Anreissplatte an!",
        "choices": [
            "Die Anreissplatte wird wegen ihrer ebenen Oberflaeche vorzugsweise zum Richten von Halbzeugen benutzt.",
            "Die Anreissplatte dient zum Koernen und Meisseln duenner Werkstuecke.",
            "Weil die Anreissplatte stets sauber zu halten ist, ist sie die geeignete Unterlage zum Einstauchen...",
            "Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."
        ],
        "correct_choices": ["Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."]
    },
    {
        "question": "10. Warum muss bei den letzten Hueben vor dem Durchsaegen des Werkstuecks der Druck auf das Saegeblatt verringert werden?",
        "choices": [
            "weil andernfalls das getrennte Werkstueck zu Boden faellt.",
            "damit der Schnitt не am Ende verlaeuft.",
            "damit das Saegeblatt не zu warm wird.",
            "damit Handverletzungen durch ein ploetzliches Abrutschen der Saege nach dem Durchsaegen vermieden werden."
        ],
        "correct_choices": ["damit Handverletzungen durch ein ploetzliches Abrutschen der Saege nach dem Durchsaegen vermieden werden."]
    },
    {
        "question": "11. Wie wird ein Saegeschnitt am Werkstueck zweckmaessig angesaegt? Kreuzen Sie die beiden richtigen Antworten an.",
        "choices": [
            "a) Damit die Saege не seitlich verrutscht, wird die Saege beim Ansagen so gefuehrt, dass moeglichst kein Anstellwinkel entsteht.",
            "b) Das Feilen einer Fuehrungskerbe an der Schnittstelle vor dem Saegevorgang erleichtert das Ansaegen.",
            "c) Zum Ansaegen in das Werkstueck ist so zu spannen, dass die Anreisslinie rechts vom Saegeblatt liegt.",
            "d) Das Einhalten eines kleinen Anstellwinkels traegt ebenfalls zu einem sicheren Ansaegen des Saegeschnitts bei.",
            "e) Das Ansaegen wird wesentlich erleichtert, wenn beim Rueckhub kraeftig auf das Saegeblatt gedrueckt wird."
        ],
        "correct_choices": [
            "b) Das Feilen einer Fuehrungskerbe an der Schnittstelle vor dem Saegevorgang erleichtert das Ansaegen.",
            "d) Das Einhalten eines kleinen Anstellwinkels traegt ebenfalls zu einem sicheren Ansaegen des Saegeschnitts bei."
        ]
    },
    {
        "question": "12. Welche drei Aussagen sind zutreffend? Anreissen / Stahlmassstab / Reissnadel.",
        "choices": [
            "a) Der Stahlmassstab kann notfalls auch als Schraubendreher verwendet werden.",
            "b) Der Stahlmassstab soll не verdreht und verbogen werden.",
            "c) Das Stahllineal dient als Fuehrung der Reissnadel beim Anreissen.",
            "d) Der lange, flache Schenkel des Anschlagwinkels darf не als Fuehrung benutzt werden.",
            "e) Damit die Reissnadel не zu tief eindringt, ist ihre Spitze abgerundet.",
            "f) Zum Anreissen von harten Werkstoffen werden Stahlreissnadeln mit gehaerteten Spitzen verwendet.",
            "g) Die Spitzen der Reissnadeln werden so schlank gefertigt, damit die Reissnadeln не als Koerner verwendet werden."
        ],
        "correct_choices": [
            "b) Der Stahlmassstab soll не verdreht und verbogen werden.",
            "c) Das Stahllineal dient als Fuehrung der Reissnadel beim Anreissen.",
            "f) Zum Anreissen von harten Werkstoffen werden Stahlreissnadeln mit gehaerteten Spitzen verwendet."
        ]
    },
    {
        "question": "13. Welches Bild zeigt ein Saegeblatt mit geschraenkten Zaehnen?",
        "choices": ["Bild 1", "Bild 2", "Bild 3 (Zaehne abwechselnd nach links und rechts gebogen)", "Bild 4", "Bild 5"],
        "correct_choices": ["Bild 3 (Zaehne abwechselnd nach links und rechts gebogen)"]
    },
    {
        "question": "14. Welche drei der nachstehenden Behauptungen ueber das Koernen sind zutreffend?",
        "choices": [
            "a) Der Koerner wird leicht neben dem Anreisspunkt aufgesetzt...",
            "b) Die Handkante wird beim Aufsetzen des Koerners auf das Werkstueck gelegt, damit der Koerner sicherer gefuehrt werden kann.",
            "c) Der Koerner wird nach dem Aufsetzen aufgerichtet. Er muss dann senkrecht zur Werkstueckoberflaeche stehen.",
            "d) Damit der Koerner не zu tief in das Werkstueck eindringt, ist seine Spitze не gehaertet.",
            "e) Der Schlag mit dem Hammer muss genau in Richtung der Koernerachse erfolgen...",
            "f) Der Koerner muss genau senkrecht aufgesetzt werden... Die Hand soll dabei das Werkstueck не beruehren."
        ],
        "correct_choices": [
            "b) Die Handkante wird beim Aufsetzen des Koerners auf das Werkstueck gelegt, damit der Koerner sicherer gefuehrt werden kann.",
            "c) Der Koerner wird nach dem Aufsetzen aufgerichtet. Er muss dann senkrecht zur Werkstueckoberflaeche stehen.",
            "e) Der Schlag mit dem Hammer muss genau in Richtung der Koernerachse erfolgen..."
        ]
    },
    {
        "question": "15. Saegeblaetter werden aus unlegiertem Werkzeugstahl oder aus HSS hergestellt. Was bedeutet HSS?",
        "choices": ["Hochleistungsschnellarbeitsstahl (Hochleistungsschnellschnittstahl)", "Harter Spezial Stahl", "High Speed System"],
        "correct_choices": ["Hochleistungsschnellarbeitsstahl (Hochleistungsschnellschnittstahl)"]
    },
    {
        "question": "16. Warum muessen duenne Werkstuecke flach und не hochkant eingespant werden?",
        "choices": [
            "Damit es не federt, die Saege не einhakt und die Saegezaehne не abbrechen.",
            "Um Material zu sparen.",
            "Damit der Schnitt schneller geht."
        ],
        "correct_choices": ["Damit es не federt, die Saege не einhakt und die Saegezaehne не abbrechen."]
    },
    {
        "question": "17. Welche zwei Arten von mechanischen Trennverfahren gibt es im Allgemeinen?",
        "choices": ["Spanen und Zerteilen", "Schneiden und Schmelzen", "Brechen und Saegen"],
        "correct_choices": ["Spanen und Zerteilen"]
    },
    {
        "question": "18. Benenne die abgebildeten Trennverfahren (Reihenfolge laut Bild).",
        "choices": [
            "Saegen, Feilen, Bohren, Senken, Reiben, Innengewindeschneiden, Aussengewindeschneiden",
            "Feilen, Saegen, Senken, Bohren, Reiben, Aussengewindeschneiden, Innengewindeschneiden",
            "Saegen, Feilen, Fraesen, Bohren, Reiben, Drehen, Schleifen"
        ],
        "correct_choices": ["Saegen, Feilen, Bohren, Senken, Reiben, Innengewindeschneiden, Aussengewindeschneiden"]
    }
]

class BentelerQuizApp(App):
    def build(self):
        self.questions = list(QUIZ_DATA)
        random.shuffle(self.questions)
        self.current_index = 0
        self.score = 0
        self.selected_buttons = []
        
        self.main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        self.question_label = Label(
            text="", 
            size_hint_y=None, 
            text_size=(Window.width - 30, None),
            halign='center',
            valign='middle',
            font_size='16sp'
        )
        self.question_label.bind(texture_size=self.question_label.setter('size'))
        self.main_layout.add_widget(self.question_label)
        
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.choices_layout = BoxLayout(orientation='vertical', spacing=8, size_hint_y=None)
        self.choices_layout.bind(minimum_height=self.choices_layout.setter('height'))
        self.scroll_view.add_widget(self.choices_layout)
        self.main_layout.add_widget(self.scroll_view)
        
        self.action_btn = Button(text="Antworten (Ответить)", size_hint_y=None, height=50, background_color=(0.1, 0.5, 0.8, 1))
        self.action_btn.bind(on_press=self.handle_action)
        self.main_layout.add_widget(self.action_btn)
        
        self.load_question()
        return self.main_layout

    def load_question(self):
        self.selected_buttons = []
        self.choices_layout.clear_widgets()
        
        if self.current_index < len(self.questions):
            q = self.questions[self.current_index]
            self.question_label.text = f"Frage {self.current_index + 1}/{len(self.questions)}\n\n{q['question']}"
            self.action_btn.text = "Antworten (Ответить)"
            self.action_btn.background_color = (0.1, 0.5, 0.8, 1)
            
            for choice in q['choices']:
                btn = Button(
                    text=choice, 
                    size_hint_y=None, 
                    height=60,
                    text_size=(Window.width - 40, None),
                    halign='left',
                    valign='middle',
                    padding=(10, 5)
                )
                btn.bind(on_press=self.select_choice)
                self.choices_layout.add_widget(btn)
        else:
            self.question_label.text = f"🏁 Вы прошли весь тест!\nВаш результат: {self.score} из {len(self.questions)}"
            self.action_btn.text = "Wiederholen (Заново)"
            self.action_btn.background_color = (0.2, 0.7, 0.2, 1)

    def select_choice(self, instance):
        if self.action_btn.text != "Antworten (Ответить)":
            return
            
        if instance in self.selected_buttons:
            self.selected_buttons.remove(instance)
            instance.background_color = (1, 1, 1, 1)
        else:
            self.selected_buttons.append(instance)
            instance.background_color = (0.7, 0.8, 1, 1)

    def handle_action(self, instance):
        if self.action_btn.text == "Wiederholen (Заново)":
            self.current_index = 0
            self.score = 0
            random.shuffle(self.questions)
            self.load_question()
            return
            
        if self.action_btn.text == "Naechste Frage (Дальше)":
            self.current_index += 1
            self.load_question()
            return
            
        if not self.selected_buttons:
            return
            
        q = self.questions[self.current_index]
        user_answers = set([btn.text for btn in self.selected_buttons])
        correct_answers = set(q['correct_choices'])
        
        for btn in self.choices_layout.children:
            if btn.text in correct_answers:
                btn.background_color = (0.2, 0.7, 0.2, 1)
            elif btn.text in user_answers:
                btn.background_color = (0.8, 0.2, 0.2, 1)
                
        if user_answers == correct_answers:
            self.score += 1
            self.action_btn.text = "Richtig! -> Naechste Frage (Дальше)"
            self.action_btn.background_color = (0.2, 0.7, 0.2, 1)
        else:
            self.action_btn.text = "Falsch! -> Naechste Frage (Дальше)"
            self.action_btn.background_color = (0.8, 0.2, 0.2, 1)
            
        self.action_btn.text = "Naechste Frage (Дальше)"

if __name__ == '__main__':
    BentelerQuizApp().run()
