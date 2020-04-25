作業環境は vscodeが前提

## 実行環境構築
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
