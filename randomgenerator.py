import random
style=["Melded ","Fused ","Blended ","Mingled ","Welded ","Smooth ","Crushed ","Swished ","Twisted ","Stirred "]
adjective=["Rocky Road","Mango Pinapple","Cookie Cream","Vanilla Caramel","Banana","Vanilla Bean","Berry","Strawberry","Mamey","Chocolate"]
shake=[" Parfait"," Frosty"," Shake"," Twist"," Blend"," Cream"," Blast"," Stream"," Smoothie"," Supreme"]
style_length= len(style)
adjective_length= len(adjective)
shake_length= len(shake)
for i in range(10):
	random_index=random.randint(0, style_length-1)
	random_index=random.randint(0,adjective_length-1)
	random_index=random.randint(0,shake_length-1)
	print(style[random_index] + adjective[random_index] + shake[random_index])

	
	
	
# Band Names Ahead!!!!
#Nevermind

