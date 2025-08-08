

# Slot: accelerating_voltage 


_Accelerating voltage in kV_





URI: [biostride_schema:accelerating_voltage](https://w3id.org/biostride/schema/accelerating_voltage)
Alias: accelerating_voltage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:accelerating_voltage |
| native | biostride_schema:accelerating_voltage |




## LinkML Source

<details>
```yaml
name: accelerating_voltage
description: Accelerating voltage in kV
from_schema: https://w3id.org/biostride/
rank: 1000
alias: accelerating_voltage
owner: CryoEMInstrument
domain_of:
- CryoEMInstrument
range: integer
any_of:
- equals_number: 120
- equals_number: 200
- equals_number: 300

```
</details>