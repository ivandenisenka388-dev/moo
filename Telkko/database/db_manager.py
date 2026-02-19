"""
TELKKO - Менеджер базы данных
"""

import sqlite3
import os
from datetime import datetime


class DatabaseManager:
    """Класс для работы с базой данных"""
    
    def __init__(self, db_path='data/telkko.db'):
        # Создаем папку data если её нет
        os.makedirs('data', exist_ok=True)
        
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()
    
    def create_tables(self):
        """Создание таблиц"""
        cursor = self.conn.cursor()
        
        # Таблица пользователей
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT UNIQUE,
                login TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                avatar TEXT,
                created_at TIMESTAMP
            )
        ''')
        
        # Таблица контактов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                contact_id INTEGER,
                nickname TEXT,
                created_at TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (contact_id) REFERENCES users(id)
            )
        ''')
        
        # Таблица сообщений
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT,
                sender_id INTEGER,
                text TEXT,
                timestamp TIMESTAMP,
                is_read INTEGER DEFAULT 0,
                FOREIGN KEY (sender_id) REFERENCES users(id)
            )
        ''')
        
        self.conn.commit()
    
    def add_user(self, name, phone, login, password):
        """Добавление пользователя"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, phone, login, password, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, phone, login, password, datetime.now()))
            self.conn.commit()
            return True
        except:
            return False
    
    def get_user(self, login, password):
        """Получение пользователя"""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT id, name, phone, login, avatar
            FROM users WHERE login = ? AND password = ?
        ''', (login, password))
        
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'name': row[1],
                'phone': row[2],
                'login': row[3],
                'avatar': row[4]
            }
        return None
    
    def close(self):
        """Закрытие соединения"""
        if self.conn:
            self.conn.close()
