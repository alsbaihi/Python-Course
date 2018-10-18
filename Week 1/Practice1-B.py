{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your number:-50\n",
      "-50\n",
      "6250000\n"
     ]
    }
   ],
   "source": [
    " Y = int(input(\"Enter your number:\"))\n",
    "print (Y)\n",
    "if Y < -100:\n",
    "    print(-Y)\n",
    "elif -100 <= Y and Y <= -25:\n",
    "    print(Y**4)\n",
    "elif -25 < Y  and Y <= 0:\n",
    "    print(3*Y**2-1)\n",
    "elif 0 < Y  and Y <= 100:\n",
    "    print((180/2)*Y + 3**Y)\n",
    "else:\n",
    "    print(Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
