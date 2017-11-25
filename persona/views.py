# -*- coding: utf-8 -*-
from django.shortcuts import render
from persona.Persona import Persona, Trabajo


def persona(request, persona_id):
    data = {
       'id': persona_id,
       'nombre':"franklin",
       'apellido':"Briones",
       }
    return render(request, 'persona/persona.html', data)


def personas(request):
    t1 = Trabajo(1, "programador", "patito", 1000)
    t2 = Trabajo(2, "practicante", "gobierno", 2500)
    t3 = Trabajo(8, "cocinero", "gran cheff", 1000)
    
    p1 = Persona(1, "franklin", "Briones", 24,[t1,t3])
    p2 = Persona(2, "Eduardo", "Alarcon", 28,[t1,t2,t3])
    p3 = Persona(3, "Erick", "Briones", 16,[t1,t2])
   
    data = {
       'personas':[p1,p2,p3]
       }
    
    
    return render(request, 'persona/personas.html', data) 