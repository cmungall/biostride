
# Class: Dataset

A collection of studies

URI: [biostride_schema:Dataset](https://w3id.org/biostride/schema/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[NamedThing],[Study]<studies%200..*-++[Dataset&#124;keywords:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[NamedThing],[Study]<studies%200..*-++[Dataset&#124;keywords:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[Dataset])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Attributes


### Own

 * [➞keywords](dataset__keywords.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞studies](dataset__studies.md)  <sub>0..\*</sub>
     * Range: [Study](Study.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
