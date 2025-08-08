

# Slot: pixel_size 


_Pixel size in Angstroms_





URI: [biostride_schema:pixel_size](https://w3id.org/biostride/schema/pixel_size)
Alias: pixel_size

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/biostride/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | biostride_schema:pixel_size |
| native | biostride_schema:pixel_size |




## LinkML Source

<details>
```yaml
name: pixel_size
description: Pixel size in Angstroms
from_schema: https://w3id.org/biostride/
rank: 1000
alias: pixel_size
owner: Image
domain_of:
- Image
range: float

```
</details>