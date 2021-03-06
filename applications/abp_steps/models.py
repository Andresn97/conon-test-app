from django.db import models

from applications.base.models import BaseModel, BaseModelActive
from applications.users.models import User
from applications.abp.models import TeamAbp, TeamDetailAbp

from .api.api_opinion_step_one_abp.managers import OpinionStepOneAbpManager
from .api.api_interaction_step_one_abp.managers import InteractionStepOneAbpManager
from .api.api_question_step_one_abp.managers import QuestionStepOneAbpManager
from .api.api_answer_step_one_abp.managers import AnswerStepOneAbpManager
from .api.api_student_idea_step_two_abp.managers import StudentIdeaStepTwoAbpManager
from .api.api_rate_student_idea_step_two_abp.managers import RateStudentIdeaStepTwoAbpManager
from .api.api_learned_concept_step_three_abp.managers import LearnedConceptStepThreeAbpManager
from .api.api_learned_concept_reference_step_three_abp.managers import \
    LearnedConceptReferenceStepThreeAbpManager
from .api.api_unknown_concept_step_four_abp.managers import UnknownConceptStepFourAbpManager
from .api.api_unknown_concept_reference_step_four_abp.managers import \
    UnknownConceptReferenceStepFourAbpManager
from .api.api_perform_action_step_five_abp.managers import PerformActionStepFiveAbpManager
from .api.api_rate_perform_action_step_five_abp.managers import RatePerformActionStepFiveAbpManager
from .api.api_problem_definition_step_six_abp.managers import ProblemDefinitionStepSixAbpManager
from .api.api_problem_definition_reference_step_six_abp.managers import \
    ProblemDefinitionReferenceStepFixAbpManager
from .api.api_get_information_step_seven_abp.managers import GetInformationStepSevenAbpManager
from .api.api_information_reference_step_seven_abp.managers import \
    InformationReferenceStepSevenAbpManager
from .api.api_problem_resolution_step_eight_abp.managers import ProblemResolutionStepEightAbpManager


class OpinionStepOneAbp(BaseModel):
    opinion = models.TextField(
        null=False,
        blank=False
    )
    active = models.BooleanField(
        default=True,
        null=False,
        blank=True
    )

    team_detail_abp = models.ForeignKey(
        TeamDetailAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = OpinionStepOneAbpManager()

    def __str__(self):
        return self.opinion

    class Meta:
        db_table = 'opinion_step_one_abp'
        verbose_name = 'OpinionStepOneAbp'


class InteractionStepOneAbp(BaseModel):
    class InteractionStepOneAbpStatus(models.IntegerChoices):
        NOTHING = 0
        DISAGREE = 1
        AGREE = 2

    opinion_interaction = models.PositiveSmallIntegerField(
        choices=InteractionStepOneAbpStatus.choices,
        default=0,
        null=False,
        blank=False
    )
    active = models.BooleanField(
        default=True,
        null=False,
        blank=True
    )

    objects = InteractionStepOneAbpManager()

    opinion_step_one_abp = models.ForeignKey(
        OpinionStepOneAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.get_opinion_interaction_display()

    class Meta:
        db_table = 'interaction_step_one_abp'
        verbose_name = 'InteractionStepOneAbp'


class QuestionStepOneAbp(BaseModel):
    moderator_question = models.CharField(
        max_length=250,
        null=False,
        blank=False
    )
    active = models.BooleanField(
        default=True,
        null=False,
        blank=True
    )

    team_abp = models.ForeignKey(
        TeamAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = QuestionStepOneAbpManager()

    def __str__(self):
        return self.moderator_question

    class Meta:
        db_table = 'question_step_one_abp'
        verbose_name = 'QuestionStepOneAbp'


class AnswerStepOneAbp(BaseModel):
    teacher_answer = models.TextField(
        null=False,
        blank=False
    )
    active = models.BooleanField(
        default=True,
        null=False,
        blank=True
    )

    question_step_one_abp = models.ForeignKey(
        QuestionStepOneAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = AnswerStepOneAbpManager()

    def __str__(self):
        return self.teacher_answer

    class Meta:
        db_table = 'answer_step_one_abp'
        verbose_name = 'AnswerStepOneAbp'


class StudentIdeaStepTwoAbp(BaseModelActive):
    student_idea = models.TextField(null=False, blank=False)

    team_detail_abp = models.ForeignKey(
        TeamDetailAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = StudentIdeaStepTwoAbpManager()

    def __str__(self):
        return self.student_idea

    class Meta:
        db_table = 'student_idea_step_one_abp'
        verbose_name = 'StudentIdeaStepTwoAbp'


class RateStudentIdeaStepTwoAbp(BaseModelActive):
    rate_student_idea = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False
    )

    student_idea_step_two_abp = models.ForeignKey(
        StudentIdeaStepTwoAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = RateStudentIdeaStepTwoAbpManager()

    def __str__(self):
        return f'{self.rate_student_idea}'

    class Meta:
        db_table = 'rating_student_idea_step_one_abp'
        verbose_name = 'RatingStudentIdeaStepTwoAbp'


class LearnedConceptStepThreeAbp(BaseModelActive):
    learned_concept = models.TextField(null=False, blank=False)

    team_abp = models.ForeignKey(
        TeamAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = LearnedConceptStepThreeAbpManager()

    def __str__(self):
        return self.learned_concept

    class Meta:
        db_table = 'learned_concept_step_three_abp'
        verbose_name = 'LearnedConceptStepThreeAbp'


class LearnedConceptReferenceStepThreeAbp(BaseModelActive):
    url_reference = models.URLField(null=False, blank=False)

    learned_concept_step_three_abp = models.ForeignKey(
        LearnedConceptStepThreeAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = LearnedConceptReferenceStepThreeAbpManager()

    def __str__(self):
        return self.url_reference

    class Meta:
        db_table = 'learned_concept_reference_step_three_abp'
        verbose_name = 'LearnedConceptReferenceStepThreeAbp'


class UnknownConceptStepFourAbp(BaseModelActive):
    unknown_concept = models.TextField(null=False, blank=False)

    team_abp = models.ForeignKey(
        TeamAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = UnknownConceptStepFourAbpManager()

    def __str__(self):
        return self.unknown_concept

    class Meta:
        db_table = 'unknown_concept_step_four_abp'
        verbose_name = 'UnknownConceptStepFourAbp'


class UnknownConceptReferenceStepFourAbp(BaseModelActive):
    url_reference = models.URLField(null=False, blank=False)

    unknown_concept_step_four_abp = models.ForeignKey(
        UnknownConceptStepFourAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = UnknownConceptReferenceStepFourAbpManager()

    def __str__(self):
        return self.url_reference

    class Meta:
        db_table = 'unknown_concept_reference_step_four_abp'
        verbose_name = 'UnknownConceptReferenceStepFourAbp'


class PerformActionStepFiveAbp(BaseModelActive):
    action = models.TextField(null=False, blank=False)

    team_detail_abp = models.ForeignKey(
        TeamDetailAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = PerformActionStepFiveAbpManager()

    def __str__(self):
        return self.action

    class Meta:
        db_table = 'perform_action_step_five_abp'
        verbose_name = 'PerformActionStepFiveAbp'


class RatePerformActionStepFiveAbp(BaseModelActive):
    rate_perform_action = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False
    )

    perform_action_step_five_abp = models.ForeignKey(
        PerformActionStepFiveAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = RatePerformActionStepFiveAbpManager()

    def __str__(self):
        return f'{self.rate_perform_action}'

    class Meta:
        db_table = 'rate_perform_action_step_five_abp'
        verbose_name = 'RatePerformActionStepFiveAbp'


class ProblemDefinitionStepSixAbp(BaseModelActive):
    problem_definition = models.TextField(null=False, blank=False)
    observations = models.TextField(null=False, blank=True)

    team_abp = models.ForeignKey(
        TeamAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = ProblemDefinitionStepSixAbpManager()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'problem_definition_step_six_abp'
        verbose_name = 'ProblemDefinitionStepSixAbp'


class ProblemDefinitionReferenceStepSixAbp(BaseModelActive):
    problem_reference = models.URLField(
        null=False,
        blank=False
    )

    team_abp = models.ForeignKey(
        TeamAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = ProblemDefinitionReferenceStepFixAbpManager()

    def __str__(self):
        return self.problem_reference

    class Meta:
        db_table = 'problem_definition_reference_step_six_abp'
        verbose_name = 'ProblemDefinitionReferenceStepSixAbp'


class GetInformationStepSevenAbp(BaseModelActive):
    get_information = models.TextField(null=False, blank=False)
    observations = models.TextField(
        null=False,
        blank=True,
        default=''
    )

    team_abp = models.ForeignKey(
        TeamAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = GetInformationStepSevenAbpManager()

    def __str__(self):
        return self.get_information

    class Meta:
        db_table = 'get_information_step_seven_abp'
        verbose_name = 'GetInformationStepSevenAbp'


class InformationReferenceStepSevenAbp(BaseModelActive):
    information_reference = models.URLField(null=False, blank=False)

    team_abp = models.ForeignKey(
        TeamAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = InformationReferenceStepSevenAbpManager()

    def __str__(self):
        return self.information_reference

    class Meta:
        db_table = 'information_reference_step_seven_abp'
        verbose_name = 'InformationReferenceStepSevenAbp'


class ProblemResolutionStepEightAbp(BaseModelActive):
    problem_resolution = models.TextField(null=False, blank=False)
    video_url = models.URLField(null=False, blank=True)
    image_references = models.JSONField(null=False, blank=True)
    observations = models.TextField(
        null=False,
        blank=True,
        default=''
    )

    team_abp = models.ForeignKey(
        TeamAbp,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    objects = ProblemResolutionStepEightAbpManager()

    def __str__(self):
        return self.problem_resolution

    class Meta:
        db_table = 'problem_resolution_step_eight_abp'
        verbose_name = 'ProblemResolutionStepEightAbp'
