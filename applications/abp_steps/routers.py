from rest_framework import routers

from .api.api_opinion_step_one_abp.viewsets import OpinionStepOneAbpViewSet
from .api.api_interaction_step_one_abp.viewsets import InteractionStepOneAbpViewSet
from .api.api_question_step_one_abp.viewsets import QuestionStepOneAbpViewSet
from .api.api_answer_step_one_abp.viewsets import AnswerStepOneAbpViewSet
from .api.api_student_idea_step_two_abp.viewsets import StudentIdeaStepTwoAbpViewSet
from .api.api_rate_student_idea_step_two_abp.viewsets import RateStudentIdeaStepTwoAbpViewSet
from .api.api_learned_concept_step_three_abp.viewsets import LearnedConceptStepThreeAbpViewSet
from .api.api_learned_concept_reference_step_three_abp.viewsets import \
    LearnedConceptReferenceStepThreeAbpViewSet
from .api.api_unknown_concept_step_four_abp.viewsets import UnknownConceptStepFourAbpViewSet
from .api.api_unknown_concept_reference_step_four_abp.viewsets import \
    UnknownConceptReferenceStepFourAbpViewSet
from .api.api_perform_action_step_five_abp.viewsets import PerformActionStepFiveAbpViewSet
from .api.api_rate_perform_action_step_five_abp.viewsets import RatePerformActionStepFiveAbpViewSet
from .api.api_problem_definition_step_six_abp.viewsets import ProblemDefinitionStepSixAbpViewSet
from .api.api_problem_definition_reference_step_six_abp.viewsets import \
    ProblemDefinitionReferenceStepSixAbpViewSet
from .api.api_get_information_step_seven_abp.viewsets import GetInformationStepSevenAbpViewSet
from .api.api_information_reference_step_seven_abp.viewsets import \
    InformationReferenceStepSevenAbpViewSet
from .api.api_problem_resolution_step_eight_abp.viewsets import ProblemResolutionStepEightAbpViewSet


router = routers.DefaultRouter()

router.register(
    r'step-one/opinion',
    OpinionStepOneAbpViewSet,
    basename='opinion_step_one_abp'
)
router.register(
    r'step-one/interaction',
    InteractionStepOneAbpViewSet,
    basename='interaction_step_one_abp'
)
router.register(
    r'step-one/question',
    QuestionStepOneAbpViewSet,
    basename='question_step_one_abp'
)
router.register(
    r'step-one/answer',
    AnswerStepOneAbpViewSet,
    basename='answer_step_one_abp'
)
router.register(
    r'step-two/student-idea',
    StudentIdeaStepTwoAbpViewSet,
    basename='student_idea_step_two_abp'
)
router.register(
    r'step-two/rate-student-idea',
    RateStudentIdeaStepTwoAbpViewSet,
    basename='rate_student_idea_step_two_abp'
)
router.register(
    r'step-three/learned-concept',
    LearnedConceptStepThreeAbpViewSet,
    basename='learned_concept_step_three_abp'
)
router.register(
    r'step-three/learned-concept-reference',
    LearnedConceptReferenceStepThreeAbpViewSet,
    basename='learned_concept_reference_step_three_abp'
)
router.register(
    r'step-four/unknown-concept',
    UnknownConceptStepFourAbpViewSet,
    basename='unknown_concept_step_four_abp'
)
router.register(
    r'step-four/unknown-concept-reference',
    UnknownConceptReferenceStepFourAbpViewSet,
    basename='unknown_concept_reference_step_four_abp'
)
router.register(
    r'step-five/perform-action',
    PerformActionStepFiveAbpViewSet,
    basename='perform_action_step_five_abp'
)
router.register(
    r'step-five/rate-perform-action',
    RatePerformActionStepFiveAbpViewSet,
    basename='rate_perform_action_step_five_abp'
)
router.register(
    r'step-six/problem-definition',
    ProblemDefinitionStepSixAbpViewSet,
    basename='problem_definition_step_six_abp'
)
router.register(
    r'step-six/problem-definition-reference',
    ProblemDefinitionReferenceStepSixAbpViewSet,
    basename='problem_definition_reference_step_six_abp'
)
router.register(
    r'step-seven/get-information-abp',
    GetInformationStepSevenAbpViewSet,
    basename='get_information_step_seven_abp'
)
router.register(
    r'step-seven/information-reference',
    InformationReferenceStepSevenAbpViewSet,
    basename='information_reference_step_seven_abp'
)
router.register(
    r'step-eight/problem-resolution',
    ProblemResolutionStepEightAbpViewSet,
    basename='problem_resolution_step_eight_abp'
),

urlpatterns = router.urls
