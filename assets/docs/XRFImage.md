
# Class: XRFImage

X-ray fluorescence (XRF) image showing elemental distribution

URI: [biostride_schema:XRFImage](https://w3id.org/biostride/schema/XRFImage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D]^-[XRFImage&#124;beam_energy:float%20%3F;beam_size:float%20%3F;dwell_time:float%20%3F;elements_measured:string%20*;source_type:XRaySourceTypeEnum%20%3F;detector_type:string%20%3F;flux:float%20%3F;calibration_standard:string%20%3F;defocus(i):float%20%3F;astigmatism(i):float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D]^-[XRFImage&#124;beam_energy:float%20%3F;beam_size:float%20%3F;dwell_time:float%20%3F;elements_measured:string%20*;source_type:XRaySourceTypeEnum%20%3F;detector_type:string%20%3F;flux:float%20%3F;calibration_standard:string%20%3F;defocus(i):float%20%3F;astigmatism(i):float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)

## Attributes


### Own

 * [➞beam_energy](xRFImage__beam_energy.md)  <sub>0..1</sub>
     * Description: X-ray beam energy in keV
     * Range: [Float](types/Float.md)
 * [➞beam_size](xRFImage__beam_size.md)  <sub>0..1</sub>
     * Description: X-ray beam size in micrometers
     * Range: [Float](types/Float.md)
 * [➞dwell_time](xRFImage__dwell_time.md)  <sub>0..1</sub>
     * Description: Dwell time per pixel in milliseconds
     * Range: [Float](types/Float.md)
 * [➞elements_measured](xRFImage__elements_measured.md)  <sub>0..\*</sub>
     * Description: Elements detected and measured
     * Range: [String](types/String.md)
 * [➞source_type](xRFImage__source_type.md)  <sub>0..1</sub>
     * Description: X-ray source type (synchrotron or lab-source)
     * Range: [XRaySourceTypeEnum](XRaySourceTypeEnum.md)
 * [➞detector_type](xRFImage__detector_type.md)  <sub>0..1</sub>
     * Description: Type of X-ray detector used
     * Range: [String](types/String.md)
 * [➞flux](xRFImage__flux.md)  <sub>0..1</sub>
     * Description: Photon flux in photons/second
     * Range: [Float](types/Float.md)
 * [➞calibration_standard](xRFImage__calibration_standard.md)  <sub>0..1</sub>
     * Description: Reference standard used for calibration
     * Range: [String](types/String.md)

### Inherited from Image2D:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞file_name](image__file_name.md)  <sub>1..1</sub>
     * Description: Image file name
     * Range: [String](types/String.md)
 * [➞acquisition_date](image__acquisition_date.md)  <sub>0..1</sub>
     * Description: Date image was acquired
     * Range: [String](types/String.md)
 * [➞pixel_size](image__pixel_size.md)  <sub>0..1</sub>
     * Description: Pixel size in Angstroms
     * Range: [Float](types/Float.md)
 * [➞dimensions_x](image__dimensions_x.md)  <sub>0..1</sub>
     * Description: Image width in pixels
     * Range: [Integer](types/Integer.md)
 * [➞dimensions_y](image__dimensions_y.md)  <sub>0..1</sub>
     * Description: Image height in pixels
     * Range: [Integer](types/Integer.md)
 * [➞exposure_time](image__exposure_time.md)  <sub>0..1</sub>
     * Description: Exposure time in seconds
     * Range: [Float](types/Float.md)
 * [➞dose](image__dose.md)  <sub>0..1</sub>
     * Description: Electron dose in e-/Å²
     * Range: [Float](types/Float.md)
 * [➞defocus](image2D__defocus.md)  <sub>0..1</sub>
     * Description: Defocus value in micrometers
     * Range: [Float](types/Float.md)
 * [➞astigmatism](image2D__astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism value
     * Range: [Float](types/Float.md)
