
# Class: XRayPreparation

X-ray crystallography specific preparation

URI: [biostride_schema:XRayPreparation](https://w3id.org/biostride/schema/XRayPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SamplePreparation]^-[XRayPreparation&#124;crystallization_method:CrystallizationMethodEnum%20%3F;crystallization_conditions:string%20%3F;crystal_size:string%20%3F;cryoprotectant:string%20%3F;cryoprotectant_concentration:float%20%3F;mounting_method:string%20%3F;flash_cooling_method:string%20%3F;preparation_type(i):string;sample_id(i):string;preparation_date(i):string%20%3F;operator_id(i):string%20%3F;protocol_description(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[SamplePreparation])](https://yuml.me/diagram/nofunky;dir:TB/class/[SamplePreparation]^-[XRayPreparation&#124;crystallization_method:CrystallizationMethodEnum%20%3F;crystallization_conditions:string%20%3F;crystal_size:string%20%3F;cryoprotectant:string%20%3F;cryoprotectant_concentration:float%20%3F;mounting_method:string%20%3F;flash_cooling_method:string%20%3F;preparation_type(i):string;sample_id(i):string;preparation_date(i):string%20%3F;operator_id(i):string%20%3F;protocol_description(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[SamplePreparation])

## Parents

 *  is_a: [SamplePreparation](SamplePreparation.md) - A process that prepares a sample for imaging

## Attributes


### Own

 * [➞crystallization_method](xRayPreparation__crystallization_method.md)  <sub>0..1</sub>
     * Description: Method used for crystallization
     * Range: [CrystallizationMethodEnum](CrystallizationMethodEnum.md)
 * [➞crystallization_conditions](xRayPreparation__crystallization_conditions.md)  <sub>0..1</sub>
     * Description: Detailed crystallization conditions
     * Range: [String](types/String.md)
 * [➞crystal_size](xRayPreparation__crystal_size.md)  <sub>0..1</sub>
     * Description: Crystal dimensions in micrometers
     * Range: [String](types/String.md)
 * [➞cryoprotectant](xRayPreparation__cryoprotectant.md)  <sub>0..1</sub>
     * Description: Cryoprotectant used
     * Range: [String](types/String.md)
 * [➞cryoprotectant_concentration](xRayPreparation__cryoprotectant_concentration.md)  <sub>0..1</sub>
     * Description: Cryoprotectant concentration percentage
     * Range: [Float](types/Float.md)
 * [➞mounting_method](xRayPreparation__mounting_method.md)  <sub>0..1</sub>
     * Description: Crystal mounting method
     * Range: [String](types/String.md)
 * [➞flash_cooling_method](xRayPreparation__flash_cooling_method.md)  <sub>0..1</sub>
     * Description: Flash cooling protocol
     * Range: [String](types/String.md)

### Inherited from SamplePreparation:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞preparation_type](samplePreparation__preparation_type.md)  <sub>1..1</sub>
     * Description: Type of sample preparation
     * Range: [String](types/String.md)
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
