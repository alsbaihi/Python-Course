{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "list values: [23, 76, 97, 28, 10, 8, 2, 4, 6]\n",
      "The Mean for the list values:  28.22222222222222\n",
      "The Median for the list values: 10.0\n",
      "The Standard Deviation for the list values: 32.57394247546744\n"
     ]
    }
   ],
   "source": [
    "# Mathmatical Statistics Using Numpy Modules\n",
    "import numpy as np\n",
    "x =[23,76,97,28,10,8,2,4,6]\n",
    "print(\"list values:\", x)\n",
    "print(\"The Mean for the list values: \",np.mean(x))\n",
    "print(\"The Median for the list values:\", np.median(x))\n",
    "print(\"The Standard Deviation for the list values:\",np.nanstd(x))"
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
