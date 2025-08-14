# Auto generated from biostride.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-14T19:41:02
# Schema: biostride-schema
#
# id: https://w3id.org/biostride/
# description: BioStride is a comprehensive schema for representing multimodal structural biology imaging data,
#   from atomic-resolution structures to tissue-level organization. It supports diverse experimental
#   techniques including cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and
#   spectroscopic imaging.
#
#   ## Schema Organization
#
#   The schema follows a hierarchical structure that mirrors how structural biology research is organized:
#
#   The top-level entity is a [Dataset](Dataset.md), which serves as a container for related research.
#   A dataset might represent all data from a specific grant, collaboration, or publication.
#
#   Each dataset contains one or more [Studies](Study.md), which are focused investigations of specific
#   biological questions. For example, a study might investigate "Heat stress response in Arabidopsis"
#   or "Structure of the human ribosome under different conditions."
#
#   Within each study, you'll find:
#
#   ### Biological Materials
#   - [Samples](Sample.md): The biological specimens being studied (proteins, nucleic acids, complexes,
#     cells, tissues). Each sample includes detailed molecular composition, buffer conditions, and
#     storage information. For example, a purified protein with its sequence, concentration, and buffer pH.
#
#   - [Sample Preparations](SamplePreparation.md): How samples were prepared for specific techniques.
#     This includes cryo-EM grid preparation (vitrification parameters), crystallization conditions for
#     X-ray studies, or staining protocols for fluorescence microscopy.
#
#   ### Data Collection
#   - [Instruments](Instrument.md): The equipment used, from Titan Krios microscopes to synchrotron
#     beamlines. Each instrument type ([CryoEMInstrument](CryoEMInstrument.md),
#     [XRayInstrument](XRayInstrument.md), [SAXSInstrument](SAXSInstrument.md)) has specific parameters
#     like accelerating voltage, detector type, or beam energy.
#
#   - [Experiment Runs](ExperimentRun.md): Individual data collection sessions that link samples to
#     instruments. An experiment run captures when, how, and under what conditions data was collected,
#     including quality metrics like resolution and completeness.
#
#   ### Data Processing
#   - [Workflow Runs](WorkflowRun.md): Computational processing steps applied to raw data. This includes
#     motion correction for cryo-EM movies, 3D reconstruction, model building, or phase determination
#     for crystallography. Each workflow tracks the software used, parameters, and computational resources.
#
#   ### Data Products
#   - [Data Files](DataFile.md): Any files generated or used, from raw data to final models. Each file
#     is tracked with checksums for data integrity and typed (micrograph, particles, volume, model).
#
#   - [Images](Image.md): Specialized classes for different imaging modalities:
#     - [Image2D](Image2D.md): Micrographs, diffraction patterns
#     - [Image3D](Image3D.md): 3D reconstructions, tomograms
#     - [FTIRImage](FTIRImage.md): Molecular composition maps from infrared spectroscopy
#     - [FluorescenceImage](FluorescenceImage.md): Fluorophore-labeled cellular components
#     - [OpticalImage](OpticalImage.md): Brightfield/phase contrast microscopy
#     - [XRFImage](XRFImage.md): Elemental distribution maps
#
#   ## Example Usage
#
#   A typical cryo-EM study of a protein complex would include:
#   1. Sample records for the purified complex with molecular weight and buffer composition
#   2. Grid preparation details with vitrification parameters
#   3. Microscope specifications and data collection parameters
#   4. Processing workflows from motion correction through 3D refinement
#   5. Final reconstructed volumes and fitted atomic models
#
#   A multimodal plant imaging study might combine:
#   1. Whole plant optical imaging for morphology
#   2. XRF imaging to map nutrient distribution
#   3. FTIR spectroscopy to identify stress-related molecular changes
#   4. Fluorescence microscopy to track specific protein responses
#   5. Cryo-EM of isolated organelles for ultrastructural details
#
#   ## Key Features
#
#   - **Technique-agnostic core**: The same schema handles data from any structural biology method
#   - **Rich metadata**: Comprehensive tracking from sample to structure
#   - **Workflow provenance**: Complete computational reproducibility
#   - **Multimodal support**: Seamlessly integrate data across scales and techniques
#   - **Standards-compliant**: Follows FAIR principles and integrates with existing ontologies
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
BIOSTRIDE = CurieNamespace('biostride', 'https://w3id.org/biostride/')
BIOSTRIDE_SCHEMA = CurieNamespace('biostride_schema', 'https://w3id.org/biostride/schema/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
DEFAULT_ = BIOSTRIDE_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class DatasetId(NamedThingId):
    pass


class StudyId(NamedThingId):
    pass


class SampleId(NamedThingId):
    pass


class SamplePreparationId(NamedThingId):
    pass


class InstrumentId(NamedThingId):
    pass


class CryoEMInstrumentId(InstrumentId):
    pass


class XRayInstrumentId(InstrumentId):
    pass


class SAXSInstrumentId(InstrumentId):
    pass


class ExperimentRunId(NamedThingId):
    pass


class WorkflowRunId(NamedThingId):
    pass


class DataFileId(NamedThingId):
    pass


class ImageId(NamedThingId):
    pass


class Image2DId(ImageId):
    pass


class Image3DId(ImageId):
    pass


class FTIRImageId(ImageId):
    pass


class FluorescenceImageId(Image2DId):
    pass


class OpticalImageId(Image2DId):
    pass


class XRFImageId(Image2DId):
    pass


class OntologyTermId(NamedThingId):
    pass


class CryoEMPreparationId(SamplePreparationId):
    pass


class XRayPreparationId(SamplePreparationId):
    pass


class SAXSPreparationId(SamplePreparationId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A named thing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["NamedThing"]
    class_class_curie: ClassVar[str] = "biostride_schema:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttributeGroup(YAMLRoot):
    """
    A grouping of related data attributes that form a logical unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["AttributeGroup"]
    class_class_curie: ClassVar[str] = "biostride_schema:AttributeGroup"
    class_name: ClassVar[str] = "AttributeGroup"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.AttributeGroup

    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(NamedThing):
    """
    A collection of studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["Dataset"]
    class_class_curie: ClassVar[str] = "biostride_schema:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.Dataset

    id: Union[str, DatasetId] = None
    keywords: Optional[Union[str, list[str]]] = empty_list()
    instruments: Optional[Union[dict[Union[str, InstrumentId], Union[dict, "Instrument"]], list[Union[dict, "Instrument"]]]] = empty_dict()
    studies: Optional[Union[dict[Union[str, StudyId], Union[dict, "Study"]], list[Union[dict, "Study"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        self._normalize_inlined_as_list(slot_name="instruments", slot_type=Instrument, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(NamedThing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["Study"]
    class_class_curie: ClassVar[str] = "biostride_schema:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.Study

    id: Union[str, StudyId] = None
    samples: Optional[Union[dict[Union[str, SampleId], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()
    sample_preparations: Optional[Union[dict[Union[str, SamplePreparationId], Union[dict, "SamplePreparation"]], list[Union[dict, "SamplePreparation"]]]] = empty_dict()
    instrument_runs: Optional[Union[dict[Union[str, ExperimentRunId], Union[dict, "ExperimentRun"]], list[Union[dict, "ExperimentRun"]]]] = empty_dict()
    workflow_runs: Optional[Union[dict[Union[str, WorkflowRunId], Union[dict, "WorkflowRun"]], list[Union[dict, "WorkflowRun"]]]] = empty_dict()
    data_files: Optional[Union[dict[Union[str, DataFileId], Union[dict, "DataFile"]], list[Union[dict, "DataFile"]]]] = empty_dict()
    images: Optional[Union[dict[Union[str, ImageId], Union[dict, "Image"]], list[Union[dict, "Image"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sample_preparations", slot_type=SamplePreparation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="instrument_runs", slot_type=ExperimentRun, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="workflow_runs", slot_type=WorkflowRun, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_files", slot_type=DataFile, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="images", slot_type=Image, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(NamedThing):
    """
    A biological sample used in structural biology experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["Sample"]
    class_class_curie: ClassVar[str] = "biostride_schema:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.Sample

    id: Union[str, SampleId] = None
    sample_code: str = None
    sample_type: Union[str, "SampleTypeEnum"] = None
    molecular_composition: Optional[Union[dict, "MolecularComposition"]] = None
    molecular_weight: Optional[float] = None
    concentration: Optional[float] = None
    concentration_unit: Optional[Union[str, "ConcentrationUnitEnum"]] = None
    buffer_composition: Optional[Union[dict, "BufferComposition"]] = None
    preparation_method: Optional[str] = None
    storage_conditions: Optional[Union[dict, "StorageConditions"]] = None
    organism: Optional[Union[str, OntologyTermId]] = None
    anatomy: Optional[Union[str, OntologyTermId]] = None
    cell_type: Optional[Union[str, OntologyTermId]] = None
    parent_sample_id: Optional[Union[str, SampleId]] = None
    purity_percentage: Optional[float] = None
    quality_metrics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self._is_empty(self.sample_code):
            self.MissingRequiredField("sample_code")
        if not isinstance(self.sample_code, str):
            self.sample_code = str(self.sample_code)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.molecular_composition is not None and not isinstance(self.molecular_composition, MolecularComposition):
            self.molecular_composition = MolecularComposition(**as_dict(self.molecular_composition))

        if self.molecular_weight is not None and not isinstance(self.molecular_weight, float):
            self.molecular_weight = float(self.molecular_weight)

        if self.concentration is not None and not isinstance(self.concentration, float):
            self.concentration = float(self.concentration)

        if self.concentration_unit is not None and not isinstance(self.concentration_unit, ConcentrationUnitEnum):
            self.concentration_unit = ConcentrationUnitEnum(self.concentration_unit)

        if self.buffer_composition is not None and not isinstance(self.buffer_composition, BufferComposition):
            self.buffer_composition = BufferComposition(**as_dict(self.buffer_composition))

        if self.preparation_method is not None and not isinstance(self.preparation_method, str):
            self.preparation_method = str(self.preparation_method)

        if self.storage_conditions is not None and not isinstance(self.storage_conditions, StorageConditions):
            self.storage_conditions = StorageConditions(**as_dict(self.storage_conditions))

        if self.organism is not None and not isinstance(self.organism, OntologyTermId):
            self.organism = OntologyTermId(self.organism)

        if self.anatomy is not None and not isinstance(self.anatomy, OntologyTermId):
            self.anatomy = OntologyTermId(self.anatomy)

        if self.cell_type is not None and not isinstance(self.cell_type, OntologyTermId):
            self.cell_type = OntologyTermId(self.cell_type)

        if self.parent_sample_id is not None and not isinstance(self.parent_sample_id, SampleId):
            self.parent_sample_id = SampleId(self.parent_sample_id)

        if self.purity_percentage is not None and not isinstance(self.purity_percentage, float):
            self.purity_percentage = float(self.purity_percentage)

        if self.quality_metrics is not None and not isinstance(self.quality_metrics, str):
            self.quality_metrics = str(self.quality_metrics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplePreparation(NamedThing):
    """
    A process that prepares a sample for imaging
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["SamplePreparation"]
    class_class_curie: ClassVar[str] = "biostride_schema:SamplePreparation"
    class_name: ClassVar[str] = "SamplePreparation"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.SamplePreparation

    id: Union[str, SamplePreparationId] = None
    type: str = None
    sample_id: str = None
    preparation_date: Optional[str] = None
    operator_id: Optional[str] = None
    protocol_description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplePreparationId):
            self.id = SamplePreparationId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        self.type = str(self.class_name)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self.preparation_date is not None and not isinstance(self.preparation_date, str):
            self.preparation_date = str(self.preparation_date)

        if self.operator_id is not None and not isinstance(self.operator_id, str):
            self.operator_id = str(self.operator_id)

        if self.protocol_description is not None and not isinstance(self.protocol_description, str):
            self.protocol_description = str(self.protocol_description)

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_type):
            self.MissingRequiredField("unknown_type")
        self.unknown_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class Instrument(NamedThing):
    """
    An instrument used to collect data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["Instrument"]
    class_class_curie: ClassVar[str] = "biostride_schema:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.Instrument

    id: Union[str, InstrumentId] = None
    instrument_code: str = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    installation_date: Optional[str] = None
    current_status: Optional[Union[str, "InstrumentStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstrumentId):
            self.id = InstrumentId(self.id)

        if self._is_empty(self.instrument_code):
            self.MissingRequiredField("instrument_code")
        if not isinstance(self.instrument_code, str):
            self.instrument_code = str(self.instrument_code)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.installation_date is not None and not isinstance(self.installation_date, str):
            self.installation_date = str(self.installation_date)

        if self.current_status is not None and not isinstance(self.current_status, InstrumentStatusEnum):
            self.current_status = InstrumentStatusEnum(self.current_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CryoEMInstrument(Instrument):
    """
    Cryo-EM microscope specifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["CryoEMInstrument"]
    class_class_curie: ClassVar[str] = "biostride_schema:CryoEMInstrument"
    class_name: ClassVar[str] = "CryoEMInstrument"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.CryoEMInstrument

    id: Union[str, CryoEMInstrumentId] = None
    instrument_code: str = None
    accelerating_voltage: Optional[int] = None
    cs_corrector: Optional[Union[bool, Bool]] = None
    phase_plate: Optional[Union[bool, Bool]] = None
    detector_type: Optional[Union[str, "DetectorTypeEnum"]] = None
    detector_dimensions: Optional[str] = None
    pixel_size_min: Optional[float] = None
    pixel_size_max: Optional[float] = None
    autoloader_capacity: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CryoEMInstrumentId):
            self.id = CryoEMInstrumentId(self.id)

        if self.accelerating_voltage is not None and not isinstance(self.accelerating_voltage, int):
            self.accelerating_voltage = int(self.accelerating_voltage)

        if self.cs_corrector is not None and not isinstance(self.cs_corrector, Bool):
            self.cs_corrector = Bool(self.cs_corrector)

        if self.phase_plate is not None and not isinstance(self.phase_plate, Bool):
            self.phase_plate = Bool(self.phase_plate)

        if self.detector_type is not None and not isinstance(self.detector_type, DetectorTypeEnum):
            self.detector_type = DetectorTypeEnum(self.detector_type)

        if self.detector_dimensions is not None and not isinstance(self.detector_dimensions, str):
            self.detector_dimensions = str(self.detector_dimensions)

        if self.pixel_size_min is not None and not isinstance(self.pixel_size_min, float):
            self.pixel_size_min = float(self.pixel_size_min)

        if self.pixel_size_max is not None and not isinstance(self.pixel_size_max, float):
            self.pixel_size_max = float(self.pixel_size_max)

        if self.autoloader_capacity is not None and not isinstance(self.autoloader_capacity, int):
            self.autoloader_capacity = int(self.autoloader_capacity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRayInstrument(Instrument):
    """
    X-ray diffractometer or synchrotron beamline specifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["XRayInstrument"]
    class_class_curie: ClassVar[str] = "biostride_schema:XRayInstrument"
    class_name: ClassVar[str] = "XRayInstrument"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.XRayInstrument

    id: Union[str, XRayInstrumentId] = None
    instrument_code: str = None
    source_type: Optional[Union[str, "XRaySourceTypeEnum"]] = None
    energy_min: Optional[float] = None
    energy_max: Optional[float] = None
    beam_size_min: Optional[float] = None
    beam_size_max: Optional[float] = None
    flux_density: Optional[float] = None
    monochromator_type: Optional[str] = None
    goniometer_type: Optional[str] = None
    crystal_cooling_capability: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRayInstrumentId):
            self.id = XRayInstrumentId(self.id)

        if self.source_type is not None and not isinstance(self.source_type, XRaySourceTypeEnum):
            self.source_type = XRaySourceTypeEnum(self.source_type)

        if self.energy_min is not None and not isinstance(self.energy_min, float):
            self.energy_min = float(self.energy_min)

        if self.energy_max is not None and not isinstance(self.energy_max, float):
            self.energy_max = float(self.energy_max)

        if self.beam_size_min is not None and not isinstance(self.beam_size_min, float):
            self.beam_size_min = float(self.beam_size_min)

        if self.beam_size_max is not None and not isinstance(self.beam_size_max, float):
            self.beam_size_max = float(self.beam_size_max)

        if self.flux_density is not None and not isinstance(self.flux_density, float):
            self.flux_density = float(self.flux_density)

        if self.monochromator_type is not None and not isinstance(self.monochromator_type, str):
            self.monochromator_type = str(self.monochromator_type)

        if self.goniometer_type is not None and not isinstance(self.goniometer_type, str):
            self.goniometer_type = str(self.goniometer_type)

        if self.crystal_cooling_capability is not None and not isinstance(self.crystal_cooling_capability, Bool):
            self.crystal_cooling_capability = Bool(self.crystal_cooling_capability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SAXSInstrument(Instrument):
    """
    SAXS/WAXS instrument specifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["SAXSInstrument"]
    class_class_curie: ClassVar[str] = "biostride_schema:SAXSInstrument"
    class_name: ClassVar[str] = "SAXSInstrument"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.SAXSInstrument

    id: Union[str, SAXSInstrumentId] = None
    instrument_code: str = None
    q_range_min: Optional[float] = None
    q_range_max: Optional[float] = None
    detector_distance_min: Optional[float] = None
    detector_distance_max: Optional[float] = None
    sample_changer_capacity: Optional[int] = None
    temperature_control_range: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SAXSInstrumentId):
            self.id = SAXSInstrumentId(self.id)

        if self.q_range_min is not None and not isinstance(self.q_range_min, float):
            self.q_range_min = float(self.q_range_min)

        if self.q_range_max is not None and not isinstance(self.q_range_max, float):
            self.q_range_max = float(self.q_range_max)

        if self.detector_distance_min is not None and not isinstance(self.detector_distance_min, float):
            self.detector_distance_min = float(self.detector_distance_min)

        if self.detector_distance_max is not None and not isinstance(self.detector_distance_max, float):
            self.detector_distance_max = float(self.detector_distance_max)

        if self.sample_changer_capacity is not None and not isinstance(self.sample_changer_capacity, int):
            self.sample_changer_capacity = int(self.sample_changer_capacity)

        if self.temperature_control_range is not None and not isinstance(self.temperature_control_range, str):
            self.temperature_control_range = str(self.temperature_control_range)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentRun(NamedThing):
    """
    An experimental data collection session
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["ExperimentRun"]
    class_class_curie: ClassVar[str] = "biostride_schema:ExperimentRun"
    class_name: ClassVar[str] = "ExperimentRun"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.ExperimentRun

    id: Union[str, ExperimentRunId] = None
    experiment_code: str = None
    sample_id: str = None
    instrument_id: Union[str, InstrumentId] = None
    technique: Union[str, "TechniqueEnum"] = None
    experiment_date: Optional[str] = None
    operator_id: Optional[str] = None
    experimental_conditions: Optional[Union[dict, "ExperimentalConditions"]] = None
    data_collection_strategy: Optional[Union[dict, "DataCollectionStrategy"]] = None
    quality_metrics: Optional[Union[dict, "QualityMetrics"]] = None
    raw_data_location: Optional[str] = None
    processing_status: Optional[Union[str, "ProcessingStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentRunId):
            self.id = ExperimentRunId(self.id)

        if self._is_empty(self.experiment_code):
            self.MissingRequiredField("experiment_code")
        if not isinstance(self.experiment_code, str):
            self.experiment_code = str(self.experiment_code)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self._is_empty(self.instrument_id):
            self.MissingRequiredField("instrument_id")
        if not isinstance(self.instrument_id, InstrumentId):
            self.instrument_id = InstrumentId(self.instrument_id)

        if self._is_empty(self.technique):
            self.MissingRequiredField("technique")
        if not isinstance(self.technique, TechniqueEnum):
            self.technique = TechniqueEnum(self.technique)

        if self.experiment_date is not None and not isinstance(self.experiment_date, str):
            self.experiment_date = str(self.experiment_date)

        if self.operator_id is not None and not isinstance(self.operator_id, str):
            self.operator_id = str(self.operator_id)

        if self.experimental_conditions is not None and not isinstance(self.experimental_conditions, ExperimentalConditions):
            self.experimental_conditions = ExperimentalConditions(**as_dict(self.experimental_conditions))

        if self.data_collection_strategy is not None and not isinstance(self.data_collection_strategy, DataCollectionStrategy):
            self.data_collection_strategy = DataCollectionStrategy(**as_dict(self.data_collection_strategy))

        if self.quality_metrics is not None and not isinstance(self.quality_metrics, QualityMetrics):
            self.quality_metrics = QualityMetrics(**as_dict(self.quality_metrics))

        if self.raw_data_location is not None and not isinstance(self.raw_data_location, str):
            self.raw_data_location = str(self.raw_data_location)

        if self.processing_status is not None and not isinstance(self.processing_status, ProcessingStatusEnum):
            self.processing_status = ProcessingStatusEnum(self.processing_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkflowRun(NamedThing):
    """
    A computational processing workflow execution
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["WorkflowRun"]
    class_class_curie: ClassVar[str] = "biostride_schema:WorkflowRun"
    class_name: ClassVar[str] = "WorkflowRun"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.WorkflowRun

    id: Union[str, WorkflowRunId] = None
    workflow_code: str = None
    workflow_type: Union[str, "WorkflowTypeEnum"] = None
    experiment_id: str = None
    software_name: str = None
    processing_level: Optional[int] = None
    software_version: Optional[str] = None
    processing_parameters: Optional[str] = None
    compute_resources: Optional[Union[dict, "ComputeResources"]] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    output_files: Optional[Union[Union[str, DataFileId], list[Union[str, DataFileId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowRunId):
            self.id = WorkflowRunId(self.id)

        if self._is_empty(self.workflow_code):
            self.MissingRequiredField("workflow_code")
        if not isinstance(self.workflow_code, str):
            self.workflow_code = str(self.workflow_code)

        if self._is_empty(self.workflow_type):
            self.MissingRequiredField("workflow_type")
        if not isinstance(self.workflow_type, WorkflowTypeEnum):
            self.workflow_type = WorkflowTypeEnum(self.workflow_type)

        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self._is_empty(self.software_name):
            self.MissingRequiredField("software_name")
        if not isinstance(self.software_name, str):
            self.software_name = str(self.software_name)

        if self.processing_level is not None and not isinstance(self.processing_level, int):
            self.processing_level = int(self.processing_level)

        if self.software_version is not None and not isinstance(self.software_version, str):
            self.software_version = str(self.software_version)

        if self.processing_parameters is not None and not isinstance(self.processing_parameters, str):
            self.processing_parameters = str(self.processing_parameters)

        if self.compute_resources is not None and not isinstance(self.compute_resources, ComputeResources):
            self.compute_resources = ComputeResources(**as_dict(self.compute_resources))

        if self.started_at is not None and not isinstance(self.started_at, str):
            self.started_at = str(self.started_at)

        if self.completed_at is not None and not isinstance(self.completed_at, str):
            self.completed_at = str(self.completed_at)

        if not isinstance(self.output_files, list):
            self.output_files = [self.output_files] if self.output_files is not None else []
        self.output_files = [v if isinstance(v, DataFileId) else DataFileId(v) for v in self.output_files]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataFile(NamedThing):
    """
    A data file generated or used in the study
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["DataFile"]
    class_class_curie: ClassVar[str] = "biostride_schema:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.DataFile

    id: Union[str, DataFileId] = None
    file_name: str = None
    file_format: Union[str, "FileFormatEnum"] = None
    file_path: Optional[str] = None
    file_size_bytes: Optional[int] = None
    checksum: Optional[str] = None
    creation_date: Optional[str] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataFileId):
            self.id = DataFileId(self.id)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.file_format):
            self.MissingRequiredField("file_format")
        if not isinstance(self.file_format, FileFormatEnum):
            self.file_format = FileFormatEnum(self.file_format)

        if self.file_path is not None and not isinstance(self.file_path, str):
            self.file_path = str(self.file_path)

        if self.file_size_bytes is not None and not isinstance(self.file_size_bytes, int):
            self.file_size_bytes = int(self.file_size_bytes)

        if self.checksum is not None and not isinstance(self.checksum, str):
            self.checksum = str(self.checksum)

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeEnum):
            self.data_type = DataTypeEnum(self.data_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image(NamedThing):
    """
    An image file from structural biology experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["Image"]
    class_class_curie: ClassVar[str] = "biostride_schema:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.Image

    id: Union[str, ImageId] = None
    file_name: str = None
    acquisition_date: Optional[str] = None
    pixel_size: Optional[float] = None
    dimensions_x: Optional[int] = None
    dimensions_y: Optional[int] = None
    exposure_time: Optional[float] = None
    dose: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImageId):
            self.id = ImageId(self.id)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.acquisition_date is not None and not isinstance(self.acquisition_date, str):
            self.acquisition_date = str(self.acquisition_date)

        if self.pixel_size is not None and not isinstance(self.pixel_size, float):
            self.pixel_size = float(self.pixel_size)

        if self.dimensions_x is not None and not isinstance(self.dimensions_x, int):
            self.dimensions_x = int(self.dimensions_x)

        if self.dimensions_y is not None and not isinstance(self.dimensions_y, int):
            self.dimensions_y = int(self.dimensions_y)

        if self.exposure_time is not None and not isinstance(self.exposure_time, float):
            self.exposure_time = float(self.exposure_time)

        if self.dose is not None and not isinstance(self.dose, float):
            self.dose = float(self.dose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image2D(Image):
    """
    A 2D image (micrograph, diffraction pattern)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["Image2D"]
    class_class_curie: ClassVar[str] = "biostride_schema:Image2D"
    class_name: ClassVar[str] = "Image2D"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.Image2D

    id: Union[str, Image2DId] = None
    file_name: str = None
    defocus: Optional[float] = None
    astigmatism: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Image2DId):
            self.id = Image2DId(self.id)

        if self.defocus is not None and not isinstance(self.defocus, float):
            self.defocus = float(self.defocus)

        if self.astigmatism is not None and not isinstance(self.astigmatism, float):
            self.astigmatism = float(self.astigmatism)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image3D(Image):
    """
    A 3D volume or tomogram
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["Image3D"]
    class_class_curie: ClassVar[str] = "biostride_schema:Image3D"
    class_name: ClassVar[str] = "Image3D"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.Image3D

    id: Union[str, Image3DId] = None
    file_name: str = None
    dimensions_z: Optional[int] = None
    voxel_size: Optional[float] = None
    reconstruction_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Image3DId):
            self.id = Image3DId(self.id)

        if self.dimensions_z is not None and not isinstance(self.dimensions_z, int):
            self.dimensions_z = int(self.dimensions_z)

        if self.voxel_size is not None and not isinstance(self.voxel_size, float):
            self.voxel_size = float(self.voxel_size)

        if self.reconstruction_method is not None and not isinstance(self.reconstruction_method, str):
            self.reconstruction_method = str(self.reconstruction_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FTIRImage(Image):
    """
    Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational
    spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["FTIRImage"]
    class_class_curie: ClassVar[str] = "biostride_schema:FTIRImage"
    class_name: ClassVar[str] = "FTIRImage"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.FTIRImage

    id: Union[str, FTIRImageId] = None
    file_name: str = None
    wavenumber_min: Optional[float] = None
    wavenumber_max: Optional[float] = None
    spectral_resolution: Optional[float] = None
    number_of_scans: Optional[int] = None
    apodization_function: Optional[str] = None
    molecular_signatures: Optional[Union[str, list[str]]] = empty_list()
    background_correction: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FTIRImageId):
            self.id = FTIRImageId(self.id)

        if self.wavenumber_min is not None and not isinstance(self.wavenumber_min, float):
            self.wavenumber_min = float(self.wavenumber_min)

        if self.wavenumber_max is not None and not isinstance(self.wavenumber_max, float):
            self.wavenumber_max = float(self.wavenumber_max)

        if self.spectral_resolution is not None and not isinstance(self.spectral_resolution, float):
            self.spectral_resolution = float(self.spectral_resolution)

        if self.number_of_scans is not None and not isinstance(self.number_of_scans, int):
            self.number_of_scans = int(self.number_of_scans)

        if self.apodization_function is not None and not isinstance(self.apodization_function, str):
            self.apodization_function = str(self.apodization_function)

        if not isinstance(self.molecular_signatures, list):
            self.molecular_signatures = [self.molecular_signatures] if self.molecular_signatures is not None else []
        self.molecular_signatures = [v if isinstance(v, str) else str(v) for v in self.molecular_signatures]

        if self.background_correction is not None and not isinstance(self.background_correction, str):
            self.background_correction = str(self.background_correction)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FluorescenceImage(Image2D):
    """
    Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["FluorescenceImage"]
    class_class_curie: ClassVar[str] = "biostride_schema:FluorescenceImage"
    class_name: ClassVar[str] = "FluorescenceImage"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.FluorescenceImage

    id: Union[str, FluorescenceImageId] = None
    file_name: str = None
    excitation_wavelength: Optional[float] = None
    emission_wavelength: Optional[float] = None
    excitation_filter: Optional[str] = None
    emission_filter: Optional[str] = None
    fluorophore: Optional[str] = None
    channel_name: Optional[str] = None
    laser_power: Optional[float] = None
    pinhole_size: Optional[float] = None
    quantum_yield: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FluorescenceImageId):
            self.id = FluorescenceImageId(self.id)

        if self.excitation_wavelength is not None and not isinstance(self.excitation_wavelength, float):
            self.excitation_wavelength = float(self.excitation_wavelength)

        if self.emission_wavelength is not None and not isinstance(self.emission_wavelength, float):
            self.emission_wavelength = float(self.emission_wavelength)

        if self.excitation_filter is not None and not isinstance(self.excitation_filter, str):
            self.excitation_filter = str(self.excitation_filter)

        if self.emission_filter is not None and not isinstance(self.emission_filter, str):
            self.emission_filter = str(self.emission_filter)

        if self.fluorophore is not None and not isinstance(self.fluorophore, str):
            self.fluorophore = str(self.fluorophore)

        if self.channel_name is not None and not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self.laser_power is not None and not isinstance(self.laser_power, float):
            self.laser_power = float(self.laser_power)

        if self.pinhole_size is not None and not isinstance(self.pinhole_size, float):
            self.pinhole_size = float(self.pinhole_size)

        if self.quantum_yield is not None and not isinstance(self.quantum_yield, float):
            self.quantum_yield = float(self.quantum_yield)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpticalImage(Image2D):
    """
    Visible light optical microscopy or photography image
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["OpticalImage"]
    class_class_curie: ClassVar[str] = "biostride_schema:OpticalImage"
    class_name: ClassVar[str] = "OpticalImage"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.OpticalImage

    id: Union[str, OpticalImageId] = None
    file_name: str = None
    illumination_type: Optional[Union[str, "IlluminationTypeEnum"]] = None
    magnification: Optional[float] = None
    numerical_aperture: Optional[float] = None
    color_channels: Optional[Union[str, list[str]]] = empty_list()
    white_balance: Optional[str] = None
    contrast_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OpticalImageId):
            self.id = OpticalImageId(self.id)

        if self.illumination_type is not None and not isinstance(self.illumination_type, IlluminationTypeEnum):
            self.illumination_type = IlluminationTypeEnum(self.illumination_type)

        if self.magnification is not None and not isinstance(self.magnification, float):
            self.magnification = float(self.magnification)

        if self.numerical_aperture is not None and not isinstance(self.numerical_aperture, float):
            self.numerical_aperture = float(self.numerical_aperture)

        if not isinstance(self.color_channels, list):
            self.color_channels = [self.color_channels] if self.color_channels is not None else []
        self.color_channels = [v if isinstance(v, str) else str(v) for v in self.color_channels]

        if self.white_balance is not None and not isinstance(self.white_balance, str):
            self.white_balance = str(self.white_balance)

        if self.contrast_method is not None and not isinstance(self.contrast_method, str):
            self.contrast_method = str(self.contrast_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRFImage(Image2D):
    """
    X-ray fluorescence (XRF) image showing elemental distribution
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["XRFImage"]
    class_class_curie: ClassVar[str] = "biostride_schema:XRFImage"
    class_name: ClassVar[str] = "XRFImage"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.XRFImage

    id: Union[str, XRFImageId] = None
    file_name: str = None
    beam_energy: Optional[float] = None
    beam_size: Optional[float] = None
    dwell_time: Optional[float] = None
    elements_measured: Optional[Union[str, list[str]]] = empty_list()
    source_type: Optional[Union[str, "XRaySourceTypeEnum"]] = None
    detector_type: Optional[str] = None
    flux: Optional[float] = None
    calibration_standard: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRFImageId):
            self.id = XRFImageId(self.id)

        if self.beam_energy is not None and not isinstance(self.beam_energy, float):
            self.beam_energy = float(self.beam_energy)

        if self.beam_size is not None and not isinstance(self.beam_size, float):
            self.beam_size = float(self.beam_size)

        if self.dwell_time is not None and not isinstance(self.dwell_time, float):
            self.dwell_time = float(self.dwell_time)

        if not isinstance(self.elements_measured, list):
            self.elements_measured = [self.elements_measured] if self.elements_measured is not None else []
        self.elements_measured = [v if isinstance(v, str) else str(v) for v in self.elements_measured]

        if self.source_type is not None and not isinstance(self.source_type, XRaySourceTypeEnum):
            self.source_type = XRaySourceTypeEnum(self.source_type)

        if self.detector_type is not None and not isinstance(self.detector_type, str):
            self.detector_type = str(self.detector_type)

        if self.flux is not None and not isinstance(self.flux, float):
            self.flux = float(self.flux)

        if self.calibration_standard is not None and not isinstance(self.calibration_standard, str):
            self.calibration_standard = str(self.calibration_standard)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImageFeature(AttributeGroup):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["ImageFeature"]
    class_class_curie: ClassVar[str] = "biostride_schema:ImageFeature"
    class_name: ClassVar[str] = "ImageFeature"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.ImageFeature

    terms: Optional[Union[str, OntologyTermId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.terms is not None and not isinstance(self.terms, OntologyTermId):
            self.terms = OntologyTermId(self.terms)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyTerm(NamedThing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["OntologyTerm"]
    class_class_curie: ClassVar[str] = "biostride_schema:OntologyTerm"
    class_name: ClassVar[str] = "OntologyTerm"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.OntologyTerm

    id: Union[str, OntologyTermId] = None
    label: Optional[str] = None
    definition: Optional[str] = None
    ontology: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyTermId):
            self.id = OntologyTermId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.ontology is not None and not isinstance(self.ontology, str):
            self.ontology = str(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularComposition(AttributeGroup):
    """
    Molecular composition of a sample
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["MolecularComposition"]
    class_class_curie: ClassVar[str] = "biostride_schema:MolecularComposition"
    class_name: ClassVar[str] = "MolecularComposition"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.MolecularComposition

    sequences: Optional[Union[str, list[str]]] = empty_list()
    modifications: Optional[Union[str, list[str]]] = empty_list()
    ligands: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.sequences, list):
            self.sequences = [self.sequences] if self.sequences is not None else []
        self.sequences = [v if isinstance(v, str) else str(v) for v in self.sequences]

        if not isinstance(self.modifications, list):
            self.modifications = [self.modifications] if self.modifications is not None else []
        self.modifications = [v if isinstance(v, str) else str(v) for v in self.modifications]

        if not isinstance(self.ligands, list):
            self.ligands = [self.ligands] if self.ligands is not None else []
        self.ligands = [v if isinstance(v, str) else str(v) for v in self.ligands]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BufferComposition(AttributeGroup):
    """
    Buffer composition for sample storage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["BufferComposition"]
    class_class_curie: ClassVar[str] = "biostride_schema:BufferComposition"
    class_name: ClassVar[str] = "BufferComposition"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.BufferComposition

    ph: Optional[float] = None
    components: Optional[Union[str, list[str]]] = empty_list()
    additives: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, str) else str(v) for v in self.components]

        if not isinstance(self.additives, list):
            self.additives = [self.additives] if self.additives is not None else []
        self.additives = [v if isinstance(v, str) else str(v) for v in self.additives]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageConditions(AttributeGroup):
    """
    Storage conditions for samples
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["StorageConditions"]
    class_class_curie: ClassVar[str] = "biostride_schema:StorageConditions"
    class_name: ClassVar[str] = "StorageConditions"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.StorageConditions

    temperature: Optional[float] = None
    temperature_unit: Optional[Union[str, "TemperatureUnitEnum"]] = None
    duration: Optional[str] = None
    atmosphere: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        if self.temperature_unit is not None and not isinstance(self.temperature_unit, TemperatureUnitEnum):
            self.temperature_unit = TemperatureUnitEnum(self.temperature_unit)

        if self.duration is not None and not isinstance(self.duration, str):
            self.duration = str(self.duration)

        if self.atmosphere is not None and not isinstance(self.atmosphere, str):
            self.atmosphere = str(self.atmosphere)

        super().__post_init__(**kwargs)


class TechniqueSpecificPreparation(AttributeGroup):
    """
    Base class for technique-specific preparation details
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["TechniqueSpecificPreparation"]
    class_class_curie: ClassVar[str] = "biostride_schema:TechniqueSpecificPreparation"
    class_name: ClassVar[str] = "TechniqueSpecificPreparation"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.TechniqueSpecificPreparation


@dataclass(repr=False)
class CryoEMPreparation(SamplePreparation):
    """
    Cryo-EM specific sample preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["CryoEMPreparation"]
    class_class_curie: ClassVar[str] = "biostride_schema:CryoEMPreparation"
    class_name: ClassVar[str] = "CryoEMPreparation"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.CryoEMPreparation

    id: Union[str, CryoEMPreparationId] = None
    type: str = None
    sample_id: str = None
    grid_type: Optional[Union[str, "GridTypeEnum"]] = None
    support_film: Optional[str] = None
    hole_size: Optional[float] = None
    vitrification_method: Optional[Union[str, "VitrificationMethodEnum"]] = None
    blot_time: Optional[float] = None
    blot_force: Optional[int] = None
    humidity_percentage: Optional[float] = None
    chamber_temperature: Optional[float] = None
    plasma_treatment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CryoEMPreparationId):
            self.id = CryoEMPreparationId(self.id)

        if self.grid_type is not None and not isinstance(self.grid_type, GridTypeEnum):
            self.grid_type = GridTypeEnum(self.grid_type)

        if self.support_film is not None and not isinstance(self.support_film, str):
            self.support_film = str(self.support_film)

        if self.hole_size is not None and not isinstance(self.hole_size, float):
            self.hole_size = float(self.hole_size)

        if self.vitrification_method is not None and not isinstance(self.vitrification_method, VitrificationMethodEnum):
            self.vitrification_method = VitrificationMethodEnum(self.vitrification_method)

        if self.blot_time is not None and not isinstance(self.blot_time, float):
            self.blot_time = float(self.blot_time)

        if self.blot_force is not None and not isinstance(self.blot_force, int):
            self.blot_force = int(self.blot_force)

        if self.humidity_percentage is not None and not isinstance(self.humidity_percentage, float):
            self.humidity_percentage = float(self.humidity_percentage)

        if self.chamber_temperature is not None and not isinstance(self.chamber_temperature, float):
            self.chamber_temperature = float(self.chamber_temperature)

        if self.plasma_treatment is not None and not isinstance(self.plasma_treatment, str):
            self.plasma_treatment = str(self.plasma_treatment)

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_type):
            self.MissingRequiredField("unknown_type")
        self.unknown_type = str(self.class_name)


@dataclass(repr=False)
class XRayPreparation(SamplePreparation):
    """
    X-ray crystallography specific preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["XRayPreparation"]
    class_class_curie: ClassVar[str] = "biostride_schema:XRayPreparation"
    class_name: ClassVar[str] = "XRayPreparation"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.XRayPreparation

    id: Union[str, XRayPreparationId] = None
    type: str = None
    sample_id: str = None
    crystallization_method: Optional[Union[str, "CrystallizationMethodEnum"]] = None
    crystallization_conditions: Optional[str] = None
    crystal_size: Optional[str] = None
    cryoprotectant: Optional[str] = None
    cryoprotectant_concentration: Optional[float] = None
    mounting_method: Optional[str] = None
    flash_cooling_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRayPreparationId):
            self.id = XRayPreparationId(self.id)

        if self.crystallization_method is not None and not isinstance(self.crystallization_method, CrystallizationMethodEnum):
            self.crystallization_method = CrystallizationMethodEnum(self.crystallization_method)

        if self.crystallization_conditions is not None and not isinstance(self.crystallization_conditions, str):
            self.crystallization_conditions = str(self.crystallization_conditions)

        if self.crystal_size is not None and not isinstance(self.crystal_size, str):
            self.crystal_size = str(self.crystal_size)

        if self.cryoprotectant is not None and not isinstance(self.cryoprotectant, str):
            self.cryoprotectant = str(self.cryoprotectant)

        if self.cryoprotectant_concentration is not None and not isinstance(self.cryoprotectant_concentration, float):
            self.cryoprotectant_concentration = float(self.cryoprotectant_concentration)

        if self.mounting_method is not None and not isinstance(self.mounting_method, str):
            self.mounting_method = str(self.mounting_method)

        if self.flash_cooling_method is not None and not isinstance(self.flash_cooling_method, str):
            self.flash_cooling_method = str(self.flash_cooling_method)

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_type):
            self.MissingRequiredField("unknown_type")
        self.unknown_type = str(self.class_name)


@dataclass(repr=False)
class SAXSPreparation(SamplePreparation):
    """
    SAXS/WAXS specific preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["SAXSPreparation"]
    class_class_curie: ClassVar[str] = "biostride_schema:SAXSPreparation"
    class_name: ClassVar[str] = "SAXSPreparation"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.SAXSPreparation

    id: Union[str, SAXSPreparationId] = None
    type: str = None
    sample_id: str = None
    concentration_series: Optional[Union[float, list[float]]] = empty_list()
    buffer_matching_protocol: Optional[str] = None
    sample_cell_type: Optional[str] = None
    cell_path_length: Optional[float] = None
    temperature_control: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SAXSPreparationId):
            self.id = SAXSPreparationId(self.id)

        if not isinstance(self.concentration_series, list):
            self.concentration_series = [self.concentration_series] if self.concentration_series is not None else []
        self.concentration_series = [v if isinstance(v, float) else float(v) for v in self.concentration_series]

        if self.buffer_matching_protocol is not None and not isinstance(self.buffer_matching_protocol, str):
            self.buffer_matching_protocol = str(self.buffer_matching_protocol)

        if self.sample_cell_type is not None and not isinstance(self.sample_cell_type, str):
            self.sample_cell_type = str(self.sample_cell_type)

        if self.cell_path_length is not None and not isinstance(self.cell_path_length, float):
            self.cell_path_length = float(self.cell_path_length)

        if self.temperature_control is not None and not isinstance(self.temperature_control, str):
            self.temperature_control = str(self.temperature_control)

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_type):
            self.MissingRequiredField("unknown_type")
        self.unknown_type = str(self.class_name)


@dataclass(repr=False)
class ExperimentalConditions(AttributeGroup):
    """
    Environmental and experimental conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["ExperimentalConditions"]
    class_class_curie: ClassVar[str] = "biostride_schema:ExperimentalConditions"
    class_name: ClassVar[str] = "ExperimentalConditions"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.ExperimentalConditions

    temperature: Optional[float] = None
    humidity: Optional[float] = None
    pressure: Optional[float] = None
    atmosphere: Optional[str] = None
    beam_energy: Optional[float] = None
    exposure_time: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        if self.humidity is not None and not isinstance(self.humidity, float):
            self.humidity = float(self.humidity)

        if self.pressure is not None and not isinstance(self.pressure, float):
            self.pressure = float(self.pressure)

        if self.atmosphere is not None and not isinstance(self.atmosphere, str):
            self.atmosphere = str(self.atmosphere)

        if self.beam_energy is not None and not isinstance(self.beam_energy, float):
            self.beam_energy = float(self.beam_energy)

        if self.exposure_time is not None and not isinstance(self.exposure_time, float):
            self.exposure_time = float(self.exposure_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataCollectionStrategy(AttributeGroup):
    """
    Strategy for data collection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["DataCollectionStrategy"]
    class_class_curie: ClassVar[str] = "biostride_schema:DataCollectionStrategy"
    class_name: ClassVar[str] = "DataCollectionStrategy"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.DataCollectionStrategy

    collection_mode: Optional[Union[str, "CollectionModeEnum"]] = None
    total_frames: Optional[int] = None
    frame_rate: Optional[float] = None
    total_dose: Optional[float] = None
    dose_per_frame: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.collection_mode is not None and not isinstance(self.collection_mode, CollectionModeEnum):
            self.collection_mode = CollectionModeEnum(self.collection_mode)

        if self.total_frames is not None and not isinstance(self.total_frames, int):
            self.total_frames = int(self.total_frames)

        if self.frame_rate is not None and not isinstance(self.frame_rate, float):
            self.frame_rate = float(self.frame_rate)

        if self.total_dose is not None and not isinstance(self.total_dose, float):
            self.total_dose = float(self.total_dose)

        if self.dose_per_frame is not None and not isinstance(self.dose_per_frame, float):
            self.dose_per_frame = float(self.dose_per_frame)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualityMetrics(AttributeGroup):
    """
    Quality metrics for experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["QualityMetrics"]
    class_class_curie: ClassVar[str] = "biostride_schema:QualityMetrics"
    class_name: ClassVar[str] = "QualityMetrics"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.QualityMetrics

    resolution: Optional[float] = None
    completeness: Optional[float] = None
    signal_to_noise: Optional[float] = None
    r_factor: Optional[float] = None
    i_zero: Optional[float] = None
    rg: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.resolution is not None and not isinstance(self.resolution, float):
            self.resolution = float(self.resolution)

        if self.completeness is not None and not isinstance(self.completeness, float):
            self.completeness = float(self.completeness)

        if self.signal_to_noise is not None and not isinstance(self.signal_to_noise, float):
            self.signal_to_noise = float(self.signal_to_noise)

        if self.r_factor is not None and not isinstance(self.r_factor, float):
            self.r_factor = float(self.r_factor)

        if self.i_zero is not None and not isinstance(self.i_zero, float):
            self.i_zero = float(self.i_zero)

        if self.rg is not None and not isinstance(self.rg, float):
            self.rg = float(self.rg)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputeResources(AttributeGroup):
    """
    Computational resources used
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA["ComputeResources"]
    class_class_curie: ClassVar[str] = "biostride_schema:ComputeResources"
    class_name: ClassVar[str] = "ComputeResources"
    class_model_uri: ClassVar[URIRef] = BIOSTRIDE_SCHEMA.ComputeResources

    cpu_hours: Optional[float] = None
    gpu_hours: Optional[float] = None
    memory_gb: Optional[float] = None
    storage_gb: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cpu_hours is not None and not isinstance(self.cpu_hours, float):
            self.cpu_hours = float(self.cpu_hours)

        if self.gpu_hours is not None and not isinstance(self.gpu_hours, float):
            self.gpu_hours = float(self.gpu_hours)

        if self.memory_gb is not None and not isinstance(self.memory_gb, float):
            self.memory_gb = float(self.memory_gb)

        if self.storage_gb is not None and not isinstance(self.storage_gb, float):
            self.storage_gb = float(self.storage_gb)

        super().__post_init__(**kwargs)


# Enumerations
class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological samples
    """
    protein = PermissibleValue(
        text="protein",
        description="Protein sample")
    nucleic_acid = PermissibleValue(
        text="nucleic_acid",
        description="Nucleic acid sample (DNA or RNA)")
    complex = PermissibleValue(
        text="complex",
        description="Protein-protein or protein-nucleic acid complex")
    membrane_protein = PermissibleValue(
        text="membrane_protein",
        description="Membrane protein sample")
    virus = PermissibleValue(
        text="virus",
        description="Viral particle")
    organelle = PermissibleValue(
        text="organelle",
        description="Cellular organelle")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological samples",
    )

class ConcentrationUnitEnum(EnumDefinitionImpl):
    """
    Units for concentration measurement
    """
    mg_per_ml = PermissibleValue(
        text="mg_per_ml",
        description="Milligrams per milliliter")
    micromolar = PermissibleValue(
        text="micromolar",
        description="Micromolar")
    millimolar = PermissibleValue(
        text="millimolar",
        description="Millimolar")
    nanomolar = PermissibleValue(
        text="nanomolar",
        description="Nanomolar")

    _defn = EnumDefinition(
        name="ConcentrationUnitEnum",
        description="Units for concentration measurement",
    )

class TemperatureUnitEnum(EnumDefinitionImpl):
    """
    Units for temperature measurement
    """
    celsius = PermissibleValue(
        text="celsius",
        description="Degrees Celsius")
    kelvin = PermissibleValue(
        text="kelvin",
        description="Kelvin")
    fahrenheit = PermissibleValue(
        text="fahrenheit",
        description="Degrees Fahrenheit")

    _defn = EnumDefinition(
        name="TemperatureUnitEnum",
        description="Units for temperature measurement",
    )

class GridTypeEnum(EnumDefinitionImpl):
    """
    Types of EM grids
    """
    c_flat = PermissibleValue(
        text="c_flat",
        description="C-flat holey carbon grid")
    quantifoil = PermissibleValue(
        text="quantifoil",
        description="Quantifoil holey carbon grid")
    lacey_carbon = PermissibleValue(
        text="lacey_carbon",
        description="Lacey carbon grid")
    ultrathin_carbon = PermissibleValue(
        text="ultrathin_carbon",
        description="Ultrathin carbon film")
    gold = PermissibleValue(
        text="gold",
        description="Gold grid")

    _defn = EnumDefinition(
        name="GridTypeEnum",
        description="Types of EM grids",
    )

class VitrificationMethodEnum(EnumDefinitionImpl):
    """
    Methods for vitrification
    """
    plunge_freezing = PermissibleValue(
        text="plunge_freezing",
        description="Plunge freezing in liquid ethane")
    high_pressure_freezing = PermissibleValue(
        text="high_pressure_freezing",
        description="High pressure freezing")
    slam_freezing = PermissibleValue(
        text="slam_freezing",
        description="Slam freezing")

    _defn = EnumDefinition(
        name="VitrificationMethodEnum",
        description="Methods for vitrification",
    )

class CrystallizationMethodEnum(EnumDefinitionImpl):
    """
    Methods for protein crystallization
    """
    vapor_diffusion_hanging = PermissibleValue(
        text="vapor_diffusion_hanging",
        description="Vapor diffusion hanging drop")
    vapor_diffusion_sitting = PermissibleValue(
        text="vapor_diffusion_sitting",
        description="Vapor diffusion sitting drop")
    microbatch = PermissibleValue(
        text="microbatch",
        description="Microbatch under oil")
    dialysis = PermissibleValue(
        text="dialysis",
        description="Dialysis method")
    free_interface_diffusion = PermissibleValue(
        text="free_interface_diffusion",
        description="Free interface diffusion")

    _defn = EnumDefinition(
        name="CrystallizationMethodEnum",
        description="Methods for protein crystallization",
    )

class InstrumentStatusEnum(EnumDefinitionImpl):
    """
    Operational status of instruments
    """
    operational = PermissibleValue(
        text="operational",
        description="Instrument is operational")
    maintenance = PermissibleValue(
        text="maintenance",
        description="Instrument under maintenance")
    offline = PermissibleValue(
        text="offline",
        description="Instrument is offline")
    commissioning = PermissibleValue(
        text="commissioning",
        description="Instrument being commissioned")

    _defn = EnumDefinition(
        name="InstrumentStatusEnum",
        description="Operational status of instruments",
    )

class DetectorTypeEnum(EnumDefinitionImpl):
    """
    Types of detectors for cryo-EM
    """
    direct_electron = PermissibleValue(
        text="direct_electron",
        description="Direct electron detector")
    ccd = PermissibleValue(
        text="ccd",
        description="CCD camera")
    cmos = PermissibleValue(
        text="cmos",
        description="CMOS detector")
    hybrid_pixel = PermissibleValue(
        text="hybrid_pixel",
        description="Hybrid pixel detector")

    _defn = EnumDefinition(
        name="DetectorTypeEnum",
        description="Types of detectors for cryo-EM",
    )

class XRaySourceTypeEnum(EnumDefinitionImpl):
    """
    Types of X-ray sources
    """
    synchrotron = PermissibleValue(
        text="synchrotron",
        description="Synchrotron radiation source")
    rotating_anode = PermissibleValue(
        text="rotating_anode",
        description="Rotating anode generator")
    microfocus = PermissibleValue(
        text="microfocus",
        description="Microfocus sealed tube")
    metal_jet = PermissibleValue(
        text="metal_jet",
        description="Liquid metal jet source")

    _defn = EnumDefinition(
        name="XRaySourceTypeEnum",
        description="Types of X-ray sources",
    )

class TechniqueEnum(EnumDefinitionImpl):
    """
    Structural biology techniques
    """
    cryo_em = PermissibleValue(
        text="cryo_em",
        description="Cryo-electron microscopy")
    xray_crystallography = PermissibleValue(
        text="xray_crystallography",
        description="X-ray crystallography")
    saxs = PermissibleValue(
        text="saxs",
        description="Small-angle X-ray scattering")
    waxs = PermissibleValue(
        text="waxs",
        description="Wide-angle X-ray scattering")
    sans = PermissibleValue(
        text="sans",
        description="Small-angle neutron scattering")
    cryo_et = PermissibleValue(
        text="cryo_et",
        description="Cryo-electron tomography")
    electron_microscopy = PermissibleValue(
        text="electron_microscopy",
        description="General electron microscopy")
    mass_spectrometry = PermissibleValue(
        text="mass_spectrometry",
        description="Mass spectrometry")

    _defn = EnumDefinition(
        name="TechniqueEnum",
        description="Structural biology techniques",
    )

class ProcessingStatusEnum(EnumDefinitionImpl):
    """
    Processing status
    """
    raw = PermissibleValue(
        text="raw",
        description="Raw data")
    preprocessing = PermissibleValue(
        text="preprocessing",
        description="Being preprocessed")
    processing = PermissibleValue(
        text="processing",
        description="Being processed")
    completed = PermissibleValue(
        text="completed",
        description="Processing completed")
    failed = PermissibleValue(
        text="failed",
        description="Processing failed")

    _defn = EnumDefinition(
        name="ProcessingStatusEnum",
        description="Processing status",
    )

class WorkflowTypeEnum(EnumDefinitionImpl):
    """
    Types of processing workflows
    """
    motion_correction = PermissibleValue(
        text="motion_correction",
        description="Motion correction for cryo-EM")
    ctf_estimation = PermissibleValue(
        text="ctf_estimation",
        description="CTF estimation")
    particle_picking = PermissibleValue(
        text="particle_picking",
        description="Particle picking")
    classification_2d = PermissibleValue(
        text="classification_2d",
        description="2D classification")
    classification_3d = PermissibleValue(
        text="classification_3d",
        description="3D classification")
    refinement = PermissibleValue(
        text="refinement",
        description="3D refinement")
    model_building = PermissibleValue(
        text="model_building",
        description="Atomic model building")
    phasing = PermissibleValue(
        text="phasing",
        description="Phase determination")
    integration = PermissibleValue(
        text="integration",
        description="Data integration")
    scaling = PermissibleValue(
        text="scaling",
        description="Data scaling")
    saxs_analysis = PermissibleValue(
        text="saxs_analysis",
        description="SAXS data analysis")
    em_2d_classification = PermissibleValue(
        text="em_2d_classification",
        description="EM 2D classification")
    mass_spec_deconvolution = PermissibleValue(
        text="mass_spec_deconvolution",
        description="Mass spectrometry deconvolution")

    _defn = EnumDefinition(
        name="WorkflowTypeEnum",
        description="Types of processing workflows",
    )

class FileFormatEnum(EnumDefinitionImpl):
    """
    File formats
    """
    mrc = PermissibleValue(
        text="mrc",
        description="MRC format for EM data")
    tiff = PermissibleValue(
        text="tiff",
        description="TIFF image format")
    hdf5 = PermissibleValue(
        text="hdf5",
        description="HDF5 hierarchical data format")
    star = PermissibleValue(
        text="star",
        description="STAR format for metadata")
    pdb = PermissibleValue(
        text="pdb",
        description="PDB coordinate format")
    mmcif = PermissibleValue(
        text="mmcif",
        description="mmCIF format")
    mtz = PermissibleValue(
        text="mtz",
        description="MTZ reflection format")
    cbf = PermissibleValue(
        text="cbf",
        description="Crystallographic Binary Format")
    ascii = PermissibleValue(
        text="ascii",
        description="ASCII text format")
    thermo_raw = PermissibleValue(
        text="thermo_raw",
        description="Thermo Fisher RAW format")
    zip = PermissibleValue(
        text="zip",
        description="ZIP compressed archive")

    _defn = EnumDefinition(
        name="FileFormatEnum",
        description="File formats",
    )

class DataTypeEnum(EnumDefinitionImpl):
    """
    Types of data
    """
    micrograph = PermissibleValue(
        text="micrograph",
        description="Electron micrograph")
    diffraction = PermissibleValue(
        text="diffraction",
        description="Diffraction pattern")
    scattering = PermissibleValue(
        text="scattering",
        description="Scattering data")
    particles = PermissibleValue(
        text="particles",
        description="Particle stack")
    volume = PermissibleValue(
        text="volume",
        description="3D volume")
    model = PermissibleValue(
        text="model",
        description="Atomic model")
    metadata = PermissibleValue(
        text="metadata",
        description="Metadata file")
    raw_data = PermissibleValue(
        text="raw_data",
        description="Raw experimental data")
    processed_data = PermissibleValue(
        text="processed_data",
        description="Processed data")

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Types of data",
    )

class CollectionModeEnum(EnumDefinitionImpl):
    """
    Data collection modes
    """
    counting = PermissibleValue(
        text="counting",
        description="Counting mode")
    super_resolution = PermissibleValue(
        text="super_resolution",
        description="Super-resolution mode")
    continuous = PermissibleValue(
        text="continuous",
        description="Continuous collection")
    oscillation = PermissibleValue(
        text="oscillation",
        description="Oscillation method")
    still = PermissibleValue(
        text="still",
        description="Still images")
    batch = PermissibleValue(
        text="batch",
        description="Batch mode collection")
    sec_saxs = PermissibleValue(
        text="sec_saxs",
        description="SEC-SAXS collection mode")
    single_particle = PermissibleValue(
        text="single_particle",
        description="Single particle analysis mode")

    _defn = EnumDefinition(
        name="CollectionModeEnum",
        description="Data collection modes",
    )

class IlluminationTypeEnum(EnumDefinitionImpl):
    """
    Types of illumination for optical microscopy
    """
    brightfield = PermissibleValue(
        text="brightfield",
        description="Brightfield illumination")
    darkfield = PermissibleValue(
        text="darkfield",
        description="Darkfield illumination")
    phase_contrast = PermissibleValue(
        text="phase_contrast",
        description="Phase contrast microscopy")
    dic = PermissibleValue(
        text="dic",
        description="Differential interference contrast (DIC/Nomarski)")
    fluorescence = PermissibleValue(
        text="fluorescence",
        description="Fluorescence illumination")
    confocal = PermissibleValue(
        text="confocal",
        description="Confocal laser scanning")
    polarized = PermissibleValue(
        text="polarized",
        description="Polarized light microscopy")
    oblique = PermissibleValue(
        text="oblique",
        description="Oblique illumination")

    _defn = EnumDefinition(
        name="IlluminationTypeEnum",
        description="Types of illumination for optical microscopy",
    )

# Slots
class slots:
    pass

slots.namedThing__id = Slot(uri=BIOSTRIDE_SCHEMA.id, name="namedThing__id", curie=BIOSTRIDE_SCHEMA.curie('id'),
                   model_uri=BIOSTRIDE_SCHEMA.namedThing__id, domain=None, range=URIRef)

slots.namedThing__title = Slot(uri=DCTERMS.title, name="namedThing__title", curie=DCTERMS.curie('title'),
                   model_uri=BIOSTRIDE_SCHEMA.namedThing__title, domain=None, range=Optional[str])

slots.namedThing__description = Slot(uri=BIOSTRIDE_SCHEMA.description, name="namedThing__description", curie=BIOSTRIDE_SCHEMA.curie('description'),
                   model_uri=BIOSTRIDE_SCHEMA.namedThing__description, domain=None, range=Optional[str])

slots.attributeGroup__description = Slot(uri=BIOSTRIDE_SCHEMA.description, name="attributeGroup__description", curie=BIOSTRIDE_SCHEMA.curie('description'),
                   model_uri=BIOSTRIDE_SCHEMA.attributeGroup__description, domain=None, range=Optional[str])

slots.dataset__keywords = Slot(uri=BIOSTRIDE_SCHEMA.keywords, name="dataset__keywords", curie=BIOSTRIDE_SCHEMA.curie('keywords'),
                   model_uri=BIOSTRIDE_SCHEMA.dataset__keywords, domain=None, range=Optional[Union[str, list[str]]])

slots.dataset__instruments = Slot(uri=BIOSTRIDE_SCHEMA.instruments, name="dataset__instruments", curie=BIOSTRIDE_SCHEMA.curie('instruments'),
                   model_uri=BIOSTRIDE_SCHEMA.dataset__instruments, domain=None, range=Optional[Union[dict[Union[str, InstrumentId], Union[dict, Instrument]], list[Union[dict, Instrument]]]])

slots.dataset__studies = Slot(uri=BIOSTRIDE_SCHEMA.studies, name="dataset__studies", curie=BIOSTRIDE_SCHEMA.curie('studies'),
                   model_uri=BIOSTRIDE_SCHEMA.dataset__studies, domain=None, range=Optional[Union[dict[Union[str, StudyId], Union[dict, Study]], list[Union[dict, Study]]]])

slots.study__samples = Slot(uri=BIOSTRIDE_SCHEMA.samples, name="study__samples", curie=BIOSTRIDE_SCHEMA.curie('samples'),
                   model_uri=BIOSTRIDE_SCHEMA.study__samples, domain=None, range=Optional[Union[dict[Union[str, SampleId], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.study__sample_preparations = Slot(uri=BIOSTRIDE_SCHEMA.sample_preparations, name="study__sample_preparations", curie=BIOSTRIDE_SCHEMA.curie('sample_preparations'),
                   model_uri=BIOSTRIDE_SCHEMA.study__sample_preparations, domain=None, range=Optional[Union[dict[Union[str, SamplePreparationId], Union[dict, SamplePreparation]], list[Union[dict, SamplePreparation]]]])

slots.study__instrument_runs = Slot(uri=BIOSTRIDE_SCHEMA.instrument_runs, name="study__instrument_runs", curie=BIOSTRIDE_SCHEMA.curie('instrument_runs'),
                   model_uri=BIOSTRIDE_SCHEMA.study__instrument_runs, domain=None, range=Optional[Union[dict[Union[str, ExperimentRunId], Union[dict, ExperimentRun]], list[Union[dict, ExperimentRun]]]])

slots.study__workflow_runs = Slot(uri=BIOSTRIDE_SCHEMA.workflow_runs, name="study__workflow_runs", curie=BIOSTRIDE_SCHEMA.curie('workflow_runs'),
                   model_uri=BIOSTRIDE_SCHEMA.study__workflow_runs, domain=None, range=Optional[Union[dict[Union[str, WorkflowRunId], Union[dict, WorkflowRun]], list[Union[dict, WorkflowRun]]]])

slots.study__data_files = Slot(uri=BIOSTRIDE_SCHEMA.data_files, name="study__data_files", curie=BIOSTRIDE_SCHEMA.curie('data_files'),
                   model_uri=BIOSTRIDE_SCHEMA.study__data_files, domain=None, range=Optional[Union[dict[Union[str, DataFileId], Union[dict, DataFile]], list[Union[dict, DataFile]]]])

slots.study__images = Slot(uri=BIOSTRIDE_SCHEMA.images, name="study__images", curie=BIOSTRIDE_SCHEMA.curie('images'),
                   model_uri=BIOSTRIDE_SCHEMA.study__images, domain=None, range=Optional[Union[dict[Union[str, ImageId], Union[dict, Image]], list[Union[dict, Image]]]])

slots.sample__sample_code = Slot(uri=BIOSTRIDE_SCHEMA.sample_code, name="sample__sample_code", curie=BIOSTRIDE_SCHEMA.curie('sample_code'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__sample_code, domain=None, range=str)

slots.sample__sample_type = Slot(uri=BIOSTRIDE_SCHEMA.sample_type, name="sample__sample_type", curie=BIOSTRIDE_SCHEMA.curie('sample_type'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__sample_type, domain=None, range=Union[str, "SampleTypeEnum"])

slots.sample__molecular_composition = Slot(uri=BIOSTRIDE_SCHEMA.molecular_composition, name="sample__molecular_composition", curie=BIOSTRIDE_SCHEMA.curie('molecular_composition'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__molecular_composition, domain=None, range=Optional[Union[dict, MolecularComposition]])

slots.sample__molecular_weight = Slot(uri=BIOSTRIDE_SCHEMA.molecular_weight, name="sample__molecular_weight", curie=BIOSTRIDE_SCHEMA.curie('molecular_weight'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__molecular_weight, domain=None, range=Optional[float])

slots.sample__concentration = Slot(uri=BIOSTRIDE_SCHEMA.concentration, name="sample__concentration", curie=BIOSTRIDE_SCHEMA.curie('concentration'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__concentration, domain=None, range=Optional[float])

slots.sample__concentration_unit = Slot(uri=BIOSTRIDE_SCHEMA.concentration_unit, name="sample__concentration_unit", curie=BIOSTRIDE_SCHEMA.curie('concentration_unit'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__concentration_unit, domain=None, range=Optional[Union[str, "ConcentrationUnitEnum"]])

slots.sample__buffer_composition = Slot(uri=BIOSTRIDE_SCHEMA.buffer_composition, name="sample__buffer_composition", curie=BIOSTRIDE_SCHEMA.curie('buffer_composition'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__buffer_composition, domain=None, range=Optional[Union[dict, BufferComposition]])

slots.sample__preparation_method = Slot(uri=BIOSTRIDE_SCHEMA.preparation_method, name="sample__preparation_method", curie=BIOSTRIDE_SCHEMA.curie('preparation_method'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__preparation_method, domain=None, range=Optional[str])

slots.sample__storage_conditions = Slot(uri=BIOSTRIDE_SCHEMA.storage_conditions, name="sample__storage_conditions", curie=BIOSTRIDE_SCHEMA.curie('storage_conditions'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__storage_conditions, domain=None, range=Optional[Union[dict, StorageConditions]])

slots.sample__organism = Slot(uri=BIOSTRIDE_SCHEMA.organism, name="sample__organism", curie=BIOSTRIDE_SCHEMA.curie('organism'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__organism, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__anatomy = Slot(uri=BIOSTRIDE_SCHEMA.anatomy, name="sample__anatomy", curie=BIOSTRIDE_SCHEMA.curie('anatomy'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__anatomy, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__cell_type = Slot(uri=BIOSTRIDE_SCHEMA.cell_type, name="sample__cell_type", curie=BIOSTRIDE_SCHEMA.curie('cell_type'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__cell_type, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__parent_sample_id = Slot(uri=BIOSTRIDE_SCHEMA.parent_sample_id, name="sample__parent_sample_id", curie=BIOSTRIDE_SCHEMA.curie('parent_sample_id'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__parent_sample_id, domain=None, range=Optional[Union[str, SampleId]])

slots.sample__purity_percentage = Slot(uri=BIOSTRIDE_SCHEMA.purity_percentage, name="sample__purity_percentage", curie=BIOSTRIDE_SCHEMA.curie('purity_percentage'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__purity_percentage, domain=None, range=Optional[float])

slots.sample__quality_metrics = Slot(uri=BIOSTRIDE_SCHEMA.quality_metrics, name="sample__quality_metrics", curie=BIOSTRIDE_SCHEMA.curie('quality_metrics'),
                   model_uri=BIOSTRIDE_SCHEMA.sample__quality_metrics, domain=None, range=Optional[str])

slots.samplePreparation__type = Slot(uri=BIOSTRIDE_SCHEMA.type, name="samplePreparation__type", curie=BIOSTRIDE_SCHEMA.curie('type'),
                   model_uri=BIOSTRIDE_SCHEMA.samplePreparation__type, domain=None, range=str)

slots.samplePreparation__sample_id = Slot(uri=BIOSTRIDE_SCHEMA.sample_id, name="samplePreparation__sample_id", curie=BIOSTRIDE_SCHEMA.curie('sample_id'),
                   model_uri=BIOSTRIDE_SCHEMA.samplePreparation__sample_id, domain=None, range=str)

slots.samplePreparation__preparation_date = Slot(uri=BIOSTRIDE_SCHEMA.preparation_date, name="samplePreparation__preparation_date", curie=BIOSTRIDE_SCHEMA.curie('preparation_date'),
                   model_uri=BIOSTRIDE_SCHEMA.samplePreparation__preparation_date, domain=None, range=Optional[str])

slots.samplePreparation__operator_id = Slot(uri=BIOSTRIDE_SCHEMA.operator_id, name="samplePreparation__operator_id", curie=BIOSTRIDE_SCHEMA.curie('operator_id'),
                   model_uri=BIOSTRIDE_SCHEMA.samplePreparation__operator_id, domain=None, range=Optional[str])

slots.samplePreparation__protocol_description = Slot(uri=BIOSTRIDE_SCHEMA.protocol_description, name="samplePreparation__protocol_description", curie=BIOSTRIDE_SCHEMA.curie('protocol_description'),
                   model_uri=BIOSTRIDE_SCHEMA.samplePreparation__protocol_description, domain=None, range=Optional[str])

slots.instrument__instrument_code = Slot(uri=BIOSTRIDE_SCHEMA.instrument_code, name="instrument__instrument_code", curie=BIOSTRIDE_SCHEMA.curie('instrument_code'),
                   model_uri=BIOSTRIDE_SCHEMA.instrument__instrument_code, domain=None, range=str)

slots.instrument__manufacturer = Slot(uri=BIOSTRIDE_SCHEMA.manufacturer, name="instrument__manufacturer", curie=BIOSTRIDE_SCHEMA.curie('manufacturer'),
                   model_uri=BIOSTRIDE_SCHEMA.instrument__manufacturer, domain=None, range=Optional[str])

slots.instrument__model = Slot(uri=BIOSTRIDE_SCHEMA.model, name="instrument__model", curie=BIOSTRIDE_SCHEMA.curie('model'),
                   model_uri=BIOSTRIDE_SCHEMA.instrument__model, domain=None, range=Optional[str])

slots.instrument__installation_date = Slot(uri=BIOSTRIDE_SCHEMA.installation_date, name="instrument__installation_date", curie=BIOSTRIDE_SCHEMA.curie('installation_date'),
                   model_uri=BIOSTRIDE_SCHEMA.instrument__installation_date, domain=None, range=Optional[str])

slots.instrument__current_status = Slot(uri=BIOSTRIDE_SCHEMA.current_status, name="instrument__current_status", curie=BIOSTRIDE_SCHEMA.curie('current_status'),
                   model_uri=BIOSTRIDE_SCHEMA.instrument__current_status, domain=None, range=Optional[Union[str, "InstrumentStatusEnum"]])

slots.cryoEMInstrument__accelerating_voltage = Slot(uri=BIOSTRIDE_SCHEMA.accelerating_voltage, name="cryoEMInstrument__accelerating_voltage", curie=BIOSTRIDE_SCHEMA.curie('accelerating_voltage'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMInstrument__accelerating_voltage, domain=None, range=Optional[int])

slots.cryoEMInstrument__cs_corrector = Slot(uri=BIOSTRIDE_SCHEMA.cs_corrector, name="cryoEMInstrument__cs_corrector", curie=BIOSTRIDE_SCHEMA.curie('cs_corrector'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMInstrument__cs_corrector, domain=None, range=Optional[Union[bool, Bool]])

slots.cryoEMInstrument__phase_plate = Slot(uri=BIOSTRIDE_SCHEMA.phase_plate, name="cryoEMInstrument__phase_plate", curie=BIOSTRIDE_SCHEMA.curie('phase_plate'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMInstrument__phase_plate, domain=None, range=Optional[Union[bool, Bool]])

slots.cryoEMInstrument__detector_type = Slot(uri=BIOSTRIDE_SCHEMA.detector_type, name="cryoEMInstrument__detector_type", curie=BIOSTRIDE_SCHEMA.curie('detector_type'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMInstrument__detector_type, domain=None, range=Optional[Union[str, "DetectorTypeEnum"]])

slots.cryoEMInstrument__detector_dimensions = Slot(uri=BIOSTRIDE_SCHEMA.detector_dimensions, name="cryoEMInstrument__detector_dimensions", curie=BIOSTRIDE_SCHEMA.curie('detector_dimensions'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMInstrument__detector_dimensions, domain=None, range=Optional[str])

slots.cryoEMInstrument__pixel_size_min = Slot(uri=BIOSTRIDE_SCHEMA.pixel_size_min, name="cryoEMInstrument__pixel_size_min", curie=BIOSTRIDE_SCHEMA.curie('pixel_size_min'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMInstrument__pixel_size_min, domain=None, range=Optional[float])

slots.cryoEMInstrument__pixel_size_max = Slot(uri=BIOSTRIDE_SCHEMA.pixel_size_max, name="cryoEMInstrument__pixel_size_max", curie=BIOSTRIDE_SCHEMA.curie('pixel_size_max'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMInstrument__pixel_size_max, domain=None, range=Optional[float])

slots.cryoEMInstrument__autoloader_capacity = Slot(uri=BIOSTRIDE_SCHEMA.autoloader_capacity, name="cryoEMInstrument__autoloader_capacity", curie=BIOSTRIDE_SCHEMA.curie('autoloader_capacity'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMInstrument__autoloader_capacity, domain=None, range=Optional[int])

slots.xRayInstrument__source_type = Slot(uri=BIOSTRIDE_SCHEMA.source_type, name="xRayInstrument__source_type", curie=BIOSTRIDE_SCHEMA.curie('source_type'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__source_type, domain=None, range=Optional[Union[str, "XRaySourceTypeEnum"]])

slots.xRayInstrument__energy_min = Slot(uri=BIOSTRIDE_SCHEMA.energy_min, name="xRayInstrument__energy_min", curie=BIOSTRIDE_SCHEMA.curie('energy_min'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__energy_min, domain=None, range=Optional[float])

slots.xRayInstrument__energy_max = Slot(uri=BIOSTRIDE_SCHEMA.energy_max, name="xRayInstrument__energy_max", curie=BIOSTRIDE_SCHEMA.curie('energy_max'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__energy_max, domain=None, range=Optional[float])

slots.xRayInstrument__beam_size_min = Slot(uri=BIOSTRIDE_SCHEMA.beam_size_min, name="xRayInstrument__beam_size_min", curie=BIOSTRIDE_SCHEMA.curie('beam_size_min'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__beam_size_min, domain=None, range=Optional[float])

slots.xRayInstrument__beam_size_max = Slot(uri=BIOSTRIDE_SCHEMA.beam_size_max, name="xRayInstrument__beam_size_max", curie=BIOSTRIDE_SCHEMA.curie('beam_size_max'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__beam_size_max, domain=None, range=Optional[float])

slots.xRayInstrument__flux_density = Slot(uri=BIOSTRIDE_SCHEMA.flux_density, name="xRayInstrument__flux_density", curie=BIOSTRIDE_SCHEMA.curie('flux_density'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__flux_density, domain=None, range=Optional[float])

slots.xRayInstrument__monochromator_type = Slot(uri=BIOSTRIDE_SCHEMA.monochromator_type, name="xRayInstrument__monochromator_type", curie=BIOSTRIDE_SCHEMA.curie('monochromator_type'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__monochromator_type, domain=None, range=Optional[str])

slots.xRayInstrument__goniometer_type = Slot(uri=BIOSTRIDE_SCHEMA.goniometer_type, name="xRayInstrument__goniometer_type", curie=BIOSTRIDE_SCHEMA.curie('goniometer_type'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__goniometer_type, domain=None, range=Optional[str])

slots.xRayInstrument__crystal_cooling_capability = Slot(uri=BIOSTRIDE_SCHEMA.crystal_cooling_capability, name="xRayInstrument__crystal_cooling_capability", curie=BIOSTRIDE_SCHEMA.curie('crystal_cooling_capability'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayInstrument__crystal_cooling_capability, domain=None, range=Optional[Union[bool, Bool]])

slots.sAXSInstrument__q_range_min = Slot(uri=BIOSTRIDE_SCHEMA.q_range_min, name="sAXSInstrument__q_range_min", curie=BIOSTRIDE_SCHEMA.curie('q_range_min'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSInstrument__q_range_min, domain=None, range=Optional[float])

slots.sAXSInstrument__q_range_max = Slot(uri=BIOSTRIDE_SCHEMA.q_range_max, name="sAXSInstrument__q_range_max", curie=BIOSTRIDE_SCHEMA.curie('q_range_max'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSInstrument__q_range_max, domain=None, range=Optional[float])

slots.sAXSInstrument__detector_distance_min = Slot(uri=BIOSTRIDE_SCHEMA.detector_distance_min, name="sAXSInstrument__detector_distance_min", curie=BIOSTRIDE_SCHEMA.curie('detector_distance_min'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSInstrument__detector_distance_min, domain=None, range=Optional[float])

slots.sAXSInstrument__detector_distance_max = Slot(uri=BIOSTRIDE_SCHEMA.detector_distance_max, name="sAXSInstrument__detector_distance_max", curie=BIOSTRIDE_SCHEMA.curie('detector_distance_max'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSInstrument__detector_distance_max, domain=None, range=Optional[float])

slots.sAXSInstrument__sample_changer_capacity = Slot(uri=BIOSTRIDE_SCHEMA.sample_changer_capacity, name="sAXSInstrument__sample_changer_capacity", curie=BIOSTRIDE_SCHEMA.curie('sample_changer_capacity'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSInstrument__sample_changer_capacity, domain=None, range=Optional[int])

slots.sAXSInstrument__temperature_control_range = Slot(uri=BIOSTRIDE_SCHEMA.temperature_control_range, name="sAXSInstrument__temperature_control_range", curie=BIOSTRIDE_SCHEMA.curie('temperature_control_range'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSInstrument__temperature_control_range, domain=None, range=Optional[str])

slots.experimentRun__experiment_code = Slot(uri=BIOSTRIDE_SCHEMA.experiment_code, name="experimentRun__experiment_code", curie=BIOSTRIDE_SCHEMA.curie('experiment_code'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__experiment_code, domain=None, range=str)

slots.experimentRun__sample_id = Slot(uri=BIOSTRIDE_SCHEMA.sample_id, name="experimentRun__sample_id", curie=BIOSTRIDE_SCHEMA.curie('sample_id'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__sample_id, domain=None, range=str)

slots.experimentRun__instrument_id = Slot(uri=BIOSTRIDE_SCHEMA.instrument_id, name="experimentRun__instrument_id", curie=BIOSTRIDE_SCHEMA.curie('instrument_id'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__instrument_id, domain=None, range=Union[str, InstrumentId])

slots.experimentRun__experiment_date = Slot(uri=BIOSTRIDE_SCHEMA.experiment_date, name="experimentRun__experiment_date", curie=BIOSTRIDE_SCHEMA.curie('experiment_date'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__experiment_date, domain=None, range=Optional[str])

slots.experimentRun__operator_id = Slot(uri=BIOSTRIDE_SCHEMA.operator_id, name="experimentRun__operator_id", curie=BIOSTRIDE_SCHEMA.curie('operator_id'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__operator_id, domain=None, range=Optional[str])

slots.experimentRun__technique = Slot(uri=BIOSTRIDE_SCHEMA.technique, name="experimentRun__technique", curie=BIOSTRIDE_SCHEMA.curie('technique'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__technique, domain=None, range=Union[str, "TechniqueEnum"])

slots.experimentRun__experimental_conditions = Slot(uri=BIOSTRIDE_SCHEMA.experimental_conditions, name="experimentRun__experimental_conditions", curie=BIOSTRIDE_SCHEMA.curie('experimental_conditions'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__experimental_conditions, domain=None, range=Optional[Union[dict, ExperimentalConditions]])

slots.experimentRun__data_collection_strategy = Slot(uri=BIOSTRIDE_SCHEMA.data_collection_strategy, name="experimentRun__data_collection_strategy", curie=BIOSTRIDE_SCHEMA.curie('data_collection_strategy'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__data_collection_strategy, domain=None, range=Optional[Union[dict, DataCollectionStrategy]])

slots.experimentRun__quality_metrics = Slot(uri=BIOSTRIDE_SCHEMA.quality_metrics, name="experimentRun__quality_metrics", curie=BIOSTRIDE_SCHEMA.curie('quality_metrics'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__quality_metrics, domain=None, range=Optional[Union[dict, QualityMetrics]])

slots.experimentRun__raw_data_location = Slot(uri=BIOSTRIDE_SCHEMA.raw_data_location, name="experimentRun__raw_data_location", curie=BIOSTRIDE_SCHEMA.curie('raw_data_location'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__raw_data_location, domain=None, range=Optional[str])

slots.experimentRun__processing_status = Slot(uri=BIOSTRIDE_SCHEMA.processing_status, name="experimentRun__processing_status", curie=BIOSTRIDE_SCHEMA.curie('processing_status'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentRun__processing_status, domain=None, range=Optional[Union[str, "ProcessingStatusEnum"]])

slots.workflowRun__workflow_code = Slot(uri=BIOSTRIDE_SCHEMA.workflow_code, name="workflowRun__workflow_code", curie=BIOSTRIDE_SCHEMA.curie('workflow_code'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__workflow_code, domain=None, range=str)

slots.workflowRun__workflow_type = Slot(uri=BIOSTRIDE_SCHEMA.workflow_type, name="workflowRun__workflow_type", curie=BIOSTRIDE_SCHEMA.curie('workflow_type'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__workflow_type, domain=None, range=Union[str, "WorkflowTypeEnum"])

slots.workflowRun__experiment_id = Slot(uri=BIOSTRIDE_SCHEMA.experiment_id, name="workflowRun__experiment_id", curie=BIOSTRIDE_SCHEMA.curie('experiment_id'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__experiment_id, domain=None, range=str)

slots.workflowRun__processing_level = Slot(uri=BIOSTRIDE_SCHEMA.processing_level, name="workflowRun__processing_level", curie=BIOSTRIDE_SCHEMA.curie('processing_level'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__processing_level, domain=None, range=Optional[int])

slots.workflowRun__software_name = Slot(uri=BIOSTRIDE_SCHEMA.software_name, name="workflowRun__software_name", curie=BIOSTRIDE_SCHEMA.curie('software_name'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__software_name, domain=None, range=str)

slots.workflowRun__software_version = Slot(uri=BIOSTRIDE_SCHEMA.software_version, name="workflowRun__software_version", curie=BIOSTRIDE_SCHEMA.curie('software_version'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__software_version, domain=None, range=Optional[str])

slots.workflowRun__processing_parameters = Slot(uri=BIOSTRIDE_SCHEMA.processing_parameters, name="workflowRun__processing_parameters", curie=BIOSTRIDE_SCHEMA.curie('processing_parameters'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__processing_parameters, domain=None, range=Optional[str])

slots.workflowRun__compute_resources = Slot(uri=BIOSTRIDE_SCHEMA.compute_resources, name="workflowRun__compute_resources", curie=BIOSTRIDE_SCHEMA.curie('compute_resources'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__compute_resources, domain=None, range=Optional[Union[dict, ComputeResources]])

slots.workflowRun__started_at = Slot(uri=BIOSTRIDE_SCHEMA.started_at, name="workflowRun__started_at", curie=BIOSTRIDE_SCHEMA.curie('started_at'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__started_at, domain=None, range=Optional[str])

slots.workflowRun__completed_at = Slot(uri=BIOSTRIDE_SCHEMA.completed_at, name="workflowRun__completed_at", curie=BIOSTRIDE_SCHEMA.curie('completed_at'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__completed_at, domain=None, range=Optional[str])

slots.workflowRun__output_files = Slot(uri=BIOSTRIDE_SCHEMA.output_files, name="workflowRun__output_files", curie=BIOSTRIDE_SCHEMA.curie('output_files'),
                   model_uri=BIOSTRIDE_SCHEMA.workflowRun__output_files, domain=None, range=Optional[Union[Union[str, DataFileId], list[Union[str, DataFileId]]]])

slots.dataFile__file_name = Slot(uri=BIOSTRIDE_SCHEMA.file_name, name="dataFile__file_name", curie=BIOSTRIDE_SCHEMA.curie('file_name'),
                   model_uri=BIOSTRIDE_SCHEMA.dataFile__file_name, domain=None, range=str)

slots.dataFile__file_path = Slot(uri=BIOSTRIDE_SCHEMA.file_path, name="dataFile__file_path", curie=BIOSTRIDE_SCHEMA.curie('file_path'),
                   model_uri=BIOSTRIDE_SCHEMA.dataFile__file_path, domain=None, range=Optional[str])

slots.dataFile__file_format = Slot(uri=BIOSTRIDE_SCHEMA.file_format, name="dataFile__file_format", curie=BIOSTRIDE_SCHEMA.curie('file_format'),
                   model_uri=BIOSTRIDE_SCHEMA.dataFile__file_format, domain=None, range=Union[str, "FileFormatEnum"])

slots.dataFile__file_size_bytes = Slot(uri=BIOSTRIDE_SCHEMA.file_size_bytes, name="dataFile__file_size_bytes", curie=BIOSTRIDE_SCHEMA.curie('file_size_bytes'),
                   model_uri=BIOSTRIDE_SCHEMA.dataFile__file_size_bytes, domain=None, range=Optional[int])

slots.dataFile__checksum = Slot(uri=BIOSTRIDE_SCHEMA.checksum, name="dataFile__checksum", curie=BIOSTRIDE_SCHEMA.curie('checksum'),
                   model_uri=BIOSTRIDE_SCHEMA.dataFile__checksum, domain=None, range=Optional[str])

slots.dataFile__creation_date = Slot(uri=BIOSTRIDE_SCHEMA.creation_date, name="dataFile__creation_date", curie=BIOSTRIDE_SCHEMA.curie('creation_date'),
                   model_uri=BIOSTRIDE_SCHEMA.dataFile__creation_date, domain=None, range=Optional[str])

slots.dataFile__data_type = Slot(uri=BIOSTRIDE_SCHEMA.data_type, name="dataFile__data_type", curie=BIOSTRIDE_SCHEMA.curie('data_type'),
                   model_uri=BIOSTRIDE_SCHEMA.dataFile__data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.image__file_name = Slot(uri=BIOSTRIDE_SCHEMA.file_name, name="image__file_name", curie=BIOSTRIDE_SCHEMA.curie('file_name'),
                   model_uri=BIOSTRIDE_SCHEMA.image__file_name, domain=None, range=str)

slots.image__acquisition_date = Slot(uri=BIOSTRIDE_SCHEMA.acquisition_date, name="image__acquisition_date", curie=BIOSTRIDE_SCHEMA.curie('acquisition_date'),
                   model_uri=BIOSTRIDE_SCHEMA.image__acquisition_date, domain=None, range=Optional[str])

slots.image__pixel_size = Slot(uri=BIOSTRIDE_SCHEMA.pixel_size, name="image__pixel_size", curie=BIOSTRIDE_SCHEMA.curie('pixel_size'),
                   model_uri=BIOSTRIDE_SCHEMA.image__pixel_size, domain=None, range=Optional[float])

slots.image__dimensions_x = Slot(uri=BIOSTRIDE_SCHEMA.dimensions_x, name="image__dimensions_x", curie=BIOSTRIDE_SCHEMA.curie('dimensions_x'),
                   model_uri=BIOSTRIDE_SCHEMA.image__dimensions_x, domain=None, range=Optional[int])

slots.image__dimensions_y = Slot(uri=BIOSTRIDE_SCHEMA.dimensions_y, name="image__dimensions_y", curie=BIOSTRIDE_SCHEMA.curie('dimensions_y'),
                   model_uri=BIOSTRIDE_SCHEMA.image__dimensions_y, domain=None, range=Optional[int])

slots.image__exposure_time = Slot(uri=BIOSTRIDE_SCHEMA.exposure_time, name="image__exposure_time", curie=BIOSTRIDE_SCHEMA.curie('exposure_time'),
                   model_uri=BIOSTRIDE_SCHEMA.image__exposure_time, domain=None, range=Optional[float])

slots.image__dose = Slot(uri=BIOSTRIDE_SCHEMA.dose, name="image__dose", curie=BIOSTRIDE_SCHEMA.curie('dose'),
                   model_uri=BIOSTRIDE_SCHEMA.image__dose, domain=None, range=Optional[float])

slots.image2D__defocus = Slot(uri=BIOSTRIDE_SCHEMA.defocus, name="image2D__defocus", curie=BIOSTRIDE_SCHEMA.curie('defocus'),
                   model_uri=BIOSTRIDE_SCHEMA.image2D__defocus, domain=None, range=Optional[float])

slots.image2D__astigmatism = Slot(uri=BIOSTRIDE_SCHEMA.astigmatism, name="image2D__astigmatism", curie=BIOSTRIDE_SCHEMA.curie('astigmatism'),
                   model_uri=BIOSTRIDE_SCHEMA.image2D__astigmatism, domain=None, range=Optional[float])

slots.image3D__dimensions_z = Slot(uri=BIOSTRIDE_SCHEMA.dimensions_z, name="image3D__dimensions_z", curie=BIOSTRIDE_SCHEMA.curie('dimensions_z'),
                   model_uri=BIOSTRIDE_SCHEMA.image3D__dimensions_z, domain=None, range=Optional[int])

slots.image3D__voxel_size = Slot(uri=BIOSTRIDE_SCHEMA.voxel_size, name="image3D__voxel_size", curie=BIOSTRIDE_SCHEMA.curie('voxel_size'),
                   model_uri=BIOSTRIDE_SCHEMA.image3D__voxel_size, domain=None, range=Optional[float])

slots.image3D__reconstruction_method = Slot(uri=BIOSTRIDE_SCHEMA.reconstruction_method, name="image3D__reconstruction_method", curie=BIOSTRIDE_SCHEMA.curie('reconstruction_method'),
                   model_uri=BIOSTRIDE_SCHEMA.image3D__reconstruction_method, domain=None, range=Optional[str])

slots.fTIRImage__wavenumber_min = Slot(uri=BIOSTRIDE_SCHEMA.wavenumber_min, name="fTIRImage__wavenumber_min", curie=BIOSTRIDE_SCHEMA.curie('wavenumber_min'),
                   model_uri=BIOSTRIDE_SCHEMA.fTIRImage__wavenumber_min, domain=None, range=Optional[float])

slots.fTIRImage__wavenumber_max = Slot(uri=BIOSTRIDE_SCHEMA.wavenumber_max, name="fTIRImage__wavenumber_max", curie=BIOSTRIDE_SCHEMA.curie('wavenumber_max'),
                   model_uri=BIOSTRIDE_SCHEMA.fTIRImage__wavenumber_max, domain=None, range=Optional[float])

slots.fTIRImage__spectral_resolution = Slot(uri=BIOSTRIDE_SCHEMA.spectral_resolution, name="fTIRImage__spectral_resolution", curie=BIOSTRIDE_SCHEMA.curie('spectral_resolution'),
                   model_uri=BIOSTRIDE_SCHEMA.fTIRImage__spectral_resolution, domain=None, range=Optional[float])

slots.fTIRImage__number_of_scans = Slot(uri=BIOSTRIDE_SCHEMA.number_of_scans, name="fTIRImage__number_of_scans", curie=BIOSTRIDE_SCHEMA.curie('number_of_scans'),
                   model_uri=BIOSTRIDE_SCHEMA.fTIRImage__number_of_scans, domain=None, range=Optional[int])

slots.fTIRImage__apodization_function = Slot(uri=BIOSTRIDE_SCHEMA.apodization_function, name="fTIRImage__apodization_function", curie=BIOSTRIDE_SCHEMA.curie('apodization_function'),
                   model_uri=BIOSTRIDE_SCHEMA.fTIRImage__apodization_function, domain=None, range=Optional[str])

slots.fTIRImage__molecular_signatures = Slot(uri=BIOSTRIDE_SCHEMA.molecular_signatures, name="fTIRImage__molecular_signatures", curie=BIOSTRIDE_SCHEMA.curie('molecular_signatures'),
                   model_uri=BIOSTRIDE_SCHEMA.fTIRImage__molecular_signatures, domain=None, range=Optional[Union[str, list[str]]])

slots.fTIRImage__background_correction = Slot(uri=BIOSTRIDE_SCHEMA.background_correction, name="fTIRImage__background_correction", curie=BIOSTRIDE_SCHEMA.curie('background_correction'),
                   model_uri=BIOSTRIDE_SCHEMA.fTIRImage__background_correction, domain=None, range=Optional[str])

slots.fluorescenceImage__excitation_wavelength = Slot(uri=BIOSTRIDE_SCHEMA.excitation_wavelength, name="fluorescenceImage__excitation_wavelength", curie=BIOSTRIDE_SCHEMA.curie('excitation_wavelength'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__excitation_wavelength, domain=None, range=Optional[float])

slots.fluorescenceImage__emission_wavelength = Slot(uri=BIOSTRIDE_SCHEMA.emission_wavelength, name="fluorescenceImage__emission_wavelength", curie=BIOSTRIDE_SCHEMA.curie('emission_wavelength'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__emission_wavelength, domain=None, range=Optional[float])

slots.fluorescenceImage__excitation_filter = Slot(uri=BIOSTRIDE_SCHEMA.excitation_filter, name="fluorescenceImage__excitation_filter", curie=BIOSTRIDE_SCHEMA.curie('excitation_filter'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__excitation_filter, domain=None, range=Optional[str])

slots.fluorescenceImage__emission_filter = Slot(uri=BIOSTRIDE_SCHEMA.emission_filter, name="fluorescenceImage__emission_filter", curie=BIOSTRIDE_SCHEMA.curie('emission_filter'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__emission_filter, domain=None, range=Optional[str])

slots.fluorescenceImage__fluorophore = Slot(uri=BIOSTRIDE_SCHEMA.fluorophore, name="fluorescenceImage__fluorophore", curie=BIOSTRIDE_SCHEMA.curie('fluorophore'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__fluorophore, domain=None, range=Optional[str])

slots.fluorescenceImage__channel_name = Slot(uri=BIOSTRIDE_SCHEMA.channel_name, name="fluorescenceImage__channel_name", curie=BIOSTRIDE_SCHEMA.curie('channel_name'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__channel_name, domain=None, range=Optional[str])

slots.fluorescenceImage__laser_power = Slot(uri=BIOSTRIDE_SCHEMA.laser_power, name="fluorescenceImage__laser_power", curie=BIOSTRIDE_SCHEMA.curie('laser_power'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__laser_power, domain=None, range=Optional[float])

slots.fluorescenceImage__pinhole_size = Slot(uri=BIOSTRIDE_SCHEMA.pinhole_size, name="fluorescenceImage__pinhole_size", curie=BIOSTRIDE_SCHEMA.curie('pinhole_size'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__pinhole_size, domain=None, range=Optional[float])

slots.fluorescenceImage__quantum_yield = Slot(uri=BIOSTRIDE_SCHEMA.quantum_yield, name="fluorescenceImage__quantum_yield", curie=BIOSTRIDE_SCHEMA.curie('quantum_yield'),
                   model_uri=BIOSTRIDE_SCHEMA.fluorescenceImage__quantum_yield, domain=None, range=Optional[float])

slots.opticalImage__illumination_type = Slot(uri=BIOSTRIDE_SCHEMA.illumination_type, name="opticalImage__illumination_type", curie=BIOSTRIDE_SCHEMA.curie('illumination_type'),
                   model_uri=BIOSTRIDE_SCHEMA.opticalImage__illumination_type, domain=None, range=Optional[Union[str, "IlluminationTypeEnum"]])

slots.opticalImage__magnification = Slot(uri=BIOSTRIDE_SCHEMA.magnification, name="opticalImage__magnification", curie=BIOSTRIDE_SCHEMA.curie('magnification'),
                   model_uri=BIOSTRIDE_SCHEMA.opticalImage__magnification, domain=None, range=Optional[float])

slots.opticalImage__numerical_aperture = Slot(uri=BIOSTRIDE_SCHEMA.numerical_aperture, name="opticalImage__numerical_aperture", curie=BIOSTRIDE_SCHEMA.curie('numerical_aperture'),
                   model_uri=BIOSTRIDE_SCHEMA.opticalImage__numerical_aperture, domain=None, range=Optional[float])

slots.opticalImage__color_channels = Slot(uri=BIOSTRIDE_SCHEMA.color_channels, name="opticalImage__color_channels", curie=BIOSTRIDE_SCHEMA.curie('color_channels'),
                   model_uri=BIOSTRIDE_SCHEMA.opticalImage__color_channels, domain=None, range=Optional[Union[str, list[str]]])

slots.opticalImage__white_balance = Slot(uri=BIOSTRIDE_SCHEMA.white_balance, name="opticalImage__white_balance", curie=BIOSTRIDE_SCHEMA.curie('white_balance'),
                   model_uri=BIOSTRIDE_SCHEMA.opticalImage__white_balance, domain=None, range=Optional[str])

slots.opticalImage__contrast_method = Slot(uri=BIOSTRIDE_SCHEMA.contrast_method, name="opticalImage__contrast_method", curie=BIOSTRIDE_SCHEMA.curie('contrast_method'),
                   model_uri=BIOSTRIDE_SCHEMA.opticalImage__contrast_method, domain=None, range=Optional[str])

slots.xRFImage__beam_energy = Slot(uri=BIOSTRIDE_SCHEMA.beam_energy, name="xRFImage__beam_energy", curie=BIOSTRIDE_SCHEMA.curie('beam_energy'),
                   model_uri=BIOSTRIDE_SCHEMA.xRFImage__beam_energy, domain=None, range=Optional[float])

slots.xRFImage__beam_size = Slot(uri=BIOSTRIDE_SCHEMA.beam_size, name="xRFImage__beam_size", curie=BIOSTRIDE_SCHEMA.curie('beam_size'),
                   model_uri=BIOSTRIDE_SCHEMA.xRFImage__beam_size, domain=None, range=Optional[float])

slots.xRFImage__dwell_time = Slot(uri=BIOSTRIDE_SCHEMA.dwell_time, name="xRFImage__dwell_time", curie=BIOSTRIDE_SCHEMA.curie('dwell_time'),
                   model_uri=BIOSTRIDE_SCHEMA.xRFImage__dwell_time, domain=None, range=Optional[float])

slots.xRFImage__elements_measured = Slot(uri=BIOSTRIDE_SCHEMA.elements_measured, name="xRFImage__elements_measured", curie=BIOSTRIDE_SCHEMA.curie('elements_measured'),
                   model_uri=BIOSTRIDE_SCHEMA.xRFImage__elements_measured, domain=None, range=Optional[Union[str, list[str]]])

slots.xRFImage__source_type = Slot(uri=BIOSTRIDE_SCHEMA.source_type, name="xRFImage__source_type", curie=BIOSTRIDE_SCHEMA.curie('source_type'),
                   model_uri=BIOSTRIDE_SCHEMA.xRFImage__source_type, domain=None, range=Optional[Union[str, "XRaySourceTypeEnum"]])

slots.xRFImage__detector_type = Slot(uri=BIOSTRIDE_SCHEMA.detector_type, name="xRFImage__detector_type", curie=BIOSTRIDE_SCHEMA.curie('detector_type'),
                   model_uri=BIOSTRIDE_SCHEMA.xRFImage__detector_type, domain=None, range=Optional[str])

slots.xRFImage__flux = Slot(uri=BIOSTRIDE_SCHEMA.flux, name="xRFImage__flux", curie=BIOSTRIDE_SCHEMA.curie('flux'),
                   model_uri=BIOSTRIDE_SCHEMA.xRFImage__flux, domain=None, range=Optional[float])

slots.xRFImage__calibration_standard = Slot(uri=BIOSTRIDE_SCHEMA.calibration_standard, name="xRFImage__calibration_standard", curie=BIOSTRIDE_SCHEMA.curie('calibration_standard'),
                   model_uri=BIOSTRIDE_SCHEMA.xRFImage__calibration_standard, domain=None, range=Optional[str])

slots.imageFeature__terms = Slot(uri=BIOSTRIDE_SCHEMA.terms, name="imageFeature__terms", curie=BIOSTRIDE_SCHEMA.curie('terms'),
                   model_uri=BIOSTRIDE_SCHEMA.imageFeature__terms, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.ontologyTerm__label = Slot(uri=BIOSTRIDE_SCHEMA.label, name="ontologyTerm__label", curie=BIOSTRIDE_SCHEMA.curie('label'),
                   model_uri=BIOSTRIDE_SCHEMA.ontologyTerm__label, domain=None, range=Optional[str])

slots.ontologyTerm__definition = Slot(uri=BIOSTRIDE_SCHEMA.definition, name="ontologyTerm__definition", curie=BIOSTRIDE_SCHEMA.curie('definition'),
                   model_uri=BIOSTRIDE_SCHEMA.ontologyTerm__definition, domain=None, range=Optional[str])

slots.ontologyTerm__ontology = Slot(uri=BIOSTRIDE_SCHEMA.ontology, name="ontologyTerm__ontology", curie=BIOSTRIDE_SCHEMA.curie('ontology'),
                   model_uri=BIOSTRIDE_SCHEMA.ontologyTerm__ontology, domain=None, range=Optional[str])

slots.molecularComposition__sequences = Slot(uri=BIOSTRIDE_SCHEMA.sequences, name="molecularComposition__sequences", curie=BIOSTRIDE_SCHEMA.curie('sequences'),
                   model_uri=BIOSTRIDE_SCHEMA.molecularComposition__sequences, domain=None, range=Optional[Union[str, list[str]]])

slots.molecularComposition__modifications = Slot(uri=BIOSTRIDE_SCHEMA.modifications, name="molecularComposition__modifications", curie=BIOSTRIDE_SCHEMA.curie('modifications'),
                   model_uri=BIOSTRIDE_SCHEMA.molecularComposition__modifications, domain=None, range=Optional[Union[str, list[str]]])

slots.molecularComposition__ligands = Slot(uri=BIOSTRIDE_SCHEMA.ligands, name="molecularComposition__ligands", curie=BIOSTRIDE_SCHEMA.curie('ligands'),
                   model_uri=BIOSTRIDE_SCHEMA.molecularComposition__ligands, domain=None, range=Optional[Union[str, list[str]]])

slots.bufferComposition__ph = Slot(uri=BIOSTRIDE_SCHEMA.ph, name="bufferComposition__ph", curie=BIOSTRIDE_SCHEMA.curie('ph'),
                   model_uri=BIOSTRIDE_SCHEMA.bufferComposition__ph, domain=None, range=Optional[float])

slots.bufferComposition__components = Slot(uri=BIOSTRIDE_SCHEMA.components, name="bufferComposition__components", curie=BIOSTRIDE_SCHEMA.curie('components'),
                   model_uri=BIOSTRIDE_SCHEMA.bufferComposition__components, domain=None, range=Optional[Union[str, list[str]]])

slots.bufferComposition__additives = Slot(uri=BIOSTRIDE_SCHEMA.additives, name="bufferComposition__additives", curie=BIOSTRIDE_SCHEMA.curie('additives'),
                   model_uri=BIOSTRIDE_SCHEMA.bufferComposition__additives, domain=None, range=Optional[Union[str, list[str]]])

slots.storageConditions__temperature = Slot(uri=BIOSTRIDE_SCHEMA.temperature, name="storageConditions__temperature", curie=BIOSTRIDE_SCHEMA.curie('temperature'),
                   model_uri=BIOSTRIDE_SCHEMA.storageConditions__temperature, domain=None, range=Optional[float])

slots.storageConditions__temperature_unit = Slot(uri=BIOSTRIDE_SCHEMA.temperature_unit, name="storageConditions__temperature_unit", curie=BIOSTRIDE_SCHEMA.curie('temperature_unit'),
                   model_uri=BIOSTRIDE_SCHEMA.storageConditions__temperature_unit, domain=None, range=Optional[Union[str, "TemperatureUnitEnum"]])

slots.storageConditions__duration = Slot(uri=BIOSTRIDE_SCHEMA.duration, name="storageConditions__duration", curie=BIOSTRIDE_SCHEMA.curie('duration'),
                   model_uri=BIOSTRIDE_SCHEMA.storageConditions__duration, domain=None, range=Optional[str])

slots.storageConditions__atmosphere = Slot(uri=BIOSTRIDE_SCHEMA.atmosphere, name="storageConditions__atmosphere", curie=BIOSTRIDE_SCHEMA.curie('atmosphere'),
                   model_uri=BIOSTRIDE_SCHEMA.storageConditions__atmosphere, domain=None, range=Optional[str])

slots.cryoEMPreparation__grid_type = Slot(uri=BIOSTRIDE_SCHEMA.grid_type, name="cryoEMPreparation__grid_type", curie=BIOSTRIDE_SCHEMA.curie('grid_type'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__grid_type, domain=None, range=Optional[Union[str, "GridTypeEnum"]])

slots.cryoEMPreparation__support_film = Slot(uri=BIOSTRIDE_SCHEMA.support_film, name="cryoEMPreparation__support_film", curie=BIOSTRIDE_SCHEMA.curie('support_film'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__support_film, domain=None, range=Optional[str])

slots.cryoEMPreparation__hole_size = Slot(uri=BIOSTRIDE_SCHEMA.hole_size, name="cryoEMPreparation__hole_size", curie=BIOSTRIDE_SCHEMA.curie('hole_size'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__hole_size, domain=None, range=Optional[float])

slots.cryoEMPreparation__vitrification_method = Slot(uri=BIOSTRIDE_SCHEMA.vitrification_method, name="cryoEMPreparation__vitrification_method", curie=BIOSTRIDE_SCHEMA.curie('vitrification_method'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__vitrification_method, domain=None, range=Optional[Union[str, "VitrificationMethodEnum"]])

slots.cryoEMPreparation__blot_time = Slot(uri=BIOSTRIDE_SCHEMA.blot_time, name="cryoEMPreparation__blot_time", curie=BIOSTRIDE_SCHEMA.curie('blot_time'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__blot_time, domain=None, range=Optional[float])

slots.cryoEMPreparation__blot_force = Slot(uri=BIOSTRIDE_SCHEMA.blot_force, name="cryoEMPreparation__blot_force", curie=BIOSTRIDE_SCHEMA.curie('blot_force'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__blot_force, domain=None, range=Optional[int])

slots.cryoEMPreparation__humidity_percentage = Slot(uri=BIOSTRIDE_SCHEMA.humidity_percentage, name="cryoEMPreparation__humidity_percentage", curie=BIOSTRIDE_SCHEMA.curie('humidity_percentage'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__humidity_percentage, domain=None, range=Optional[float])

slots.cryoEMPreparation__chamber_temperature = Slot(uri=BIOSTRIDE_SCHEMA.chamber_temperature, name="cryoEMPreparation__chamber_temperature", curie=BIOSTRIDE_SCHEMA.curie('chamber_temperature'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__chamber_temperature, domain=None, range=Optional[float])

slots.cryoEMPreparation__plasma_treatment = Slot(uri=BIOSTRIDE_SCHEMA.plasma_treatment, name="cryoEMPreparation__plasma_treatment", curie=BIOSTRIDE_SCHEMA.curie('plasma_treatment'),
                   model_uri=BIOSTRIDE_SCHEMA.cryoEMPreparation__plasma_treatment, domain=None, range=Optional[str])

slots.xRayPreparation__crystallization_method = Slot(uri=BIOSTRIDE_SCHEMA.crystallization_method, name="xRayPreparation__crystallization_method", curie=BIOSTRIDE_SCHEMA.curie('crystallization_method'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayPreparation__crystallization_method, domain=None, range=Optional[Union[str, "CrystallizationMethodEnum"]])

slots.xRayPreparation__crystallization_conditions = Slot(uri=BIOSTRIDE_SCHEMA.crystallization_conditions, name="xRayPreparation__crystallization_conditions", curie=BIOSTRIDE_SCHEMA.curie('crystallization_conditions'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayPreparation__crystallization_conditions, domain=None, range=Optional[str])

slots.xRayPreparation__crystal_size = Slot(uri=BIOSTRIDE_SCHEMA.crystal_size, name="xRayPreparation__crystal_size", curie=BIOSTRIDE_SCHEMA.curie('crystal_size'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayPreparation__crystal_size, domain=None, range=Optional[str])

slots.xRayPreparation__cryoprotectant = Slot(uri=BIOSTRIDE_SCHEMA.cryoprotectant, name="xRayPreparation__cryoprotectant", curie=BIOSTRIDE_SCHEMA.curie('cryoprotectant'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayPreparation__cryoprotectant, domain=None, range=Optional[str])

slots.xRayPreparation__cryoprotectant_concentration = Slot(uri=BIOSTRIDE_SCHEMA.cryoprotectant_concentration, name="xRayPreparation__cryoprotectant_concentration", curie=BIOSTRIDE_SCHEMA.curie('cryoprotectant_concentration'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayPreparation__cryoprotectant_concentration, domain=None, range=Optional[float])

slots.xRayPreparation__mounting_method = Slot(uri=BIOSTRIDE_SCHEMA.mounting_method, name="xRayPreparation__mounting_method", curie=BIOSTRIDE_SCHEMA.curie('mounting_method'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayPreparation__mounting_method, domain=None, range=Optional[str])

slots.xRayPreparation__flash_cooling_method = Slot(uri=BIOSTRIDE_SCHEMA.flash_cooling_method, name="xRayPreparation__flash_cooling_method", curie=BIOSTRIDE_SCHEMA.curie('flash_cooling_method'),
                   model_uri=BIOSTRIDE_SCHEMA.xRayPreparation__flash_cooling_method, domain=None, range=Optional[str])

slots.sAXSPreparation__concentration_series = Slot(uri=BIOSTRIDE_SCHEMA.concentration_series, name="sAXSPreparation__concentration_series", curie=BIOSTRIDE_SCHEMA.curie('concentration_series'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSPreparation__concentration_series, domain=None, range=Optional[Union[float, list[float]]])

slots.sAXSPreparation__buffer_matching_protocol = Slot(uri=BIOSTRIDE_SCHEMA.buffer_matching_protocol, name="sAXSPreparation__buffer_matching_protocol", curie=BIOSTRIDE_SCHEMA.curie('buffer_matching_protocol'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSPreparation__buffer_matching_protocol, domain=None, range=Optional[str])

slots.sAXSPreparation__sample_cell_type = Slot(uri=BIOSTRIDE_SCHEMA.sample_cell_type, name="sAXSPreparation__sample_cell_type", curie=BIOSTRIDE_SCHEMA.curie('sample_cell_type'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSPreparation__sample_cell_type, domain=None, range=Optional[str])

slots.sAXSPreparation__cell_path_length = Slot(uri=BIOSTRIDE_SCHEMA.cell_path_length, name="sAXSPreparation__cell_path_length", curie=BIOSTRIDE_SCHEMA.curie('cell_path_length'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSPreparation__cell_path_length, domain=None, range=Optional[float])

slots.sAXSPreparation__temperature_control = Slot(uri=BIOSTRIDE_SCHEMA.temperature_control, name="sAXSPreparation__temperature_control", curie=BIOSTRIDE_SCHEMA.curie('temperature_control'),
                   model_uri=BIOSTRIDE_SCHEMA.sAXSPreparation__temperature_control, domain=None, range=Optional[str])

slots.experimentalConditions__temperature = Slot(uri=BIOSTRIDE_SCHEMA.temperature, name="experimentalConditions__temperature", curie=BIOSTRIDE_SCHEMA.curie('temperature'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentalConditions__temperature, domain=None, range=Optional[float])

slots.experimentalConditions__humidity = Slot(uri=BIOSTRIDE_SCHEMA.humidity, name="experimentalConditions__humidity", curie=BIOSTRIDE_SCHEMA.curie('humidity'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentalConditions__humidity, domain=None, range=Optional[float])

slots.experimentalConditions__pressure = Slot(uri=BIOSTRIDE_SCHEMA.pressure, name="experimentalConditions__pressure", curie=BIOSTRIDE_SCHEMA.curie('pressure'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentalConditions__pressure, domain=None, range=Optional[float])

slots.experimentalConditions__atmosphere = Slot(uri=BIOSTRIDE_SCHEMA.atmosphere, name="experimentalConditions__atmosphere", curie=BIOSTRIDE_SCHEMA.curie('atmosphere'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentalConditions__atmosphere, domain=None, range=Optional[str])

slots.experimentalConditions__beam_energy = Slot(uri=BIOSTRIDE_SCHEMA.beam_energy, name="experimentalConditions__beam_energy", curie=BIOSTRIDE_SCHEMA.curie('beam_energy'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentalConditions__beam_energy, domain=None, range=Optional[float])

slots.experimentalConditions__exposure_time = Slot(uri=BIOSTRIDE_SCHEMA.exposure_time, name="experimentalConditions__exposure_time", curie=BIOSTRIDE_SCHEMA.curie('exposure_time'),
                   model_uri=BIOSTRIDE_SCHEMA.experimentalConditions__exposure_time, domain=None, range=Optional[float])

slots.dataCollectionStrategy__collection_mode = Slot(uri=BIOSTRIDE_SCHEMA.collection_mode, name="dataCollectionStrategy__collection_mode", curie=BIOSTRIDE_SCHEMA.curie('collection_mode'),
                   model_uri=BIOSTRIDE_SCHEMA.dataCollectionStrategy__collection_mode, domain=None, range=Optional[Union[str, "CollectionModeEnum"]])

slots.dataCollectionStrategy__total_frames = Slot(uri=BIOSTRIDE_SCHEMA.total_frames, name="dataCollectionStrategy__total_frames", curie=BIOSTRIDE_SCHEMA.curie('total_frames'),
                   model_uri=BIOSTRIDE_SCHEMA.dataCollectionStrategy__total_frames, domain=None, range=Optional[int])

slots.dataCollectionStrategy__frame_rate = Slot(uri=BIOSTRIDE_SCHEMA.frame_rate, name="dataCollectionStrategy__frame_rate", curie=BIOSTRIDE_SCHEMA.curie('frame_rate'),
                   model_uri=BIOSTRIDE_SCHEMA.dataCollectionStrategy__frame_rate, domain=None, range=Optional[float])

slots.dataCollectionStrategy__total_dose = Slot(uri=BIOSTRIDE_SCHEMA.total_dose, name="dataCollectionStrategy__total_dose", curie=BIOSTRIDE_SCHEMA.curie('total_dose'),
                   model_uri=BIOSTRIDE_SCHEMA.dataCollectionStrategy__total_dose, domain=None, range=Optional[float])

slots.dataCollectionStrategy__dose_per_frame = Slot(uri=BIOSTRIDE_SCHEMA.dose_per_frame, name="dataCollectionStrategy__dose_per_frame", curie=BIOSTRIDE_SCHEMA.curie('dose_per_frame'),
                   model_uri=BIOSTRIDE_SCHEMA.dataCollectionStrategy__dose_per_frame, domain=None, range=Optional[float])

slots.qualityMetrics__resolution = Slot(uri=BIOSTRIDE_SCHEMA.resolution, name="qualityMetrics__resolution", curie=BIOSTRIDE_SCHEMA.curie('resolution'),
                   model_uri=BIOSTRIDE_SCHEMA.qualityMetrics__resolution, domain=None, range=Optional[float])

slots.qualityMetrics__completeness = Slot(uri=BIOSTRIDE_SCHEMA.completeness, name="qualityMetrics__completeness", curie=BIOSTRIDE_SCHEMA.curie('completeness'),
                   model_uri=BIOSTRIDE_SCHEMA.qualityMetrics__completeness, domain=None, range=Optional[float])

slots.qualityMetrics__signal_to_noise = Slot(uri=BIOSTRIDE_SCHEMA.signal_to_noise, name="qualityMetrics__signal_to_noise", curie=BIOSTRIDE_SCHEMA.curie('signal_to_noise'),
                   model_uri=BIOSTRIDE_SCHEMA.qualityMetrics__signal_to_noise, domain=None, range=Optional[float])

slots.qualityMetrics__r_factor = Slot(uri=BIOSTRIDE_SCHEMA.r_factor, name="qualityMetrics__r_factor", curie=BIOSTRIDE_SCHEMA.curie('r_factor'),
                   model_uri=BIOSTRIDE_SCHEMA.qualityMetrics__r_factor, domain=None, range=Optional[float])

slots.qualityMetrics__i_zero = Slot(uri=BIOSTRIDE_SCHEMA.i_zero, name="qualityMetrics__i_zero", curie=BIOSTRIDE_SCHEMA.curie('i_zero'),
                   model_uri=BIOSTRIDE_SCHEMA.qualityMetrics__i_zero, domain=None, range=Optional[float])

slots.qualityMetrics__rg = Slot(uri=BIOSTRIDE_SCHEMA.rg, name="qualityMetrics__rg", curie=BIOSTRIDE_SCHEMA.curie('rg'),
                   model_uri=BIOSTRIDE_SCHEMA.qualityMetrics__rg, domain=None, range=Optional[float])

slots.computeResources__cpu_hours = Slot(uri=BIOSTRIDE_SCHEMA.cpu_hours, name="computeResources__cpu_hours", curie=BIOSTRIDE_SCHEMA.curie('cpu_hours'),
                   model_uri=BIOSTRIDE_SCHEMA.computeResources__cpu_hours, domain=None, range=Optional[float])

slots.computeResources__gpu_hours = Slot(uri=BIOSTRIDE_SCHEMA.gpu_hours, name="computeResources__gpu_hours", curie=BIOSTRIDE_SCHEMA.curie('gpu_hours'),
                   model_uri=BIOSTRIDE_SCHEMA.computeResources__gpu_hours, domain=None, range=Optional[float])

slots.computeResources__memory_gb = Slot(uri=BIOSTRIDE_SCHEMA.memory_gb, name="computeResources__memory_gb", curie=BIOSTRIDE_SCHEMA.curie('memory_gb'),
                   model_uri=BIOSTRIDE_SCHEMA.computeResources__memory_gb, domain=None, range=Optional[float])

slots.computeResources__storage_gb = Slot(uri=BIOSTRIDE_SCHEMA.storage_gb, name="computeResources__storage_gb", curie=BIOSTRIDE_SCHEMA.curie('storage_gb'),
                   model_uri=BIOSTRIDE_SCHEMA.computeResources__storage_gb, domain=None, range=Optional[float])
