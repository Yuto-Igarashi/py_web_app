作業環境は vscodeが前提

## 実行環境構築(初めの1回のみ)
cloneしたら、リポジトリのディレクトリに移動する。
```
cd py_web_app
```

仮想環境を作成する。
```
python -m venv venv
```

仮想環境に入る。
```
source venv/bin/activate
```

vscodeで使用するsettings.jsonを作成する。
```
mkdir .vscode
cd .vscode
touch settings.json
```

仮想環境のpythonのパスを確認する。
```
which python
```

settings.jsonに以下を記載する。
```
{
    "python.pythonPath": "which pythonで確認したパスを記載",
    "python.venvFolders": [
        "venv"
    ]
}
```

requirements.txt の内容をpipインストールする。
```
pip install -r requirements.txt
```

これで、環境構築完了。

### 仮想環境を離脱する
```
deactivate
```

## 新しいパッケージをインストールしたい場合
pipインストールを行う。　
仮想環境に入っている前提。その仮想環境下でpipインストールを行うと、グローバルなpython環境には影響しない。
```
pip install pytest
```

requirements.txtにpipインストールした内容を書き込む。
```
pip freeze > requirements.txt
```

## 暗号化キー情報を扱うファイルkey.pyの作成
key.pyを作成する
```
touch key.py
```

どちらも任意の文字列で大丈夫です
```
SECRET_KEY = "123344fefdedwesdfe"
SALT = "dvdvdve23erfefe"
```

## SQL環境を作成する
前提:Homebrewをインストール済み、Homebrewにて、mysqlをインストール済み。mysqlに入れる。

以下のsqlを実行し、py_web_app_sampleのdatabaseを作成する。
```
sql/create_database.sql
```

続いて、onegaicontents　、usersのテーブルを作成する。
```
sql/create_table_users.sql
sql/create_table_onegaicontents.sql
```



## 作業時の対応
作業をする時は以下を行う。

pythonの仮想環境に入る。
```
source venv/bin/activate
```

仮想環境を離脱する場合は以下を実行。
```
deactivate
```

mysqlを起動する。
```
mysql.server start
```

mysqlに入る。(パスワードを設定している場合は、入力する)
```
mysql -uroot -p
```

mysqlを停止する場合は以下を実行する
```
mysql.server stop
```



