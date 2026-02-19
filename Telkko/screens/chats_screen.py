"""
TELKKO - Экран списка чатов
"""

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, ThreeLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDIconButton
from kivy.metrics import dp
from components.chat_item import ChatItem


class ChatsScreen(Screen):
    """Экран со списком чатов"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def on_enter(self):
        """При входе на экран"""
        self.load_chats()
    
    def build_ui(self):
        """Создание интерфейса"""
        layout = MDBoxLayout(orientation='vertical')
        
        # Верхняя панель
        self.toolbar = MDTopAppBar(
            title='TELKKO',
            left_action_items=[['menu', lambda x: self.open_menu()]],
            right_action_items=[
                ['magnify', lambda x: self.search()],
                ['dots-vertical', lambda x: self.open_options()]
            ]
        )
        layout.add_widget(self.toolbar)
        
        # Список чатов
        self.scroll = ScrollView()
        self.chats_list = MDList(
            spacing=dp(5),
            padding=[dp(10), dp(5)]
        )
        self.scroll.add_widget(self.chats_list)
        layout.add_widget(self.scroll)
        
        # Кнопка нового чата
        self.new_chat_btn = MDIconButton(
            icon='pencil',
            pos_hint={'center_x': 0.9, 'center_y': 0.1},
            md_bg_color=self.theme_cls.primary_color,
            theme_text_color='Custom',
            text_color=(1, 1, 1, 1)
        )
        self.new_chat_btn.bind(on_press=self.new_chat)
        layout.add_widget(self.new_chat_btn)
        
        self.add_widget(layout)
    
    def load_chats(self):
        """Загрузка чатов из БД"""
        self.chats_list.clear_widgets()
        
        # Пример чатов (в реальном приложении - из БД)
        chats = [
            {
                'name': 'Иван Петров',
                'last_message': 'Привет! Как дела?',
                'time': '14:30',
                'avatar': 'assets/images/default_avatar.png',
                'unread': 2
            },
            {
                'name': 'Мария Иванова',
                'last_message': 'Фото',
                'time': '12:15',
                'avatar': 'assets/images/default_avatar.png',
                'unread': 0
            },
            {
                'name': 'Алексей Сидоров',
                'last_message': '👍',
                'time': 'Вчера',
                'avatar': 'assets/images/default_avatar.png',
                'unread': 5
            }
        ]
        
        for chat in chats:
            item = ChatItem(chat_data=chat)
            item.bind(on_release=lambda x, c=chat: self.open_chat(c))
            self.chats_list.add_widget(item)
    
    def open_chat(self, chat):
        """Открыть чат"""
        app = MDApp.get_running_app()
        app.current_chat = chat
        self.manager.current = 'chat'
    
    def new_chat(self, instance):
        """Новый чат"""
        self.manager.current = 'contacts'
    
    def search(self):
        """Поиск"""
        pass
    
    def open_menu(self):
        """Открыть меню"""
        pass
    
    def open_options(self):
        """Открыть опции"""
        pass
