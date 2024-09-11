from typing import List, Literal, Optional, Union, Dict, Any
from pydantic import BaseModel, conint, constr, HttpUrl # type: ignore
from datetime import datetime, date
from enum import Enum

# Enum Definitions
class ResourceType(str, Enum):
    Patient = "Patient"
    Practitioner = "Practitioner"
    PractitionerRole = "PractitionerRole"
    Organization = "Organization"
    Encounter = "Encounter"

# Extension class
class Extension(BaseModel):
    url: str
    valueString: Optional[str] = None
    valueInteger: Optional[int] = None
    valueBoolean: Optional[bool] = None
    valueCode: Optional[str] = None
    valueDate: Optional[date] = None
    valueDateTime: Optional[datetime] = None
    valueDecimal: Optional[float] = None
    valueUri: Optional[HttpUrl] = None
    # valueAttachment: Optional[Dict[str, Any]] = None
    # valueReference: Optional[Dict[str, Any]] = None

class Coding(BaseModel):
    system: Optional[str] = None
    version: Optional[str] = None
    code: Optional[str] = None
    display: Optional[str] = None
    userSelected: Optional[bool] = None

# Reusable models from the FHIR spec
class Identifier(BaseModel):
    use: Optional[str] = None
    system: Optional[str] = None
    value: Optional[str] = None
    period: Optional['Period'] = None
    assigner: Optional['Reference'] = None

class CodeableConcept(BaseModel):
    coding: Optional[List['Coding']] = None
    text: Optional[str] = None

class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[ResourceType] = None  # Using ResourceType Enum
    identifier: Optional[Identifier] = None
    display: Optional[str] = None

class Period(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class BackboneElement(BaseModel):
    extension: Optional[List[Extension]] = None  # Using the Extension class
    modifierExtension: Optional[List[Extension]] = None  # Using the Extension class

class SimpleQuantity(BaseModel):
    value: Optional[float] = None
    unit: Optional[str] = None
    system: Optional[str] = None
    code: Optional[str] = None

class Money(BaseModel):
    value: Optional[float] = None
    currency: Optional[str] = None

# Custom models for Coverage
class CoverageClass(BackboneElement):
    type: CodeableConcept
    value: Optional[str] = None  # 1..1 string
    name: Optional[str] = None

class CostToBeneficiary(BackboneElement):
    type: Optional[CodeableConcept] = None
    valueQuantity: Optional[SimpleQuantity] = None
    valueMoney: Optional[Money] = None
    exception: Optional[List['Exception']] = None

class Exception(BackboneElement):
    type: CodeableConcept
    period: Optional[Period] = None

# Main Coverage model
class Coverage(BaseModel):
    resourceType: Literal["Coverage"] = "Coverage"
    identifier: Optional[List[Identifier]] = None  # 0..* Identifier
    status: str  # 1..1 code (active | cancelled | draft | entered-in-error)
    type: Optional[CodeableConcept] = None  # 0..1 CodeableConcept
    policyHolder: Optional[Reference] = None  # 0..1 Reference(Patient | RelatedPerson | Organization)
    subscriber: Optional[Reference] = None  # 0..1 Reference(Patient | RelatedPerson)
    subscriberId: Optional[str] = None  # 0..1 string
    beneficiary: Reference  # 1..1 Reference(Patient)
    dependent: Optional[str] = None  # 0..1 string
    relationship: Optional[CodeableConcept] = None  # 0..1 CodeableConcept
    period: Optional[Period] = None  # 0..1 Period
    payor: List[Reference]  # 1..* Reference(Organization | Patient | RelatedPerson)
    class_: Optional[List[CoverageClass]] = None  # 0..* BackboneElement
    order: Optional[int] = None  # 0..1 positiveInt
    network: Optional[str] = None  # 0..1 string
    costToBeneficiary: Optional[List[CostToBeneficiary]] = None  # 0..* BackboneElement
    subrogation: Optional[bool] = None  # 0..1 boolean
    contract: Optional[List[Reference]] = None  # 0..* Reference(Contract)
    extension: Optional[List[Extension]] = None  # Adding extension field
    modifierExtension: Optional[List[Extension]] = None  # Adding modifierExtension field

    class Config:
        allow_population_by_field_name = True


