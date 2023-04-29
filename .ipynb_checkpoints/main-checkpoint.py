{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3aa3b1e7-69f0-42f7-9753-072f8061411f",
   "metadata": {},
   "source": [
    "https://youtu.be/4nsTce1Oce8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "26d236e7-fb5d-46c5-9db4-468084e32634",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\hatak\\anaconda3\\lib\\site-packages (1.21.0)\n",
      "Requirement already satisfied: watchdog in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (4.11.3)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (13.3.4)\n",
      "Requirement already satisfied: numpy in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: pyarrow>=4.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (3.1.31)\n",
      "Requirement already satisfied: click>=7.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: requests>=2.4 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (2.28.1)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (4.3.0)\n",
      "Requirement already satisfied: toml in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: protobuf<4,>=3.12 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: python-dateutil in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: altair<5,>=3.2.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: blinker>=1.0.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: tornado>=6.0.3 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: pympler>=0.9 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: cachetools>=4.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (5.3.0)\n",
      "Requirement already satisfied: tzlocal>=1.1 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (4.3)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (0.8.1b0)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: pandas<2,>=0.25 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (1.4.4)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (9.2.0)\n",
      "Requirement already satisfied: validators>=0.2 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from streamlit) (0.20.0)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from altair<5,>=3.2.0->streamlit) (4.16.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from altair<5,>=3.2.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: entrypoints in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from altair<5,>=3.2.0->streamlit) (0.4)\n",
      "Requirement already satisfied: toolz in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from altair<5,>=3.2.0->streamlit) (0.11.2)\n",
      "Requirement already satisfied: colorama in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from click>=7.0->streamlit) (0.4.5)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19->streamlit) (4.0.10)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (3.8.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from packaging>=14.1->streamlit) (3.0.9)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from pandas<2,>=0.25->streamlit) (2022.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from python-dateutil->streamlit) (1.16.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (1.26.11)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2022.9.14)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (3.3)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: tzdata in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from tzlocal>=1.1->streamlit) (2023.3)\n",
      "Requirement already satisfied: pytz-deprecation-shim in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from validators>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from jinja2->altair<5,>=3.2.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\hatak\\anaconda3\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit) (0.1.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7be27717-6d4e-4a05-a474-ae9fbbba0e1b",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "illegal target for annotation (1105537035.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\hatak\\AppData\\Local\\Temp\\ipykernel_30820\\1105537035.py\"\u001b[1;36m, line \u001b[1;32m4\u001b[0m\n\u001b[1;33m    \"execution_count\": None\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m illegal target for annotation\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "with st.echo(), st.spinner(\"Wait for it...\"):\n",
    "    # 出力するコードを書く\n",
    "    st.title('サプーアプリ')\n",
    "    st.caption('これはサプーの動画用のテストアプリです')\n",
    "    \"execution_count\": None"
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
