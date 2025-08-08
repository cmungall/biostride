# Enum: WorkflowTypeEnum 




_Types of processing workflows_



URI: [biostride_schema:WorkflowTypeEnum](https://w3id.org/biostride/schema/WorkflowTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| motion_correction | None | Motion correction for cryo-EM |
| ctf_estimation | None | CTF estimation |
| particle_picking | None | Particle picking |
| classification_2d | None | 2D classification |
| classification_3d | None | 3D classification |
| refinement | None | 3D refinement |
| model_building | None | Atomic model building |
| phasing | None | Phase determination |
| integration | None | Data integration |
| scaling | None | Data scaling |




## Slots

| Name | Description |
| ---  | --- |
| [workflow_type](workflow_type.md) | Type of processing workflow |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/






## LinkML Source

<details>
```yaml
name: WorkflowTypeEnum
description: Types of processing workflows
from_schema: https://w3id.org/biostride/
rank: 1000
permissible_values:
  motion_correction:
    text: motion_correction
    description: Motion correction for cryo-EM
  ctf_estimation:
    text: ctf_estimation
    description: CTF estimation
  particle_picking:
    text: particle_picking
    description: Particle picking
  classification_2d:
    text: classification_2d
    description: 2D classification
  classification_3d:
    text: classification_3d
    description: 3D classification
  refinement:
    text: refinement
    description: 3D refinement
  model_building:
    text: model_building
    description: Atomic model building
  phasing:
    text: phasing
    description: Phase determination
  integration:
    text: integration
    description: Data integration
  scaling:
    text: scaling
    description: Data scaling

```
</details>