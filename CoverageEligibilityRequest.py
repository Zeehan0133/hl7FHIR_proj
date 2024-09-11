from typing import List, Literal, Optional, Union
from pydantic import BaseModel, Field, PositiveInt,HttpUrl # type: ignore
from datetime import date, datetime
from enum import Enum

# Enum Definitions
class FinancialResourceStatusCodes(str, Enum):
    active = "active"
    cancelled = "cancelled"
    draft = "draft"
    entered_in_error = "entered-in-error"

class EligibilityRequestPurpose(str, Enum):
    auth_requirements = "auth-requirements"
    benefits = "benefits"
    discovery = "discovery"
    validation = "validation"

class Identifier(BaseModel):
    use: Optional[str] = None
    system: Optional[str] = None
    value: Optional[str] = None
    period: Optional["Period"] = None
    assigner: Optional["Reference"] = None

class Period(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class CodeableConcept(BaseModel):
    coding: Optional[List["Coding"]] = None
    text: Optional[str] = None

class Coding(BaseModel):
    system: Optional[str] = None
    version: Optional[str] = None
    code: Optional[str] = None
    display: Optional[str] = None
    userSelected: Optional[bool] = None

class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[Identifier] = None
    display: Optional[str] = None

class BackboneElement(BaseModel):
    modifierExtension: Optional[List["Extension"]] = None

class SimpleQuantity(BaseModel):
    value: Optional[float] = None
    unit: Optional[str] = None
    system: Optional[str] = None
    code: Optional[str] = None

class Meta(BaseModel):
    versionId: Optional[str] = None
    lastUpdated: Optional[datetime] = None
    source: Optional[str] = None
    profile: Optional[List[HttpUrl]] = None
    security: Optional[List[Coding]] = None
    tag: Optional[List[Coding]] = None

class Resource(BaseModel):
    id: Optional[str] = None
    meta: Optional[Meta] = None
    implicitRules: Optional[str] = None
    language: Optional[str] = None

class Money(BaseModel):
    value: Optional[float] = None
    currency: Optional[str] = None

class Extension(BaseModel):
    url: str
    valueString: Optional[str] = None
    valueInteger: Optional[int] = None
    valueBoolean: Optional[bool] = None
    valueCode: Optional[str] = None
    valueDate: Optional[date] = None
    valueDateTime: Optional[datetime] = None
    valueDecimal: Optional[float] = None

class Narrative(BaseModel):
    status: Literal['generated', 'extensions', 'additional', 'empty']
    div: str  # XHTML content, ensure safe handling if displaying in UI


class Meta(BaseModel):
    versionId: Optional[str] = None
    lastUpdated: Optional[datetime] = None
    source: Optional[str] = None
    profile: Optional[List[str]] = None
    security: Optional[List[Coding]] = None
    tag: Optional[List[Coding]] = None

class DomainResource(BaseModel):
    id: Optional[str] = None
    meta: Optional[Meta] = None
    implicitRules: Optional[str] = None
    language: Optional[str] = None
    text: Optional[Narrative] = None
    contained: Optional[List["Resource"]] = None
    extension: Optional[List[Extension]] = None
    modifierExtension: Optional[List[Extension]] = None

class CoverageEligibilityRequestInsurance(BackboneElement):
    focal: Optional[bool] = None
    coverage: Reference
    businessArrangement: Optional[str] = None

class CoverageEligibilityRequestSupportingInfo(BackboneElement):
    sequence: PositiveInt
    information: Reference
    appliesToAll: Optional[bool] = None

class CoverageEligibilityRequestItemDiagnosis(BackboneElement):
    diagnosisCodeableConcept: Optional[CodeableConcept] = None
    diagnosisReference: Optional[Reference] = None

class CoverageEligibilityRequestItem(BackboneElement):
    supportingInfoSequence: Optional[List[PositiveInt]] = None
    category: Optional[CodeableConcept] = None
    productOrService: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    provider: Optional[Reference] = None
    quantity: Optional["SimpleQuantity"] = None
    unitPrice: Optional["Money"] = None
    facility: Optional[Reference] = None
    diagnosis: Optional[List[CoverageEligibilityRequestItemDiagnosis]] = None
    detail: Optional[List[Reference]] = None

class CoverageEligibilityRequest(DomainResource):
    resourceType: Literal["CoverageEligibilityRequest"] = "CoverageEligibilityRequest"
    identifier: Optional[List[Identifier]] = None
    status: FinancialResourceStatusCodes
    priority: Optional[CodeableConcept] = None
    purpose: List[EligibilityRequestPurpose]
    patient: Reference
    servicedDate: Optional[date] = None
    servicedPeriod: Optional[Period] = None
    created: datetime
    enterer: Optional[Reference] = None
    provider: Optional[Reference] = None
    insurer: Reference
    facility: Optional[Reference] = None
    supportingInfo: Optional[List[CoverageEligibilityRequestSupportingInfo]] = None
    insurance: Optional[List[CoverageEligibilityRequestInsurance]] = None
    item: Optional[List[CoverageEligibilityRequestItem]] = None

