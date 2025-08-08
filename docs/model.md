

# Slot: model 


_Instrument model_





URI: [biostride_schema:model](https://w3id.org/biostride/schema/model)
Alias: model

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:model |
| native | biostride_schema:model |




## LinkML Source

<details>
```yaml
name: model
description: Instrument model
from_schema: https://w3id.org/biostride/
rank: 1000
alias: model
owner: Instrument
domain_of:
- Instrument
range: string

```
</details>