from typing import List, Literal, Optional, Union
from pydantic import BaseModel,HttpUrl, Field # type: ignore
from datetime import datetime


class Identifier(BaseModel):
    system: Optional[str]
    value: Optional[str]


class Coding(BaseModel):
    system: Optional[str]
    version: Optional[str]
    code: Optional[str]
    display: Optional[str]
    userSelected: Optional[bool]


class CodeableConcept(BaseModel):
    coding: Optional[List[Coding]]
    text: Optional[str]


class Reference(BaseModel):
    reference: Optional[str]
    display: Optional[str]


class Period(BaseModel):
    start: Optional[datetime]
    end: Optional[datetime]


class Age(BaseModel):
    value: Optional[float]
    unit: Optional[str]
    system: Optional[str]
    code: Optional[str]


class Range(BaseModel):
    low: Optional[float]
    high: Optional[float]


class Quantity(BaseModel):
    value: Optional[float]
    unit: Optional[str]
    system: Optional[str]
    code: Optional[str]


class Annotation(BaseModel):
    authorReference: Optional[Reference]
    authorString: Optional[str]
    time: Optional[datetime]
    text: str


class Extension(BaseModel):
    url: str
    valueString: Optional[str]
    valueBoolean: Optional[bool]
    valueInteger: Optional[int]
    valueDateTime: Optional[datetime]
    valueDecimal: Optional[float]
    valueUri: Optional[HttpUrl] = None
    valueCode: Optional[str]
    valueQuantity: Optional[Quantity]
    valueReference: Optional[Reference]


class BackboneElement(BaseModel):
    extension: Optional[List[Extension]] = None
    modifierExtension: Optional[List[Extension]] = None


class Reaction(BackboneElement):
    substance: Optional[CodeableConcept]
    manifestation: List[CodeableConcept]
    description: Optional[str]
    onset: Optional[datetime]
    severity: Optional[str]  # mild | moderate | severe
    exposureRoute: Optional[CodeableConcept]
    note: Optional[List[Annotation]]


class Narrative(BaseModel):
    status: str  # e.g., generated, extensions, additional, or empty
    div: str  # The actual content of the narrative, usually in XHTML format


class Meta(BaseModel):
    versionId: Optional[str]
    lastUpdated: Optional[datetime]
    profile: Optional[List[HttpUrl]]
    security: Optional[List[Coding]]
    tag: Optional[List[Coding]]


class Resource(BaseModel):
    resourceType: str


class AllergyIntolerance(BaseModel):
    resourceType: Literal["AllergyIntolerance"] = "AllergyIntolerance"
    id: Optional[str]
    meta: Optional[Meta]
    implicitRules: Optional[HttpUrl] = None
    language: Optional[str]
    text: Optional[Narrative]
    contained: Optional[List[Resource]]  # List of contained resources
    extension: Optional[List[Extension]]
    modifierExtension: Optional[List[Extension]]

    identifier: Optional[List[Identifier]]
    clinicalStatus: Optional[CodeableConcept]  # active | inactive | resolved
    verificationStatus: Optional[CodeableConcept]  # unconfirmed | confirmed | refuted | entered-in-error
    type: Optional[str]  # allergy | intolerance
    category: Optional[List[str]]  # food | medication | environment | biologic
    criticality: Optional[str]  # low | high | unable-to-assess
    code: Optional[CodeableConcept]
    patient: Reference
    encounter: Optional[Reference]

    onsetDateTime: Optional[datetime]
    onsetAge: Optional[Age]
    onsetPeriod: Optional[Period]
    onsetRange: Optional[Range]
    onsetString: Optional[str]

    recordedDate: Optional[datetime]
    recorder: Optional[Reference]
    asserter: Optional[Reference]
    lastOccurrence: Optional[datetime]
    note: Optional[List[Annotation]]
    reaction: Optional[List[Reaction]]

    class Config:
        extra = "forbid"


# Example Usage
example_allergy = AllergyIntolerance(
    patient=Reference(reference="Patient/123"),
    clinicalStatus=CodeableConcept(text="active"),
    verificationStatus=CodeableConcept(text="confirmed"),
    text=Narrative(
        status="generated",
        div="<div>Example narrative text</div>"
    ),
    meta=Meta(
        versionId="v1",
        lastUpdated=datetime.utcnow(),
        profile=["http://example.org/fhir/StructureDefinition/example-profile"],
        security=[Coding(system="http://example.org/fhir/security", code="confidential")],
        tag=[Coding(system="http://example.org/fhir/tag", code="urgent")]
    ),
    extension=[
        Extension(
            url="http://example.org/fhir/StructureDefinition/example-extension",
            valueQuantity=Quantity(value=5.5, unit="mg/dL", system="http://unitsofmeasure.org", code="mg/dL")
        )
    ]
)
