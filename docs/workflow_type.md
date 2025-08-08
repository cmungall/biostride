

# Slot: workflow_type 


_Type of processing workflow_





URI: [biostride_schema:workflow_type](https://w3id.org/biostride/schema/workflow_type)
Alias: workflow_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [WorkflowTypeEnum](WorkflowTypeEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:workflow_type |
| native | biostride_schema:workflow_type |




## LinkML Source

<details>
```yaml
name: workflow_type
description: Type of processing workflow
from_schema: https://w3id.org/biostride/
rank: 1000
alias: workflow_type
owner: WorkflowRun
domain_of:
- WorkflowRun
range: WorkflowTypeEnum
required: true

```
</details>