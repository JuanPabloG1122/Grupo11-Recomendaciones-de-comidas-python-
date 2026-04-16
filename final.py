
## --- SPRINT 2 ---
#   1- Añadir dos promedios, uno general y otro condicionado (Este puede variar segun que comida del dia sea x ejempl)
#   2- Justificar con los promedios anteriores la recomendacion final (Dentro de todo esto no tiene)
#   3- Con Maximos y minimos sacar datos de promedios con el punto 1


z
import colorama as c
from colorama import init, Fore, Back, Style

# VARIABLES
presupuesto = 0
costo = 0
cantidad = 0
descuento = 0
comida = ""
gusto = ""
agregado = ""
bebida = ""
tacc = ""
combo = ""
dieta = ""

# ESTILIZACION (al chat gpt le pregunte lo basico, esto fue hecho por una persona de carne y hueso)
sty_si_no = "(" + c.Fore.BLUE + "si" + c.Style.RESET_ALL + "/" + c.Fore.YELLOW +"no" + c.Style.RESET_ALL + ")"
sty_opciones = c.Fore.BLUE # + c.Fore.BLACK

err_typo = c.Back.YELLOW + c.Fore.BLACK + "error: escribiste mal, por favor escirbir de vuelta" + c.Style.RESET_ALL
err_num =  c.Back.YELLOW + c.Fore.BLACK + "error: opcion invalida, por favor escirbir de vuelta" + c.Style.RESET_ALL

comida_budin = c.Fore.BLUE + "Budin de Banana" + c.Style.RESET_ALL + "(costo: " + c.Fore.GREEN + "$100" + c.Style.RESET_ALL + ")"
comida_tostado = c.Fore.BLUE + "Budin de Banana" + c.Style.RESET_ALL + "(costo: " + c.Fore.GREEN + "$100" + c.Style.RESET_ALL + ")"
comida_medialuna = c.Fore.BLUE + "Medialuna" + c.Style.RESET_ALL + "(costo: " + c.Fore.GREEN + "$50" + c.Style.RESET_ALL + ")"
comida_alfajor =  c.Fore.BLUE + "Alfajor" + c.Style.RESET_ALL + "(costo: " + c.Fore.GREEN + "$25" + c.Style.RESET_ALL + ")"

bebida_cafe = c.Fore.BLUE + "cafe" + c.Style.RESET_ALL + "(costo: " + c.Fore.GREEN + "$240" + c.Style.RESET_ALL + ")"
bebida_te = c.Fore.BLUE + "te" + c.Style.RESET_ALL + "(costo: " + c.Fore.GREEN + "$180" + c.Style.RESET_ALL + ")"
bebida_aguaS = c.Fore.BLUE + "agua saborizada" + c.Style.RESET_ALL + "(costo: " + c.Fore.GREEN + "$270" + c.Style.RESET_ALL + ")"
bebida_yogurS =  c.Fore.BLUE + "yogur saludable" + c.Style.RESET_ALL + "(costo: " + c.Fore.GREEN + "$300" + c.Style.RESET_ALL + ")"
# no usamos colores rojos porque es un color agresivo, no es bueno para el negocio

# PLAN
# presupuesto
# tacc? (string que se agrega al final)
# preguntamos dieta (keto/veggie/vegan), recomendaciones
# preguntamos comida del dia (1/2/3/4), recomendaciones
    # comidas dulces/saladas con lo de la ma;ana
        # agregado y tipo de endulzante
    # comidas saludables en las potentes
        # bebidas y extras y hielo
        # ingredientes a eliminar? (un string se agrega al final)
# armar pedido (descuento)

while True:
    print(f"{c.Back.GREEN + c.Fore.BLACK}bienvenido al recomendador de del restaurante \"calle 11\" online!{c.Style.RESET_ALL}")

    while presupuesto == 0:
        presupuesto = int(input(f"cuanto presupuesto hay para gastar? {c.Fore.GREEN}$"))
        match presupuesto: #tratamos de evitar que no nos sale error si no ponemos nada en el input, pero no se pudo.
            case _ if presupuesto <= 0:
                print(err_typo)
                presupuesto = 0
            case _ if presupuesto >= 1:
                break
            case _:
                print(err_typo)
                presupuesto = 0

    while tacc == "":
        tacc = input(f"{c.Style.RESET_ALL}puedes comer tacc? {sty_si_no} ")
        match tacc:
            case "si":
                break
            case "no":
                break
            case _:
                print(err_typo)
                tacc = ""

    dieta = input(f"estas siguiendo una dieta? {sty_si_no} ")
    while dieta:
        if (dieta == "si" or dieta == "Si" or dieta == "SI" or dieta == "s"):
            dieta = input(f"cual dieta estas siguiendo? {sty_opciones}vegano{c.Style.RESET_ALL}, {sty_opciones}vegetariano {c.Style.RESET_ALL}o{sty_opciones} keto{c.Style.RESET_ALL}? ")
            match dieta:
                case "vegano":
                    break
                case "vegetariano":
                    break
                case "keto":
                    break
                case _:
                    print(err_typo)
                    dieta = "si"
        elif (dieta == "no"  or dieta == "No" or dieta == "NO" or dieta == "n"):
            dieta = "keto" #!!!!!
            break

    comida_del_dia = input(f"de que comida del dia te interesa saber? ({sty_opciones}desayuno{c.Style.RESET_ALL}/{sty_opciones}almuerzo{c.Style.RESET_ALL}/{sty_opciones}merienda{c.Style.RESET_ALL}/{sty_opciones}cena{c.Style.RESET_ALL}) ")
    match comida_del_dia:

        case "desayuno" | "merienda":
            if dieta == "vegetariano":
                print("entre nuestras opciones te recomendamos esto...")
                print(f"1: {sty_opciones}tostada con palta {c.Style.RESET_ALL}({c.Fore.GREEN}$100{c.Style.RESET_ALL})")
                print(f"2: {sty_opciones}una fruta a eleccion {c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL})")
                comida_int = int(input("opcion: "))
                while comida_int:
                    match comida_int:
                        case 1:
                            comida = "tostada con palta"
                            costo += 100
                            break
                        case 2:
                            comida = "una fruta a eleccion"
                            costo += 50
                            break
                        case _:
                            print(err_num)
                            print(f"1: {sty_opciones}tostada con palta {c.Style.RESET_ALL}({c.Fore.GREEN}$100{c.Style.RESET_ALL})")
                            print(f"2: {sty_opciones}una fruta a eleccion {c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL})")
                            comida_int = int(input("opcion: "))

            elif dieta == "vegano":
                print("entre nuestras opciones te recomendamos esto...")
                print(f"1: {sty_opciones}donas veganas {c.Style.RESET_ALL}({c.Fore.GREEN}$100{c.Style.RESET_ALL})")
                print(f"2: {sty_opciones}medialuna vegana {c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL})")
                comida_int = int(input("opcion: "))
                while comida_int:
                    match comida_int:
                        case 1:
                            comida = "donas veganas"
                            costo += 100
                            break
                        case 2:
                            comida = "medialunas veganas"
                            costo += 50
                            break
                        case _:
                            print(err_num)
                            print(f"1: {sty_opciones}donas veganas {c.Style.RESET_ALL}({c.Fore.GREEN}$100{c.Style.RESET_ALL})")
                            print(f"2: {sty_opciones}medialunas veganas {c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL})")
                            comida_int = int(input("opcion: "))

            else:
                print("entre nuestras opciones te recomendamos esto...")
                print(f"1: {sty_opciones}muffin con almendra {c.Style.RESET_ALL}({c.Fore.GREEN}$100{c.Style.RESET_ALL})")
                print(f"2: {sty_opciones}tostada con manteca o mermelada a eleccion {c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL})")
                comida_int = int(input("opcion: "))
                while comida_int:
                    match comida_int:
                        case 1:
                            comida = "muffin con almendra"
                            costo += 100
                            break
                        case 2:
                            comida = "tostada con manteca o mermelada a eleccion"
                            costo += 50
                            break
                        case _:
                            print(err_num)
                            print(f"1: {sty_opciones}muffin con almendra {c.Style.RESET_ALL}({c.Fore.GREEN}$100{c.Style.RESET_ALL})")
                            print(f"2: {sty_opciones}tostada con manteca o mermelada a eleccion {c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL})")
                            comida_int = int(input("opcion: "))

            print("que vas a tomar?...")
            print(f"1: {sty_opciones}te{c.Style.RESET_ALL}({c.Fore.GREEN}$25{c.Style.RESET_ALL})")
            print(f"2: {sty_opciones}yogur{c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL}) ({c.Fore.YELLOW}CONTIENE LACTEOS{c.Style.RESET_ALL})")
            print(f"3: {sty_opciones}nada{c.Style.RESET_ALL}")
            bebida_int = int(input("opcion: "))
            while bebida_int:
                match bebida_int:
                    case 1:
                        bebida = "te"
                        costo += 25
                        break
                    case 2:
                        bebida = "yogur"
                        costo += 50
                        break
                    case 3:
                        bebida = ""
                        break
                    case _:
                        print(err_num)
                        print(f"1: {sty_opciones}te{c.Style.RESET_ALL}({c.Fore.GREEN}$25{c.Style.RESET_ALL})")
                        print(f"2: {sty_opciones}yogur{c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL}) ({c.Fore.YELLOW}CONTIENE LACTEOS{c.Style.RESET_ALL})")
                        print(f"3: {sty_opciones}nada{c.Style.RESET_ALL}")
                        bebida_int = int(input("opcion: "))

            if not (bebida == 2 or bebida == 3): # chatgpt puede tener un poco de agua
                print("preferiria tomar con...")
                print(f"1: {sty_opciones}azucar{c.Style.RESET_ALL}")
                print(f"2: {sty_opciones}edulcorante{c.Style.RESET_ALL}")
                print(f"3: {sty_opciones}nada{c.Style.RESET_ALL}")
                agregado_int = int(input("opcion: "))
                while agregado_int:
                    match agregado_int:
                        case 1:
                            agregado = "con azucar"
                            break
                        case 2:
                            agregado = "con edulcorante"
                            break
                        case 3:
                            agregado = ""
                            break
                        case _:
                            print(err_typo)
                            print(f"1: {sty_opciones}azucar{c.Style.RESET_ALL}")
                            print(f"2: {sty_opciones}edulcorante{c.Style.RESET_ALL}")
                            print(f"3: {sty_opciones}nada{c.Style.RESET_ALL}")
                            agregado_int = int(input("opcion: "))

        case "almuerzo" | "cena":
            saludable = input(f"vas a querer que te recomendemos comida{sty_opciones} saludable{c.Style.RESET_ALL}? {sty_si_no} ")
            match saludable:

                case "si":
                    if dieta == "vegetariano":
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}dos patys de lentejas con pure de papas {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                        print(f"2: {sty_opciones}tarta de acelga con morron {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                        comida_int = int(input("opcion: "))
                        while comida_int:
                            match comida_int:
                                case 1:
                                    comida = "dos patys de lentejas con pure de papas"
                                    costo += 500
                                    break
                                case 2:
                                    comida = "tarta de acelga con morron"
                                    costo += 400
                                    break
                                case _:
                                    print(err_typo)
                                    print(f"1: {sty_opciones}dos patys de lentejas con pure de papas {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                                    print(f"2: {sty_opciones}tarta de acelga con morron {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                                    comida_int = int(input("opcion: "))

                    elif dieta == "vegano":
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}tofu con tomates y arroz {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                        print(f"2: {sty_opciones}hummus {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                        comida_int = int(input("opcion: "))
                        while comida_int:
                            match comida_int:
                                case 1:
                                    costo += 500
                                    comida = "tofu con tomates y arroz"
                                    break
                                case 2:
                                    costo += 400
                                    comida = "hummus"
                                    break
                                case _:
                                    print(err_typo)
                                    print(f"1: {sty_opciones}tofu con tomates y arroz {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                                    print(f"2: {sty_opciones}hummus {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                                    comida_int = int(input("opcion: "))

                    else:
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}churrasco con fideos con aceite y ajo {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                        print(f"2: {sty_opciones}milanesas al horno con pure {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                        comida_int = int(input("opcion: "))
                        while comida_int:
                            match comida_int:
                                case 1:
                                    costo += 500
                                    comida = "churrasco con fideos con aceite y ajo"
                                    break
                                case 2:
                                    costo += 400
                                    comida = "milanesas al horno con pure"
                                    break
                                case _:
                                    print(err_typo)
                                    print(f"1: {sty_opciones}churrasco con fideos con aceite y ajo {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                                    print(f"2: {sty_opciones}milanesas al horno con pure {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                                    comida_int = int(input("opcion: "))

                case "no":
                    if dieta == "vegetariano":
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}dos patys de lentejas con pure de papas {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                        print(f"2: {sty_opciones}tarta de acelga con morron {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                        comida_int = int(input("opcion: "))
                        while comida_int:
                            match comida_int:
                                case 1:
                                    costo += 500
                                    comida = "dos patys de lentejas con pure de papas"
                                    break
                                case 2:
                                    costo += 400
                                    comida = "tarta de acelga con morron"
                                    break
                                case _:
                                    print(err_typo)
                                    comida_int = int(input("opcion: "))
                                    print(f"1: {sty_opciones}dos patys de lentejas con pure de papas {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                                    print(f"2: {sty_opciones}tarta de acelga con morron {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")

                    elif dieta == "vegano":
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}tofu con tomates y arroz {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                        print(f"2: {sty_opciones}hummus {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                        comida_int = int(input("opcion: "))
                        while comida_int:
                            match comida_int:
                                case 1:
                                    costo += 500
                                    comida = "tofu con tomates y arroz"
                                    break
                                case 2:
                                    costo += 400
                                    comida = "hummus"
                                    break
                                case _:
                                    print(err_typo)
                                    print(f"1: {sty_opciones}tofu con tomates y arroz {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                                    print(f"2: {sty_opciones}hummus {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                                    comida_int = int(input("opcion: "))

                    else:
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}churrasco con fideos con aceite y ajo {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                        print(f"2: {sty_opciones}milanesas al horno con pure {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                        comida_int = int(input("opcion: "))
                        while comida_int:
                            match comida_int:
                                case 1:
                                    costo += 500
                                    comida = "churrasco con fideos con aceite y ajo"
                                    break
                                case 2:
                                    costo += 400
                                    comida = "milanesas al horno con pure"
                                    break
                                case _:
                                    print(err_typo)
                                    print(f"1: {sty_opciones}churrasco con fideos con aceite y ajo {c.Style.RESET_ALL}({c.Fore.GREEN}$500{c.Style.RESET_ALL})")
                                    print(f"2: {sty_opciones}milanesas al horno con pure {c.Style.RESET_ALL}({c.Fore.GREEN}$400{c.Style.RESET_ALL})")
                                    comida_int = int(input("opcion: "))

            print("en cuanto a bebidas...")
            print(f"1: {sty_opciones}agua {c.Style.RESET_ALL}")
            print(f"2: {sty_opciones}gaseosa {c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL})")
            print(f"3: {sty_opciones}nada{c.Style.RESET_ALL}")
            bebida_int = int(input("opcion: "))
            while bebida_int:
                match bebida_int:
                    case 1:
                        bebida = "agua"
                        break
                    case 2:
                        bebida = "gaseosa"
                        costo += 50
                        break
                    case 3:
                        bebida = "nada"
                        break
                    case _:
                        print(err_typo)
                        print(f"1: {sty_opciones}agua {c.Style.RESET_ALL}")
                        print(f"2: {sty_opciones}gaseosa {c.Style.RESET_ALL}({c.Fore.GREEN}$50{c.Style.RESET_ALL})")
                        print(f"3: {sty_opciones}nada{c.Style.RESET_ALL}")
                        bebida_int = int(input("opcion: "))

            hielo = ""
            while hielo:
                hielo = input(f"desea agregarle {sty_opciones}hielo{c.Style.RESET_ALL} a su bebida sin costo? {sty_si_no}")
                match hielo:
                    case "si":
                        bebida = f"{bebida} con hielo"
                        break
                    case "no":
                        bebida = bebida
                        break
                    case _:
                        print(err_typo)
                        hielo = input(f"desea agregarle {sty_opciones}hielo{c.Style.RESET_ALL} a su bebida? {sty_si_no}")

    gente = int(input("cuantos van a comer? (hasta 4 personas aplica un descuento) ")) #ok
    while gente:
        match gente:
            case 1:
                descuento = 0.9
                break
            case 2:
                descuento = 0.85
                break
            case _:
                descuento = 0.8
                break

    bebida_final = "" #ok
    if bebida != "":
        bebida_final = f" y {bebida}"
    eliminado = ""
    while eliminado:
        eliminado += input("escribe las cosas que querrias ver eliminadas de tu comida (no mandes nada para terminar)\nentrada: ")
        if eliminado != "":
            eliminado += "(menos:"
        while eliminado != "":
            eliminado += input("escribe las cosas que querrias ver eliminadas de tu comida (vacio para terminar)\nentrada: ")
            eliminado += ", "
        if eliminado != "":
            eliminado += ")"
        break
    break #sin inputs despues de esto


recomendacion = f"{sty_opciones}{comida}{bebida_final}{agregado}{c.Style.RESET_ALL}"
poco_presupuesto = ""
if presupuesto < costo:
    poco_presupuesto = f"aunque tu presupuesto ({c.Fore.YELLOW}${presupuesto}{c.Style.RESET_ALL}) sea poco sabemos que esta comida vale la pena"
else:
    poco_presupuesto = f"porque tu presupuesto ({c.Fore.GREEN}${presupuesto}{c.Style.RESET_ALL}) te alcanza"

tacc_final = ""
if tacc != "no":
    tacc_final = "(sin tacc)"
else:
    tacc_final = ""

costo_final = f"{c.Fore.GREEN}${costo * descuento}{c.Style.RESET_ALL}"

if comida_del_dia == "almuerzo" or "cena":
    comida_grande = "que llena"
else:
    comida_grande = "liviano"

razon_1 = f"\n1: tu dieta es {sty_opciones + dieta + c.Style.RESET_ALL}"
razon_2 = f"\n2: estas planeando comer algo {c.Fore.GREEN + comida_grande + c.Style.RESET_ALL}"
razon_3 = f"\n3: {poco_presupuesto}, siendo el costo final {costo_final}"

razon_final = f"{razon_1}\n{razon_2}\n{razon_3}"

print(f" te recomendamos {recomendacion} {eliminado} {tacc_final} {c.Fore.GREEN}porque...{c.Style.RESET_ALL}\n{razon_final}")
print(f"esperamos que vengas pronto! nos encontramos en {c.Fore.GREEN}Avellaneda frente a la plaza Adolfo Alsina, nos vemos!{c.Style.RESET_ALL}")
