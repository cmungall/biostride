
# Class: Study



URI: [biostride_schema:Study](https://w3id.org/biostride/schema/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[Image]<images%200..*-++[Study&#124;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[DataFile]<data_files%200..*-++[Study],[WorkflowRun]<workflow_runs%200..*-++[Study],[ExperimentRun]<instrument_runs%200..*-++[Study],[SamplePreparation]<sample_preparations%200..*-++[Study],[Sample]<samples%200..*-++[Study],[Dataset]++-%20studies%200..*>[Study],[NamedThing]^-[Study],[SamplePreparation],[Sample],[NamedThing],[Image],[ExperimentRun],[Dataset],[DataFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[Image]<images%200..*-++[Study&#124;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[DataFile]<data_files%200..*-++[Study],[WorkflowRun]<workflow_runs%200..*-++[Study],[ExperimentRun]<instrument_runs%200..*-++[Study],[SamplePreparation]<sample_preparations%200..*-++[Study],[Sample]<samples%200..*-++[Study],[Dataset]++-%20studies%200..*>[Study],[NamedThing]^-[Study],[SamplePreparation],[Sample],[NamedThing],[Image],[ExperimentRun],[Dataset],[DataFile])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞studies](dataset__studies.md)*  <sub>0..\*</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [➞samples](study__samples.md)  <sub>0..\*</sub>
     * Range: [Sample](Sample.md)
 * [➞sample_preparations](study__sample_preparations.md)  <sub>0..\*</sub>
     * Range: [SamplePreparation](SamplePreparation.md)
 * [➞instrument_runs](study__instrument_runs.md)  <sub>0..\*</sub>
     * Range: [ExperimentRun](ExperimentRun.md)
 * [➞workflow_runs](study__workflow_runs.md)  <sub>0..\*</sub>
     * Range: [WorkflowRun](WorkflowRun.md)
 * [➞data_files](study__data_files.md)  <sub>0..\*</sub>
     * Range: [DataFile](DataFile.md)
 * [➞images](study__images.md)  <sub>0..\*</sub>
     * Range: [Image](Image.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
