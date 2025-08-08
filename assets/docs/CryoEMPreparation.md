
# Class: CryoEMPreparation

Cryo-EM specific sample preparation

URI: [biostride_schema:CryoEMPreparation](https://w3id.org/biostride/schema/CryoEMPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation],[TechniqueSpecificPreparation]^-[CryoEMPreparation&#124;grid_type:GridTypeEnum%20%3F;support_film:string%20%3F;hole_size:float%20%3F;vitrification_method:VitrificationMethodEnum%20%3F;blot_time:float%20%3F;blot_force:integer%20%3F;humidity_percentage:float%20%3F;chamber_temperature:float%20%3F;plasma_treatment:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation],[TechniqueSpecificPreparation]^-[CryoEMPreparation&#124;grid_type:GridTypeEnum%20%3F;support_film:string%20%3F;hole_size:float%20%3F;vitrification_method:VitrificationMethodEnum%20%3F;blot_time:float%20%3F;blot_force:integer%20%3F;humidity_percentage:float%20%3F;chamber_temperature:float%20%3F;plasma_treatment:string%20%3F])

## Parents

 *  is_a: [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) - Base class for technique-specific preparation details

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
