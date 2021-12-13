# -*- coding: utf-8 -*-
# Time: 2020-08-02 18:26
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: app.py

from app import create_app
from flask_script import Manager, Server

app = create_app()
Manager = Manager(app)

Manager.add_command("run", Server(use_debugger=False))
Manager.add_command("pro",Server(port=5000,host="127.0.0.1",use_debugger=False, use_reloader=True))
Manager.add_command("dev",Server(port=1312,host="127.0.0.1",use_debugger=True, use_reloader=True))
Manager.add_command("devnet",Server(port=5000,host="0.0.0.0",use_debugger=True, use_reloader=True))

if __name__ == '__main__':
    Manager.run()
