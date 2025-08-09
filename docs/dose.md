

# Slot: dose 


_Electron dose in e-/Å²_





URI: [biostride_schema:dose](https://w3id.org/biostride/schema/dose)
Alias: dose

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:dose |
| native | biostride_schema:dose |




## LinkML Source

<details>
```yaml
name: dose
description: Electron dose in e-/Å²
from_schema: https://w3id.org/biostride/
rank: 1000
alias: dose
owner: Image
domain_of:
- Image
range: float

```
</details>