from django.shortcuts import render

# Create your views here.
def renderIndex(request):
    datos={"img1":"lebron.jpg",
           "img2":"curry.jpg",
           "img3":"kevin.jpg"}
    return render(request,"PruebaApp/index.html",datos)

def renderLebron(request):
    datos= {"Nombre":"Lebron James",
            "Equipo":"Los Angeles Lakers",
            "Edad":"39",
            "Campeonatos":"5",
            "img":"lebron.jpg"}
    return render(request,"PruebaApp/jugador.html",datos)


def renderCurry(request):
    datos= {"Nombre":"Stephen Curry",
            "Equipo":"Golden State Warriors",
            "Edad":"32",
            "Campeonatos":"3",
            "img":"curry.jpg"}
    return render(request,"PruebaApp/jugador.html",datos)


def renderKevin(request):
    datos= {"Nombre":"Kevin Durant",
            "Equipo":"Golden State Warriors",
            "Edad":"34",
            "Campeonatos":"2",
            "img":"kevin.jpg"}
    return render(request,"PruebaApp/jugador.html",datos)