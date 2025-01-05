## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE.TXT file for details.
LANG: PL, ENG, DE, RU, JP


ENG

===BEGIN====

pip install -r requirements.txt

By default, the user is: username: admin password: super_secure_password

It is recommended to delete the shop.db file before the first run (this will remove the default user). 
(The user will be created anew when running backend.py). 
In the backend.py file, change the host and port in the last line of code to your own settings.

Next, run the backend.py file. If you have deleted the shop.db file, you can add a user. First, in the add_user.py file, 
change the username and password in the last line of code to your desired settings. Then, run the add_user.py file. 
It will add the user and password to the shop.db file.

====ADDING AND REMOVING OFFERS====

To access the admin page, you need to enter \admin after the address of your store's page, e.g., "http://127.0.0.1/admin". 
There, you will first be greeted by the login page, where you must enter your username and password. 
After logging in, you will see the page for adding and removing offers, 
which is simple enough for even your grandmother, who struggles with using a computer without you, to handle.

PL

===POCZĄTEK====

pip install -r requriements.txt

domyślnie użytkownik to:
nazwa: admin
hasło: super_secure_password

najlepiej przed pierwszym uruchomieniem usuń plik shop.db (w taki sposób usuniesz domyślnego użytkownika)
(użytkownik utworzy się nowy po uruchomieniu backend.py)
w pliku backend.py w ostatniej linijce kodu zmień host i port na własne ustawienie.

Następnie uruchom plik backend.py, jeśli usunąłeś plik shop.db możesz dodać użytkownika, najpierw w kodzie pliku add_user.py w
ostatniej linijce zmień nazwę użytkownika i hasło na własne ustawienie. Potem uruchom plik add_user.py, on doda użytkownika i 
hasło do pliku shop.db.

====DODAWANIE I USUWANIE OFERT====

gdy aby wejść na stronę admina musisz wpisać \admin po adresie swojej strony sklepu, np "http:\\127.0.0.1\admin"
tam najpierw odwiedzi cię strona logowania gdzie musisz użyć swojej nazwy użytkownika oraz hasła, po zalogowaniu się zobaczysz
stronę do dodawania i usuwania ofert która jest na tyle prosta że poradzi sobie na niej nawet twoja babcia nie radząca sobie bez
ciebie z obsługą komputera.

DE


===BEGINN====

pip install -r requirements.txt

Standardmäßig ist der Benutzer: Benutzername: admin Passwort: super_secure_password

Es wird empfohlen, die Datei shop.db vor dem ersten Start zu löschen (dies entfernt den Standardbenutzer). 
(Der Benutzer wird beim Start von backend.py neu erstellt). 
Ändern Sie im backend.py-Datei die Host- und Port-Einstellungen in der letzten Codezeile auf Ihre eigenen Einstellungen.

Führen Sie dann die Datei backend.py aus. Wenn Sie die Datei shop.db gelöscht haben, können Sie einen Benutzer hinzufügen. 
Ändern Sie zuerst im add_user.py-Code in der letzten Zeile den Benutzernamen und das Passwort auf Ihre eigenen Einstellungen. 
Führen Sie dann die Datei add_user.py aus. Sie fügt den Benutzer und das Passwort in die Datei shop.db ein.

====HINZUFÜGEN UND ENTFERNEN VON ANGEBOTEN====

Um zur Admin-Seite zu gelangen, müssen Sie \admin an die Adresse Ihrer Shop-Seite anhängen, z. B. "http://127.0.0.1/admin". 
Dort wird zuerst die Login-Seite angezeigt, auf der Sie Ihren Benutzernamen und Ihr Passwort eingeben müssen. 
Nach dem Login sehen Sie die Seite zum Hinzufügen und Entfernen von Angeboten, die so einfach ist, 
dass sogar Ihre Großmutter, die ohne Sie keinen Computer benutzen kann, damit zurechtkommt.

RU

===НАЧАЛО====

pip install -r requirements.txt

По умолчанию пользователь: имя: admin пароль: super_secure_password

Рекомендуется удалить файл shop.db перед первым запуском (это удалит пользователя по умолчанию). 
(Пользователь будет создан заново при запуске backend.py). 
В файле backend.py измените хост и порт в последней строке кода на свои собственные настройки.

Затем запустите файл backend.py. Если вы удалили файл shop.db, можно добавить пользователя. 
Сначала в файле add_user.py измените имя пользователя и пароль в последней строке кода на нужные настройки. 
Затем запустите файл add_user.py. Он добавит пользователя и пароль в файл shop.db.

====ДОБАВЛЕНИЕ И УДАЛЕНИЕ ПРЕДЛОЖЕНИЙ====

Чтобы попасть на страницу администратора, нужно ввести \admin после адреса вашего магазина, например "http://127.0.0.1/admin". 
Там вас сначала встретит страница логина, где нужно ввести ваше имя пользователя и пароль. 
После входа вы увидите страницу для добавления и удаления предложений, которая настолько проста, что с ней справится даже ваша бабушка, 
которая не может обойтись без вас, чтобы пользоваться компьютером.

Это всё, всего хорошего!

JP

===開始====

pip install -r requirements.txt

デフォルトのユーザーは次の通りです： ユーザー名: admin パスワード: super_secure_password

最初の実行前に shop.db ファイルを削除することをお勧めします（これでデフォルトのユーザーが削除されます）。 （backend.py を実行すると新しいユーザーが作成されます）。 
backend.py ファイルの最後の行でホストとポートを自分の設定に変更してください。

その後、backend.py ファイルを実行します。もし shop.db ファイルを削除した場合は、ユーザーを追加できます。最初に add_user.py 
ファイルのコードで最後の行のユーザー名とパスワードを自分の設定に変更してください。それから add_user.py ファイルを実行すると、ユーザーとパスワードが 
shop.db ファイルに追加されます。

====オファーの追加と削除====

管理者ページにアクセスするには、ショップページのアドレスの後に \admin を入力する必要があります。例："http://127.0.0.1/admin"。 
そこでは最初にログインページが表示され、ユーザー名とパスワードを入力する必要があります。ログイン後、オファーを追加および削除するページが表示され、非常にシンプルなので、コンピューターの操作が苦手なあなたの祖母でも簡単に使いこなせます。

以上、すべての幸運を！

ポーランドからの挨拶

