name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

height_cms = height * 2.54
weight_kgs = weight * 0.45359237

print "My weight in kg is: %d." % weight_kgs
print "My height in cm is: %d." % height_cms

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
print "This is a print with r: %r." % weight