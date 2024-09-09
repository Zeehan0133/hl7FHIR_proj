from typing import List, Optional
from pydantic import BaseModel, Field # type: ignore
from datetime import datetime



class Identifier(BaseModel):
    use: Optional[str] = None
    type: Optional['CodeableConcept'] = None
    system: Optional[str] = None
    value: Optional[str] = None

class Coding(BaseModel):
    system: Optional[str] = None
    code: Optional[str] = None
    display: Optional[str] = None

class CodeableConcept(BaseModel):
    coding: Optional[List[Coding]] = None
    text: Optional[str] = None

class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[Identifier] = None
    display: Optional[str] = None

class Period(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class Duration(BaseModel):
    value: Optional[float] = None
    unit: Optional[str] = None
    system: Optional[str] = None
    code: Optional[str] = None

class EncounterStatusHistory(BaseModel):
    status: str  # planned | arrived | triaged | in-progress | onleave | finished | cancelled
    period: Period

class EncounterClassHistory(BaseModel):
    class_: Coding = Field(..., alias="class")
    period: Period

class EncounterParticipant(BaseModel):
    type: Optional[List[CodeableConcept]] = None
    period: Optional[Period] = None
    individual: Optional[Reference] = None

class EncounterDiagnosis(BaseModel):
    condition: Reference
    use: Optional[CodeableConcept] = None
    rank: Optional[int] = None

class EncounterHospitalization(BaseModel):
    preAdmissionIdentifier: Optional[Identifier] = None
    origin: Optional[Reference] = None
    admitSource: Optional[CodeableConcept] = None
    reAdmission: Optional[CodeableConcept] = None
    dietPreference: Optional[List[CodeableConcept]] = None
    specialCourtesy: Optional[List[CodeableConcept]] = None
    specialArrangement: Optional[List[CodeableConcept]] = None
    destination: Optional[Reference] = None
    dischargeDisposition: Optional[CodeableConcept] = None

class EncounterLocation(BaseModel):
    location: Reference
    status: Optional[str] = None  # planned | active | reserved | completed
    physicalType: Optional[CodeableConcept] = None
    period: Optional[Period] = None

class Encounter(BaseModel):
    resourceType: str = Field("Encounter", const=True)
    identifier: Optional[List[Identifier]] = None
    status: str  # planned | arrived | triaged | in-progress | onleave | finished | cancelled
    statusHistory: Optional[List[EncounterStatusHistory]] = None
    class_: Coding = Field(..., alias="class")
    classHistory: Optional[List[EncounterClassHistory]] = None
    type: Optional[List[CodeableConcept]] = None
    serviceType: Optional[CodeableConcept] = None
    priority: Optional[CodeableConcept] = None
    subject: Optional[Reference] = None
    episodeOfCare: Optional[List[Reference]] = None
    basedOn: Optional[List[Reference]] = None
    participant: Optional[List[EncounterParticipant]] = None
    appointment: Optional[List[Reference]] = None
    period: Optional[Period] = None
    length: Optional[Duration] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[Reference]] = None
    diagnosis: Optional[List[EncounterDiagnosis]] = None
    account: Optional[List[Reference]] = None
    hospitalization: Optional[EncounterHospitalization] = None
    location: Optional[List[EncounterLocation]] = None
    serviceProvider: Optional[Reference] = None
    partOf: Optional[Reference] = None
