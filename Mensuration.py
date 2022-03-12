{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "af24d5b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Length of the Rectangle4\n",
      "Enter the Breath of the Rectangle5\n",
      "Area of a Rectangle is : 20\n"
     ]
    }
   ],
   "source": [
    "#\"FIND THE AREA OF RECTANGLE\"\n",
    "Length = int(input(\"Enter the Length of the Rectangle\"))\n",
    "Breath = int(input(\"Enter the Breath of the Rectangle\"))\n",
    "Area_of_Rectangle = Length * Breath\n",
    "print(\"Area of a Rectangle is :\",Area_of_Rectangle)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cf3e723f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Length of the Square :6\n",
      "Area of a Square is : 36\n"
     ]
    }
   ],
   "source": [
    "#AREA OF A SQUARE\n",
    "Length1 = int(input(\"Enter the Length of the Square :\"))\n",
    "Area_of_Square = Length1* Length1\n",
    "print(\"Area of a Square is :\",Area_of_Square)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d64c35e0",
   "metadata": {},
   "source": [
    "#"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c2cf49d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the radius of a circle :3\n",
      "Enter the Area of a Circle : 28.26\n"
     ]
    }
   ],
   "source": [
    "#AREA OF A CIRCLE\n",
    "Radius = int(input(\"Enter the radius of a circle :\"))\n",
    "Area_of_Circle = 3.14 * Radius**2\n",
    "print(\"Enter the Area of a Circle :\",Area_of_Circle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "02770ec6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Length of the Rectangle :7\n",
      "Enter the Breath of the Rectangle :5\n",
      "Parameter of the Rectangle is : 24\n"
     ]
    }
   ],
   "source": [
    "#PARAMETER OF A RECTANGLE\n",
    "Length = int(input(\"Enter the Length of the Rectangle :\"))\n",
    "Breath = int(input(\"Enter the Breath of the Rectangle :\"))\n",
    "Parameter_of_Rectangle = 2*Length + 2*Breath\n",
    "print(\"Parameter of the Rectangle is :\",Parameter_of_Rectangle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7377e6c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Length of a Square :6\n",
      "Parameter of the Square is : 24\n"
     ]
    }
   ],
   "source": [
    "#PARAMETER OF A SQUARE\n",
    "Length = int(input(\"Enter the Length of a Square :\"))\n",
    "Parameter_of_Square = 4*Length\n",
    "print(\"Parameter of the Square is :\",Parameter_of_Square)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7a9adfde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Radius of a Circle :6\n",
      "Circumference of a Circle is : 37.68\n"
     ]
    }
   ],
   "source": [
    "#CIRCUMFERENCE OF A CIRCLE\n",
    "Radius = int(input(\"Enter the Radius of a Circle :\"))\n",
    "Circumference_of_Circle = 2 * 3.14 * Radius\n",
    "print(\"Circumference of a Circle is :\",Circumference_of_Circle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3d2548e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Length of a Cube :8\n",
      "Volume of a Cube is : 512\n"
     ]
    }
   ],
   "source": [
    "#VOLUME OF A CUBE\n",
    "Length = int(input(\"Enter the Length of a Cube :\"))\n",
    "Volume_of_Cube = Length**3\n",
    "print(\"Volume of a Cube is :\",Volume_of_Cube)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8ffc704a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Length of a Cube :4\n",
      "Total Surface Area of a Cube is : 96\n"
     ]
    }
   ],
   "source": [
    "#TOTAL SURFACE AREA OF A CUBE\n",
    "Length = int(input(\"Enter the Length of a Cube :\"))\n",
    "Total_Surface_Area_of_Cube = 6 * Length**2\n",
    "print(\"Total Surface Area of a Cube is :\",Total_Surface_Area_of_Cube)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1b2f904f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Length of a Cuboid :8\n",
      "Enter the Breath of a Cuboid :6\n",
      "Enter the Height of a Cuboid :4\n",
      "Volume of a Cuboid is : 192\n"
     ]
    }
   ],
   "source": [
    "#VOLUME OF A CUBOID\n",
    "Length = int(input(\"Enter the Length of a Cuboid :\"))\n",
    "Breath = int(input(\"Enter the Breath of a Cuboid :\"))\n",
    "Height = int(input(\"Enter the Height of a Cuboid :\"))\n",
    "Volume_of_Cuboid = Length * Breath * Height\n",
    "print(\"Volume of a Cuboid is :\",Volume_of_Cuboid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "f47e2f63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Length of a Cuboid :4\n",
      "Enter the Breath of a Cuboid :3\n",
      "Enter the Height of a Cuboid :6\n",
      "Total Surface Area of a Cuboid is : 54\n"
     ]
    }
   ],
   "source": [
    "#TOTAL SURFACE AREA OF A CUBOID\n",
    "Length = int(input(\"Enter the Length of a Cuboid :\"))\n",
    "Breath = int(input(\"Enter the Breath of a Cuboid :\"))\n",
    "Height = int(input(\"Enter the Height of a Cuboid :\"))\n",
    "Total_Surface_Area_of_Cuboid = Length * Breath + Breath * Height + Length * Height\n",
    "print(\"Total Surface Area of a Cuboid is :\",Total_Surface_Area_of_Cuboid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc41d6d3",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
