
# Class: BufferComposition

Buffer composition for sample storage

URI: [biostride_schema:BufferComposition](https://w3id.org/biostride/schema/BufferComposition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]++-%20buffer_composition%200..1>[BufferComposition&#124;ph:float%20%3F;components:string%20*;additives:string%20*;description(i):string%20%3F],[AttributeGroup]^-[BufferComposition],[Sample],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]++-%20buffer_composition%200..1>[BufferComposition&#124;ph:float%20%3F;components:string%20*;additives:string%20*;description(i):string%20%3F],[AttributeGroup]^-[BufferComposition],[Sample],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞buffer_composition](sample__buffer_composition.md)*  <sub>0..1</sub>  **[BufferComposition](BufferComposition.md)**

## Attributes


### Own

 * [➞ph](bufferComposition__ph.md)  <sub>0..1</sub>
     * Description: pH of the buffer
     * Range: [Float](types/Float.md)
 * [➞components](bufferComposition__components.md)  <sub>0..\*</sub>
     * Description: Buffer components and their concentrations
     * Range: [String](types/String.md)
 * [➞additives](bufferComposition__additives.md)  <sub>0..\*</sub>
     * Description: Additional additives in the buffer
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
