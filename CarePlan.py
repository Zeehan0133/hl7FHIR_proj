from typing import List, Literal, Optional, Union
from observation import Timing
from pydantic import BaseModel,HttpUrl, Field # type: ignore
from enum import Enum
from datetime import datetime

# Enumerations
class RequestStatus(str, Enum):
    draft = "draft"
    active = "active"
    on_hold = "on-hold"
    revoked = "revoked"
    completed = "completed"
    entered_in_error = "entered-in-error"
    unknown = "unknown"

class CarePlanIntent(str, Enum):
    proposal = "proposal"
    plan = "plan"
    order = "order"
    option = "option"

class CarePlanActivityKind(str, Enum):
    appointment = "Appointment"
    communication_request = "CommunicationRequest"
    device_request = "DeviceRequest"
    medication_request = "MedicationRequest"
    nutrition_order = "NutritionOrder"
    task = "Task"
    service_request = "ServiceRequest"
    vision_prescription = "VisionPrescription"

class CarePlanActivityStatus(str, Enum):
    not_started = "not-started"
    scheduled = "scheduled"
    in_progress = "in-progress"
    on_hold = "on-hold"
    completed = "completed"
    cancelled = "cancelled"
    stopped = "stopped"
    unknown = "unknown"
    entered_in_error = "entered-in-error"

# Basic FHIR elements
class Identifier(BaseModel):
    use: Optional[str]
    type: Optional['CodeableConcept']
    system: Optional[str]
    value: Optional[str]

class Reference(BaseModel):
    reference: Optional[str]
    type: Optional[str]
    identifier: Optional[Identifier]
    display: Optional[str]

class CodeableConcept(BaseModel):
    coding: Optional[List['Coding']]
    text: Optional[str]

class Coding(BaseModel):
    system: Optional[str]
    version: Optional[str]
    code: Optional[str]
    display: Optional[str]
    userSelected: Optional[bool]

class Period(BaseModel):
    start: Optional[datetime]
    end: Optional[datetime]

class Annotation(BaseModel):
    authorReference: Optional[Reference]
    authorString: Optional[str]
    time: Optional[datetime]
    text: str

class SimpleQuantity(BaseModel):
    value: Optional[float]
    comparator: Optional[str]
    unit: Optional[str]
    system: Optional[str]
    code: Optional[str]

# BackboneElement: Activity.detail
class CarePlanActivityDetail(BaseModel):
    kind: Optional[CarePlanActivityKind]
    instantiatesCanonical: Optional[List[str]]
    instantiatesUri: Optional[List[HttpUrl]]
    code: Optional[CodeableConcept]
    reasonCode: Optional[List[CodeableConcept]]
    reasonReference: Optional[List[Reference]]
    goal: Optional[List[Reference]]
    status: CarePlanActivityStatus
    statusReason: Optional[CodeableConcept]
    doNotPerform: Optional[bool]
    scheduledTiming: Optional['Timing']
    scheduledPeriod: Optional[Period]
    scheduledString: Optional[str]
    location: Optional[Reference]
    performer: Optional[List[Reference]]
    productCodeableConcept: Optional[CodeableConcept]
    productReference: Optional[Reference]
    dailyAmount: Optional[SimpleQuantity]
    quantity: Optional[SimpleQuantity]
    description: Optional[str]

# BackboneElement: Activity
class CarePlanActivity(BaseModel):
    outcomeCodeableConcept: Optional[List[CodeableConcept]]
    outcomeReference: Optional[List[Reference]]
    progress: Optional[List[Annotation]]
    reference: Optional[Reference]
    detail: Optional[CarePlanActivityDetail]

# Main CarePlan Model
class CarePlan(BaseModel):
    resourceType: Literal["CarePlan"] ="CarePlan"
    identifier: Optional[List[Identifier]]
    instantiatesCanonical: Optional[List[str]]
    instantiatesUri: Optional[List[HttpUrl]]
    basedOn: Optional[List[Reference]]
    replaces: Optional[List[Reference]]
    partOf: Optional[List[Reference]]
    status: RequestStatus
    intent: CarePlanIntent
    category: Optional[List[CodeableConcept]]
    title: Optional[str]
    description: Optional[str]
    subject: Reference
    encounter: Optional[Reference]
    period: Optional[Period]
    created: Optional[datetime]
    author: Optional[Reference]
    contributor: Optional[List[Reference]]
    careTeam: Optional[List[Reference]]
    addresses: Optional[List[Reference]]
    supportingInfo: Optional[List[Reference]]
    goal: Optional[List[Reference]]
    activity: Optional[List[CarePlanActivity]]
    note: Optional[List[Annotation]]

    class Config:
        # Example: Enable orm_mode for SQLAlchemy integration
        orm_mode = True

