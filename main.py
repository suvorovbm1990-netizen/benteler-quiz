import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Полная база данных тестов по индустриальной механике (Benteler)
QUIZ_DATA = [
    {
        "question": "Was ist die Grundform aller Werkzeugschneiden?",
        "choices": ["Der Keil", "Der Freiwinkel", "Der Spanwinkel", "Der Keilwinkel"],
        "correct_choices": ["Der Keil"]
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
        "correct_choices": ["Anreissnadel, Stangenzirkel, Hoehenreisser"]
    },
    {
        "question": "Kreuzen Sie die richtige Aussage (eine) ueber die Anreissplatte an!",
        "choices": [
            "Die Anreissplatte wird wegen ihrer ebenen Oberflaeche vorzugsweise zum Richten von Halbzeugen benutzt.",
            "Die Anreissplatte dient zum Koernen und Meisseln duenner Werkstuecke.",
            "Weil die Anreissplatte stets sauber zu halten ist, ist sie die geeignete Unterlage zum Einstauchen der Feilenangel...",
            "Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."
        ],
        "correct_choices": ["Die Anreissplatte darf nur zum Anreissen und Messen benutzt werden."]
    },
    {
        "question": "Warum muss bei den letzten Hueben vor dem Durchsaegen des Werkstuecks der Druck auf das Saegeblatt verringert werden?",
        "choices": [
            "weil andernfalls das getrennte Werkstueck zu Boden faellt.",
            "damit der Schnitt nicht am Ende verlaeuft.",
            "damit das Saegeblatt nicht zu warm wird.",
            "damit Handverletzungen durch ein ploetzliches Abrutschen der Saege nach dem Durchsaegen vermieden werden."
        ],
        "correct_choices": ["damit Handverletzungen durch ein ploetzliches Abrutschen der Saege nach dem Durchsaegen vermieden werden."]
    },
    {
        "question": "Wie wird ein Saegeschnitt am Werkstueck zweckmaessig angesaegt? (Выберите ВСЕ правильные)",
        "choices": [
            "Damit die Saege nicht seitlich verrutscht, wird die Saege beim Ansaegen so gefuehrt, dass moeglichst kein Anstellwinkel...",
            "Das Feilen einer Fuehrungskerbe an der Schnittstelle vor dem Saegevorgang erleichtert das Ansaegen...",
            "Zum Ansaegen in das Werkstueck ist so zu spannen, dass die Anreisslinie rechts vom Saegeblatt liegt...",
            "Das Einhalten eines kleinen Anstellwinkels traegt देखील zu einem sicheren Ansaegen des Saegeschnitts bei.",
            "Das Ansaegen wird wesentlich erleichtert, wenn beim Rueckhub kraeftig auf das Saegeblatt gedrueckt wird..."
        ],
        "correct_choices": [
            "Das Feilen einer Fuehrungskerbe an der Schnittstelle vor dem Saegevorgang erleichtert das Ansaegen...",
            "Das Einhalten eines kleinen Anstellwinkels traegt देखील zu einem sicheren Ansaegen des Saegeschnitts bei."
        ]
    }
]

class BentelerQuizApp(App):
    def build(self):
        self.title = "Benteler Mechanics Trainer"
        self.questions = list(QUIZ_DATA)
        random.shuffle(self.questions)
        self.current_index = 0
        self.score = 0
        self.selected_choices = []

        # Главный контейнер приложения
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Скролл для длинных вопросов
        scroll = ScrollView(size_hint=(1, 0.3))
        self.question_label = Label(
            text="", 
            font_size='20sp', 
            text_size=(Window.width - 40, None), 
            halign='center', 
            valign='middle'
        )
        scroll.add_widget(self.question_label)
        self.main_layout.add_widget(scroll)

        # Контейнер для кнопок вариантов ответов
        self.choices_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.5))
        self.main_layout.add_widget(self.choices_layout)

        # Кнопка подтверждения ответа / перехода дальше
        self.action_button = Button(
            text="Antworten (Ответить)", 
            size_hint=(1, 0.12), 
            background_color=(0.1, 0.6, 0.8, 1),
            font_size='18sp'
        )
        self.action_button.bind(on_press=self.handle_action)
        self.main_layout.add_widget(self.action_button)

        self.load_question()
        return self.main_layout

    def load_question(self):
        self.selected_choices = []
        if self.current_index < len(self.questions):
            self.current_question = self.questions[self.current_index]
            self.question_label.text = f"Frage {self.current_index + 1}/{len(self.questions)}:\n\n{self.current_question['question']}"
            
            # Очищаем старые кнопки
            self.choices_layout.clear_widgets()
            
            # Перемешиваем варианты
            choices = list(self.current_question['choices'])
            random.shuffle(choices)
            
            # Создаем новые кнопки
            for choice in choices:
                btn = Button(
                    text=choice, 
                    background_color=(0.3, 0.3, 0.3, 1), 
                    text_size=(Window.width - 60, None),
                    halign='left',
                    valign='middle',
                    padding=(15, 10)
                )
                btn.bind(on_press=self.toggle_choice)
                self.choices_layout.add_widget(btn)
                
            self.action_button.text = "Antworten (Ответить)"
            self.action_button.background_color = (0.1, 0.6, 0.8, 1)
        else:
            # Конец теста
            self.question_label.text = f"🏆 Итог: {self.score} из {len(self.questions)} верно!"
            self.choices_layout.clear_widgets()
            self.action_button.text = "Neu starten (Заново)"
            self.action_button.background_color = (0.2, 0.8, 0.2, 1)

    def toggle_choice(self, instance):
        # Если это режим просмотра результатов, кнопки вариантов не кликаются
        if "Nächste" in self.action_button.text or "Neu starten" in self.action_button.text:
            return
            
        if instance.text in self.selected_choices:
            self.selected_choices.remove(instance.text)
            instance.background_color = (0.3, 0.3, 0.3, 1)
        else:
            self.selected_choices.append(instance.text)
            instance.background_color = (0.2, 0.5, 0.8, 1)

    def handle_action(self, instance):
        if "Neu starten" in instance.text:
            self.current_index = 0
            self.score = 0
            random.shuffle(self.questions)
            self.load_question()
            return

        if "Nächste" in instance.text:
            self.current_index += 1
            self.load_question()
            return

        if not self.selected_choices:
            return

        # Проверка ответов
        correct = set(self.current_question['correct_choices'])
        user = set(self.selected_choices)

        # Подсвечиваем кнопки результатов
        for btn in self.choices_layout.children:
            if btn.text in correct:
                btn.background_color = (0.2, 0.7, 0.2, 1)  # Зеленый — правильный
            elif btn.text in user and btn.text not in correct:
                btn.background_color = (0.8, 0.2, 0.2, 1)  # Красный — ваша ошибка

        if user == correct:
            self.score += 1
            instance.text = "Richtig! -> Nächste Frage"
            instance.background_color = (0.2, 0.7, 0.2, 1)
        else:
            instance.text = "Falsch! -> Nächste Frage"
            instance.background_color = (0.8, 0.2, 0.2, 1)

if __name__ == '__main__':
    BentelerQuizApp().run()