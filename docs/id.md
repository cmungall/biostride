

# Slot: id 



URI: [biostride_schema:id](https://w3id.org/biostride/schema/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [OntologyTerm](OntologyTerm.md) |  |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [Study](Study.md) |  |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [Dataset](Dataset.md) | A collection of studies |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:id |
| native | biostride_schema:id |




## LinkML Source

<details>
```yaml
name: id
alias: id
domain_of:
- NamedThing
- OntologyTerm
range: string

```
</details>