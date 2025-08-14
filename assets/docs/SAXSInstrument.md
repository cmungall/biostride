
# Class: SAXSInstrument

SAXS/WAXS instrument specifications

URI: [biostride_schema:SAXSInstrument](https://w3id.org/biostride/schema/SAXSInstrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument]^-[SAXSInstrument&#124;q_range_min:float%20%3F;q_range_max:float%20%3F;detector_distance_min:float%20%3F;detector_distance_max:float%20%3F;sample_changer_capacity:integer%20%3F;temperature_control_range:string%20%3F;instrument_code(i):string;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Instrument])](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument]^-[SAXSInstrument&#124;q_range_min:float%20%3F;q_range_max:float%20%3F;detector_distance_min:float%20%3F;detector_distance_max:float%20%3F;sample_changer_capacity:integer%20%3F;temperature_control_range:string%20%3F;instrument_code(i):string;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Instrument])

## Parents

 *  is_a: [Instrument](Instrument.md) - An instrument used to collect data

## Attributes


### Own

 * [➞q_range_min](sAXSInstrument__q_range_min.md)  <sub>0..1</sub>
     * Description: Minimum q value in inverse Angstroms
     * Range: [Float](types/Float.md)
 * [➞q_range_max](sAXSInstrument__q_range_max.md)  <sub>0..1</sub>
     * Description: Maximum q value in inverse Angstroms
     * Range: [Float](types/Float.md)
 * [➞detector_distance_min](sAXSInstrument__detector_distance_min.md)  <sub>0..1</sub>
     * Description: Minimum detector distance in mm
     * Range: [Float](types/Float.md)
 * [➞detector_distance_max](sAXSInstrument__detector_distance_max.md)  <sub>0..1</sub>
     * Description: Maximum detector distance in mm
     * Range: [Float](types/Float.md)
 * [➞sample_changer_capacity](sAXSInstrument__sample_changer_capacity.md)  <sub>0..1</sub>
     * Description: Number of samples in automatic sample changer
     * Range: [Integer](types/Integer.md)
 * [➞temperature_control_range](sAXSInstrument__temperature_control_range.md)  <sub>0..1</sub>
     * Description: Temperature control range in Celsius
     * Range: [String](types/String.md)

### Inherited from Instrument:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞instrument_code](instrument__instrument_code.md)  <sub>1..1</sub>
     * Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
     * Range: [String](types/String.md)
 * [➞manufacturer](instrument__manufacturer.md)  <sub>0..1</sub>
     * Description: Instrument manufacturer
     * Range: [String](types/String.md)
 * [➞model](instrument__model.md)  <sub>0..1</sub>
     * Description: Instrument model
     * Range: [String](types/String.md)
 * [➞installation_date](instrument__installation_date.md)  <sub>0..1</sub>
     * Description: Date of instrument installation
     * Range: [String](types/String.md)
 * [➞current_status](instrument__current_status.md)  <sub>0..1</sub>
     * Description: Current operational status
     * Range: [InstrumentStatusEnum](InstrumentStatusEnum.md)
