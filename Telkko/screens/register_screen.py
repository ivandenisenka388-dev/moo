"""
TELKKO - Экран регистрации
"""

from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from database.db_manager import DatabaseManager
from utils.constants import BLUE_COLOR


class RegisterScreen(Screen):
    """Экран регистрации Telkko"""
    
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
            spacing=15,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Заголовок
        title = MDLabel(
            text='Регистрация в Telkko',
            font_style='H5',
            halign='center',
            size_hint_y=None,
            height=80
        )
        layout.add_widget(title)
        
        # Поля ввода
        self.name_input = MDTextField(
            hint_text='Имя',
            size_hint_y=None,
            height=56,
            mode='rectangle'
        )
        layout.add_widget(self.name_input)
        
        self.phone_input = MDTextField(
            hint_text='Телефон',
            size_hint_y=None,
            height=56,
            mode='rectangle'
        )
        layout.add_widget(self.phone_input)
        
        self.login_input = MDTextField(
            hint_text='Логин',
            size_hint_y=None,
            height=56,
            mode='rectangle'
        )
        layout.add_widget(self.login_input)
        
        self.password_input = MDTextField(
            hint_text='Пароль',
            password=True,
            size_hint_y=None,
            height=56,
            mode='rectangle'
        )
        layout.add_widget(self.password_input)
        
        self.confirm_input = MDTextField(
            hint_text='Подтвердите пароль',
            password=True,
            size_hint_y=None,
            height=56,
            mode='rectangle'
        )
        layout.add_widget(self.confirm_input)
        
        # Кнопка регистрации
        register_btn = MDRaisedButton(
            text='ЗАРЕГИСТРИРОВАТЬСЯ',
            size_hint_y=None,
            height=50,
            md_bg_color=BLUE_COLOR
        )
        register_btn.bind(on_press=self.on_register)
        layout.add_widget(register_btn)
        
        # Кнопка назад
        back_btn = MDFlatButton(
            text='Назад',
            size_hint_y=None,
            height=40
        )
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def on_register(self, instance):
        """Обработка регистрации"""
        name = self.name_input.text
        phone = self.phone_input.text
        login = self.login_input.text
        password = self.password_input.text
        confirm = self.confirm_input.text
        
        if not all([name, phone, login, password, confirm]):
            self.show_dialog('Ошибка', 'Заполните все поля')
            return
        
        if password != confirm:
            self.show_dialog('Ошибка', 'Пароли не совпадают')
            return
        
        if self.db.add_user(name, phone, login, password):
            self.show_success_dialog('Успех', 'Регистрация успешна!')
        else:
            self.show_dialog('Ошибка', 'Пользователь уже существует')
    
    def go_back(self, instance):
        """Вернуться назад"""
        self.manager.current = 'login'
    
    def show_dialog(self, title, text):
        """Показать диалог ошибки"""
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
    
    def show_success_dialog(self, title, text):
        """Показать диалог успеха"""
        self.dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(
                    text='OK',
                    on_release=lambda x: [self.dialog.dismiss(), self.go_back(None)]
                )
            ]
        )
        self.dialog.open()
