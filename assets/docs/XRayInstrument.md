
# Class: XRayInstrument

X-ray diffractometer or synchrotron beamline specifications

URI: [biostride_schema:XRayInstrument](https://w3id.org/biostride/schema/XRayInstrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument]^-[XRayInstrument&#124;source_type:XRaySourceTypeEnum%20%3F;energy_min:float%20%3F;energy_max:float%20%3F;beam_size_min:float%20%3F;beam_size_max:float%20%3F;flux_density:float%20%3F;monochromator_type:string%20%3F;goniometer_type:string%20%3F;crystal_cooling_capability:boolean%20%3F;instrument_code(i):string;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Instrument])](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument]^-[XRayInstrument&#124;source_type:XRaySourceTypeEnum%20%3F;energy_min:float%20%3F;energy_max:float%20%3F;beam_size_min:float%20%3F;beam_size_max:float%20%3F;flux_density:float%20%3F;monochromator_type:string%20%3F;goniometer_type:string%20%3F;crystal_cooling_capability:boolean%20%3F;instrument_code(i):string;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Instrument])

## Parents

 *  is_a: [Instrument](Instrument.md) - An instrument used to collect data

## Attributes


### Own

 * [➞source_type](xRayInstrument__source_type.md)  <sub>0..1</sub>
     * Description: Type of X-ray source
     * Range: [XRaySourceTypeEnum](XRaySourceTypeEnum.md)
 * [➞energy_min](xRayInstrument__energy_min.md)  <sub>0..1</sub>
     * Description: Minimum X-ray energy in keV
     * Range: [Float](types/Float.md)
 * [➞energy_max](xRayInstrument__energy_max.md)  <sub>0..1</sub>
     * Description: Maximum X-ray energy in keV
     * Range: [Float](types/Float.md)
 * [➞beam_size_min](xRayInstrument__beam_size_min.md)  <sub>0..1</sub>
     * Description: Minimum beam size in micrometers
     * Range: [Float](types/Float.md)
 * [➞beam_size_max](xRayInstrument__beam_size_max.md)  <sub>0..1</sub>
     * Description: Maximum beam size in micrometers
     * Range: [Float](types/Float.md)
 * [➞flux_density](xRayInstrument__flux_density.md)  <sub>0..1</sub>
     * Description: Photon flux density in photons/s/mm²
     * Range: [Float](types/Float.md)
 * [➞monochromator_type](xRayInstrument__monochromator_type.md)  <sub>0..1</sub>
     * Description: Type of monochromator
     * Range: [String](types/String.md)
 * [➞goniometer_type](xRayInstrument__goniometer_type.md)  <sub>0..1</sub>
     * Description: Type of goniometer
     * Range: [String](types/String.md)
 * [➞crystal_cooling_capability](xRayInstrument__crystal_cooling_capability.md)  <sub>0..1</sub>
     * Description: Crystal cooling system available
     * Range: [Boolean](types/Boolean.md)

### Inherited from Instrument:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞instrument_code](instrument__instrument_code.md)  <sub>1..1</sub>
     * Description: Unique identifier code for the instrument
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
