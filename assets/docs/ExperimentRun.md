
# Class: ExperimentRun

An experimental data collection session

URI: [biostride_schema:ExperimentRun](https://w3id.org/biostride/schema/ExperimentRun)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QualityMetrics],[NamedThing],[Instrument],[ExperimentalConditions],[QualityMetrics]<quality_metrics%200..1-++[ExperimentRun&#124;experiment_code:string;sample_id:string;experiment_date:string%20%3F;operator_id:string%20%3F;technique:TechniqueEnum;raw_data_location:string%20%3F;processing_status:ProcessingStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[DataCollectionStrategy]<data_collection_strategy%200..1-++[ExperimentRun],[ExperimentalConditions]<experimental_conditions%200..1-++[ExperimentRun],[Instrument]<instrument_id%201..1-%20[ExperimentRun],[Study]++-%20instrument_runs%200..*>[ExperimentRun],[NamedThing]^-[ExperimentRun],[Study],[DataCollectionStrategy])](https://yuml.me/diagram/nofunky;dir:TB/class/[QualityMetrics],[NamedThing],[Instrument],[ExperimentalConditions],[QualityMetrics]<quality_metrics%200..1-++[ExperimentRun&#124;experiment_code:string;sample_id:string;experiment_date:string%20%3F;operator_id:string%20%3F;technique:TechniqueEnum;raw_data_location:string%20%3F;processing_status:ProcessingStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[DataCollectionStrategy]<data_collection_strategy%200..1-++[ExperimentRun],[ExperimentalConditions]<experimental_conditions%200..1-++[ExperimentRun],[Instrument]<instrument_id%201..1-%20[ExperimentRun],[Study]++-%20instrument_runs%200..*>[ExperimentRun],[NamedThing]^-[ExperimentRun],[Study],[DataCollectionStrategy])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞instrument_runs](study__instrument_runs.md)*  <sub>0..\*</sub>  **[ExperimentRun](ExperimentRun.md)**

## Attributes


### Own

 * [➞experiment_code](experimentRun__experiment_code.md)  <sub>1..1</sub>
     * Description: Human-friendly laboratory or facility identifier for the experiment (e.g., 'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and cross-referencing within laboratory systems.
     * Range: [String](types/String.md)
 * [➞sample_id](experimentRun__sample_id.md)  <sub>1..1</sub>
     * Description: Reference to the sample being analyzed
     * Range: [String](types/String.md)
 * [➞instrument_id](experimentRun__instrument_id.md)  <sub>1..1</sub>
     * Description: Reference to the instrument used
     * Range: [Instrument](Instrument.md)
 * [➞experiment_date](experimentRun__experiment_date.md)  <sub>0..1</sub>
     * Description: Date of the experiment
     * Range: [String](types/String.md)
 * [➞operator_id](experimentRun__operator_id.md)  <sub>0..1</sub>
     * Description: Person who performed the experiment
     * Range: [String](types/String.md)
 * [➞technique](experimentRun__technique.md)  <sub>1..1</sub>
     * Description: Technique used for data collection
     * Range: [TechniqueEnum](TechniqueEnum.md)
 * [➞experimental_conditions](experimentRun__experimental_conditions.md)  <sub>0..1</sub>
     * Description: Environmental and experimental conditions
     * Range: [ExperimentalConditions](ExperimentalConditions.md)
 * [➞data_collection_strategy](experimentRun__data_collection_strategy.md)  <sub>0..1</sub>
     * Description: Strategy for data collection
     * Range: [DataCollectionStrategy](DataCollectionStrategy.md)
 * [➞quality_metrics](experimentRun__quality_metrics.md)  <sub>0..1</sub>
     * Description: Quality metrics for the experiment
     * Range: [QualityMetrics](QualityMetrics.md)
 * [➞raw_data_location](experimentRun__raw_data_location.md)  <sub>0..1</sub>
     * Description: Location of raw data files
     * Range: [String](types/String.md)
 * [➞processing_status](experimentRun__processing_status.md)  <sub>0..1</sub>
     * Description: Current processing status
     * Range: [ProcessingStatusEnum](ProcessingStatusEnum.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
