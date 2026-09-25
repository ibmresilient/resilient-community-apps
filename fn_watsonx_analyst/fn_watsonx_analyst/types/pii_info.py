from typing import List, TypedDict


class PIIInfo(TypedDict):
    """Type for incident PII info"""

    asssessment: str

    data_encrypted: bool
    data_contained: bool
    data_format: any

    exposure: int

    gdpr_harm_risk: any
    gdpr_lawful_data_processing_categories: List[any]
    alberta_health_risk_assessment: any
    california_health_risk_assessment: any
    new_zealand_risk_assessment: any
    singapore_risk_assessment: any
