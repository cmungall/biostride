
# Class: WorkflowRun

A computational processing workflow execution

URI: [biostride_schema:WorkflowRun](https://w3id.org/biostride/schema/WorkflowRun)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataFile]<output_files%200..*-%20[WorkflowRun&#124;workflow_code:string;workflow_type:WorkflowTypeEnum;experiment_id:string;processing_level:integer%20%3F;software_name:string;software_version:string%20%3F;processing_parameters:string%20%3F;started_at:string%20%3F;completed_at:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[ComputeResources]<compute_resources%200..1-++[WorkflowRun],[Study]++-%20workflow_runs%200..*>[WorkflowRun],[NamedThing]^-[WorkflowRun],[Study],[NamedThing],[DataFile],[ComputeResources])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataFile]<output_files%200..*-%20[WorkflowRun&#124;workflow_code:string;workflow_type:WorkflowTypeEnum;experiment_id:string;processing_level:integer%20%3F;software_name:string;software_version:string%20%3F;processing_parameters:string%20%3F;started_at:string%20%3F;completed_at:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[ComputeResources]<compute_resources%200..1-++[WorkflowRun],[Study]++-%20workflow_runs%200..*>[WorkflowRun],[NamedThing]^-[WorkflowRun],[Study],[NamedThing],[DataFile],[ComputeResources])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞workflow_runs](study__workflow_runs.md)*  <sub>0..\*</sub>  **[WorkflowRun](WorkflowRun.md)**

## Attributes


### Own

 * [➞workflow_code](workflowRun__workflow_code.md)  <sub>1..1</sub>
     * Description: Unique workflow identifier
     * Range: [String](types/String.md)
 * [➞workflow_type](workflowRun__workflow_type.md)  <sub>1..1</sub>
     * Description: Type of processing workflow
     * Range: [WorkflowTypeEnum](WorkflowTypeEnum.md)
 * [➞experiment_id](workflowRun__experiment_id.md)  <sub>1..1</sub>
     * Description: Reference to the source experiment
     * Range: [String](types/String.md)
 * [➞processing_level](workflowRun__processing_level.md)  <sub>0..1</sub>
     * Description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
     * Range: [Integer](types/Integer.md)
 * [➞software_name](workflowRun__software_name.md)  <sub>1..1</sub>
     * Description: Software used for processing
     * Range: [String](types/String.md)
 * [➞software_version](workflowRun__software_version.md)  <sub>0..1</sub>
     * Description: Software version
     * Range: [String](types/String.md)
 * [➞processing_parameters](workflowRun__processing_parameters.md)  <sub>0..1</sub>
     * Description: Parameters used in processing
     * Range: [String](types/String.md)
 * [➞compute_resources](workflowRun__compute_resources.md)  <sub>0..1</sub>
     * Description: Computational resources used
     * Range: [ComputeResources](ComputeResources.md)
 * [➞started_at](workflowRun__started_at.md)  <sub>0..1</sub>
     * Description: Workflow start time
     * Range: [String](types/String.md)
 * [➞completed_at](workflowRun__completed_at.md)  <sub>0..1</sub>
     * Description: Workflow completion time
     * Range: [String](types/String.md)
 * [➞output_files](workflowRun__output_files.md)  <sub>0..\*</sub>
     * Description: Output files generated
     * Range: [DataFile](DataFile.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
