{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "5\n",
      "7\n",
      "11\n",
      "13\n",
      "17\n",
      "19\n"
     ]
    }
   ],
   "source": [
    "# programme that print the first n prime numbers.\n",
    "\n",
    "def print_prime_numbers(n):\n",
    "     for i in range (2,n+1):\n",
    "            count=0\n",
    "            for y in range(2,i):\n",
    "                if(i%y !=0):\n",
    "                     count+=1\n",
    "            if (count==i-2):\n",
    "                print (i)\n",
    "            \n",
    "print_prime_numbers(20)\n",
    "\n"
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
