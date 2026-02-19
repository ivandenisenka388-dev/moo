"""
TELKKO - Экран контактов
"""

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp


class ContactsScreen(Screen):
    """Экран со списком контактов"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        """Создание интерфейса"""
        layout = MDBoxLayout(orientation='vertical')
        
        # Верхняя панель
        self.toolbar = MDTopAppBar(
            title='Контакты',
            left_action_items=[['arrow-left', lambda x: self.go_back()]],
            right_action_items=[['account-plus', lambda x: self.add_contact()]]
        )
        layout.add_widget(self.toolbar)
        
        # Список контактов
        scroll = ScrollView()
        contacts_list = MDList(spacing=dp(5))
        
        # Пример контактов
        contacts = [
            'Иван Петров',
            'Мария Иванова',
            'Алексей Сидоров',
            'Елена Козлова',
            'Дмитрий Смирнов'
        ]
        
        for contact in contacts:
            item = OneLineListItem(
                text=contact,
                on_release=lambda x, c=contact: self.open_chat(c)
            )
            contacts_list.add_widget(item)
        
        scroll.add_widget(contacts_list)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def open_chat(self, contact):
        """Открыть чат с контактом"""
        app = MDApp.get_running_app()
        app.current_chat = {'name': contact}
        self.manager.current = 'chat'
    
    def add_contact(self):
        """Добавить контакт"""
        pass
    
    def go_back(self):
        """Назад"""
        self.manager.current = 'chats'
