import Database
import json


class Menu:

    def __init__(self):
        self.menu = [
            {
                'name': 'Задачи',
                'path': 'tasks',
                'submenu': [
                    {
                        'name': 'Активные',
                        'path': '/active'
                    },
                    {
                        'name': 'Завершенные',
                        'path': '/done'
                    },
                    {
                        'name': 'Завершенные с ошибками',
                        'path': '/error'
                    }
                ]
            }
        ]
        with Database.session_scope() as session:
            results = session.query(Database.Method).all()
            menu = [
                {
                    'name': 'Группы',
                    'path': 'collector_groups',
                    'submenu': []
                },
                {
                    'name': 'Пользователи',
                    'path': 'collector_users',
                    'submenu': []
                }
            ]
            for result in results:
                if 0 <= result.list < 2:
                    menu[result.list]['submenu'].append(
                            {
                                'name': result.title,
                                'path': '/' + result.name
                            }
                    )
            self.menu += menu

        def get_menu():
            return self.menu






