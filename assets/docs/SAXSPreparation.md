
# Class: SAXSPreparation

SAXS/WAXS specific preparation

URI: [biostride_schema:SAXSPreparation](https://w3id.org/biostride/schema/SAXSPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SamplePreparation],[SamplePreparation]^-[SAXSPreparation&#124;concentration_series:float%20*;buffer_matching_protocol:string%20%3F;sample_cell_type:string%20%3F;cell_path_length:float%20%3F;temperature_control:string%20%3F;preparation_type(i):string;sample_id(i):string;preparation_date(i):string%20%3F;operator_id(i):string%20%3F;protocol_description(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[SamplePreparation],[SamplePreparation]^-[SAXSPreparation&#124;concentration_series:float%20*;buffer_matching_protocol:string%20%3F;sample_cell_type:string%20%3F;cell_path_length:float%20%3F;temperature_control:string%20%3F;preparation_type(i):string;sample_id(i):string;preparation_date(i):string%20%3F;operator_id(i):string%20%3F;protocol_description(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [SamplePreparation](SamplePreparation.md) - A process that prepares a sample for imaging

## Attributes


### Own

 * [➞concentration_series](sAXSPreparation__concentration_series.md)  <sub>0..\*</sub>
     * Description: Concentration values for series measurements
     * Range: [Float](types/Float.md)
 * [➞buffer_matching_protocol](sAXSPreparation__buffer_matching_protocol.md)  <sub>0..1</sub>
     * Description: Protocol for buffer matching
     * Range: [String](types/String.md)
 * [➞sample_cell_type](sAXSPreparation__sample_cell_type.md)  <sub>0..1</sub>
     * Description: Type of sample cell used
     * Range: [String](types/String.md)
 * [➞cell_path_length](sAXSPreparation__cell_path_length.md)  <sub>0..1</sub>
     * Description: Path length in mm
     * Range: [Float](types/Float.md)
 * [➞temperature_control](sAXSPreparation__temperature_control.md)  <sub>0..1</sub>
     * Description: Temperature control settings
     * Range: [String](types/String.md)

### Inherited from SamplePreparation:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞preparation_type](samplePreparation__preparation_type.md)  <sub>1..1</sub>
     * Description: Type of sample preparation
     * Range: [String](types/String.md)
 * [➞sample_id](samplePreparation__sample_id.md)  <sub>1..1</sub>
     * Description: Reference to the sample being prepared
     * Range: [String](types/String.md)
 * [➞preparation_date](samplePreparation__preparation_date.md)  <sub>0..1</sub>
     * Description: Date of sample preparation
     * Range: [String](types/String.md)
 * [➞operator_id](samplePreparation__operator_id.md)  <sub>0..1</sub>
     * Description: Person who performed the preparation
     * Range: [String](types/String.md)
 * [➞protocol_description](samplePreparation__protocol_description.md)  <sub>0..1</sub>
     * Description: Detailed protocol description
     * Range: [String](types/String.md)
