{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/Users/samaralsbaihi/Downloads/Notebooks\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['3.2.3 FOREX, Weather and Translation.ipynb',\n",
       " '3.2.1 Intro to APIs and ISS.ipynb',\n",
       " 'Untitled1.ipynb',\n",
       " '3.1 Tuples and Dictionaries.ipynb',\n",
       " 'demo.txt',\n",
       " 'week1',\n",
       " 'Untitled.ipynb',\n",
       " '3.4 Writing and Reading Files in Python.ipynb',\n",
       " 'appendfile.txt',\n",
       " 'Untitled2.ipynb',\n",
       " 'demofile.txt',\n",
       " 'week1.txt',\n",
       " '3.0 Assignments Solutions.ipynb',\n",
       " '.ipynb_checkpoints',\n",
       " '3.5 Exception Handling.ipynb',\n",
       " '3.2.2 Google API! .ipynb',\n",
       " 'Practice1-A.txt']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "print(os.getcwd())\n",
    "'C:\\\\Program Files\\\\Notebook'\n",
    "\n",
    "\n",
    "os.listdir()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['weekA.txt']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " os.listdir()\n",
    "['week1.txt']\n",
    "os.rename ('week1.txt','weekA.txt')\n",
    "os.listdir()\n",
    "['weekA.txt']\n",
    "\n",
    "    "
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
