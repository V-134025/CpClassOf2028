t = True
f = False
#1: Identify Variables (or conditions) and assign them boolean values
#2: In you noteboot, write the logical expressions using and, or, and not

# 1.
# Create a program that checks if it is sunny and you have sunglasses.
# Output should be True only if both are true.
s = f
g = f

if s and g is True:
    print("you go outside")
else:
    print("nothing changed")


# 2.
# Check if you have homework or you have a project due.
# Output should be True if at least one is true.
h=t
p=f

if h or g is True:
    print("NOOOOO")
else:
    print("eh")

# 3.
# Check if you are not tired.
# Use the not operator.
tire=f
if not tire is True:
    print("not tired")
else:
    print("yawn")

# 4.
# “If it is raining, then you bring an umbrella.”
# Write this as: if raining then umbrella, which is (not raining) or umbrella.
r = t
if r is t:
    print("bring umbrella")
else:
    print("no umbrella")

# 5.

# “It is weekend if and only if you don’t have school.”
# Translate to (weekend and not school) or (not weekend and school == False).
w=t
s=f
if w and not s == t:
    print(":J")
else:
    print("saddening")

# 6. 
# “You can play video games if exactly one of these is true: it’s weekend or you finished homework.”
w=f
hw=t
if w or hw == t:
    if w == hw:
        print("NOTHING")
    else:
        print("games")
else:
    print("NOTHING")

# 7. Robot Logic
# “The robot goes outside if it’s raining and it wears boots, or if it’s not raining and it doesn’t wear boots.”
r=f
b=f
if r == b:
    print("outside")
else:
    print("in in in in in")

# 8. Safety System
# “The alarm sounds if there is smoke and the door is closed.”
s=f
close=t
if s and close is t:
    print("BEEEEP BEEEEP BEEEEP BEEEEEEEEp")
else:
    print("...")
# 9. School Decision
# “You can go on a school trip if you have permission and paid the fee, or if the teacher gives special approval.”
p=t
fee=t
spass=f
if (p and fee is t) or (spass is t):
    print("TRIP TRIP TRIP")
else:
    print(":C")

# 10. Party Decision
# “You will go to the party if you are invited and it’s Friday, or if your best friend is going.”
i=f
fri=t
bf=f
if (i and fri is t) or (bf is t):
    print("you go")
else:
    print("you,, gulp,, dont")