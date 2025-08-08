
# Class: SamplePreparation

A process that prepares a sample for imaging

URI: [biostride_schema:SamplePreparation](https://w3id.org/biostride/schema/SamplePreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]++-%20sample_preparations%200..*>[SamplePreparation&#124;preparation_type:PreparationTypeEnum;sample_id:string;preparation_date:string%20%3F;operator_id:string%20%3F;protocol_description:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[SamplePreparation],[Study],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]++-%20sample_preparations%200..*>[SamplePreparation&#124;preparation_type:PreparationTypeEnum;sample_id:string;preparation_date:string%20%3F;operator_id:string%20%3F;protocol_description:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[SamplePreparation],[Study],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞sample_preparations](study__sample_preparations.md)*  <sub>0..\*</sub>  **[SamplePreparation](SamplePreparation.md)**

## Attributes


### Own

 * [➞preparation_type](samplePreparation__preparation_type.md)  <sub>1..1</sub>
     * Description: Type of sample preparation
     * Range: [PreparationTypeEnum](PreparationTypeEnum.md)
 * [➞sample_id](samplePreparation__sample_id.md)  <sub>1..1</sub>
     * Description: Reference to the sample being prepared
     * Range: [String](types/String.md)
 * [➞preparation_date](samplePreparation__preparation_date.md)  <sub>0..1</sub>
     * Description: Date of sample preparation
     * Range: [String](types/String.md)
 * [➞operator_id](samplePreparation__operator_id.md)  <sub>0..1</sub>
     * Description: Person who performed the preparation
     * Range: [String](types/String.md)
 * [➞protocol_description](samplePreparation__protocol_description.md)  <sub>0..1</sub>
     * Description: Detailed protocol description
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
