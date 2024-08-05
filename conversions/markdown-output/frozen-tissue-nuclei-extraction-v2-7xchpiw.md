```markdown
# Goal/Experiment:
Extraction of nuclei from frozen tissue for single-nuclei sequencing, employing droplet-based/10X technology.

# Frozen Tissue Nuclei Extraction (v2)

**Authors**: Carly Martin¹, Abdul Abdul¹, Charles Vanderburg¹, Naeem Nadaf¹, Ashley Feirrera¹, Evan Macosko¹  
**Affiliation**: ¹Broad Institute  
**Date**: Oct 08, 2019  
**Link**: [dx.doi.org/10.17504/protocols.io.7xchpiw](https://dx.doi.org/10.17504/protocols.io.7xchpiw)  
**Reviewer**: Velina Kozareva

**Abstract**  
Protocol for extraction of nuclei from frozen tissue in preparation for single-nuclei sequencing (droplet-based/10X).

This protocol is based strongly on a similar extraction protocol from the [McCarroll lab](https://mccarrolllab.org/).

### Materials and Reagents

**Disassociation Buffer**
Below are the components and preparation details:

| Reagent                | MW      | Concentration (mM) | For 1L (g or mL) | For 2L (g or mL) |
|------------------------|---------|--------------------|------------------|------------------|
| Na₂SO₄ (Sodium Sulfate)  | 142.04 | 82                 | 11.65            | 23.3             |
| K₂SO₄ (Potassium Sulfate)| 174.26 | 30                 | 5.23             | 10.46            |
| Glucose                | 180.2   | 10                 | 1.81             | 3.62             |
| HEPES                  | 238.3   | 10                 | 2.39             | 4.78             |
| MgCl₂·6H₂O             | 203.31  | 5                  | 5 mL (1M stock)  | 10 mL (1M stock) |

**Disassociation Buffer + Extraction Additives**
- Dissociation Buffer
- 1% Kollidon VA64
- 1% Triton X100
- 1:40 RNase-inhibitor

### Protocol Steps

1. **Make Disassociation Buffer**
   Prepare 50 mLs per sample:
   Combine the reagents as specified in the table above.
   
2. **Prepare Extraction Buffer**
   Prepare 3 mLs per sample:
   Combine the disassociation buffer with 1% Kollidon VA64, 1% Triton X100, and 1:40 RNase-inhibitor.
   
3. **Chill Buffers**
   - Chill all buffers to 4°C and maintain on ice when in use.

4. **Prepare Equipment**
   - Cold block dissecting tray, maintained at -20°C.
   - Chilled clean razor blades and glass slides.
   - 3 mL syringe with a 26 1/2 gauge needle, chilled to 4°C.
   - 12-well tissue-culture plate with well-bottoms colored with a marker, placed on ice.
   - Place 2 mL of chilled extraction buffer in the first well.
   - Falcon tube with ~50 mL chilled DB (Dissociation Buffer).
   - DAPI (1:1000) (diluted from [ThermoFisher D1306](https://www.thermofisher.com/order/catalog/product/D1306)).
   - 50 µm Eppendorf tube filter, chilled to 4°C (available [here](https://us.sysmex-flowcytometry.com/consumables/celltrics-filters/1445/sterile-single-pack-celltrics-filters-50)).
   - Two 50 mL tubes placed on ice.
   - c-Chip FR hemocytometer.

5. **Collect Supplies for FACS**
   - 96-well cold block, chilled to -20°C ([Eppendorf](https://www.daigger.com/eppendorf-pcr-coolers-14616-group)).
   - 200 µL 5% BSA-DB.
   - 20 µL collection buffer: DB with 1:40 RNase-inhibitor (prepare immediately before FACS session).

6. **Begin Extraction (All Steps with Cold Buffers on Ice)**
   - Chop the tissue on ice, place it immediately into the extraction buffer.
   - Shave the frozen sample on the glass slide, removing excess frost/damaged tissue. Prepare 2 mL cold extraction buffer by pipetting up and down 20 times.

7. **Detergent Incubation and Trituration**
   - Perform mechanical trituration by pipetting up and down 20 times with a 1000 µL pipette approximately every 2.5 minutes over a 10-minute incubation period.

8. **Mechanical Dissociation**
   - Use the chilled needle/syringe to express the sample for final mechanical dissociation. Repeat if necessary.

9. **Large Volume Wash**
   - Extract nuclei into an empty 30 mL tube, add chilled DB to ~30 mL total volume.

10. **Split Sample**
    - Divide the nuclei into two 50 mL conical tubes (~15 mL each).

11. **Centrifuge**
    - Spin at 600 rcf in a swinging bucket centrifuge for 10 minutes at 4°C.

12. **Remove Supernatant**
    - Carefully aspirate ~13 mL wash buffer with a serological pipette, avoid disturbing the pellet. Leave 500-300 µL in the bottom. Resuspend the nuclei carefully.

13. **Filter Nuclei Clumps**
    - Use a 40 µm eppendorf tube filter to filter the nuclei sample into an epi tube.

14. **Stain DNA**
    - Add 1 µL DAPI to 1 mL nuclei sample, incubate and place the nuclei into a FR hemocytometer to check concentration and quality.

15. **FACS Enrichment for Single Nuclei**
    - Use a 70 µm chip on a Sony SH800 sorter with specific settings.

16. **Prepare Collection PCR Tubes**
    - Coat PCR tube walls with 5% BSA-DB, wash with 200 µL DB, and add 20 µL collection buffer.
    - FACS into the tube using a 1% FSC threshold on the DAPI peak.

17. **Calculate Nuclei Concentration**
    - Create a 1:10 dilution and count nuclei using a hemocytometer. Multiply average by 10 (dilution factor) and then by 5 (hemocytometer factor) to get the concentration in nuclei/µL.

18. **Preparation for 10X Sequencing**
    - Maximum 17000 nuclei, with post-loss input of 10000. Max conc. for 10X v3: 364 n/µL; input vol.: 46.6 µL.

### endofoutput
```