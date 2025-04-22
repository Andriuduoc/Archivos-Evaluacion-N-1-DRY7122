# Script 3: Clasificar número de ACL
acl = int(input("Ingrese el número de ACL IPv4: "))

if 1 <= acl <= 99 or 1300 <= acl <= 1999:
    print("Es una ACL Estándar.")
elif 100 <= acl <= 199 or 2000 <= acl <= 2699:
    print("Es una ACL Extendida.")
else:
    print("El número ingresado no corresponde a una ACL válida.")
