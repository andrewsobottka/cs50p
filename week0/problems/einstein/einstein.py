# Even if you haven't studied phsyics (recently or ever!), you might have heard
#  that E = mc^2, wherein E represents energy (measured in Joules), m
#  represents mass (measured in kilograms), and c represents the speed of light
#  (measured approximately as 300,000,000 meters per second), per Albert
#  Einstein et al. Essentially, the formula means that mass and energy are
#  equivalent.

# In this file, implement a program in Python that prompts the user for a mass
#  as an integer (in kilograms) and then outputs the equivalent number of
#  Joules as an integer. Assume that the user will input an integer.
 
def main():
    mass = input("Input mass in kilograms\nm: ")
    print(f"E: {energy(int(mass))} Joules")

def energy(m):
    # Speed of Light:
    c = 300000000
    # Return Energy in Joules
    return(m * c**2)

main()
