from django.db import models


class PersonManager(models.Manager):

    def __str__(self):
        return f'{self.identification} - {self.full_name()}'

    def mapper(self):
        return dict(
            id=self.id,
            name=self.name,
            last_name=self.last_name,
            identification=self.identification,
            gender=self.gender,
            age=self.age,
            phone=self.phone
        )

    # Get Person data to a Student
    def is_deleted(self, pk=None):
        person = None
        try:
            person = self.filter(id=pk, auth_state='A').first()
        except:
            pass
        return person

    def get_person_list(self):
        return self.filter(auth_state='A').order_by('last_name')

    def get_person_detail_data(self, pk=None):
        try:
            return self.filter(id=pk, auth_state='A').first()
        except:
            return None

    def get_many_persons(self, persons=None):
        result = None
        try:
            if persons is not None:
                result = list(self.in_bulk(persons).values())
        except:
            pass
        return result

    def get_person_by_user(self, user_id=None):
        try:
            return self.select_related('student', 'teacher').\
                filter(user=user_id, auth_state='A').first()
        except:
            return None
