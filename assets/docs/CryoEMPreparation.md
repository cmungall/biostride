
# Class: CryoEMPreparation

Cryo-EM specific sample preparation

URI: [biostride_schema:CryoEMPreparation](https://w3id.org/biostride/schema/CryoEMPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SamplePreparation],[SamplePreparation]^-[CryoEMPreparation&#124;grid_type:GridTypeEnum%20%3F;support_film:string%20%3F;hole_size:float%20%3F;vitrification_method:VitrificationMethodEnum%20%3F;blot_time:float%20%3F;blot_force:integer%20%3F;humidity_percentage:float%20%3F;chamber_temperature:float%20%3F;plasma_treatment:string%20%3F;preparation_type(i):string;sample_id(i):string;preparation_date(i):string%20%3F;operator_id(i):string%20%3F;protocol_description(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[SamplePreparation],[SamplePreparation]^-[CryoEMPreparation&#124;grid_type:GridTypeEnum%20%3F;support_film:string%20%3F;hole_size:float%20%3F;vitrification_method:VitrificationMethodEnum%20%3F;blot_time:float%20%3F;blot_force:integer%20%3F;humidity_percentage:float%20%3F;chamber_temperature:float%20%3F;plasma_treatment:string%20%3F;preparation_type(i):string;sample_id(i):string;preparation_date(i):string%20%3F;operator_id(i):string%20%3F;protocol_description(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [SamplePreparation](SamplePreparation.md) - A process that prepares a sample for imaging

## Attributes


### Own

 * [➞grid_type](cryoEMPreparation__grid_type.md)  <sub>0..1</sub>
     * Description: Type of EM grid used
     * Range: [GridTypeEnum](GridTypeEnum.md)
 * [➞support_film](cryoEMPreparation__support_film.md)  <sub>0..1</sub>
     * Description: Support film type
     * Range: [String](types/String.md)
 * [➞hole_size](cryoEMPreparation__hole_size.md)  <sub>0..1</sub>
     * Description: Hole size in micrometers
     * Range: [Float](types/Float.md)
 * [➞vitrification_method](cryoEMPreparation__vitrification_method.md)  <sub>0..1</sub>
     * Description: Method used for vitrification
     * Range: [VitrificationMethodEnum](VitrificationMethodEnum.md)
 * [➞blot_time](cryoEMPreparation__blot_time.md)  <sub>0..1</sub>
     * Description: Blotting time in seconds
     * Range: [Float](types/Float.md)
 * [➞blot_force](cryoEMPreparation__blot_force.md)  <sub>0..1</sub>
     * Description: Blotting force setting
     * Range: [Integer](types/Integer.md)
 * [➞humidity_percentage](cryoEMPreparation__humidity_percentage.md)  <sub>0..1</sub>
     * Description: Chamber humidity during vitrification
     * Range: [Float](types/Float.md)
 * [➞chamber_temperature](cryoEMPreparation__chamber_temperature.md)  <sub>0..1</sub>
     * Description: Chamber temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞plasma_treatment](cryoEMPreparation__plasma_treatment.md)  <sub>0..1</sub>
     * Description: Plasma treatment details
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
