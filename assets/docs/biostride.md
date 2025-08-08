
# biostride-schema


**metamodel version:** 1.7.0

**version:** None


A linkml schema for representing structural biological imaging data and experiments plus results


### Classes

 * [BufferComposition](BufferComposition.md) - Buffer composition for sample storage
 * [ComputeResources](ComputeResources.md) - Computational resources used
 * [DataCollectionStrategy](DataCollectionStrategy.md) - Strategy for data collection
 * [ExperimentalConditions](ExperimentalConditions.md) - Environmental and experimental conditions
 * [ImageFeature](ImageFeature.md)
 * [MolecularComposition](MolecularComposition.md) - Molecular composition of a sample
 * [NamedThing](NamedThing.md) - A named thing
     * [DataFile](DataFile.md) - A data file generated or used in the study
     * [Dataset](Dataset.md) - A collection of studies
     * [ExperimentRun](ExperimentRun.md) - An experimental data collection session
     * [Image](Image.md) - An image file from structural biology experiments
         * [FTIRImage](FTIRImage.md) - Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy
         * [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)
             * [FluorescenceImage](FluorescenceImage.md) - Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
             * [OpticalImage](OpticalImage.md) - Visible light optical microscopy or photography image
             * [XRFImage](XRFImage.md) - X-ray fluorescence (XRF) image showing elemental distribution
         * [Image3D](Image3D.md) - A 3D volume or tomogram
     * [Instrument](Instrument.md) - An instrument used to collect data
         * [CryoEMInstrument](CryoEMInstrument.md) - Cryo-EM microscope specifications
         * [SAXSInstrument](SAXSInstrument.md) - SAXS/WAXS instrument specifications
         * [XRayInstrument](XRayInstrument.md) - X-ray diffractometer or synchrotron beamline specifications
     * [Sample](Sample.md) - A biological sample used in structural biology experiments
     * [SamplePreparation](SamplePreparation.md) - A process that prepares a sample for imaging
     * [Study](Study.md)
     * [WorkflowRun](WorkflowRun.md) - A computational processing workflow execution
 * [OntologyTerm](OntologyTerm.md)
 * [QualityMetrics](QualityMetrics.md) - Quality metrics for experiments
 * [StorageConditions](StorageConditions.md) - Storage conditions for samples
 * [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) - Base class for technique-specific preparation details
     * [CryoEMPreparation](CryoEMPreparation.md) - Cryo-EM specific sample preparation
     * [SAXSPreparation](SAXSPreparation.md) - SAXS/WAXS specific preparation
     * [XRayPreparation](XRayPreparation.md) - X-ray crystallography specific preparation

### Mixins


### Slots

 * [➞additives](bufferComposition__additives.md) - Additional additives in the buffer
 * [➞components](bufferComposition__components.md) - Buffer components and their concentrations
 * [➞ph](bufferComposition__ph.md) - pH of the buffer
 * [➞cpu_hours](computeResources__cpu_hours.md) - CPU hours used
 * [➞gpu_hours](computeResources__gpu_hours.md) - GPU hours used
 * [➞memory_gb](computeResources__memory_gb.md) - Maximum memory used in GB
 * [➞storage_gb](computeResources__storage_gb.md) - Storage used in GB
 * [➞accelerating_voltage](cryoEMInstrument__accelerating_voltage.md) - Accelerating voltage in kV
 * [➞autoloader_capacity](cryoEMInstrument__autoloader_capacity.md) - Number of grids the autoloader can hold
 * [➞cs_corrector](cryoEMInstrument__cs_corrector.md) - Spherical aberration corrector present
 * [➞detector_dimensions](cryoEMInstrument__detector_dimensions.md) - Detector dimensions in pixels (e.g., 4096x4096)
 * [➞detector_type](cryoEMInstrument__detector_type.md) - Type of detector
 * [➞phase_plate](cryoEMInstrument__phase_plate.md) - Phase plate available
 * [➞pixel_size_max](cryoEMInstrument__pixel_size_max.md) - Maximum pixel size in Angstroms per pixel
 * [➞pixel_size_min](cryoEMInstrument__pixel_size_min.md) - Minimum pixel size in Angstroms per pixel
 * [➞blot_force](cryoEMPreparation__blot_force.md) - Blotting force setting
 * [➞blot_time](cryoEMPreparation__blot_time.md) - Blotting time in seconds
 * [➞chamber_temperature](cryoEMPreparation__chamber_temperature.md) - Chamber temperature in Celsius
 * [➞grid_type](cryoEMPreparation__grid_type.md) - Type of EM grid used
 * [➞hole_size](cryoEMPreparation__hole_size.md) - Hole size in micrometers
 * [➞humidity_percentage](cryoEMPreparation__humidity_percentage.md) - Chamber humidity during vitrification
 * [➞plasma_treatment](cryoEMPreparation__plasma_treatment.md) - Plasma treatment details
 * [➞support_film](cryoEMPreparation__support_film.md) - Support film type
 * [➞vitrification_method](cryoEMPreparation__vitrification_method.md) - Method used for vitrification
 * [➞collection_mode](dataCollectionStrategy__collection_mode.md) - Mode of data collection
 * [➞dose_per_frame](dataCollectionStrategy__dose_per_frame.md) - Dose per frame
 * [➞frame_rate](dataCollectionStrategy__frame_rate.md) - Frames per second
 * [➞total_dose](dataCollectionStrategy__total_dose.md) - Total electron dose for cryo-EM
 * [➞total_frames](dataCollectionStrategy__total_frames.md) - Total number of frames/images
 * [➞checksum](dataFile__checksum.md) - SHA-256 checksum for data integrity
 * [➞creation_date](dataFile__creation_date.md) - File creation date
 * [➞data_type](dataFile__data_type.md) - Type of data in the file
 * [➞file_format](dataFile__file_format.md) - File format
 * [➞file_name](dataFile__file_name.md) - Name of the file
 * [➞file_path](dataFile__file_path.md) - Path to the file
 * [➞file_size_bytes](dataFile__file_size_bytes.md) - File size in bytes
 * [➞keywords](dataset__keywords.md)
 * [➞studies](dataset__studies.md)
 * [➞data_collection_strategy](experimentRun__data_collection_strategy.md) - Strategy for data collection
 * [➞experiment_code](experimentRun__experiment_code.md) - Unique experiment identifier
 * [➞experiment_date](experimentRun__experiment_date.md) - Date of the experiment
 * [➞experimental_conditions](experimentRun__experimental_conditions.md) - Environmental and experimental conditions
 * [➞instrument_id](experimentRun__instrument_id.md) - Reference to the instrument used
 * [➞operator_id](experimentRun__operator_id.md) - Person who performed the experiment
 * [➞processing_status](experimentRun__processing_status.md) - Current processing status
 * [➞quality_metrics](experimentRun__quality_metrics.md) - Quality metrics for the experiment
 * [➞raw_data_location](experimentRun__raw_data_location.md) - Location of raw data files
 * [➞sample_id](experimentRun__sample_id.md) - Reference to the sample being analyzed
 * [➞technique](experimentRun__technique.md) - Technique used for data collection
 * [➞atmosphere](experimentalConditions__atmosphere.md) - Atmosphere composition
 * [➞humidity](experimentalConditions__humidity.md) - Humidity percentage
 * [➞pressure](experimentalConditions__pressure.md) - Pressure in kPa
 * [➞temperature](experimentalConditions__temperature.md) - Temperature in Celsius
 * [➞apodization_function](fTIRImage__apodization_function.md) - Mathematical function used for apodization
 * [➞background_correction](fTIRImage__background_correction.md) - Method used for background correction
 * [➞molecular_signatures](fTIRImage__molecular_signatures.md) - Identified molecular signatures or peaks
 * [➞number_of_scans](fTIRImage__number_of_scans.md) - Number of scans averaged for the spectrum
 * [➞spectral_resolution](fTIRImage__spectral_resolution.md) - Spectral resolution in cm⁻¹
 * [➞wavenumber_max](fTIRImage__wavenumber_max.md) - Maximum wavenumber in cm⁻¹
 * [➞wavenumber_min](fTIRImage__wavenumber_min.md) - Minimum wavenumber in cm⁻¹
 * [➞channel_name](fluorescenceImage__channel_name.md) - Name of the fluorescence channel (e.g., DAPI, GFP, RFP)
 * [➞emission_filter](fluorescenceImage__emission_filter.md) - Specifications of the emission filter
 * [➞emission_wavelength](fluorescenceImage__emission_wavelength.md) - Emission wavelength in nanometers
 * [➞excitation_filter](fluorescenceImage__excitation_filter.md) - Specifications of the excitation filter
 * [➞excitation_wavelength](fluorescenceImage__excitation_wavelength.md) - Excitation wavelength in nanometers
 * [➞fluorophore](fluorescenceImage__fluorophore.md) - Name or type of fluorophore used
 * [➞laser_power](fluorescenceImage__laser_power.md) - Laser power in milliwatts or percentage
 * [➞pinhole_size](fluorescenceImage__pinhole_size.md) - Pinhole size in Airy units for confocal microscopy
 * [➞quantum_yield](fluorescenceImage__quantum_yield.md) - Quantum yield of the fluorophore
 * [➞astigmatism](image2D__astigmatism.md) - Astigmatism value
 * [➞defocus](image2D__defocus.md) - Defocus value in micrometers
 * [➞dimensions_z](image3D__dimensions_z.md) - Image depth in pixels/slices
 * [➞reconstruction_method](image3D__reconstruction_method.md) - Method used for 3D reconstruction
 * [➞voxel_size](image3D__voxel_size.md) - Voxel size in Angstroms
 * [➞terms](imageFeature__terms.md)
 * [➞acquisition_date](image__acquisition_date.md) - Date image was acquired
 * [➞dimensions_x](image__dimensions_x.md) - Image width in pixels
 * [➞dimensions_y](image__dimensions_y.md) - Image height in pixels
 * [➞dose](image__dose.md) - Electron dose in e-/Å²
 * [➞exposure_time](image__exposure_time.md) - Exposure time in seconds
 * [➞file_name](image__file_name.md) - Image file name
 * [➞pixel_size](image__pixel_size.md) - Pixel size in Angstroms
 * [➞current_status](instrument__current_status.md) - Current operational status
 * [➞installation_date](instrument__installation_date.md) - Date of instrument installation
 * [➞instrument_code](instrument__instrument_code.md) - Unique identifier code for the instrument
 * [➞manufacturer](instrument__manufacturer.md) - Instrument manufacturer
 * [➞model](instrument__model.md) - Instrument model
 * [➞ligands](molecularComposition__ligands.md) - Bound ligands or cofactors
 * [➞modifications](molecularComposition__modifications.md) - Post-translational modifications or chemical modifications
 * [➞sequences](molecularComposition__sequences.md) - Amino acid or nucleotide sequences
 * [➞description](namedThing__description.md)
 * [➞id](namedThing__id.md)
 * [➞title](namedThing__title.md)
 * [➞definition](ontologyTerm__definition.md)
 * [➞id](ontologyTerm__id.md)
 * [➞label](ontologyTerm__label.md)
 * [➞ontology](ontologyTerm__ontology.md)
 * [➞color_channels](opticalImage__color_channels.md) - Color channels present (e.g., RGB, grayscale)
 * [➞contrast_method](opticalImage__contrast_method.md) - Contrast enhancement method used
 * [➞illumination_type](opticalImage__illumination_type.md) - Type of illumination (brightfield, darkfield, phase contrast, DIC)
 * [➞magnification](opticalImage__magnification.md) - Optical magnification factor
 * [➞numerical_aperture](opticalImage__numerical_aperture.md) - Numerical aperture of the objective lens
 * [➞white_balance](opticalImage__white_balance.md) - White balance settings
 * [➞completeness](qualityMetrics__completeness.md) - Data completeness percentage
 * [➞r_factor](qualityMetrics__r_factor.md) - R-factor for crystallography
 * [➞resolution](qualityMetrics__resolution.md) - Resolution in Angstroms
 * [➞signal_to_noise](qualityMetrics__signal_to_noise.md) - Signal to noise ratio
 * [➞detector_distance_max](sAXSInstrument__detector_distance_max.md) - Maximum detector distance in mm
 * [➞detector_distance_min](sAXSInstrument__detector_distance_min.md) - Minimum detector distance in mm
 * [➞q_range_max](sAXSInstrument__q_range_max.md) - Maximum q value in inverse Angstroms
 * [➞q_range_min](sAXSInstrument__q_range_min.md) - Minimum q value in inverse Angstroms
 * [➞sample_changer_capacity](sAXSInstrument__sample_changer_capacity.md) - Number of samples in automatic sample changer
 * [➞temperature_control_range](sAXSInstrument__temperature_control_range.md) - Temperature control range in Celsius
 * [➞buffer_matching_protocol](sAXSPreparation__buffer_matching_protocol.md) - Protocol for buffer matching
 * [➞cell_path_length](sAXSPreparation__cell_path_length.md) - Path length in mm
 * [➞concentration_series](sAXSPreparation__concentration_series.md) - Concentration values for series measurements
 * [➞sample_cell_type](sAXSPreparation__sample_cell_type.md) - Type of sample cell used
 * [➞temperature_control](sAXSPreparation__temperature_control.md) - Temperature control settings
 * [➞operator_id](samplePreparation__operator_id.md) - Person who performed the preparation
 * [➞preparation_date](samplePreparation__preparation_date.md) - Date of sample preparation
 * [➞preparation_type](samplePreparation__preparation_type.md) - Type of sample preparation
 * [➞protocol_description](samplePreparation__protocol_description.md) - Detailed protocol description
 * [➞sample_id](samplePreparation__sample_id.md) - Reference to the sample being prepared
 * [➞buffer_composition](sample__buffer_composition.md) - Buffer composition including pH, salts, additives
 * [➞concentration](sample__concentration.md) - Sample concentration in mg/mL or µM
 * [➞concentration_unit](sample__concentration_unit.md) - Unit of concentration measurement
 * [➞molecular_composition](sample__molecular_composition.md) - Description of molecular composition including sequences, modifications, ligands
 * [➞molecular_weight](sample__molecular_weight.md) - Molecular weight in kDa
 * [➞parent_sample_id](sample__parent_sample_id.md) - Reference to parent sample for derivation tracking
 * [➞preparation_method](sample__preparation_method.md) - Method used to prepare the sample
 * [➞purity_percentage](sample__purity_percentage.md) - Sample purity as percentage
 * [➞quality_metrics](sample__quality_metrics.md) - Quality control metrics for the sample
 * [➞sample_code](sample__sample_code.md) - Unique identifier code for the sample
 * [➞sample_type](sample__sample_type.md) - Type of biological sample
 * [➞storage_conditions](sample__storage_conditions.md) - Storage conditions for the sample
 * [➞atmosphere](storageConditions__atmosphere.md) - Storage atmosphere conditions
 * [➞duration](storageConditions__duration.md) - Storage duration
 * [➞temperature](storageConditions__temperature.md) - Storage temperature in Celsius
 * [➞temperature_unit](storageConditions__temperature_unit.md) - Temperature unit
 * [➞data_files](study__data_files.md)
 * [➞images](study__images.md)
 * [➞instrument_runs](study__instrument_runs.md)
 * [➞sample_preparations](study__sample_preparations.md)
 * [➞samples](study__samples.md)
 * [➞workflow_runs](study__workflow_runs.md)
 * [➞completed_at](workflowRun__completed_at.md) - Workflow completion time
 * [➞compute_resources](workflowRun__compute_resources.md) - Computational resources used
 * [➞experiment_id](workflowRun__experiment_id.md) - Reference to the source experiment
 * [➞output_files](workflowRun__output_files.md) - Output files generated
 * [➞processing_level](workflowRun__processing_level.md) - Processing level (0=raw, 1=corrected, 2=derived, 3=model)
 * [➞processing_parameters](workflowRun__processing_parameters.md) - Parameters used in processing
 * [➞software_name](workflowRun__software_name.md) - Software used for processing
 * [➞software_version](workflowRun__software_version.md) - Software version
 * [➞started_at](workflowRun__started_at.md) - Workflow start time
 * [➞workflow_code](workflowRun__workflow_code.md) - Unique workflow identifier
 * [➞workflow_type](workflowRun__workflow_type.md) - Type of processing workflow
 * [➞beam_energy](xRFImage__beam_energy.md) - X-ray beam energy in keV
 * [➞beam_size](xRFImage__beam_size.md) - X-ray beam size in micrometers
 * [➞calibration_standard](xRFImage__calibration_standard.md) - Reference standard used for calibration
 * [➞detector_type](xRFImage__detector_type.md) - Type of X-ray detector used
 * [➞dwell_time](xRFImage__dwell_time.md) - Dwell time per pixel in milliseconds
 * [➞elements_measured](xRFImage__elements_measured.md) - Elements detected and measured
 * [➞flux](xRFImage__flux.md) - Photon flux in photons/second
 * [➞source_type](xRFImage__source_type.md) - X-ray source type (synchrotron or lab-source)
 * [➞beam_size_max](xRayInstrument__beam_size_max.md) - Maximum beam size in micrometers
 * [➞beam_size_min](xRayInstrument__beam_size_min.md) - Minimum beam size in micrometers
 * [➞crystal_cooling_capability](xRayInstrument__crystal_cooling_capability.md) - Crystal cooling system available
 * [➞energy_max](xRayInstrument__energy_max.md) - Maximum X-ray energy in keV
 * [➞energy_min](xRayInstrument__energy_min.md) - Minimum X-ray energy in keV
 * [➞flux_density](xRayInstrument__flux_density.md) - Photon flux density in photons/s/mm²
 * [➞goniometer_type](xRayInstrument__goniometer_type.md) - Type of goniometer
 * [➞monochromator_type](xRayInstrument__monochromator_type.md) - Type of monochromator
 * [➞source_type](xRayInstrument__source_type.md) - Type of X-ray source
 * [➞cryoprotectant](xRayPreparation__cryoprotectant.md) - Cryoprotectant used
 * [➞cryoprotectant_concentration](xRayPreparation__cryoprotectant_concentration.md) - Cryoprotectant concentration percentage
 * [➞crystal_size](xRayPreparation__crystal_size.md) - Crystal dimensions in micrometers
 * [➞crystallization_conditions](xRayPreparation__crystallization_conditions.md) - Detailed crystallization conditions
 * [➞crystallization_method](xRayPreparation__crystallization_method.md) - Method used for crystallization
 * [➞flash_cooling_method](xRayPreparation__flash_cooling_method.md) - Flash cooling protocol
 * [➞mounting_method](xRayPreparation__mounting_method.md) - Crystal mounting method

### Enums

 * [CollectionModeEnum](CollectionModeEnum.md) - Data collection modes
 * [ConcentrationUnitEnum](ConcentrationUnitEnum.md) - Units for concentration measurement
 * [CrystallizationMethodEnum](CrystallizationMethodEnum.md) - Methods for protein crystallization
 * [DataTypeEnum](DataTypeEnum.md) - Types of data
 * [DetectorTypeEnum](DetectorTypeEnum.md) - Types of detectors for cryo-EM
 * [FileFormatEnum](FileFormatEnum.md) - File formats
 * [GridTypeEnum](GridTypeEnum.md) - Types of EM grids
 * [IlluminationTypeEnum](IlluminationTypeEnum.md) - Types of illumination for optical microscopy
 * [InstrumentStatusEnum](InstrumentStatusEnum.md) - Operational status of instruments
 * [PreparationTypeEnum](PreparationTypeEnum.md) - Types of sample preparation
 * [ProcessingStatusEnum](ProcessingStatusEnum.md) - Processing status
 * [SampleTypeEnum](SampleTypeEnum.md) - Types of biological samples
 * [TechniqueEnum](TechniqueEnum.md) - Structural biology techniques
 * [TemperatureUnitEnum](TemperatureUnitEnum.md) - Units for temperature measurement
 * [VitrificationMethodEnum](VitrificationMethodEnum.md) - Methods for vitrification
 * [WorkflowTypeEnum](WorkflowTypeEnum.md) - Types of processing workflows
 * [XRaySourceTypeEnum](XRaySourceTypeEnum.md) - Types of X-ray sources

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
