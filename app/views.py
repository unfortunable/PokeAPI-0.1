from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
from .serializers import PokemonSerializer
import json
from rest_framework import viewsets
import requests

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def create(self, request):
        #criando a variavel cep e requisitando-a
        pokemon = request.data.get('name')

        #site para as requisicoes
        site = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        print (site)
        #definindo uma requisicao
        requisition = requests.get(site)

        json = requisition.json()

        pokemon = json.get('name', '')

        pokemons_get = {
            "name": f'pokemon'
        }

        myserializer = PokemonSerializer(data=pokemons_get)
        if myserializer.is_valid():
            pokemon_searched = Pokemon.objects.filter(pokemon=pokemon)
            pokemon_searched_exists = pokemon_searched.exists()


            if pokemon_searched_exists:
                return Response({"warning":"Your pokemon is already on SQL"})
            
            myserializer.save()
            return Response(myserializer.data)
        else:
            print(myserializer.errors)
            return Response({"aviso":f"An error has been found"})