"""
TELKKO - Экран входа
"""

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from database.db_manager import DatabaseManager
from utils.constants import BLUE_COLOR


class LoginScreen(Screen):
    """Экран входа в Telkko"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DatabaseManager()
        self.dialog = None
        self.build_ui()
    
    def build_ui(self):
        """Создание интерфейса"""
        layout = MDBoxLayout(
            orientation='vertical',
            padding=40,
            spacing=20,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Логотип
        logo_label = MDLabel(
            text='📱 TELKKO',
            font_style='H4',
            halign='center',
            size_hint_y=None,
            height=100,
            theme_text_color='Custom',
            text_color=BLUE_COLOR
        )
        layout.add_widget(logo_label)
        
        # Подзаголовок
        subtitle = MDLabel(
            text='Мессенджер как Telegram',
            font_style='Subtitle1',
            halign='center',
            size_hint_y=None,
            height=40
        )
        layout.add_widget(subtitle)
        
        # Поле логина
        self.login_input = MDTextField(
            hint_text='Телефон или логин',
            size_hint_y=None,
            height=56,
            mode='rectangle'
        )
        layout.add_widget(self.login_input)
        
        # Поле пароля
        self.password_input = MDTextField(
            hint_text='Пароль',
            password=True,
            size_hint_y=None,
            height=56,
            mode='rectangle'
        )
        layout.add_widget(self.password_input)
        
        # Кнопка входа
        login_btn = MDRaisedButton(
            text='ВОЙТИ',
            size_hint_y=None,
            height=50,
            md_bg_color=BLUE_COLOR
        )
        login_btn.bind(on_press=self.on_login)
        layout.add_widget(login_btn)
        
        # Кнопка регистрации
        register_btn = MDFlatButton(
            text='Нет аккаунта? Зарегистрироваться',
            size_hint_y=None,
            height=40,
            theme_text_color='Custom',
            text_color=BLUE_COLOR
        )
        register_btn.bind(on_press=self.go_to_register)
        layout.add_widget(register_btn)
        
        self.add_widget(layout)
    
    def on_login(self, instance):
        """Обработка входа"""
        login = self.login_input.text
        password = self.password_input.text
        
        if not login or not password:
            self.show_dialog('Ошибка', 'Заполните все поля')
            return
        
        user = self.db.get_user(login, password)
        
        if user:
            app = MDApp.get_running_app()
            app.current_user = user
            self.manager.current = 'chats'
        else:
            self.show_dialog('Ошибка', 'Неверный логин или пароль')
    
    def go_to_register(self, instance):
        """Переход на регистрацию"""
        self.manager.current = 'register'
    
    def show_dialog(self, title, text):
        """Показать диалог"""
        if self.dialog:
            self.dialog.dismiss()
        
        self.dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(
                    text='OK',
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()
