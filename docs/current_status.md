

# Slot: current_status 


_Current operational status_





URI: [biostride_schema:current_status](https://w3id.org/biostride/schema/current_status)
Alias: current_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [InstrumentStatusEnum](InstrumentStatusEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:current_status |
| native | biostride_schema:current_status |




## LinkML Source

<details>
```yaml
name: current_status
description: Current operational status
from_schema: https://w3id.org/biostride/
rank: 1000
alias: current_status
owner: Instrument
domain_of:
- Instrument
range: InstrumentStatusEnum

```
</details>