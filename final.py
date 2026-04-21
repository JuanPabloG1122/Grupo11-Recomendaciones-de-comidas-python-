## --- SPRINT 2 ---
#   1- Añadir dos promedios, uno general y otro condicionado (Este puede variar segun que comida del dia sea x ejempl)
#   2- Justificar con los promedios anteriores la recomendacion final (Dentro de todo esto no tiene)
#   3- Con Maximos y minimos sacar datos de promedios con el punto 1

# TODO list
# TODO adaptar el codigo a funciones
# TODO arreglar lo del desayuno (si pones que no le manda mecha igual; linea 131)

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

# BANDERAS
tacc = False
presupuesto = 0
costo = 0
cantidad = 0
descuento = 0
comida = ""
gusto = ""
agregado = ""
bebida = ""
combo = ""
dieta = ""

# FUNCIONES
def pregunta_si_no(pregunta):
    print(sty_fore_verde + pregunta + sty_reset)
    x = input(sty_si_no + " ")
    while True:
        if x == "si" or x == "s" or x == "SI" or x == "S" :
            resultado = True
            break
        elif x == "no" or x == "n" or x == "NO" or x == "N" :
            resultado = True
            break
        else:
            print(err_typo)
            print(sty_fore_verde + pregunta + sty_reset)
            x = input(sty_si_no)
    return resultado


# ESTILIZACION (al chat gpt le pregunte lo basico, esto fue hecho por una persona de carne y hueso)
sty_fore_verde = "\033[32m"
sty_fore_azul = "\033[33m"
sty_fore_amarillo = "\033[34m"
sty_back_verde = "\033[42m"
sty_back_azul = "\033[43m"
sty_back_amarillo = "\033[44m"
sty_reset = "\033[0m"

sty_si_no = f"({sty_fore_azul}si{sty_reset}/{sty_fore_amarillo}no{sty_reset})"
sty_opciones = sty_fore_azul

err_typo = f"{sty_back_amarillo}error: escribiste mal, por favor escirbir de vuelta{sty_reset}"
err_num = f"{sty_back_amarillo}error: opcion invalida, por favor escirbir de vuelta{sty_reset}"

comida_budin = f"{sty_fore_azul}Budin de Banana{sty_reset}(costo: {sty_fore_verde}$100{sty_reset})"
comida_tostado = f"{sty_fore_azul}Tostado {sty_reset}(costo: {sty_fore_verde}$100{sty_reset})"
comida_medialuna = f"{sty_fore_azul}Medialuna {sty_reset}({sty_fore_verde}$50{sty_reset})"
comida_alfajor = f"{sty_fore_azul}Alfajor {sty_reset}({sty_fore_verde}$25{sty_reset})"

bebida_cafe = f"{sty_fore_azul}Cafe {sty_reset}({sty_fore_verde}$240{sty_reset})"
bebida_te = f"{sty_fore_azul}Te {sty_reset}({sty_fore_verde}$180{sty_reset})"
bebida_aguaS = f"{sty_fore_azul}Agua Saborizada {sty_reset}({sty_fore_verde}$270{sty_reset})"
bebida_yogurS = f"{sty_fore_azul}Yogur Saludable {sty_reset}({sty_fore_verde}$300{sty_reset})"
# no usamos colores rojos porque es un color agresivo, no es bueno para el negocio

while True:
    print(f"{sty_fore_verde}bienvenido al recomendador de del restaurante \"calle 11\" online!{sty_reset}")

    while presupuesto == 0:
        presupuesto = int(input(f"cuanto presupuesto hay para gastar? {sty_fore_verde}$"))
        match presupuesto: #tratamos de evitar que no nos sale error si no ponemos nada en el input, pero no se pudo.
            case _ if presupuesto <= 0:
                print(err_typo)
                presupuesto = 0
            case _ if presupuesto >= 1:
                break
            case _:
                print(err_typo)
                presupuesto = 0

    tacc = pregunta_si_no("puedes comer tacc?")


    # TODO if pregunta_si_no("estas siguiendo una dieta? "):
        #  . . .

    dieta = input(f"estas siguiendo una dieta? {sty_si_no} ")
    while dieta:
        if (dieta == "si" or dieta == "Si" or dieta == "SI" or dieta == "s"):
            dieta = input(f"cual dieta estas siguiendo? {sty_opciones}vegano{sty_reset}, {sty_opciones}vegetariano {sty_reset}o{sty_opciones} keto{sty_reset}? ")
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


    # TODO if pregunta_si_no(comida_del_dia):
        # . . .

    comida_del_dia = input(f"de que comida del dia te interesa saber? ({sty_opciones}desayuno{sty_reset}/{sty_opciones}almuerzo{sty_reset}/{sty_opciones}merienda{sty_reset}/{sty_opciones}cena{sty_reset}) ")
    match comida_del_dia:

        case "desayuno" | "merienda": #TODO
            if dieta == "vegetariano":
                print("entre nuestras opciones te recomendamos esto...")
                print(f"1: {sty_opciones}tostada con palta {sty_reset}({sty_fore_verde}$100{sty_reset})")
                print(f"2: {sty_opciones}una fruta a eleccion {sty_reset}({sty_fore_verde}$50{sty_reset})")
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
                            print(f"1: {sty_opciones}tostada con palta {sty_reset}({sty_fore_verde}$100{sty_reset})")
                            print(f"2: {sty_opciones}una fruta a eleccion {sty_reset}({sty_fore_verde}$50{sty_reset})")
                            comida_int = int(input("opcion: "))

            elif dieta == "vegano":
                print("entre nuestras opciones te recomendamos esto...")
                print(f"1: {sty_opciones}donas veganas {sty_reset}({sty_fore_verde}$100{sty_reset})")
                print(f"2: {sty_opciones}medialuna vegana {sty_reset}({sty_fore_verde}$50{sty_reset})")
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
                            print(f"1: {sty_opciones}donas veganas {sty_reset}({sty_fore_verde}$100{sty_reset})")
                            print(f"2: {sty_opciones}medialunas veganas {sty_reset}({sty_fore_verde}$50{sty_reset})")
                            comida_int = int(input("opcion: "))

            else:
                print("entre nuestras opciones te recomendamos esto...")
                print(f"1: {sty_opciones}muffin con almendra {sty_reset}({sty_fore_verde}$100{sty_reset})")
                print(f"2: {sty_opciones}tostada con manteca o mermelada a eleccion {sty_reset}({sty_fore_verde}$50{sty_reset})")
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
                            print(f"1: {sty_opciones}muffin con almendra {sty_reset}({sty_fore_verde}$100{sty_reset})")
                            print(f"2: {sty_opciones}tostada con manteca o mermelada a eleccion {sty_reset}({sty_fore_verde}$50{sty_reset})")
                            comida_int = int(input("opcion: "))

            print("que vas a tomar?...")
            print(f"1: {sty_opciones}te{sty_reset}({sty_fore_verde}$25{sty_reset})")
            print(f"2: {sty_opciones}yogur{sty_reset}({sty_fore_verde}$50{sty_reset}) ({sty_fore_amarillo}CONTIENE LACTEOS{sty_reset})")
            print(f"3: {sty_opciones}nada{sty_reset}")
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
                        print(f"1: {sty_opciones}te{sty_reset}({sty_fore_verde}$25{sty_reset})")
                        print(f"2: {sty_opciones}yogur{sty_reset}({sty_fore_verde}$50{sty_reset}) ({sty_fore_amarillo}CONTIENE LACTEOS{sty_reset})")
                        print(f"3: {sty_opciones}nada{sty_reset}")
                        bebida_int = int(input("opcion: "))

            if not (bebida == 2 or bebida == 3): # chatgpt puede tener un poco de agua
                print("preferiria tomar con...")
                print(f"1: {sty_opciones}azucar{sty_reset}")
                print(f"2: {sty_opciones}edulcorante{sty_reset}")
                print(f"3: {sty_opciones}nada{sty_reset}")
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
                            print(f"1: {sty_opciones}azucar{sty_reset}")
                            print(f"2: {sty_opciones}edulcorante{sty_reset}")
                            print(f"3: {sty_opciones}nada{sty_reset}")
                            agregado_int = int(input("opcion: "))

        case "almuerzo" | "cena":
            saludable = input(f"vas a querer que te recomendemos comida{sty_opciones} saludable{sty_reset}? {sty_si_no} ")
            match saludable:

                case "si":
                    if dieta == "vegetariano":
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}dos patys de lentejas con pure de papas {sty_reset}({sty_fore_verde}$500{sty_reset})")
                        print(f"2: {sty_opciones}tarta de acelga con morron {sty_reset}({sty_fore_verde}$400{sty_reset})")
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
                                    print(f"1: {sty_opciones}dos patys de lentejas con pure de papas {sty_reset}({sty_fore_verde}$500{sty_reset})")
                                    print(f"2: {sty_opciones}tarta de acelga con morron {sty_reset}({sty_fore_verde}$400{sty_reset})")
                                    comida_int = int(input("opcion: "))

                    elif dieta == "vegano":
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}tofu con tomates y arroz {sty_reset}({sty_fore_verde}$500{sty_reset})")
                        print(f"2: {sty_opciones}hummus {sty_reset}({sty_fore_verde}$400{sty_reset})")
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
                                    print(f"1: {sty_opciones}tofu con tomates y arroz {sty_reset}({sty_fore_verde}$500{sty_reset})")
                                    print(f"2: {sty_opciones}hummus {sty_reset}({sty_fore_verde}$400{sty_reset})")
                                    comida_int = int(input("opcion: "))

                    else:
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}churrasco con fideos con aceite y ajo {sty_reset}({sty_fore_verde}$500{sty_reset})")
                        print(f"2: {sty_opciones}milanesas al horno con pure {sty_reset}({sty_fore_verde}$400{sty_reset})")
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
                                    print(f"1: {sty_opciones}churrasco con fideos con aceite y ajo {sty_reset}({sty_fore_verde}$500{sty_reset})")
                                    print(f"2: {sty_opciones}milanesas al horno con pure {sty_reset}({sty_fore_verde}$400{sty_reset})")
                                    comida_int = int(input("opcion: "))

                case "no":
                    if dieta == "vegetariano":
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}dos patys de lentejas con pure de papas {sty_reset}({sty_fore_verde}$500{sty_reset})")
                        print(f"2: {sty_opciones}tarta de acelga con morron {sty_reset}({sty_fore_verde}$400{sty_reset})")
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
                                    print(f"1: {sty_opciones}dos patys de lentejas con pure de papas {sty_reset}({sty_fore_verde}$500{sty_reset})")
                                    print(f"2: {sty_opciones}tarta de acelga con morron {sty_reset}({sty_fore_verde}$400{sty_reset})")

                    elif dieta == "vegano":
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}tofu con tomates y arroz {sty_reset}({sty_fore_verde}$500{sty_reset})")
                        print(f"2: {sty_opciones}hummus {sty_reset}({sty_fore_verde}$400{sty_reset})")
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
                                    print(f"1: {sty_opciones}tofu con tomates y arroz {sty_reset}({sty_fore_verde}$500{sty_reset})")
                                    print(f"2: {sty_opciones}hummus {sty_reset}({sty_fore_verde}$400{sty_reset})")
                                    comida_int = int(input("opcion: "))

                    else:
                        print("entre nuestras opciones te recomendamos esto...")
                        print(f"1: {sty_opciones}churrasco con fideos con aceite y ajo {sty_reset}({sty_fore_verde}$500{sty_reset})")
                        print(f"2: {sty_opciones}milanesas al horno con pure {sty_reset}({sty_fore_verde}$400{sty_reset})")
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
                                    print(f"1: {sty_opciones}churrasco con fideos con aceite y ajo {sty_reset}({sty_fore_verde}$500{sty_reset})")
                                    print(f"2: {sty_opciones}milanesas al horno con pure {sty_reset}({sty_fore_verde}$400{sty_reset})")
                                    comida_int = int(input("opcion: "))

            print("en cuanto a bebidas...")
            print(f"1: {sty_opciones}agua {sty_reset}")
            print(f"2: {sty_opciones}gaseosa {sty_reset}({sty_fore_verde}$50{sty_reset})")
            print(f"3: {sty_opciones}nada{sty_reset}")
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
                        print(f"1: {sty_opciones}agua {sty_reset}")
                        print(f"2: {sty_opciones}gaseosa {sty_reset}({sty_fore_verde}$50{sty_reset})")
                        print(f"3: {sty_opciones}nada{sty_reset}")
                        bebida_int = int(input("opcion: "))

            hielo = ""
            while hielo:
                hielo = input(f"desea agregarle {sty_opciones}hielo{sty_reset} a su bebida sin costo? {sty_si_no}")
                match hielo:
                    case "si":
                        bebida = f"{bebida} con hielo"
                        break
                    case "no":
                        bebida = bebida
                        break
                    case _:
                        print(err_typo)
                        hielo = input(f"desea agregarle {sty_opciones}hielo{sty_reset} a su bebida? {sty_si_no}")

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


recomendacion = f"{sty_opciones}{comida}{bebida_final}{agregado}{sty_reset}"
poco_presupuesto = ""
if presupuesto < costo:
    poco_presupuesto = f"aunque tu presupuesto ({sty_fore_amarillo}${presupuesto}{sty_reset}) sea poco sabemos que esta comida vale la pena"
else:
    poco_presupuesto = f"porque tu presupuesto ({sty_fore_verde}${presupuesto}{sty_reset}) te alcanza"

tacc_final = ""
if tacc:
    tacc_final = ""
else:
    tacc_final = "(sin tacc)"

costo_final = f"{sty_fore_verde}${costo * descuento}{sty_reset}"

if comida_del_dia == "almuerzo" or "cena":
    comida_grande = "que llena"
else:
    comida_grande = "liviano"

razon_1 = f"\n1: tu dieta es {sty_opciones + dieta + sty_reset}"
razon_2 = f"\n2: estas planeando comer algo {sty_fore_verde + comida_grande + sty_reset}"
razon_3 = f"\n3: {poco_presupuesto}, siendo el costo final {costo_final}"

razon_final = f"{razon_1}\n{razon_2}\n{razon_3}"

print(f" te recomendamos {recomendacion} {eliminado} {tacc_final} {sty_fore_verde}porque...{sty_reset}\n{razon_final}")
print(f"esperamos que vengas pronto! nos encontramos en {sty_fore_verde}Avellaneda frente a la plaza Adolfo Alsina, nos vemos!{sty_reset}")
