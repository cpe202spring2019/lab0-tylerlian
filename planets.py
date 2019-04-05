def weight_on_planets():
   # write your code here
   weight = input("What do you weigh on earth? ")
   weight = int(weight)
   print("\nOn Mars you would weigh %s pounds.\n\
On Jupiter you would weigh %s pounds." % \
   (weight*.38,weight*2.34))

   
   
if __name__ == '__main__':
   weight_on_planets()