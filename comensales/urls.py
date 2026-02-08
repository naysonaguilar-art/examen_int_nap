from django.urls import path
from . import views

urlpatterns = [
    # URLs de comensales (las que ya tenías)
    path("comensales_detail/<int:id_comensale>", views.comensales_detail, name="comensales_detail"),
    path("comensales_list/", views.comensales_list, name="comensales_list"),

    # URLs de películas (las nuevas del PDF)
    # 1. Listado de películas
    path("peliculas/", views.peliculas_list_view, name="peliculas_list"),

    # 2. Detalle de película
    path("peliculas/<int:id_pelicula>/", views.pelicula_detail_view, name="pelicula_detail"),

    # 3. Funciones de una película
    path("peliculas/<int:id_pelicula>/funciones/", views.funciones_list_view, name="funciones_list"),

    # 4. Entradas vendidas de una función
    path("funciones/<int:id_funcion>/entradas/", views.entradas_list_view, name="entradas_list"),

    # 5. Snacks comprados por entrada
    path("entradas/<int:id_entrada>/snacks/", views.snacks_list_view, name="snacks_list"),

    # 6. Cartelera activa
    path("cartelera/", views.cartelera_view, name="cartelera"),

    # 7. Home del cine
    path("", views.home_view, name="home"),
]