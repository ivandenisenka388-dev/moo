"""
TELKKO - Экран чата
"""

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList
from kivy.metrics import dp
from components.message_item import MessageItem
from datetime import datetime


class ChatScreen(Screen):
    """Экран чата"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.messages = []
        self.build_ui()
    
    def on_enter(self):
        """При входе в чат"""
        app = MDApp.get_running_app()
        if app.current_chat:
            self.toolbar.title = app.current_chat['name']
            self.load_messages()
    
    def build_ui(self):
        """Создание интерфейса"""
        layout = MDBoxLayout(orientation='vertical')
        
        # Верхняя панель
        self.toolbar = MDTopAppBar(
            title='Чат',
            left_action_items=[['arrow-left', lambda x: self.go_back()]],
            right_action_items=[
                ['phone', lambda x: self.call()],
                ['video', lambda x: self.video_call()],
                ['dots-vertical', lambda x: self.options()]
            ]
        )
        layout.add_widget(self.toolbar)
        
        # Область сообщений
        self.scroll = ScrollView()
        self.messages_list = MDList(
            spacing=dp(10),
            padding=[dp(10), dp(10)]
        )
        self.scroll.add_widget(self.messages_list)
        layout.add_widget(self.scroll)
        
        # Нижняя панель ввода
        bottom_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(60),
            padding=[dp(5), dp(5), dp(5), dp(5)],
            spacing=dp(5)
        )
        
        # Кнопка вложений
        attach_btn = MDIconButton(
            icon='attachment',
            size_hint_x=None,
            width=dp(48)
        )
        attach_btn.bind(on_press=self.attach_file)
        bottom_layout.add_widget(attach_btn)
        
        # Поле ввода
        self.message_input = MDTextField(
            hint_text='Сообщение...',
            size_hint_x=0.7,
            height=dp(48),
            mode='rectangle'
        )
        bottom_layout.add_widget(self.message_input)
        
        # Кнопка отправки
        send_btn = MDIconButton(
            icon='send',
            size_hint_x=None,
            width=dp(48)
        )
        send_btn.bind(on_press=self.send_message)
        bottom_layout.add_widget(send_btn)
        
        layout.add_widget(bottom_layout)
        self.add_widget(layout)
    
    def load_messages(self):
        """Загрузка сообщений"""
        self.messages_list.clear_widgets()
        
        # Пример сообщений
        messages = [
            {
                'text': 'Привет!',
                'time': '14:30',
                'is_outgoing': False,
                'status': 'read'
            },
            {
                'text': 'Здарова! Как дела?',
                'time': '14:31',
                'is_outgoing': True,
                'status': 'read'
            },
            {
                'text': 'Нормально, у тебя?',
                'time': '14:32',
                'is_outgoing': False,
                'status': 'delivered'
            }
        ]
        
        for msg in messages:
            item = MessageItem(message_data=msg)
            self.messages_list.add_widget(item)
        
        # Прокрутка вниз
        Clock.schedule_once(lambda dt: self.scroll.scroll_y(0), 0.1)
    
    def send_message(self, instance):
        """Отправка сообщения"""
        text = self.message_input.text.strip()
        if not text:
            return
        
        # Добавление сообщения
        msg = {
            'text': text,
            'time': datetime.now().strftime('%H:%M'),
            'is_outgoing': True,
            'status': 'sent'
        }
        item = MessageItem(message_data=msg)
        self.messages_list.add_widget(item)
        
        self.message_input.text = ''
        
        # Прокрутка вниз
        Clock.schedule_once(lambda dt: self.scroll.scroll_y(0), 0.1)
    
    def attach_file(self, instance):
        """Прикрепить файл"""
        pass
    
    def call(self):
        """Звонок"""
        pass
    
    def video_call(self):
        """Видеозвонок"""
        pass
    
    def options(self):
        """Опции чата"""
        pass
    
    def go_back(self):
        """Назад к списку чатов"""
        self.manager.current = 'chats'
