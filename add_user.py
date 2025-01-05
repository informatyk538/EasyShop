# Copyright (C) [2025] [Adam Kołoszycz]
#
# This file is part of [EasyShop].
#
# [EasyShop] is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# [EasyShop] is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with [EasyShop].  If not, see <https://www.gnu.org/licenses/>.


import sqlite3
from werkzeug.security import generate_password_hash

def add_user(username, password):
    hashed_password = generate_password_hash(password)
    with sqlite3.connect('shop.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            print(f"Użytkownik '{username}' został dodany.")
        except sqlite3.IntegrityError:
            print(f"Użytkownik '{username}' już istnieje.")

# ADD USER NAME AND PASSWORD
add_user('admin', 'super_secure_password')
