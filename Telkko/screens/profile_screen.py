"""
TELKKO - Экран профиля
"""

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton


class ProfileScreen(Screen):
    """Экран профиля пользователя"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        """Создание интерфейса"""
        layout = MDBoxLayout(orientation='vertical')
        
        # Верхняя панель
        toolbar = MDTopAppBar(
            title='Профиль',
            left_action_items=[['arrow-left', lambda x: self.go_back()]]
        )
        layout.add_widget(toolbar)
        
        # Контент
        content = MDBoxLayout(
            orientation='vertical',
            padding=40,
            spacing=20,
            size_hint_y=None,
            height=300,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Аватар
        avatar = MDLabel(
            text='👤',
            font_style='H2',
            halign='center',
            size_hint_y=None,
            height=100
        )
        content.add_widget(avatar)
        
        # Информация о пользователе
        app = MDApp.get_running_app()
        if app.current_user:
            name_label = MDLabel(
                text=f"Имя: {app.current_user['name']}",
                halign='center'
            )
            content.add_widget(name_label)
            
            phone_label = MDLabel(
                text=f"Телефон: {app.current_user['phone']}",
                halign='center'
            )
            content.add_widget(phone_label)
        
        # Кнопка настроек
        settings_btn = MDRaisedButton(
            text='НАСТРОЙКИ',
            size_hint_y=None,
            height=50,
            pos_hint={'center_x': 0.5}
        )
        content.add_widget(settings_btn)
        
        # Кнопка выхода
        logout_btn = MDFlatButton(
            text='ВЫЙТИ',
            size_hint_y=None,
            height=40,
            theme_text_color='Error'
        )
        logout_btn.bind(on_press=self.logout)
        content.add_widget(logout_btn)
        
        layout.add_widget(content)
        self.add_widget(layout)
    
    def logout(self, instance):
        """Выход из аккаунта"""
        app = MDApp.get_running_app()
        app.current_user = None
        self.manager.current = 'login'
    
    def go_back(self):
        """Назад"""
        self.manager.current = 'chats'
