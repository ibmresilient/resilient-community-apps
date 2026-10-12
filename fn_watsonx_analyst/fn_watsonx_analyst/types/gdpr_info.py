from typing import List, TypedDict


class GDPRInfo(TypedDict):
    """Type for incident GDPR metadata"""

    gdpr_breach_circumstances: List[any]
    gdpr_breach_type: any
    gdpr_personal_data: any
    gdpr_identification: any
    gdpr_consequences: any
    gdpr_final_assessment: any
    gdpr_breach_type_comment: any
    gdpr_personal_data_comment: any
    gdpr_identification_comment: any
    gdpr_consequences_comment: any
    gdpr_final_assessment_comment: any
    gdpr_subsequent_notification: any
