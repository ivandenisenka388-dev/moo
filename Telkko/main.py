"""
TELKKO - Главный файл приложения
"""

import os
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

# Импорт экранов
from screens.login_screen import LoginScreen
from screens.register_screen import RegisterScreen
from screens.chats_screen import ChatsScreen
from screens.chat_screen import ChatScreen
from screens.contacts_screen import ContactsScreen
from screens.profile_screen import ProfileScreen

# Импорт базы данных
from database.db_manager import DatabaseManager


class TelkkoApp(MDApp):
    """Главный класс приложения Telkko"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        self.current_user = None
        self.current_chat = None
        
    def build(self):
        """Создание интерфейса"""
        # Настройка темы (как в Telegram)
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = "500"
        
        # Создание менеджера экранов
        self.sm = ScreenManager()
        
        # Добавление экранов
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(RegisterScreen(name='register'))
        self.sm.add_widget(ChatsScreen(name='chats'))
        self.sm.add_widget(ChatScreen(name='chat'))
        self.sm.add_widget(ContactsScreen(name='contacts'))
        self.sm.add_widget(ProfileScreen(name='profile'))
        
        return self.sm
    
    def on_start(self):
        """При запуске"""
        print("✅ Telkko запущен!")
        
    def on_stop(self):
        """При остановке"""
        self.db.close()
        print("👋 Telkko остановлен")


if __name__ == "__main__":
    TelkkoApp().run()
