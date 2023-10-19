from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class SecretarioAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretarioAcademico
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class PlanificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanificacionAcademica
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioCurso
        fields = '__all__'

class ProfesorCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesorCurso
        fields = '__all__'

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = '__all__'