# -*- coding: utf-8 -*-
"""
For this assignment, you are given two complex numbers. You will print the result of their 
addition, subtraction, multiplication, division, and modulus operations. The real and imaginary precision part
should be correct up to two decimal places.

Input Format: One line of input: The real and imaginary part of a number separated by a space.
Output Format: For two complex numbers and the output should be in the following sequence on separate lines:

C + D
C - D
C * D
C / D
mod(C)
mod(D)

>> For complex numbers with non-zero real and imaginary part, the output should be in the following format:
   A + Bi
>> Replace the plus symbol (+) with a minus symbol (-) when B<0.
>> For complex numbers with a zero complex part, i.e. real numbers, the output should be:
   A + 0.00i
>> For complex numbers where the real part is zero and the complex part is non-zero, the output should be:
   0.00 + Bi
"""

def addition(r1, r2, i1, i2):
  """
  r1 : real number of 1st complex number
  i1 : imaginary number of 1st complex number
  r2 : real number of 2nd complex number
  i2: imaginary number of 2nd complex number
  """
  real = r1 + r2
  imag = i1 + i2
  sign = ""
  if imag >= 0:
    sign = "+"
  #formula
  result = str(round(real,2))+sign+str(round(imag,2))+"i"
  return result

def subtraction(r1, r2, i1, i2):
  """
  r1 : real number of 1st complex number
  i1 : imaginary number of 1st complex number
  r2 : real number of 2nd complex number
  i2: imaginary number of 2nd complex number
  """
  real = r1 - r2
  imag = i1 - i2
  sign = ""
  if imag >= 0:
    sign = "+"
  #formula
  result = str(round(real,2))+sign+str(round(imag,2))+"i"
  return result

def multiplication(r1, r2, i1, i2):
  """
  r1 : real number of 1st complex number
  i1 : imaginary number of 1st complex number
  r2 : real number of 2nd complex number
  i2: imaginary number of 2nd complex number
  """
  r = r1*r2
  ir1 = i1*r2
  ir2 = r1*i2
  ir = ir1+ir2
  i = (i1*i2)*(-1)
  real = r + i
  imag = ir
  sign = ""
  if imag >= 0:
    sign = "+"
  #formula
  result = str(round(real,2))+sign+str(round(imag,2))+"i"
  return result

def division(r1, r2, i1, i2):
  """
  r1 : real number of 1st complex number
  i1 : imaginary number of 1st complex number
  r2 : real number of 2nd complex number
  i2: imaginary number of 2nd complex number
  """
  #making variables for conjugate
  jr = r2
  ji = -(i2)
  #multiplying conjugate in numerator
  nr = r1*jr
  nir1 = i1*jr
  nir2 = r1*ji
  ni = (i1*ji)*(-1)
  nreal = nr + ni
  nimag = nir1+nir2
  
  #multiplying conjugate in denominator
  dr = r2*jr
  dir1 = i2*jr
  dir2 = r2*ji
  di = (i2*ji)*(-1)
  dreal = dr + di
  dimag = dir1+dir2
  
  #dividing dreal with numerator
  mreal = nreal/dreal
  mimag = nimag/dreal
  
  sign = ""
  if mimag >= 0:
    sign = "+"
  #formula
  result = str(round(mreal,2))+sign+str(round(mimag,2))+"i"
  return result

def modulus(r, i):
  """
  r : real number of complex number
  i : imaginary number of complex number

  """
  result = ((r**2)+(i**2))**(1/2)
  return result

def main():
  """
  r1 : real number of 1st complex number
  i1 : imaginary number of 1st complex number
  r2 : real number of 2nd complex number
  i2: imaginary number of 2nd complex number
  """
  num1 = input("Enter the first complex number: ")
  num2 = input("Enter the second complex number: ")
  num1 = num1.split(" ")
  num2 = num2.split(" ")
  r1 = float(num1[0])
  i1 = float(num1[1])
  r2 = float(num2[0])
  i2 = float(num2[1])
  
  # #Entered values
  # print("Entered Values: ")
  # print("R1: ", r1)
  # print("I1: ", i1)
  # print("R2: ", r2)
  # print("I2: ", i2)
  
  print()
  print("Results: ")
  print()
  add_result = addition(r1,r2,i1,i2)
  print("C+D: ", add_result)
  sub_result = subtraction(r1,r2,i1,i2)
  print("C-D: ", sub_result)
  multi_result = multiplication(r1,r2,i1,i2)
  print("C*D: ", multi_result)
  divide_result = division(r1,r2,i1,i2)
  print("C/D: ", divide_result)
  mod_result1 = modulus(r1,i1)
  print("mod(C): ", round(mod_result1))
  mod_result2 = modulus(r2,i2)
  print("mod(D): ", round(mod_result2,2))

  
if __name__ == "__main__":
  main()