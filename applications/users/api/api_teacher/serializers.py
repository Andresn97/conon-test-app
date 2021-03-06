from rest_framework import serializers

from applications.users.models import Teacher, Person
from applications.users.functions import is_person_assigned


# Create or Update Teacher Serializer
class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Teacher
        exclude = [
            'updated_at',
            'auth_state'
        ]

    # Return Teacher Users
    def get_user(self, obj):
        return Teacher.objects.get_user(obj.id)

    # Validation if the Person exists
    def validate_person(self, value):
        person = Person.objects.is_deleted(value.id)
        if person is None:
            raise serializers.ValidationError('Error, esta Persona no existe.')
        return value

    # Create Teacher Method
    def create(self, validated_data):
        if is_person_assigned(validated_data['person'].id):
            raise serializers.ValidationError(
                {
                    'person': ['Error, esta Persona ya fue asignada.']
                }
            )

        teacher = Teacher(**validated_data)
        teacher.save()
        return teacher

    # Update Teacher Method
    def update(self, instance, validated_data):
        if instance.person != validated_data['person']:
            raise serializers.ValidationError(
                {
                    'person': ['Error, no se puede cambiar de Persona.']
                }
            )
        update_teacher = super().update(instance, validated_data)
        update_teacher.save()
        return update_teacher

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = None

        if data['user']:
            user = {
                'id': data['user'][0],
                'username': data['user'][1],
                'email': data['user'][2]
            }
        else:
            user = {
                'id': 0,
                'username': 'No existe',
                'email': 'No existe'
            }

        return {
            'id': instance.id,
            'person': {
                'id': instance.person.id,
                'identification_type': instance.person.get_identification_type_display(),
                'identification': instance.person.identification,
                'name': instance.person.name,
                'last_name': instance.person.last_name,
                'gender': instance.person.get_gender_display(),
                'age': instance.person.age,
                'phone': instance.person.phone
            },
            'user': user,
            'title': instance.title,
            'objective': instance.objective,
            ''
            'created_at': instance.created_at
        }


class CoordinatorSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True
    )
    name = serializers.CharField(
        read_only=True
    )

    class Meta:
        fields = [
            'id',
            'name'
        ]

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'name': f"{instance['person__name']} {instance['person__last_name']}"
        }


class TeachersShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        include = [
            'id',
            'person',
            'title'
        ]

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'identification': instance['person__identification'],
            'name': f"{instance['person__name']} {instance['person__last_name']}",
            'title': instance['title'],
            'person': instance['person']
        }


class TeacherObjectShortSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance['teacher_id'],
            'identification': instance['teacher__person__identification'],
            'name': f"{instance['teacher__person__name']} {instance['teacher__person__last_name']}",
        }


class TeacherForConversationSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance['teacher__person__user'],
            'identification': instance['teacher__person__identification'],
            'name': f"{instance['teacher__person__name']} {instance['teacher__person__last_name']}",
        }


class TeacherShorListByConversation(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'identification': instance['person__identification'],
            'name': f"{instance['person__name']} {instance['person__last_name']}",
            'user': instance['person__user']
        }


class TeacherForNewConversation(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance['person__user'],
            'identification': instance['person__identification'],
            'name': f"{instance['person__name']} {instance['person__last_name']}",
        }
