
# Class: NamedThing

A named thing

URI: [biostride_schema:NamedThing](https://w3id.org/biostride/schema/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[Study],[SamplePreparation],[Sample],[NamedThing&#124;id:uriorcurie;title:string%20%3F;description:string%20%3F]^-[WorkflowRun],[NamedThing]^-[Study],[NamedThing]^-[SamplePreparation],[NamedThing]^-[Sample],[NamedThing]^-[Instrument],[NamedThing]^-[Image],[NamedThing]^-[ExperimentRun],[NamedThing]^-[Dataset],[NamedThing]^-[DataFile],[Instrument],[Image],[ExperimentRun],[Dataset],[DataFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[Study],[SamplePreparation],[Sample],[NamedThing&#124;id:uriorcurie;title:string%20%3F;description:string%20%3F]^-[WorkflowRun],[NamedThing]^-[Study],[NamedThing]^-[SamplePreparation],[NamedThing]^-[Sample],[NamedThing]^-[Instrument],[NamedThing]^-[Image],[NamedThing]^-[ExperimentRun],[NamedThing]^-[Dataset],[NamedThing]^-[DataFile],[Instrument],[Image],[ExperimentRun],[Dataset],[DataFile])

## Children

 * [DataFile](DataFile.md) - A data file generated or used in the study
 * [Dataset](Dataset.md) - A collection of studies
 * [ExperimentRun](ExperimentRun.md) - An experimental data collection session
 * [Image](Image.md) - An image file from structural biology experiments
 * [Instrument](Instrument.md) - An instrument used to collect data
 * [Sample](Sample.md) - A biological sample used in structural biology experiments
 * [SamplePreparation](SamplePreparation.md) - A process that prepares a sample for imaging
 * [Study](Study.md)
 * [WorkflowRun](WorkflowRun.md) - A computational processing workflow execution

## Referenced by Class


## Attributes


### Own

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
