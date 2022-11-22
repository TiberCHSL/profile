class Profile:

    def __init__(self,id,username,email,password,status,level=0):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.level = level

    def show(self):
        print("El id es:",self.id)
        print("El nombre de usuario es: ",self.username)
        print("El email es: ",self.email)
        print("La contraseña es: ",self.password)
        print("El status es: ",self.status)
        print("El nivel es: ",self.level)
    def changepass(self,oldpass,newpass):
        choice = int(input("Ingrese 1 si desea cambiar la contraseña: "))
        newpass = ""
        if choice == 1:
            while oldpass != self.password:
                oldpass = input("Ingrese la contraseña antigua: ")
                if oldpass == self.password:
                    self.password = input("Ingrese la nueva contraseña: ")
                    newpass = self.password
                    print("La contraseña ha sido cambiada")
                else:
                    print("Contraseña inválida")
        
    