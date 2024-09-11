from typing import List, Literal, Optional, Dict, Any, ForwardRef
from pydantic import BaseModel, HttpUrl # type: ignore
from datetime import date, datetime
from enum import Enum



class Period(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class Identifier(BaseModel):
    use: Optional[str] = None
    system: Optional[str] = None
    value: Optional[str] = None
    period: Optional['Period'] = None  # Forward reference to Period
    assigner: Optional['Reference'] = None  # Forward reference to Reference


class Coding(BaseModel):
    system: Optional[str] = None
    version: Optional[str] = None
    code: Optional[str] = None
    display: Optional[str] = None
    userSelected: Optional[bool] = None


class CodeableConcept(BaseModel):
    coding: Optional[List[Coding]] = None
    text: Optional[str] = None


class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[Identifier] = None
    display: Optional[str] = None


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


class Narrative(BaseModel):
    status: Literal['generated', 'extensions', 'additional', 'empty']
    div: str  # XHTML content, ensure safe handling if displaying in UI


class BackboneElement(BaseModel):
    extension: Optional[List[Extension]] = None  # Forward reference to Extension
    modifierExtension: Optional[List[Extension]] = None  # Forward reference to Extension


class Meta(BaseModel):
    versionId: Optional[str] = None
    lastUpdated: Optional[datetime] = None
    source: Optional[str] = None
    profile: Optional[List[HttpUrl]] = None
    security: Optional[List[Coding]] = None
    tag: Optional[List[Coding]] = None


class DomainResource(BaseModel):
    id: Optional[str] = None
    meta: Optional[Meta] = None
    implicitRules: Optional[str] = None
    language: Optional[str] = None
    text: Optional[Narrative] = None
    contained: Optional[List['DomainResource']] = None  # Forward reference to DomainResource
    extension: Optional[List[Extension]] = None
    modifierExtension: Optional[List[Extension]] = None


class CompositionAttester(BackboneElement):
    mode: str  # personal | professional | legal | official
    time: Optional[datetime] = None
    party: Optional[Reference] = None


class CompositionRelatesTo(BackboneElement):
    code: str  # replaces | transforms | signs | appends
    targetIdentifier: Optional[Identifier] = None
    targetReference: Optional[Reference] = None


class CompositionEvent(BackboneElement):
    code: Optional[List[CodeableConcept]] = None
    period: Optional[Period] = None
    detail: Optional[List[Reference]] = None


class CompositionSection(BackboneElement):
    title: Optional[str] = None
    code: Optional[CodeableConcept] = None
    author: Optional[List[Reference]] = None
    focus: Optional[Reference] = None
    text: Optional[Narrative] = None
    mode: Optional[str] = None  # working | snapshot | changes
    orderedBy: Optional[CodeableConcept] = None
    entry: Optional[List[Reference]] = None
    emptyReason: Optional[CodeableConcept] = None
    section: Optional[List['CompositionSection']] = None  # Nested sections


class Composition(DomainResource):
    resourceType: Literal["Composition"] = "Composition"
    identifier: Optional[Identifier] = None
    status: str  # preliminary | final | amended | entered-in-error
    type: CodeableConcept
    category: Optional[List[CodeableConcept]] = None
    subject: Optional[Reference] = None
    encounter: Optional[Reference] = None
    date: datetime
    author: List[Reference]
    title: str
    confidentiality: Optional[str] = None  # As defined by affinity domain
    attester: Optional[List[CompositionAttester]] = None
    custodian: Optional[Reference] = None
    relatesTo: Optional[List[CompositionRelatesTo]] = None
    event: Optional[List[CompositionEvent]] = None
    section: Optional[List[CompositionSection]] = None



