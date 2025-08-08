
# Class: Instrument

An instrument used to collect data

URI: [biostride_schema:Instrument](https://w3id.org/biostride/schema/Instrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[XRayInstrument],[SAXSInstrument],[NamedThing],[Instrument&#124;instrument_code:string;manufacturer:string%20%3F;model:string%20%3F;installation_date:string%20%3F;current_status:InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F]^-[XRayInstrument],[Instrument]^-[SAXSInstrument],[Instrument]^-[CryoEMInstrument],[NamedThing]^-[Instrument],[CryoEMInstrument])](https://yuml.me/diagram/nofunky;dir:TB/class/[XRayInstrument],[SAXSInstrument],[NamedThing],[Instrument&#124;instrument_code:string;manufacturer:string%20%3F;model:string%20%3F;installation_date:string%20%3F;current_status:InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F]^-[XRayInstrument],[Instrument]^-[SAXSInstrument],[Instrument]^-[CryoEMInstrument],[NamedThing]^-[Instrument],[CryoEMInstrument])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Children

 * [CryoEMInstrument](CryoEMInstrument.md) - Cryo-EM microscope specifications
 * [SAXSInstrument](SAXSInstrument.md) - SAXS/WAXS instrument specifications
 * [XRayInstrument](XRayInstrument.md) - X-ray diffractometer or synchrotron beamline specifications

## Referenced by Class


## Attributes


### Own

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

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
