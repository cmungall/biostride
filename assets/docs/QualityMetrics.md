
# Class: QualityMetrics

Quality metrics for experiments

URI: [biostride_schema:QualityMetrics](https://w3id.org/biostride/schema/QualityMetrics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20quality_metrics%200..1>[QualityMetrics&#124;resolution:float%20%3F;completeness:float%20%3F;signal_to_noise:float%20%3F;r_factor:float%20%3F],[ExperimentRun])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20quality_metrics%200..1>[QualityMetrics&#124;resolution:float%20%3F;completeness:float%20%3F;signal_to_noise:float%20%3F;r_factor:float%20%3F],[ExperimentRun])

## Referenced by Class

 *  **None** *[➞quality_metrics](experimentRun__quality_metrics.md)*  <sub>0..1</sub>  **[QualityMetrics](QualityMetrics.md)**

## Attributes


### Own

 * [➞resolution](qualityMetrics__resolution.md)  <sub>0..1</sub>
     * Description: Resolution in Angstroms
     * Range: [Float](types/Float.md)
 * [➞completeness](qualityMetrics__completeness.md)  <sub>0..1</sub>
     * Description: Data completeness percentage
     * Range: [Float](types/Float.md)
 * [➞signal_to_noise](qualityMetrics__signal_to_noise.md)  <sub>0..1</sub>
     * Description: Signal to noise ratio
     * Range: [Float](types/Float.md)
 * [➞r_factor](qualityMetrics__r_factor.md)  <sub>0..1</sub>
     * Description: R-factor for crystallography
     * Range: [Float](types/Float.md)
