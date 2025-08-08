
# Class: CryoEMInstrument

Cryo-EM microscope specifications

URI: [biostride_schema:CryoEMInstrument](https://w3id.org/biostride/schema/CryoEMInstrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument],[Instrument]^-[CryoEMInstrument&#124;accelerating_voltage:integer%20%3F;cs_corrector:boolean%20%3F;phase_plate:boolean%20%3F;detector_type:DetectorTypeEnum%20%3F;detector_dimensions:string%20%3F;pixel_size_min:float%20%3F;pixel_size_max:float%20%3F;autoloader_capacity:integer%20%3F;instrument_code(i):string;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument],[Instrument]^-[CryoEMInstrument&#124;accelerating_voltage:integer%20%3F;cs_corrector:boolean%20%3F;phase_plate:boolean%20%3F;detector_type:DetectorTypeEnum%20%3F;detector_dimensions:string%20%3F;pixel_size_min:float%20%3F;pixel_size_max:float%20%3F;autoloader_capacity:integer%20%3F;instrument_code(i):string;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [Instrument](Instrument.md) - An instrument used to collect data

## Attributes


### Own

 * [➞accelerating_voltage](cryoEMInstrument__accelerating_voltage.md)  <sub>0..1</sub>
     * Description: Accelerating voltage in kV
     * Range: [Integer](types/Integer.md)
 * [➞cs_corrector](cryoEMInstrument__cs_corrector.md)  <sub>0..1</sub>
     * Description: Spherical aberration corrector present
     * Range: [Boolean](types/Boolean.md)
 * [➞phase_plate](cryoEMInstrument__phase_plate.md)  <sub>0..1</sub>
     * Description: Phase plate available
     * Range: [Boolean](types/Boolean.md)
 * [➞detector_type](cryoEMInstrument__detector_type.md)  <sub>0..1</sub>
     * Description: Type of detector
     * Range: [DetectorTypeEnum](DetectorTypeEnum.md)
 * [➞detector_dimensions](cryoEMInstrument__detector_dimensions.md)  <sub>0..1</sub>
     * Description: Detector dimensions in pixels (e.g., 4096x4096)
     * Range: [String](types/String.md)
 * [➞pixel_size_min](cryoEMInstrument__pixel_size_min.md)  <sub>0..1</sub>
     * Description: Minimum pixel size in Angstroms per pixel
     * Range: [Float](types/Float.md)
 * [➞pixel_size_max](cryoEMInstrument__pixel_size_max.md)  <sub>0..1</sub>
     * Description: Maximum pixel size in Angstroms per pixel
     * Range: [Float](types/Float.md)
 * [➞autoloader_capacity](cryoEMInstrument__autoloader_capacity.md)  <sub>0..1</sub>
     * Description: Number of grids the autoloader can hold
     * Range: [Integer](types/Integer.md)

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
