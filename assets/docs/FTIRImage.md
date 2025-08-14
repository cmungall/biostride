
# Class: FTIRImage

Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy

URI: [biostride_schema:FTIRImage](https://w3id.org/biostride/schema/FTIRImage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Image],[Image]^-[FTIRImage&#124;wavenumber_min:float%20%3F;wavenumber_max:float%20%3F;spectral_resolution:float%20%3F;number_of_scans:integer%20%3F;apodization_function:string%20%3F;molecular_signatures:string%20*;background_correction:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Image],[Image]^-[FTIRImage&#124;wavenumber_min:float%20%3F;wavenumber_max:float%20%3F;spectral_resolution:float%20%3F;number_of_scans:integer%20%3F;apodization_function:string%20%3F;molecular_signatures:string%20*;background_correction:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [Image](Image.md) - An image file from structural biology experiments

## Attributes


### Own

 * [➞wavenumber_min](fTIRImage__wavenumber_min.md)  <sub>0..1</sub>
     * Description: Minimum wavenumber in cm⁻¹
     * Range: [Float](types/Float.md)
 * [➞wavenumber_max](fTIRImage__wavenumber_max.md)  <sub>0..1</sub>
     * Description: Maximum wavenumber in cm⁻¹
     * Range: [Float](types/Float.md)
 * [➞spectral_resolution](fTIRImage__spectral_resolution.md)  <sub>0..1</sub>
     * Description: Spectral resolution in cm⁻¹
     * Range: [Float](types/Float.md)
 * [➞number_of_scans](fTIRImage__number_of_scans.md)  <sub>0..1</sub>
     * Description: Number of scans averaged for the spectrum
     * Range: [Integer](types/Integer.md)
 * [➞apodization_function](fTIRImage__apodization_function.md)  <sub>0..1</sub>
     * Description: Mathematical function used for apodization
     * Range: [String](types/String.md)
 * [➞molecular_signatures](fTIRImage__molecular_signatures.md)  <sub>0..\*</sub>
     * Description: Identified molecular signatures or peaks
     * Range: [String](types/String.md)
 * [➞background_correction](fTIRImage__background_correction.md)  <sub>0..1</sub>
     * Description: Method used for background correction
     * Range: [String](types/String.md)

### Inherited from Image:

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
