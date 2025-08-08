

# Class: Instrument 


_An instrument used to collect data_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [biostride_schema:Instrument](https://w3id.org/biostride/schema/Instrument)





```mermaid
 classDiagram
    class Instrument
    click Instrument href "../Instrument/"
      NamedThing <|-- Instrument
        click NamedThing href "../NamedThing/"
      

      Instrument <|-- CryoEMInstrument
        click CryoEMInstrument href "../CryoEMInstrument/"
      Instrument <|-- XRayInstrument
        click XRayInstrument href "../XRayInstrument/"
      Instrument <|-- SAXSInstrument
        click SAXSInstrument href "../SAXSInstrument/"
      

      Instrument : current_status
        
          
    
        
        
        Instrument --> "0..1" InstrumentStatusEnum : current_status
        click InstrumentStatusEnum href "../InstrumentStatusEnum/"
    

        
      Instrument : description
        
      Instrument : id
        
      Instrument : installation_date
        
      Instrument : instrument_code
        
      Instrument : manufacturer
        
      Instrument : model
        
      Instrument : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **Instrument**
        * [CryoEMInstrument](CryoEMInstrument.md)
        * [XRayInstrument](XRayInstrument.md)
        * [SAXSInstrument](SAXSInstrument.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [instrument_code](instrument_code.md) | 1 <br/> [String](String.md) | Unique identifier code for the instrument | direct |
| [manufacturer](manufacturer.md) | 0..1 <br/> [String](String.md) | Instrument manufacturer | direct |
| [model](model.md) | 0..1 <br/> [String](String.md) | Instrument model | direct |
| [installation_date](installation_date.md) | 0..1 <br/> [String](String.md) | Date of instrument installation | direct |
| [current_status](current_status.md) | 0..1 <br/> [InstrumentStatusEnum](InstrumentStatusEnum.md) | Current operational status | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) |  | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:Instrument |
| native | biostride_schema:Instrument |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Instrument
description: An instrument used to collect data
from_schema: https://w3id.org/biostride/
is_a: NamedThing
abstract: true
attributes:
  instrument_code:
    name: instrument_code
    description: Unique identifier code for the instrument
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - Instrument
    required: true
  manufacturer:
    name: manufacturer
    description: Instrument manufacturer
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - Instrument
  model:
    name: model
    description: Instrument model
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - Instrument
  installation_date:
    name: installation_date
    description: Date of instrument installation
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - Instrument
    range: string
  current_status:
    name: current_status
    description: Current operational status
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - Instrument
    range: InstrumentStatusEnum

```
</details>

### Induced

<details>
```yaml
name: Instrument
description: An instrument used to collect data
from_schema: https://w3id.org/biostride/
is_a: NamedThing
abstract: true
attributes:
  instrument_code:
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
  manufacturer:
    name: manufacturer
    description: Instrument manufacturer
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: manufacturer
    owner: Instrument
    domain_of:
    - Instrument
    range: string
  model:
    name: model
    description: Instrument model
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: model
    owner: Instrument
    domain_of:
    - Instrument
    range: string
  installation_date:
    name: installation_date
    description: Date of instrument installation
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: installation_date
    owner: Instrument
    domain_of:
    - Instrument
    range: string
  current_status:
    name: current_status
    description: Current operational status
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: current_status
    owner: Instrument
    domain_of:
    - Instrument
    range: InstrumentStatusEnum
  id:
    name: id
    from_schema: https://w3id.org/biostride/
    rank: 1000
    identifier: true
    alias: id
    owner: Instrument
    domain_of:
    - NamedThing
    - OntologyTerm
    range: uriorcurie
    required: true
  title:
    name: title
    from_schema: https://w3id.org/biostride/
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: Instrument
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: description
    owner: Instrument
    domain_of:
    - NamedThing
    range: string

```
</details>