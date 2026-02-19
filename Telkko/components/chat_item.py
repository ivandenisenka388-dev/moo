"""
TELKKO - Элемент списка чатов
"""

from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class ChatItem(ButtonBehavior, MDCard):
    """Элемент чата в списке"""
    
    def __init__(self, chat_data, **kwargs):
        super().__init__(**kwargs)
        self.chat_data = chat_data
        self.orientation = 'horizontal'
        self.padding = dp(10)
        self.size_hint_y = None
        self.height = dp(70)
        self.radius = dp(10)
        
        self.build_ui()
    
    def build_ui(self):
        """Создание интерфейса элемента"""
        # Аватар
        avatar = MDLabel(
            text='👤',
            font_size=dp(30),
            size_hint_x=None,
            width=dp(50),
            halign='center'
        )
        self.add_widget(avatar)
        
        # Информация
        info_layout = MDBoxLayout(
            orientation='vertical',
            spacing=dp(5)
        )
        
        # Верхняя строка с именем и временем
        top_row = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(25)
        )
        
        name_label = MDLabel(
            text=self.chat_data['name'],
            font_style='Subtitle1',
            size_hint_x=0.7
        )
        top_row.add_widget(name_label)
        
        time_label = MDLabel(
            text=self.chat_data['time'],
            font_style='Caption',
            size_hint_x=0.3,
            halign='right'
        )
        top_row.add_widget(time_label)
        
        info_layout.add_widget(top_row)
        
        # Последнее сообщение
        msg_label = MDLabel(
            text=self.chat_data['last_message'],
            font_style='Body2',
            theme_text_color='Secondary'
        )
        info_layout.add_widget(msg_label)
        
        self.add_widget(info_layout)
        
        # Счетчик непрочитанных
        unread = self.chat_data.get('unread', 0)
        if unread > 0:
            unread_label = MDLabel(
                text=str(unread),
                size_hint=(None, None),
                size=(dp(24), dp(24)),
                halign='center',
                valign='middle'
            )
            
            with unread_label.canvas.before:
                Color(0.2, 0.5, 0.9, 1)
                RoundedRectangle(
                    size=unread_label.size,
                    pos=unread_label.pos,
                    radius=[dp(12)]
                )
            
            self.add_widget(unread_label)
