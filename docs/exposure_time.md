

# Slot: exposure_time 


_Exposure time in seconds_





URI: [biostride_schema:exposure_time](https://w3id.org/biostride/schema/exposure_time)
Alias: exposure_time

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
| self | biostride_schema:exposure_time |
| native | biostride_schema:exposure_time |




## LinkML Source

<details>
```yaml
name: exposure_time
description: Exposure time in seconds
from_schema: https://w3id.org/biostride/
rank: 1000
alias: exposure_time
owner: Image
domain_of:
- Image
range: float

```
</details>