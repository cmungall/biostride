

# Slot: instrument_code 


_Unique identifier code for the instrument_





URI: [biostride_schema:instrument_code](https://w3id.org/biostride/schema/instrument_code)
Alias: instrument_code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:instrument_code |
| native | biostride_schema:instrument_code |




## LinkML Source

<details>
```yaml
name: instrument_code
description: Unique identifier code for the instrument
from_schema: https://w3id.org/biostride/
rank: 1000
alias: instrument_code
owner: Instrument
domain_of:
- Instrument
range: string
required: true

```
</details>