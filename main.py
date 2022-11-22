from profile import Profile

def main():
    profile1 = Profile(1,input("Ingrese usuario: "),input("Ingrese email: "),input("Ingrese contraseña: "),input("Ingrese status: "),int(input("Ingrese nivel de la cuenta: ")))
    profile1.show()
    profile1.changepass()
    profile1.show()
main()