
# Class: ExperimentalConditions

Environmental and experimental conditions

URI: [biostride_schema:ExperimentalConditions](https://w3id.org/biostride/schema/ExperimentalConditions)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20experimental_conditions%200..1>[ExperimentalConditions&#124;temperature:float%20%3F;humidity:float%20%3F;pressure:float%20%3F;atmosphere:string%20%3F],[ExperimentRun])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20experimental_conditions%200..1>[ExperimentalConditions&#124;temperature:float%20%3F;humidity:float%20%3F;pressure:float%20%3F;atmosphere:string%20%3F],[ExperimentRun])

## Referenced by Class

 *  **None** *[➞experimental_conditions](experimentRun__experimental_conditions.md)*  <sub>0..1</sub>  **[ExperimentalConditions](ExperimentalConditions.md)**

## Attributes


### Own

 * [➞temperature](experimentalConditions__temperature.md)  <sub>0..1</sub>
     * Description: Temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞humidity](experimentalConditions__humidity.md)  <sub>0..1</sub>
     * Description: Humidity percentage
     * Range: [Float](types/Float.md)
 * [➞pressure](experimentalConditions__pressure.md)  <sub>0..1</sub>
     * Description: Pressure in kPa
     * Range: [Float](types/Float.md)
 * [➞atmosphere](experimentalConditions__atmosphere.md)  <sub>0..1</sub>
     * Description: Atmosphere composition
     * Range: [String](types/String.md)
