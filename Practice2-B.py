{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "** CURRENCY EXCHANGE PROGRAM**\n",
      "1. convert from TRY to JOD:\n",
      "2. convert from JOD to TRY:\n",
      "3. convert from USD to TRY:\n",
      "4. convert from TRY to USD:\n",
      "5. convert from JOD to USD:\n",
      "6. convert from USD to JOD:\n",
      " the amount of money: 100\n",
      "choose 1 or 2 or 3 or 4 or 5 or 6:3\n",
      " from USD to TRY equals: 569.0 TRY\n"
     ]
    }
   ],
   "source": [
    "def currency_converter():\n",
    "    print( \"** CURRENCY EXCHANGE PROGRAM**\" )\n",
    "    print(\"1. convert from TRY to JOD:\")\n",
    "    print(\"2. convert from JOD to TRY:\")\n",
    "    print(\"3. convert from USD to TRY:\")\n",
    "    print(\"4. convert from TRY to USD:\")\n",
    "    print(\"5. convert from JOD to USD:\")\n",
    "    print(\"6. convert from USD to JOD:\")\n",
    "    amount = float(input(\" the amount of money: \"))\n",
    "    choise = input(\"choose 1 or 2 or 3 or 4 or 5 or 6:\")\n",
    "\n",
    "    if choise == \"1\":\n",
    "        exchangeR_TRY_JOD = 0.12\n",
    "        print (\" from TRY to JOD equals:\" , exchangeR_TRY_JOD * amount , \"JOD\" )\n",
    "    elif choise ==\"2\" :\n",
    "        exchangeR_JOD_TRY = 8.02\n",
    "        print (\" from JOD to TRY equals:\" , exchangeR_JOD_TRY * amount , \"TRY\")\n",
    "    elif choise == \"3\":\n",
    "        exchangeR_USD_TRY = 5.69\n",
    "        print (\" from USD to TRY equals:\" , exchangeR_USD_TRY * amount , \"TRY\")\n",
    "    elif choise ==\"4\":\n",
    "        exchangeR_TRY_USD = 0.18\n",
    "        print (\" from TRY to USD equals:\" , exchangeR_TRY_USD * amount , \"USD\")\n",
    "    elif choise ==\"5\":\n",
    "        exchangeR_JOD_USD = 1.41\n",
    "        print (\" from JOD to USD equals:\" , exchangeR_JOD_USD * amount , \"USD\")\n",
    "    elif choise ==\"6\":\n",
    "        exchangeR_USD_JOD = 0.71\n",
    "        print (\" from USD to JOD equals:\" , exchangeR_USD_JOD * amount , \"JOD\")\n",
    "\n",
    "    \n",
    "currency_converter()"
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
