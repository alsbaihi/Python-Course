{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "convert from: USD\n",
      "convert to: TRY\n",
      "Available to:  ['all currencies', 'TRY']\n",
      "How many you want to convert: 100\n",
      "100.0 USD to TRY is 545.7401048921319\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "base_curr = input(\"convert from: \")\n",
    "to_curr = input(\"convert to: \")\n",
    "\n",
    "available_currencies = [\"all currencies\",base_curr,to_curr]\n",
    "\n",
    "available_currencies.remove(base_curr)\n",
    "\n",
    "print(\"Available to: \", available_currencies)\n",
    "\n",
    "amount = float(input(\"How many you want to convert: \"))\n",
    "\n",
    "base_link_forex = 'http://data.fixer.io/api/latest'\n",
    "\n",
    "parameters_forex = {\n",
    "    \"access_key\" : \"e1be8ec55a7c5fa9600ff656adf94ac4\",\n",
    "}\n",
    "response = requests.get(base_link_forex,parameters_forex).json()\n",
    "\n",
    "latest_Euro_rates =response[\"rates\"] \n",
    "                \n",
    "result = (latest_Euro_rates[to_curr]/latest_Euro_rates[base_curr]) * amount\n",
    "\n",
    "print(f\"{amount} {base_curr} to {to_curr} is {result}\") "
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
