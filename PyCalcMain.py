class Calc3:
  def __init__(self):
    pass

  def Partial_Derivatives(self):
    print("ass")

  def Calc_Vector_Parallelogram(self, vect1, vect2):
    get_cross = self.Cross_Prod(vect1, vect2, []) #no vector 3
    return((get_cross[0]**2 + get_cross[1]**2 + get_cross[2]**2) ** 0.5)


  def Check_Parallel(self, vect1, vect2):
    result_x = vect2[0]/vect1[0]
    result_y = vect2[1]/vect1[1]
    result_z = vect2[2]/vect1[2]
    print(f"X: {result_x}, Y: {result_y}, Z: {result_z}")
    return(result_x == result_y == result_z)

  def Check_Orthogonal(self, vect1, vect2):
    print("Result:", vect1[0]*vect2[0] + vect1[1]*vect2[1] + vect1[2]*vect2[2])
    return(vect1[0]*vect2[0] + vect1[1]*vect2[1] + vect1[2]*vect2[2] == 0)

  def Symmetric_Form(self, vect1, vect2):
    Coord = None
    for index in range(3): #go thru XYZ Coordinates
      if index == 0:
        Coord = "x ="
      elif index == 1:
        Coord = "y ="
      elif index == 2:
        Coord = "z" 
      print(f"{(-1*vect1[index])/vect2[index]}{Coord} ",end="")

  def Parametric_Form(self, vect1, vect2):
    Coord = None
    for index in range(3): #go thru XYZ Coordinates
      if index == 0:
        Coord = "x"
      elif index == 1:
        Coord = "y"
      elif index == 2:
        Coord = "z" 
      print(f"{Coord} = {vect1[index]} + ({vect2[index]})t")

  def Cross_Prod(self, vect1b, vect2c, vect3a):
    i = (vect1b[1] * vect2c[2]) - (vect1b[2] * vect2c[1])
    j = -1 * ((vect1b[0] * vect2c[2]) - (vect1b[2] * vect2c[0]))
    k = (vect1b[0] * vect2c[1]) - (vect1b[1] * vect2c[0])  

    result_vect = [i, j, k]
    cross_list = []
    cross_list += [["i", "j", "k"]]
    if vect3a:
      cross_list.append(vect3a)
      cross_list.append(result_vect)
    else:
      cross_list.append(vect1b)
      cross_list.append(vect2c)

    print("____________")
    print("Cross Product A x (B x C)")
    print("____________")
    for vectorvalues in cross_list:
      formatted_items = []
      for vector_rows in vectorvalues:
        if type(vector_rows) == str:
          formatted_items.append(vector_rows)
        else:
          formatted_items.append(str(int(vector_rows)))
      row_content = "   ".join(formatted_items)
      print(f"|{row_content}|")
    print("------------")

    if vect3a:
      newi = (result_vect[2] * vect3a[1]) - (result_vect[1] * vect3a[2])
      newj = -1 * ((result_vect[2] * vect3a[0]) - (result_vect[0] * vect3a[2]))
      newk = (result_vect[1] * vect3a[0]) - (result_vect[0] * vect3a[1])
      print(f"Result AxBxC = <{newi}i, {newj}j, {newk}k>")
    else:
      print(f"Result AxB = <{i}i, {j}j, {k}k>")
      return [i, j, k]

  def Dot_Prod(self, vect1, vect2):
    i = vect1[0] * vect2[0]
    j = vect1[1] * vect2[1]
    k = vect1[2] * vect2[2]
    result = i + j + k
    print(f"{i} + {j} + {k} = {result}") 


def main():
  print("----------------------------")
  print("Hey there fella! Choose what option you want!")
  options = 0
  while options != 8:
    while options > 8 or options <= 0:
      try: 
        options = int(input("1. Dot Product\n2. Cross Product\n3. Parametric Equations\n4. Symmetric Equations\n5. Check if vectors are Orthogonal\n6. Check if vectors are Parallel\n7. Calculate Vector Parallelogram\n8. Quit\nChoose Option: "))
        print("----------------------------")
      except:
        print("----------------------------")
        print("Please choose a Valid option")
    if options != 8:
      vect_1 = []
      vect_2 = []
      vect_3 = []
      calc_type = Calc3()
      problem_ask = "Vector" #Everything else

      if options == 3 or options == 4: #Parametric or Symmetric
        problem_ask = "Point"

      for vector_num in range(2):
        for vector_index in "ijk":
          grab_vector = float(input(f"Insert a number for {problem_ask} {vector_num} {vector_index}: "))
          if vector_num == 0:
            vect_1.append(grab_vector)
          elif vector_num == 1:
            vect_2.append(grab_vector)
        problem_ask = "Vector" #switch back to vector after we got point from user if they select parametric or symmetric

        if options == 2: #CROSS PRODUCT
          try:
            new_vect3 = input("Add additional vector? Y/N: ").capitalize()
          except:
            print("Please type an actual answer with words")
          if new_vect3 == "Y" or new_vect3 == "Yes":
            for vector_index in "ijk":
              grab_vector = float(input(f"Insert a number for Vector 3 {vector_index}: "))
              vect_3.append(grab_vector)

      if options == 1:
        calc_type.Dot_Prod(vect_1, vect_2)
      elif options == 2:
        if vect_3:
          calc_type.Cross_Prod(vect_2, vect_3, vect_1)
        else:
          calc_type.Cross_Prod(vect_1, vect_2, vect_3)
      elif options == 3:
        calc_type.Parametric_Form(vect_1, vect_2)
      elif options == 4:
        calc_type.Symmetric_Form(vect_1, vect_2)
      elif options == 5:
        orthogonal = calc_type.Check_Orthogonal(vect_1, vect_2)
        if orthogonal == True:
          print(f"{orthogonal} Vectors are orthogonal")
        else:
          print(f"{orthogonal} Vectors are NOT orthogonal")
      elif options == 6:
        parallel = calc_type.Check_Parallel(vect_1, vect_2)
        if parallel == True:
          print(f"{parallel} Vectors are parallel")
        else:
          print(f"{parallel} Vectors are NOT parallel")
      elif options == 7:
        parallel_area = calc_type.Calc_Vector_Parallelogram(vect_1, vect_2)
        print(f"Area: {parallel_area} square units")

      options = 0 #reset back to default

    else:
      print("Exiting...")

main()