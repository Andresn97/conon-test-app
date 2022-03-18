from django.urls import path

from applications.abp.api.api_team_abp.api import \
    get_students_by_classroom_for_to_group, get_student_team_abp
from applications.abp.api.api_rubric_abp.api import get_rubric_abp_detail_list_by_abp
from applications.abp.api.api_evaluation_abp.api import get_evaluation_apb_with_details

urlpatterns = [
    path(
        r"team-abp/new-students-for-team-abp/<int:classroom>/<int:abp>/",
        get_students_by_classroom_for_to_group,
        name="new_students_for_team_abp"
    ),
    path(
        r"team-abp/student-team-abp/<int:abp>/<int:user>/",
        get_student_team_abp,
        name="student_team_abp"
    ),
    path(
        r"rubric-abp/rubric-abp-detail-by-abp/<int:abp>/",
        get_rubric_abp_detail_list_by_abp,
        name="rubric_abp_detail_by_abp"
    ),
    path(
        r"evaluation-abp/evaluation-abp-detail-by-evaluation/<int:abp>/<int:team_detail_abp>/",
        get_evaluation_apb_with_details,
        name="evaluation_abp_detail_by_evaluation"
    ),
]
