from typing import List, Literal, Optional, Union
from pydantic import BaseModel, Field # type: ignore
from datetime import datetime


class Period(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None

# Definitions for reusable types
class Identifier(BaseModel):
    use: Optional[str] = None
    type: Optional['CodeableConcept'] = None
    system: Optional[str] = None
    value: Optional[str] = None
    period: Optional['Period'] = None
    assigner: Optional['Reference'] = None

class CodeableConcept(BaseModel):
    coding: Optional[List['Coding']] = None
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

class ContactPoint(BaseModel):
    system: Optional[str] = None
    value: Optional[str] = None
    use: Optional[str] = None
    rank: Optional[int] = None
    period: Optional[Period] = None

class Annotation(BaseModel):
    authorReference: Optional[Reference] = None
    authorString: Optional[str] = None
    time: Optional[datetime] = None
    text: str

# CareTeam participant model
class CareTeamParticipant(BaseModel):
    role: Optional[List[CodeableConcept]] = None
    member: Optional[Reference] = None
    onBehalfOf: Optional[Reference] = None
    period: Optional[Period] = None



# Placeholder classes for elements not fully expanded in the example
class Meta(BaseModel):
    versionId: Optional[str] = None
    lastUpdated: Optional[datetime] = None
    source: Optional[str] = None
    profile: Optional[List[str]] = None
    security: Optional[List[Coding]] = None
    tag: Optional[List[Coding]] = None

class Narrative(BaseModel):
    status: Literal['generated', 'extensions', 'additional', 'empty']
    div: str  # XHTML content, ensure safe handling if displaying in UI

class Resource(BaseModel):
    resourceType: str

class Extension(BaseModel):
    url: str
    valueString: Optional[str] = None
    valueCode: Optional[str] = None
    valueReference: Optional[Reference] = None

# Main CareTeam model
class CareTeam(BaseModel):
    resourceType: Literal["CareTeam"] ="CareTeam"
    id: Optional[str] = None
    meta: Optional['Meta'] = None
    implicitRules: Optional[str] = None
    language: Optional[str] = None
    text: Optional['Narrative'] = None
    contained: Optional[List['Resource']] = None
    extension: Optional[List['Extension']] = None
    modifierExtension: Optional[List['Extension']] = None
    
    identifier: Optional[List[Identifier]] = None
    status: str  # code: proposed | active | suspended | inactive | entered-in-error
    category: Optional[List[CodeableConcept]] = None
    name: Optional[str] = None
    subject: Optional[Reference] = None  # Patient | Group
    encounter: Optional[Reference] = None  # Encounter
    period: Optional[Period] = None
    participant: Optional[List[CareTeamParticipant]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[Reference]] = None
    managingOrganization: Optional[List[Reference]] = None
    telecom: Optional[List[ContactPoint]] = None
    note: Optional[List[Annotation]] = None

# Resolve forward references
# Identifier.update_forward_refs()
# CodeableConcept.update_forward_refs()
# Coding.update_forward_refs()
# Reference.update_forward_refs()
# Period.update_forward_refs()
# ContactPoint.update_forward_refs()
# Annotation.update_forward_refs()
# CareTeamParticipant.update_forward_refs()
# CareTeam.update_forward_refs()
# Meta.update_forward_refs()
# Narrative.update_forward_refs()
# Resource.update_forward_refs()
# Extension.update_forward_refs()
