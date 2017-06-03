#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app, db

from flask_script import Shell, Manager, Server
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager = Manager(app)

db.create_all(app=app)

def make_shell_context():
    return dict(app=app)

manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host="127.0.0.1", port=5000))


@manager.command
def deploy():
    """Run deployment tasks."""
    pass


if __name__ == '__main__':
    manager.run()


