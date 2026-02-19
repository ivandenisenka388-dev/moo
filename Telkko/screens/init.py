# Инициализация пакета screens
from .login_screen import LoginScreen
from .register_screen import RegisterScreen
from .chats_screen import ChatsScreen
from .chat_screen import ChatScreen
from .contacts_screen import ContactsScreen
from .profile_screen import ProfileScreen

__all__ = [
    'LoginScreen',
    'RegisterScreen',
    'ChatsScreen',
    'ChatScreen',
    'ContactsScreen',
    'ProfileScreen'
]
