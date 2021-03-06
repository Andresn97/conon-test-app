
from django.db import models


class FeaturedInformationSecretaryAcManager(models.Manager):

    def get_featured_information_secretary_ac_active_queryset(self):
        return self.select_related('team_detail_ac', 'member_ac').filter(
            team_detail_ac__active=True,
            team_detail_ac__auth_state='A',
            member_ac__active=True,
            member_ac__auth_state='A',
            active=True,
            auth_state='A'
        )

    def get_featured_information_secretary_ac_active_object_queryset(self, pk=None):
        try:
            return self.select_related('team_detail_ac', 'member_ac').filter(
                team_detail_ac__active=True,
                team_detail_ac__auth_state='A',
                member_ac__active=True,
                member_ac__auth_state='A',
                active=True,
                auth_state='A'
            ).get(id=pk)
        except:
            return None

    def get_featured_information_secretary_ac_list(self):
        return self.get_featured_information_secretary_ac_active_queryset().order_by('-created_at')

    def get_featured_information_secretary_by_team_detail(self, team_detail=None, member=None):
        try:
            return self.select_related('team_detail_ac', 'member_ac').filter(
                team_detail_ac=team_detail,
                team_detail_ac__active=True,
                team_detail_ac__auth_state='A',
                member_ac=member,
                member_ac__active=True,
                member_ac__auth_state='A',
                active=True,
                auth_state='A'
            )
        except:
            return None
