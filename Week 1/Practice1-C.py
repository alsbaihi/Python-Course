{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "whats the temperature?32\n",
      "whats the temperature?0\n",
      "0.0\n",
      "32.0\n"
     ]
    }
   ],
   "source": [
    "fahrenheit = float (input(\"whats the temperature?\"))\n",
    "celsius = float (input(\"whats the temperature?\"))\n",
    "C = (5/9)* (fahrenheit-32)\n",
    "F = (9/5)* celsius+32\n",
    "print (C)\n",
    "print (F)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "celsius:0\n",
      "Fahrenheit= {32.0}\n",
      "fahrenheit:32\n",
      "Celsius= {0.0}\n"
     ]
    }
   ],
   "source": [
    "tem1= float(input(\"celsius:\"))\n",
    "print(f\"Fahrenheit=\" ,{(9/5)* tem1+32})\n",
    "tem2= float(input(\"fahrenheit:\"))   \n",
    "print (f\"Celsius=\" , {(5/9)*(tem2-32)})"
   ]
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
