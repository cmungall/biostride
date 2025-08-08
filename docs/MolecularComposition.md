

# Class: MolecularComposition 


_Molecular composition of a sample_





URI: [biostride_schema:MolecularComposition](https://w3id.org/biostride/schema/MolecularComposition)





```mermaid
 classDiagram
    class MolecularComposition
    click MolecularComposition href "../MolecularComposition/"
      MolecularComposition : ligands
        
      MolecularComposition : modifications
        
      MolecularComposition : sequences
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sequences](sequences.md) | * <br/> [String](String.md) | Amino acid or nucleotide sequences | direct |
| [modifications](modifications.md) | * <br/> [String](String.md) | Post-translational modifications or chemical modifications | direct |
| [ligands](ligands.md) | * <br/> [String](String.md) | Bound ligands or cofactors | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Sample](Sample.md) | [molecular_composition](molecular_composition.md) | range | [MolecularComposition](MolecularComposition.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:MolecularComposition |
| native | biostride_schema:MolecularComposition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MolecularComposition
description: Molecular composition of a sample
from_schema: https://w3id.org/biostride/
attributes:
  sequences:
    name: sequences
    description: Amino acid or nucleotide sequences
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - MolecularComposition
    range: string
    multivalued: true
  modifications:
    name: modifications
    description: Post-translational modifications or chemical modifications
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - MolecularComposition
    range: string
    multivalued: true
  ligands:
    name: ligands
    description: Bound ligands or cofactors
    from_schema: https://w3id.org/biostride/
    rank: 1000
    domain_of:
    - MolecularComposition
    range: string
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: MolecularComposition
description: Molecular composition of a sample
from_schema: https://w3id.org/biostride/
attributes:
  sequences:
    name: sequences
    description: Amino acid or nucleotide sequences
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: sequences
    owner: MolecularComposition
    domain_of:
    - MolecularComposition
    range: string
    multivalued: true
  modifications:
    name: modifications
    description: Post-translational modifications or chemical modifications
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: modifications
    owner: MolecularComposition
    domain_of:
    - MolecularComposition
    range: string
    multivalued: true
  ligands:
    name: ligands
    description: Bound ligands or cofactors
    from_schema: https://w3id.org/biostride/
    rank: 1000
    alias: ligands
    owner: MolecularComposition
    domain_of:
    - MolecularComposition
    range: string
    multivalued: true

```
</details>