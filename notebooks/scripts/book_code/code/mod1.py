X = 1
import mod2

print X,        # My global X
print mod2.X,       # mod2's X
print mod2.mod3.X            # Nested mod3's X
