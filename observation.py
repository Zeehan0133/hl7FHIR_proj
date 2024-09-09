from typing import List, Literal, Optional, Union
from pydantic import BaseModel, Field # type: ignore
from datetime import datetime


class Identifier(BaseModel):
    use: Optional[str] = None
    type: Optional['CodeableConcept'] = None
    system: Optional[str] = None
    value: Optional[str] = None

class CodeableConcept(BaseModel):
    coding: Optional[List['Coding']] = None
    text: Optional[str] = None

class Coding(BaseModel):
    system: Optional[str] = None
    code: Optional[str] = None
    display: Optional[str] = None

class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[Identifier] = None
    display: Optional[str] = None

class Quantity(BaseModel):
    value: Optional[float] = None
    unit: Optional[str] = None
    system: Optional[str] = None
    code: Optional[str] = None

class Period(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class Timing(BaseModel):
    # Define the structure according to FHIR Timing
    pass

class Range(BaseModel):
    low: Optional[Quantity] = None
    high: Optional[Quantity] = None

class Ratio(BaseModel):
    numerator: Optional[Quantity] = None
    denominator: Optional[Quantity] = None

class SampledData(BaseModel):
    # Define the structure according to FHIR SampledData
    pass

class Annotation(BaseModel):
    author: Optional[Union[str, Reference]] = None
    time: Optional[datetime] = None
    text: str

class ObservationReferenceRange(BaseModel):
    low: Optional[Quantity] = None
    high: Optional[Quantity] = None
    type: Optional[CodeableConcept] = None
    appliesTo: Optional[List[CodeableConcept]] = None
    age: Optional[Range] = None
    text: Optional[str] = None

class ObservationComponent(BaseModel):
    code: CodeableConcept
    valueQuantity: Optional[Quantity] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueString: Optional[str] = None
    valueBoolean: Optional[bool] = None
    valueInteger: Optional[int] = None
    valueRange: Optional[Range] = None
    valueRatio: Optional[Ratio] = None
    valueSampledData: Optional[SampledData] = None
    valueTime: Optional[datetime] = None
    valueDateTime: Optional[datetime] = None
    valuePeriod: Optional[Period] = None
    dataAbsentReason: Optional[CodeableConcept] = None
    interpretation: Optional[List[CodeableConcept]] = None
    referenceRange: Optional[List[ObservationReferenceRange]] = None

class Observation(BaseModel):
    resourceType: Literal["Observation"] = "Observation"
    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[Reference]] = None
    partOf: Optional[List[Reference]] = None
    status: str  # Values: registered, preliminary, final, amended, etc.
    category: Optional[List[CodeableConcept]] = None
    code: CodeableConcept
    subject: Optional[Reference] = None
    focus: Optional[List[Reference]] = None
    encounter: Optional[Reference] = None
    effectiveDateTime: Optional[datetime] = None
    effectivePeriod: Optional[Period] = None
    effectiveTiming: Optional[Timing] = None
    effectiveInstant: Optional[datetime] = None
    issued: Optional[datetime] = None
    performer: Optional[List[Reference]] = None
    valueQuantity: Optional[Quantity] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueString: Optional[str] = None
    valueBoolean: Optional[bool] = None
    valueInteger: Optional[int] = None
    valueRange: Optional[Range] = None
    valueRatio: Optional[Ratio] = None
    valueSampledData: Optional[SampledData] = None
    valueTime: Optional[datetime] = None
    valueDateTime: Optional[datetime] = None
    valuePeriod: Optional[Period] = None
    dataAbsentReason: Optional[CodeableConcept] = None
    interpretation: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None
    bodySite: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    specimen: Optional[Reference] = None
    device: Optional[Reference] = None
    referenceRange: Optional[List[ObservationReferenceRange]] = None
    hasMember: Optional[List[Reference]] = None
    derivedFrom: Optional[List[Reference]] = None
    component: Optional[List[ObservationComponent]] = None
