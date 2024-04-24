# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Now, the first thing we want to do is to convert the numbers that we're getting through the inputs into numbers that we can work with
# and do mathematical operations on.
# So that means on line 11, you'll see that I've created the weight_as_integer variable to store the weight input as a whole number. 
weight_as_int = int(weight)

# On line 16, I'm converting the height that is coming in with height in meters. 
# And because none of us have one meter or two meter, we're usually somewhere in between the two. 
# This is usually represented as a floating point number. So there's a decimal point in there.
height_as_float = float(height)

bmi = weight/height**2
print(int(bmi))
