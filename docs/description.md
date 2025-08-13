

# Slot: description 



URI: [biostride_schema:description](https://w3id.org/biostride/schema/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [Dataset](Dataset.md) | A collection of studies |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [Study](Study.md) |  |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:description |
| native | biostride_schema:description |




## LinkML Source

<details>
```yaml
name: description
from_schema: https://w3id.org/biostride/
rank: 1000
alias: description
owner: NamedThing
domain_of:
- NamedThing
range: string

```
</details>