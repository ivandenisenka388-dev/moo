"""
TELKKO - Элемент сообщения в чате
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class MessageItem(MDBoxLayout):
    """Элемент сообщения в чате"""
    
    def __init__(self, message_data, **kwargs):
        super().__init__(**kwargs)
        self.message_data = message_data
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = dp(60)
        self.padding = dp(10)
        self.spacing = dp(10)
        
        self.build_ui()
    
    def build_ui(self):
        """Создание интерфейса сообщения"""
        is_outgoing = self.message_data.get('is_outgoing', False)
        
        if not is_outgoing:
            # Пустой spacer для выравнивания
            self.add_widget(MDBoxLayout(size_hint_x=0.2))
        
        # Контейнер сообщения
        msg_container = MDBoxLayout(
            orientation='vertical',
            size_hint_x=0.8,
            padding=dp(10),
            spacing=dp(5)
        )
        
        # Установка цвета фона
        with msg_container.canvas.before:
            if is_outgoing:
                Color(0.2, 0.5, 0.9, 1)  # Синий для своих
            else:
                Color(0.9, 0.9, 0.9, 1)  # Серый для чужих
            
            RoundedRectangle(
                size=msg_container.size,
                pos=msg_container.pos,
                radius=[dp(10)] * 4
            )
        
        # Текст сообщения
        text_color = (1, 1, 1, 1) if is_outgoing else (0, 0, 0, 1)
        
        text_label = MDLabel(
            text=self.message_data['text'],
            size_hint_y=None,
            height=dp(30),
            theme_text_color='Custom',
            text_color=text_color
        )
        msg_container.add_widget(text_label)
        
        # Время
        time_label = MDLabel(
            text=self.message_data['time'],
            font_style='Caption',
            size_hint_y=None,
            height=dp(20),
            halign='right',
            theme_text_color='Custom',
            text_color=(0.8, 0.8, 0.8, 1) if is_outgoing else (0.4, 0.4, 0.4, 1)
        )
        msg_container.add_widget(time_label)
        
        self.add_widget(msg_container)
        
        if is_outgoing:
            self.add_widget(MDBoxLayout(size_hint_x=0.2))
