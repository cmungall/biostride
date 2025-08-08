

# Class: ComputeResources 


_Computational resources used_





URI: [biostride_schema:ComputeResources](https://w3id.org/biostride/schema/ComputeResources)





```mermaid
 classDiagram
    class ComputeResources
    click ComputeResources href "../ComputeResources/"
      ComputeResources : cpu_hours
        
      ComputeResources : gpu_hours
        
      ComputeResources : memory_gb
        
      ComputeResources : storage_gb
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cpu_hours](cpu_hours.md) | 0..1 <br/> [Float](Float.md) | CPU hours used | direct |
| [gpu_hours](gpu_hours.md) | 0..1 <br/> [Float](Float.md) | GPU hours used | direct |
| [memory_gb](memory_gb.md) | 0..1 <br/> [Float](Float.md) | Maximum memory used in GB | direct |
| [storage_gb](storage_gb.md) | 0..1 <br/> [Float](Float.md) | Storage used in GB | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | [compute_resources](compute_resources.md) | range | [ComputeResources](ComputeResources.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:ComputeResources |
| native | biostride_schema:ComputeResources |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComputeResources
description: Computational resources used
from_schema: https://w3id.org/biostride/
attributes:
  cpu_hours:
    name: cpu_hours
    description: CPU hours used
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - ComputeResources
    range: float
  gpu_hours:
    name: gpu_hours
    description: GPU hours used
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - ComputeResources
    range: float
  memory_gb:
    name: memory_gb
    description: Maximum memory used in GB
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - ComputeResources
    range: float
  storage_gb:
    name: storage_gb
    description: Storage used in GB
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - ComputeResources
    range: float

```
</details>

### Induced

<details>
```yaml
name: ComputeResources
description: Computational resources used
from_schema: https://w3id.org/biostride/
attributes:
  cpu_hours:
    name: cpu_hours
    description: CPU hours used
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: cpu_hours
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: float
  gpu_hours:
    name: gpu_hours
    description: GPU hours used
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: gpu_hours
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: float
  memory_gb:
    name: memory_gb
    description: Maximum memory used in GB
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: memory_gb
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: float
  storage_gb:
    name: storage_gb
    description: Storage used in GB
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: storage_gb
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: float

```
</details>