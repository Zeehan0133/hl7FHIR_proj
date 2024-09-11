from typing import List, Optional, Union
from pydantic import BaseModel, Field # type: ignore
from enum import Enum
from datetime import date, datetime

class FinancialResourceStatusCodes(str, Enum):
    active = "active"
    cancelled = "cancelled"
    draft = "draft"
    entered_in_error = "entered-in-error"

class EligibilityResponsePurpose(str, Enum):
    auth_requirements = "auth-requirements"
    benefits = "benefits"
    discovery = "discovery"
    validation = "validation"

class RemittanceOutcome(str, Enum):
    queued = "queued"
    complete = "complete"
    error = "error"
    partial = "partial"

class CodeableConcept(BaseModel):
    coding: Optional[List[str]] = None
    text: Optional[str] = None

class Identifier(BaseModel):
    system: Optional[str] = None
    value: Optional[str] = None

class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[Identifier] = None

class Period(BaseModel):
    start: Optional[date] = None
    end: Optional[date] = None

class Money(BaseModel):
    value: Optional[float] = None
    currency: Optional[str] = None

class BackboneElement(BaseModel):
    modifierExtension: Optional[List[str]] = None

class CoverageEligibilityResponseItemBenefit(BaseModel):
    type: CodeableConcept
    allowedUnsignedInt: Optional[int] = None
    allowedString: Optional[str] = None
    allowedMoney: Optional[Money] = None
    usedUnsignedInt: Optional[int] = None
    usedString: Optional[str] = None
    usedMoney: Optional[Money] = None

class CoverageEligibilityResponseItem(BaseModel):
    category: Optional[CodeableConcept] = None
    productOrService: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    provider: Optional[Reference] = None
    excluded: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    network: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    term: Optional[CodeableConcept] = None
    benefit: Optional[List[CoverageEligibilityResponseItemBenefit]] = None
    authorizationRequired: Optional[bool] = None
    authorizationSupporting: Optional[List[CodeableConcept]] = None
    authorizationUrl: Optional[str] = None

class CoverageEligibilityResponseInsurance(BaseModel):
    coverage: Reference
    inforce: Optional[bool] = None
    benefitPeriod: Optional[Period] = None
    item: Optional[List[CoverageEligibilityResponseItem]] = None

class CoverageEligibilityResponseError(BaseModel):
    code: CodeableConcept

class CoverageEligibilityResponse(BaseModel):
    resourceType: str = Field("CoverageEligibilityResponse", const=True)
    identifier: Optional[List[Identifier]] = None
    status: FinancialResourceStatusCodes
    purpose: List[EligibilityResponsePurpose]
    patient: Reference
    servicedDate: Optional[date] = None
    servicedPeriod: Optional[Period] = None
    created: datetime
    requestor: Optional[Reference] = None
    request: Reference
    outcome: RemittanceOutcome
    disposition: Optional[str] = None
    insurer: Reference
    insurance: Optional[List[CoverageEligibilityResponseInsurance]] = None
    preAuthRef: Optional[str] = None
    form: Optional[CodeableConcept] = None
    error: Optional[List[CoverageEligibilityResponseError]] = None
