from django.shortcuts import render

# Create your views here.
def comensales_detail(request, id_comensale):
    print("ID Comensales: {}".format(id_comensale))
    return render(request,"comensales/comensales_detail.html", context={"id_comensales":id_comensale})

def comensales_list(request):
    #data_context={
    #    "nombre":"johan",
    #    "edad": 26,
    #    "pais":"Peru"
    #}
    data_context=[
        {
            "nombre": "johan aguilar",
            "edad": 26,
            "pais": "Peru",
            "dni": "22222222",
            "vigente": True,
        },
        {
            "nombre": "carlos rodriguez",
            "edad": 30,
            "pais": "Brasil",
            "dni": "22222222",
            "vigente": True,
        },
        {
            "nombre": "george martinez",
            "edad": 20,
            "pais": "chile",
            "dni": "66666666",
            "vigente": False,
        }
    ]
    return render(request,"comensales/comensales_list.html", context={"data":data_context})

def peliculas_list_view(request):
    # Lista hardcodeada con id, titulo, duracion_min, genero, clasificacion
    data_context = [
        {"id": 1, "titulo": "Avatar", "duracion_min": 192, "genero": "Ciencia Ficción", "clasificacion": "PG-13"},
        {"id": 2, "titulo": "Top Gun", "duracion_min": 131, "genero": "Acción", "clasificacion": "PG-13"},
        {"id": 3, "titulo": "Spider-Man", "duracion_min": 148, "genero": "Superhéroes", "clasificacion": "PG-13"},
        {"id": 4, "titulo": "Jurassic World", "duracion_min": 147, "genero": "Aventura", "clasificacion": "PG-13"},
        {"id": 5, "titulo": "Doctor Strange", "duracion_min": 126, "genero": "Fantasía", "clasificacion": "PG-13"},
        {"id": 6, "titulo": "Minions", "duracion_min": 87, "genero": "Animación", "clasificacion": "PG"},
        {"id": 7, "titulo": "Thor", "duracion_min": 119, "genero": "Superhéroes", "clasificacion": "PG-13"},
        {"id": 8, "titulo": "Black Panther", "duracion_min": 161, "genero": "Superhéroes", "clasificacion": "PG-13"},
        {"id": 9, "titulo": "Los Fabelmans", "duracion_min": 151, "genero": "Drama", "clasificacion": "PG-13"},
        {"id": 10, "titulo": "Babylon", "duracion_min": 189, "genero": "Drama", "clasificacion": "R"},
        {"id": 11, "titulo": "El Gato con Botas", "duracion_min": 102, "genero": "Animación", "clasificacion": "PG"},
        {"id": 12, "titulo": "M3GAN", "duracion_min": 102, "genero": "Terror", "clasificacion": "PG-13"},
        {"id": 13, "titulo": "Oppenheimer", "duracion_min": 180, "genero": "Drama", "clasificacion": "R"},
        {"id": 14, "titulo": "Barbie", "duracion_min": 114, "genero": "Comedia", "clasificacion": "PG-13"},
        {"id": 15, "titulo": "Guardianes de la Galaxia", "duracion_min": 150, "genero": "Superhéroes", "clasificacion": "PG-13"},
    ]
    return render(request, "cine/peliculas_list.html", context={"peliculas": data_context})


def pelicula_detail_view(request, id_pelicula):
    # Lista hardcodeada de películas
    peliculas = [
        {"id": 1, "titulo": "Avatar", "duracion_min": 192, "genero": "Ciencia Ficción", "clasificacion": "PG-13"},
        {"id": 2, "titulo": "Top Gun", "duracion_min": 131, "genero": "Acción", "clasificacion": "PG-13"},
        {"id": 3, "titulo": "Spider-Man", "duracion_min": 148, "genero": "Superhéroes", "clasificacion": "PG-13"},
    ]

    # Buscar la película por id
    pelicula = None
    for p in peliculas:
        if p["id"] == id_pelicula:
            pelicula = p
            break

    return render(request, "cine/pelicula_detail.html", context={"pelicula": pelicula})


def funciones_list_view(request, id_pelicula):
    # Lista de funciones hardcodeada
    funciones = [
        {"id": 1, "hora": "14:00", "precio": 8.50, "estado": "Disponible"},
        {"id": 2, "hora": "17:30", "precio": 10.00, "estado": "Disponible"},
        {"id": 3, "hora": "20:00", "precio": 12.00, "estado": "Agotado"},
    ]

    # Buscar título de la película (opcional, puedes solo enviar el id)
    titulo_pelicula = f"Película #{id_pelicula}"

    return render(request, "cine/funciones_list.html", context={
        "pelicula": {"titulo": titulo_pelicula},
        "funciones": funciones
    })


def entradas_list_view(request, id_funcion):
    # Lista de entradas hardcodeada
    entradas = [
        {"id": 1, "codigo": "E001", "asiento": "A5", "estado": "Vendida", "fecha_venta": "2025-02-01"},
        {"id": 2, "codigo": "E002", "asiento": "A6", "estado": "Vendida", "fecha_venta": "2025-02-01"},
        {"id": 3, "codigo": "E003", "asiento": "B3", "estado": "Reservada", "fecha_venta": "2025-02-02"},
    ]

    return render(request, "cine/entradas_list.html", context={"entradas": entradas})


def snacks_list_view(request, id_entrada):
    # Lista de TODOS los snacks (con entrada_id)
    todos_snacks = [
        {"entrada_id": 1, "producto": "Palomitas grandes", "cantidad": 2, "precio_unitario": 5.00},
        {"entrada_id": 1, "producto": "Refresco", "cantidad": 1, "precio_unitario": 3.50},
        {"entrada_id": 2, "producto": "Nachos", "cantidad": 1, "precio_unitario": 4.00},
        {"entrada_id": 3, "producto": "Chocolate", "cantidad": 3, "precio_unitario": 2.00},
    ]

    # Filtrar solo los snacks de esta entrada
    snacks = []
    for snack in todos_snacks:
        if snack["entrada_id"] == id_entrada:
            snacks.append(snack)

    # Calcular total
    total_snacks = 0
    for snack in snacks:
        total_snacks += snack["cantidad"] * snack["precio_unitario"]

    return render(request, "cine/snacks_list.html", context={
        "entrada_id": id_entrada,
        "snacks": snacks,
        "total_snacks": total_snacks
    })


def cartelera_view(request):
    # Lista con películas activas o no
    todas_peliculas = [
        {"id": 1, "titulo": "Avatar", "activa": True},
        {"id": 2, "titulo": "Top Gun", "activa": True},
        {"id": 3, "titulo": "Spider-Man", "activa": False},
        {"id": 4, "titulo": "Jurassic World", "activa": True},
    ]

    # Filtrar solo las activas
    peliculas = []
    for p in todas_peliculas:
        if p["activa"]:
            peliculas.append(p)

    return render(request, "cine/cartelera.html", context={"peliculas": peliculas})

def home_view(request):
    return render(request, "cine/home.html", context={
        "nombre_cine": "Cine Premium",
        "pelicula_destacada": "Oppenheimer",
        "total_funciones": 12
    })