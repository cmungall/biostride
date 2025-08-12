

# Slot: manufacturer 


_Instrument manufacturer_





URI: [biostride_schema:manufacturer](https://w3id.org/biostride/schema/manufacturer)
Alias: manufacturer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:manufacturer |
| native | biostride_schema:manufacturer |




## LinkML Source

<details>
```yaml
name: manufacturer
description: Instrument manufacturer
from_schema: https://w3id.org/biostride/
rank: 1000
alias: manufacturer
owner: Instrument
domain_of:
- Instrument
range: string

```
</details>