
# Class: DataCollectionStrategy

Strategy for data collection

URI: [biostride_schema:DataCollectionStrategy](https://w3id.org/biostride/schema/DataCollectionStrategy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20data_collection_strategy%200..1>[DataCollectionStrategy&#124;collection_mode:CollectionModeEnum%20%3F;total_frames:integer%20%3F;frame_rate:float%20%3F;total_dose:float%20%3F;dose_per_frame:float%20%3F],[ExperimentRun])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20data_collection_strategy%200..1>[DataCollectionStrategy&#124;collection_mode:CollectionModeEnum%20%3F;total_frames:integer%20%3F;frame_rate:float%20%3F;total_dose:float%20%3F;dose_per_frame:float%20%3F],[ExperimentRun])

## Referenced by Class

 *  **None** *[➞data_collection_strategy](experimentRun__data_collection_strategy.md)*  <sub>0..1</sub>  **[DataCollectionStrategy](DataCollectionStrategy.md)**

## Attributes


### Own

 * [➞collection_mode](dataCollectionStrategy__collection_mode.md)  <sub>0..1</sub>
     * Description: Mode of data collection
     * Range: [CollectionModeEnum](CollectionModeEnum.md)
 * [➞total_frames](dataCollectionStrategy__total_frames.md)  <sub>0..1</sub>
     * Description: Total number of frames/images
     * Range: [Integer](types/Integer.md)
 * [➞frame_rate](dataCollectionStrategy__frame_rate.md)  <sub>0..1</sub>
     * Description: Frames per second
     * Range: [Float](types/Float.md)
 * [➞total_dose](dataCollectionStrategy__total_dose.md)  <sub>0..1</sub>
     * Description: Total electron dose for cryo-EM
     * Range: [Float](types/Float.md)
 * [➞dose_per_frame](dataCollectionStrategy__dose_per_frame.md)  <sub>0..1</sub>
     * Description: Dose per frame
     * Range: [Float](types/Float.md)
