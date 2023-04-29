{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3aa3b1e7-69f0-42f7-9753-072f8061411f",
   "metadata": {},
   "source": [
    "https://youtu.be/4nsTce1Oce8\n",
    "\n",
    "\n",
    ".ipynbファイルを.pyファイルに変換するには、以下の手順を実行してください。\n",
    "\n",
    "jupyter nbconvert コマンドをインストールする必要があります。コマンドプロンプトまたはターミナルで、以下のコマンドを実行します。\n",
    "Copy code\n",
    "pip install nbconvert\n",
    ".ipynbファイルを.pyファイルに変換するには、以下のコマンドを実行してください。\n",
    "css\n",
    "Copy code\n",
    "jupyter nbconvert --to script example.ipynb\n",
    "上記の例では、 example.ipynbという名前のファイルを.pyファイルに変換しています。このコマンドを実行すると、同じディレクトリに example.py という名前のファイルが作成されます。このファイルには、.ipynbファイル内のすべてのコードセルがPythonスクリプトとして書き出されます。\n",
    "\n",
    "この方法は、Jupyter Notebookがインストールされている場合に限ります。\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
