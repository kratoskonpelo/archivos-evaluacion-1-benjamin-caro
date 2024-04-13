#este codigo está realizado enteramente por benjamin caro
ACL = int(input("ingrese el numero de su acl: "))
if ACL >=1 and ACL <=99:
    print("Su acl es estandar")
elif ACL >= 100 and ACL <= 199:
    print("Su acl es extendida")
else:
    print("El numero no corresponde a ninguna lista de acceso")
