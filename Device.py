from typing import List, Literal, Optional
from pydantic import BaseModel, Field, AnyUrl # type: ignore
from enum import Enum
from datetime import date, datetime


class Identifier(BaseModel):
    system: Optional[str] = None
    value: Optional[str] = None


class Reference(BaseModel):
    reference: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[Identifier] = None
    display: Optional[str] = None


class UDIEntryType(str, Enum):
    barcode = "barcode"
    rfid = "rfid"
    manual = "manual"


class FHIRDeviceStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    entered_in_error = "entered-in-error"
    unknown = "unknown"


class CodeableConcept(BaseModel):
    coding: Optional[List[str]] = None
    text: Optional[str] = None


class BackboneElement(BaseModel):
    modifierExtension: Optional[List[str]] = None


class UdiCarrier(BaseModel):
    deviceIdentifier: Optional[str] = None
    issuer: Optional[AnyUrl] = None
    jurisdiction: Optional[AnyUrl] = None
    carrierAIDC: Optional[str] = None
    carrierHRF: Optional[str] = None
    entryType: Optional[UDIEntryType] = None


class DeviceNameType(str, Enum):
    udi_label_name = "udi-label-name"
    user_friendly_name = "user-friendly-name"
    patient_reported_name = "patient-reported-name"
    manufacturer_name = "manufacturer-name"
    model_name = "model-name"
    other = "other"


class DeviceName(BaseModel):
    name: str
    type: DeviceNameType


class DeviceSpecialization(BaseModel):
    systemType: CodeableConcept
    version: Optional[str] = None


class DeviceVersion(BaseModel):
    type: Optional[CodeableConcept] = None
    component: Optional[Identifier] = None
    value: str


class Quantity(BaseModel):
    value: Optional[float] = None
    unit: Optional[str] = None
    system: Optional[str] = None
    code: Optional[str] = None


class DeviceProperty(BaseModel):
    type: CodeableConcept
    valueQuantity: Optional[List[Quantity]] = None
    valueCode: Optional[List[CodeableConcept]] = None


class ContactPoint(BaseModel):
    system: Optional[str] = None
    value: Optional[str] = None
    use: Optional[str] = None
    rank: Optional[int] = None


class Annotation(BaseModel):
    authorReference: Optional[Reference] = None
    time: Optional[datetime] = None
    text: str


class Device(BaseModel):
    resourceType: Literal["Device"] = "Device"
    identifier: Optional[List[Identifier]] = None
    definition: Optional[Reference] = None
    udiCarrier: Optional[List[UdiCarrier]] = None
    status: Optional[FHIRDeviceStatus] = None
    statusReason: Optional[List[CodeableConcept]] = None
    distinctIdentifier: Optional[str] = None
    manufacturer: Optional[str] = None
    manufactureDate: Optional[datetime] = None
    expirationDate: Optional[datetime] = None
    lotNumber: Optional[str] = None
    serialNumber: Optional[str] = None
    deviceName: Optional[List[DeviceName]] = None
    modelNumber: Optional[str] = None
    partNumber: Optional[str] = None
    type: Optional[CodeableConcept] = None
    specialization: Optional[List[DeviceSpecialization]] = None
    version: Optional[List[DeviceVersion]] = None
    property: Optional[List[DeviceProperty]] = None
    patient: Optional[Reference] = None
    owner: Optional[Reference] = None
    contact: Optional[List[ContactPoint]] = None
    location: Optional[Reference] = None
    url: Optional[AnyUrl] = None
    note: Optional[List[Annotation]] = None
    safety: Optional[List[CodeableConcept]] = None
    parent: Optional[Reference] = None
