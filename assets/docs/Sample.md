
# Class: Sample

A biological sample used in structural biology experiments

URI: [biostride_schema:Sample](https://w3id.org/biostride/schema/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StorageConditions],[Sample]<parent_sample_id%200..1-%20[Sample&#124;sample_code:string;sample_type:SampleTypeEnum;molecular_weight:float%20%3F;concentration:float%20%3F;concentration_unit:ConcentrationUnitEnum%20%3F;preparation_method:string%20%3F;purity_percentage:float%20%3F;quality_metrics:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[StorageConditions]<storage_conditions%200..1-++[Sample],[BufferComposition]<buffer_composition%200..1-++[Sample],[MolecularComposition]<molecular_composition%200..1-++[Sample],[Study]++-%20samples%200..*>[Sample],[NamedThing]^-[Sample],[Study],[NamedThing],[MolecularComposition],[BufferComposition])](https://yuml.me/diagram/nofunky;dir:TB/class/[StorageConditions],[Sample]<parent_sample_id%200..1-%20[Sample&#124;sample_code:string;sample_type:SampleTypeEnum;molecular_weight:float%20%3F;concentration:float%20%3F;concentration_unit:ConcentrationUnitEnum%20%3F;preparation_method:string%20%3F;purity_percentage:float%20%3F;quality_metrics:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[StorageConditions]<storage_conditions%200..1-++[Sample],[BufferComposition]<buffer_composition%200..1-++[Sample],[MolecularComposition]<molecular_composition%200..1-++[Sample],[Study]++-%20samples%200..*>[Sample],[NamedThing]^-[Sample],[Study],[NamedThing],[MolecularComposition],[BufferComposition])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞parent_sample_id](sample__parent_sample_id.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**
 *  **None** *[➞samples](study__samples.md)*  <sub>0..\*</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [➞sample_code](sample__sample_code.md)  <sub>1..1</sub>
     * Description: Unique identifier code for the sample
     * Range: [String](types/String.md)
 * [➞sample_type](sample__sample_type.md)  <sub>1..1</sub>
     * Description: Type of biological sample
     * Range: [SampleTypeEnum](SampleTypeEnum.md)
 * [➞molecular_composition](sample__molecular_composition.md)  <sub>0..1</sub>
     * Description: Description of molecular composition including sequences, modifications, ligands
     * Range: [MolecularComposition](MolecularComposition.md)
 * [➞molecular_weight](sample__molecular_weight.md)  <sub>0..1</sub>
     * Description: Molecular weight in kDa
     * Range: [Float](types/Float.md)
 * [➞concentration](sample__concentration.md)  <sub>0..1</sub>
     * Description: Sample concentration in mg/mL or µM
     * Range: [Float](types/Float.md)
 * [➞concentration_unit](sample__concentration_unit.md)  <sub>0..1</sub>
     * Description: Unit of concentration measurement
     * Range: [ConcentrationUnitEnum](ConcentrationUnitEnum.md)
 * [➞buffer_composition](sample__buffer_composition.md)  <sub>0..1</sub>
     * Description: Buffer composition including pH, salts, additives
     * Range: [BufferComposition](BufferComposition.md)
 * [➞preparation_method](sample__preparation_method.md)  <sub>0..1</sub>
     * Description: Method used to prepare the sample
     * Range: [String](types/String.md)
 * [➞storage_conditions](sample__storage_conditions.md)  <sub>0..1</sub>
     * Description: Storage conditions for the sample
     * Range: [StorageConditions](StorageConditions.md)
 * [➞parent_sample_id](sample__parent_sample_id.md)  <sub>0..1</sub>
     * Description: Reference to parent sample for derivation tracking
     * Range: [Sample](Sample.md)
 * [➞purity_percentage](sample__purity_percentage.md)  <sub>0..1</sub>
     * Description: Sample purity as percentage
     * Range: [Float](types/Float.md)
 * [➞quality_metrics](sample__quality_metrics.md)  <sub>0..1</sub>
     * Description: Quality control metrics for the sample
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
