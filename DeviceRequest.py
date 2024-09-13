from typing import List, Literal, Optional, Union
from pydantic import BaseModel, Field, AnyUrl # type: ignore
from enum import Enum
from datetime import datetime

# Basic Enums
class RequestStatus(str, Enum):
    draft = "draft"
    active = "active"
    on_hold = "on-hold"
    revoked = "revoked"
    completed = "completed"
    entered_in_error = "entered-in-error"
    unknown = "unknown"


class RequestIntent(str, Enum):
    proposal = "proposal"
    plan = "plan"
    directive = "directive"
    order = "order"
    original_order = "original-order"
    reflex_order = "reflex-order"
    filler_order = "filler-order"
    instance_order = "instance-order"
    option = "option"


class RequestPriority(str, Enum):
    routine = "routine"
    urgent = "urgent"
    asap = "asap"
    stat = "stat"


# Basic Structures
class Identifier(BaseModel):
    system: Optional[str] = None
    value: Optional[str] = None


class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[Identifier] = None
    display: Optional[str] = None


class CodeableConcept(BaseModel):
    coding: Optional[List[str]] = None
    text: Optional[str] = None


class BackboneElement(BaseModel):
    modifierExtension: Optional[List[str]] = None


class Quantity(BaseModel):
    value: Optional[float] = None
    unit: Optional[str] = None
    system: Optional[str] = None
    code: Optional[str] = None


class Range(BaseModel):
    low: Optional[Quantity] = None
    high: Optional[Quantity] = None


class Period(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class Timing(BaseModel):
    event: Optional[List[datetime]] = None


class Annotation(BaseModel):
    authorReference: Optional[Reference] = None
    time: Optional[datetime] = None
    text: str


# DeviceRequest-specific Structures
class Parameter(BaseModel):
    code: Optional[CodeableConcept] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = None
    valueRange: Optional[Range] = None
    valueBoolean: Optional[bool] = None


class DeviceRequest(BaseModel):
    resourceType: Literal["DeviceRequest"] ="DeviceRequest"
    
    # Core Fields
    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[AnyUrl]] = None
    basedOn: Optional[List[Reference]] = None
    priorRequest: Optional[List[Reference]] = None
    groupIdentifier: Optional[Identifier] = None
    status: Optional[RequestStatus] = None
    intent: RequestIntent
    priority: Optional[RequestPriority] = None

    # Code[x] Field (Union of Reference(Device) or CodeableConcept)
    codeReference: Optional[Reference] = None
    codeCodeableConcept: Optional[CodeableConcept] = None

    # Parameter (BackboneElement)
    parameter: Optional[List[Parameter]] = None

    # Subject, Encounter, Occurrence, Requester, Performer
    subject: Reference
    encounter: Optional[Reference] = None
    occurrenceDateTime: Optional[datetime] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    authoredOn: Optional[datetime] = None
    requester: Optional[Reference] = None
    performerType: Optional[CodeableConcept] = None
    performer: Optional[Reference] = None

    # Reason, Insurance, Supporting Info, Notes
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[Reference]] = None
    insurance: Optional[List[Reference]] = None
    supportingInfo: Optional[List[Reference]] = None
    note: Optional[List[Annotation]] = None

    # History (Reference Provenance)
    relevantHistory: Optional[List[Reference]] = None
