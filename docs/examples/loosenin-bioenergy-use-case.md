# Fungal Loosenins for Bioenergy Applications - Use Case Example

## Overview

This example demonstrates how BioStride can capture complex, multi-technique structural biology studies focused on bioenergy applications. The study investigates fungal loosenins - proteins that reduce biomass recalcitrance by enhancing accessibility to plant cell wall carbohydrates.

## Scientific Context

Fungal loosenins are related to plant expansins and play a crucial role in making lignocellulosic biomass more accessible for biofuel production. This example is based on the collaborative research described in the use case:

> "Plant cell wall remodeling for bioenergy and biofuel production. Fungal loosenins are a class of proteins related to plant expansins that reduce biomass recalcitrance by enhancing accessibility to carbohydrate components of the plant cell wall."

The study builds on successful characterization of PcaLOOL12 (https://doi.org/10.1186/s13068-025-02618-5) and expands to investigate:
- Multiple loosenin variants under physiologically relevant conditions
- pH-dependent conformational changes
- Protein-cellulose binding mechanisms
- Plant cell wall remodeling dynamics

## Multi-Facility Integration

This example showcases integration across multiple DOE facilities:
- **Advanced Light Source (ALS)**: SAXS/WAXS and crystallography beamlines
- **NSLS-II**: LiX beamline for additional SAXS measurements
- **SNS/HFIR**: Bio-SANS for neutron scattering with contrast matching
- **Berkeley Lab**: Cryo-EM facility for high-resolution imaging
- **EMSL**: NMR facility (referenced but not detailed in this example)
- **JGI**: Gene synthesis (referenced but not detailed in this example)

## Techniques Demonstrated

The example includes comprehensive coverage of structural biology techniques:

1. **SAXS (Small-Angle X-ray Scattering)**
   - pH titration series to study conformational flexibility
   - Time-resolved measurements of cell wall structural changes

2. **SANS (Small-Angle Neutron Scattering)**
   - Contrast matching to visualize protein binding on cellulose
   - Selective deuteration strategies

3. **X-ray Crystallography**
   - High-resolution (1.8Å) structure determination
   - Molecular replacement phasing

4. **Cryo-EM**
   - Single particle analysis of protein-cellulose complexes
   - 3.2Å reconstruction revealing binding interfaces

5. **Integrative Modeling**
   - IMP-based integration of multiple data sources
   - Dynamic binding mechanism elucidation

## Data Structure Highlights

### Sample Tracking
- Multiple protein constructs (PcaLOOL12, TrLOOL1)
- Protein-substrate complexes
- Plant cell wall samples (poplar, switchgrass)
- Detailed molecular composition including sequences, modifications, and ligands

### Experimental Workflows
- Complete processing pipelines from raw data to refined structures
- Software tracking (ATSAS, PHENIX, RELION, IMP)
- Processing levels indicating data maturity

### Data Management
- File organization across techniques
- Size tracking for large datasets (125GB particle stacks)
- Standard format specification (mtz, star, mrc, pdb)

### Biological Context
The example preserves rich biological context through:
- Protein sequences
- Post-translational modifications (glycosylation sites)
- Buffer conditions and pH variations
- Storage conditions
- Ligand interactions

## File Location

The complete YAML example is located at:
`tests/data/valid/Dataset-loosenin-bioenergy.yaml`

## Key Features Demonstrated

1. **Multi-scale approach**: From atomic resolution (crystallography) to mesoscale (SAXS/SANS) to cellular (cell wall imaging)
2. **Integrative methodology**: Combining complementary techniques for comprehensive understanding
3. **Dynamic studies**: pH-dependent conformational changes and time-resolved measurements
4. **Complex samples**: Pure proteins, protein-substrate complexes, and tissue samples
5. **Industrial relevance**: Direct application to bioenergy and sustainable fuel production

## Usage

This example can be used as a template for:
- Multi-technique structural biology studies
- Bioenergy-related protein investigations
- Integrative modeling projects
- Cross-facility collaborative research
- Studies involving protein-carbohydrate interactions

## Validation

The example validates successfully against the BioStride schema:
```bash
uv run linkml-validate -s src/biostride/schema/biostride.yaml tests/data/valid/Dataset-loosenin-bioenergy.yaml
```