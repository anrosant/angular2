from rest_framework import serializers
from .models import Platillo


'''class SerieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Serie
		fields = ('id', 'name', 'release_date', 'rating', 'category')

		pk = serializers.IntegerField(read_only=True)
		name = serializers.CharField()
		release_date = serializers.DateField()
		rating = serializers.IntegerField()
		category = serializers.ChoiceField(choices=Serie.CATEGORIES_CHOICES)

		def create(self, validated_data):
			return Serie.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.name = validated_data.get('name', instance.name)
			instance.release_date = validated_data.get('release_date', instance.release_date)
			instance.rating = validated_data.get('rating', instance.rating)
			instance.category = validated_data.get('category', instance.category)
			instance.save()
			return instance'''

class PlatilloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Platillo
		fields = ('idP','titulo', 'tipo', 'precio', 'cantidad', 'distancia','valorNutricional','imagen','valoracion')

		idP = serializers.IntegerField()
		titulo = serializers.CharField()
		tipo = serializers.CharField()
		precio = serializers.FloatField()
		cantidad = serializers.IntegerField()
		distancia = serializers.FloatField()
		valorNutricional = serializers.FloatField()
		imagen = serializers.CharField()
		valoracion = serializers.IntegerField()

		def create(self, validated_data):
			return Platillo.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.idP = validated_data.get('idP', instance.idP)
			instance.titulo = validated_data.get('titulo', instance.titulo)
			instance.tipo = validated_data.get('tipo', instance.tipo)
			instance.precio = validated_data.get('precio', instance.precio)
			instance.cantidad = validated_data.get('cantidad', instance.cantidad)
			instance.distancia = validated_data.get('distancia', instance.distancia)
			instance.valorNutricional = validated_data.get('valorNutricional', instance.valorNutricional)
			instance.imagen = validated_data.get('imagen', instance.imagen)
			instance.valoracion = validated_data.get('valoracion', instance.valoracion)
			instance.save()
			return instance
