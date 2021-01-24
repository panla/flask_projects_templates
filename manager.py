import os

from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from apps import create_app

BASE_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config/local.py')
app = create_app(BASE_CONFIG_PATH)


def create_manager():
    return Manager(app)


manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('run', Server())

if __name__ == '__main__':
    manager.run()
