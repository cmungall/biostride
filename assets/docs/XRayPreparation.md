
# Class: XRayPreparation

X-ray crystallography specific preparation

URI: [biostride_schema:XRayPreparation](https://w3id.org/biostride/schema/XRayPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation]^-[XRayPreparation&#124;crystallization_method:CrystallizationMethodEnum%20%3F;crystallization_conditions:string%20%3F;crystal_size:string%20%3F;cryoprotectant:string%20%3F;cryoprotectant_concentration:float%20%3F;mounting_method:string%20%3F;flash_cooling_method:string%20%3F],[TechniqueSpecificPreparation])](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation]^-[XRayPreparation&#124;crystallization_method:CrystallizationMethodEnum%20%3F;crystallization_conditions:string%20%3F;crystal_size:string%20%3F;cryoprotectant:string%20%3F;cryoprotectant_concentration:float%20%3F;mounting_method:string%20%3F;flash_cooling_method:string%20%3F],[TechniqueSpecificPreparation])

## Parents

 *  is_a: [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) - Base class for technique-specific preparation details

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
