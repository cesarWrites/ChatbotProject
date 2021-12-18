{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "lemmatizer = WordNetLemmatizer()\n",
    "import pickle\n",
    "import numpy as np\n",
    "from keras.models import load_model\n",
    "model = load_model('chatbot_model.h5')\n",
    "import json\n",
    "import random\n",
    "intents = json.loads(open('intents.json').read())\n",
    "words = pickle.load(open('words.pkl','rb'))\n",
    "classes = pickle.load(open('classes.pkl','rb'))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
