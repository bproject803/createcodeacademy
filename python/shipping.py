weight = 41.5
#Ground Shipping
if weight <= 2:
  cost = weight*1.50 + 20
elif weight <= 6:
  cost = weight*3 + 20
elif weight <= 10:
  cost = weight*4 + 20
else:
  cost = weight*4.75 + 20
print("Ground Shipping: $ " + str(cost))

#Cost of ground shipping premium
cost_of_premium_ground_shipping = 125
print("Ground Shipping Premium: $ " + str(cost_of_premium_ground_shipping))

#Drone Shipping
weight_drone = 41.5
if weight_drone <= 2:
  cost_drone = weight_drone*4.5 + 0
elif weight_drone <= 6:
  cost_drone = weight_drone*9 + 0
elif weight_drone <= 10:
  cost_drone = weight_drone*12 + 0
else:
  cost_drone = weight_drone*14.25 + 0
print ("Drone Shipping: $ " + str(cost_drone))
