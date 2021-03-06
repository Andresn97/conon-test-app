
from rest_framework import serializers

from applications.ac.models import TeamDetailAc, TeamAc
from applications.users.models import User


class TeamDetailAcSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamDetailAc
        exclude = [
            'updated_at',
            'auth_state'
        ]

    # State Role Type
    def validate_role_type(self, value):
        if value < 0 or value > 4:
            raise serializers.ValidationError(
                {
                    'role_type': 'Error, el rol enviado no es el correcto; '
                                 'consulte con el Administrador.'
                }
            )
        return value

    # General Validate
    def validate(self, attrs):
        if not TeamAc.objects.exists_team_ac(attrs['team_ac'].id):
            raise serializers.ValidationError(
                {
                    'team_ac': 'Error, el grupo ingresado no existe o está inactivo; '
                               'consulte con el Administrador.'
                }
            )
        if not User.objects.user_exists(attrs['owner'].id):
            raise serializers.ValidationError(
                {
                    'owner': 'Error, el usuario ingresado no existe o está inactivo; '
                             'consulte con el Administrador.'
                }
            )

        return attrs

    # Create Team Detail AC
    def create(self, validated_data):
        if TeamDetailAc.objects.get_team_ac_students_count(validated_data['team_ac'].id) == 4:
            raise serializers.ValidationError(
                {
                    'team_ac': 'Error, el grupo ya tiene cuatro integrantes en el grupo.'
                }
            )
        if TeamDetailAc.objects.exists_user_in_team_ac(
                validated_data['team_ac'].id, validated_data['owner'].id
        ):
            raise serializers.ValidationError(
                {
                    'owner': 'Error, el Estudiante enviado ya ha sido agregado a este grupo.'
                }
            )
        team_detail_ac = TeamDetailAc(**validated_data)
        team_detail_ac.save()
        return team_detail_ac

    # Update Team Detail ABP
    def update(self, instance, validated_data):
        if instance.owner != validated_data['owner']:
            raise serializers.ValidationError(
                {
                    'owner': 'No se puede cambiar de referencia de Usuario.'
                }
            )
        update_team_detail_abp = super().update(instance, validated_data)
        update_team_detail_abp.save()
        return update_team_detail_abp


class TeamDetailAcListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamDetailAc
        exclude = [
            'updated_at',
            'auth_state'
        ]

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'team_ac': {
                'id': instance.team_ac.id,
                'observations': instance.team_ac.observations,
                'ac': {
                    'id': instance.team_ac.ac.id,
                    'state': instance.team_ac.ac.state
                },
            },
            'owner': {
                'id': instance.owner.id,
                'name': instance.owner.__str__()
            },
            'role_type': instance.role_type,
            'active': instance.active,
            'created_at': instance.created_at
        }


class TeamDetailAcShortListSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'owner': {
                'id': instance.owner.id,
                'name': instance.owner.__str__()
            },
            'role_type': instance.role_type,
            'active': instance.active,
            'created_at': instance.created_at
        }
