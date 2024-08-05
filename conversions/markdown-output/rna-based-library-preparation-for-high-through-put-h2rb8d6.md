```markdown
# RNA Based Library Preparation for High Throughput Full-Length Small Ribosomal RNA Sequencing on the Illumina MiSeq and HiSeq Platforms

## Goal/Experiment
The objective of this experiment is to prepare Illumina libraries for high throughput sequencing of full-length SSU rRNA sequences from all domains of life without primer bias.

### Abstract
This protocol describes the preparation of Illumina libraries for high-throughput sequencing of full-length SSU rRNA sequences from all domains of life without primer bias. Sequences for primers and adaptors used can be found under guidelines.

Citation: Søren M. Karst, Morten S. Dueholm, Simon J. McIlroy, Rasmus H. Kirkegaard, Per H. Nielsen, Mads Albertsen  
Published: 01 Jun 2017  
dx.doi.org/10.17504/protocols.io.h2rb8d6

---

## Guidelines

### Primers and Adaptors Used for Library Preparation

| Oligo Name        | Sequence                                                                                         | Purification |
|--------------------|--------------------------------------------------------------------------------------------------|--------------|
| SSU_rRNA_RT1       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNNNNGTCGCTAACTGCGCTGGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT2       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNNNATGAGACGTTCGCTGGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT3       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNNNTCGTCACGCTGGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT4       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNNNGCTGAGAACGTTCGCTGGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT5       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNNAGAGGACGCTGGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT6       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNnGACTGACGCTGGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT7       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNNNATGAGACGTTCGTCCTGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT8       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNNCTTGCTGGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT9       | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNAGCCGTGAGGTCCTGTCCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_RT10      | AGGGGGGAAAGGTAGAATNNNNNNNNNNNNNNNAGCCTGGACCTGCTCGTATCATTCTTFFFFFFFFFFFFFFTTVVVN             | PAGE         |
| SSU_rRNA_S         | /5Phos/GGGAACTTAGTCCACAACAAAGAA/spC3/                                                        | HPLC         |
| SSU_rRNA_I         | TCCACGCATCTCTTCPNNNNNNNNNNNNNNNATAGGCTTCTTGGTGTGGTGAATTGC                                    | PAGE         |
| SSU_rRNA_pcr_fw    | GGGCGGAAAGATGAAGAT                                                                        | HPLC         |
| SSU_rRNA_pcr_rv    | TCCACAACAAAGAAAGAAATTAT                                                                 | HPLC         |
| SSU_rRNA_readtag_fw| CAAGGAAAGGACACGTCTGAACTGATGTACGAACGGAGTGGCTGCTCGTCTCTGCTCTCGAAGGCGGGGAAGAATGAAGAT             | PAGE         |
| SSU_rRNA_readtag_rv| CAAGGAAAGGACACGTCTGAACTGATGTACGAAGTGAACGGCTCGTTCTTCGGCTCCAGTCATCGCTGGAGT ACAGGACGCTGTACAAT        | PAGE         |
| SSU_rRNA_linktag_fw | AGTAGATCTGCAAGGTAGAATGTAGCTGCCCCTGCTCTGCTCTCACTCCC                                                            | PAGE         |
| SSU_rRNA_linktag_rv | AATAGATCTGCAACCACATGATTTACCTTGCTGTGCCTTCTGCAAGTGCTTCTGGAGTGCAGTAGCC                                                           | PAGE         |
| SSU_rRNA_read2_fw   | GCTCTTCGCTACTGGGGAGGAAGAGAAAGAAAAGATGAA                                                              | PAGE         |
| SSU_rRNA_read2_rv   | GGTTGTGTTCTTGGTTCTGCAATCAC                                                                | HPLC         |

### Protocol

#### SSU rRNA Size Selection

##### Step 1
Dilute the RNA to 40 ng/µL with nuclease-free water and transfer 25 µL to a 200 µL PCR tube.

##### Step 2
Heat denature the RNA at 70°C for 5 min. Snap cool the sample on an ice block for 2 min to prevent RNA from refolding. Immediately proceed to the next step.

##### Step 3
Isolate the SSU rRNA from total RNA by size selection on an E-gel electrophoresis system with a precast E-Gel CloneWell gel (Thermo Fisher Scientific):

* Use 20 µL of the heat-denatured RNA (800 ng total RNA).
* Use 500 ng GeneRuler 1 kB DNA ladder (Thermo Fisher Scientific) as a reference.
* Run the gel until the SSU peak (ca. 1,500 bp) is approximately 1 mm from the elution well.
* Now collect 20 µL elution aliquots every 15 seconds, up to a total of 16 aliquots, and the visible passing of the SSU rRNA peak.
* Pool every two aliquots to obtain 8 pooled aliquots per sample.

##### Step 4
Analyze the pooled aliquots on an Agilent 2200 Tapestation with the High Sensitivity RNA Screen tape and pool the aliquots that contain SSU rRNA.

##### Step 5
Purify the sample using RNAClean XP beads:

* Perform purification in a 2 mL Eppendorf tube.
* Use 1.0× beads.
* Wash 2× with freshly prepared 80% ethanol.
* Elute in 32 µL nuclease-free water.

#### Poly(A) Tailing of SSU rRNA

##### Step 6
Prepare the poly(A) tailing reaction in a 200 µL PCR tube:

* 30 µL sample from above (10-200 ng SSU rRNA).
* 4 µL 10× E. coli Poly(A) Polymerase Reaction Buffer (New England Biolabs).
* 4 µL 10 mM ATP (New England Biolabs).
* 1.5 µL E. coli Poly(A) Polymerase (New England Biolabs).
* 1 µL RiboLock RNase Inhibitor (Thermo Fisher Scientific).

##### Step 7
Perform polyadenylation at 37°C for 30 min.

##### Step 8
Purify the sample using RNAClean XP beads:

* Perform purification in a 2 mL Eppendorf tube.
* Use 1.0× beads.
* Wash 2× with freshly prepared 80% ethanol.
* Elude in 15 µL nuclease-free water.

##### Step 9
Validate the polyadenylation on an Agilent 2200 Tapestation using RNA Screentape. Use the untreated RNA from Step 5 as a reference.

##### Step 10
Dilute the sample to 2 ng/µL with nuclease-free water based on the gel electrophoresis results.

**Note:** If the concentration of the sample is below 2 ng/µL use it as it is. Libraries have been prepared successfully with as little as 0.45 ng/µL.

#### First Strand cDNA Synthesis

##### Step 11
Prepare the adaptor priming reaction in a 200 µL PCR tube:

* 11.5 µL sample from above (5-23 ng polyadenylated SSU rRNA).
* 0.5 µL 100 µM SSU_rRNA_RT.
* 1 µL 10 mM dNTP mix.

##### Step 12
Incubate the sample at 70°C for 5 min. Snap cooled on an ice block for 2 min. Proceed immediately to the next step.

##### Step 13
Prepare the first strand cDNA synthesis reaction in a 200 µL PCR tube:

* 13 µL sample from above
* 4 µL 5× SSIV buffer (Thermo Fisher Scientific).
* 1 µL 200 U/µL SuperScript IV Reverse Transcriptase (Thermo Fisher Scientific).
* 1 µL 100 mM DTT (Thermo Fisher Scientific).
* 1 µL RiboLock RNase Inhibitor (Thermo Fisher Scientific).

##### Step 14
Perform cDNA synthesis at 50°C for 50 min, inactivate the reaction at 80°C for 10 min, and finally cool the sample to 37°C. Proceed immediately to the next step.

##### Step 15
Add 1 µL 10 U/µL Ribonuclease H, from E. coli (cloned) (Thermo Fisher Scientific) to the cDNA from above, and incubate the sample at 37°C for 20 min to remove the RNA template.

##### Step 16
Purify the sample using AMPure XP beads:

* Perform purification in a 2 mL Eppendorf tube.
* Use 1.0× beads.
* Wash 2× with freshly prepared 80% ethanol.
* Elude in 11 µL nuclease-free water.

#### Adaptor Ligation

##### Step 17
Prepare the single-stranded adapter ligation reaction in a 200 µL PCR tube:

* 8.25 µL sample from above.
* 2.5 µL 10 µM SSU_rRNA_s.
* 5 µL 10× custom T4 RNA ligase buffer (500 mM Tris-HCl, 100 mM MgCl₂, 10 mM hexamminecobalt(III) chloride, 200 µM ATP, pH 8.0).
* 31.25 µL 40% (wt/wt) PEG 8000 (Thermo Fisher Scientific).
* 0.5 µL 1 mg/mL BSA (Thermo Fisher Scientific).

##### Step 18
Add 2.5 µL 10 U/µL T4 RNA ligase (Thermo Fisher Scientific).

##### Step 19
Perform ligation at 22°C overnight.

##### Step 20
Purify the sample using AMPure XP beads:

* Perform purification in a 2 mL Eppendorf tube.
* Use 1.0× beads.
* Wash 2× with freshly prepared 80% ethanol.
* Elude in 50 µL nuclease-free water.

**Note:** High amounts of PEG-8000 in the samples prevents stringent size selection during the AMPure XP purification. A two step AMPure purification is therefore performed to ensure the removal of free adapter oligoes.

#### Second Strand Synthesis

##### Step 21
Prepare the second strand cDNA synthesis reaction in a 200 µL PCR tube:

* 10 µL sample from above.
* 26.75 µL nuclease-free water.
* 5 µL 10× PCR Buffer (Qiagen).
* 1 µL 10 mM dNTP (Qiagen).
* 2.5 µL 10 µM SSU_rRNA_I.
* 2.5 µL 10 µM SSU_rRNA_pcr_rv.
* 2 µL 25 mM MgCl₂.
* 0.25 µL 5 U/µL Taq polymerase (Qiagen).

##### Step 22
Perform the second strand cDNA synthesis with an initial denaturation at 94°C for 3 min, followed by 2 cycles of denaturation at 94°C for 30 s, annealing at 56°C for 30 s, and extension at 72°C for 3 min.

##### Step 23
Purify the sample using AMPure XP beads:

* Perform purification in a 2 mL Eppendorf tube.
* Use 0.6× beads.
* Wash 2× with freshly prepared 80% ethanol.
* Elude in 25 µL nuclease-free water.

##### Step 24
Prepare a single-stranded DNA digestion reaction in a 200 µL PCR tube:

* 23 µL sample from above.
* 3 µL 10× S1 nuclease buffer (Thermo Fisher Scientific).
* 3 µL 3 M NaCl (Thermo Fisher Scientific).
* 1 µL 10 U/µL S1 nuclease (Thermo Fisher Scientific).

##### Step 25
Perform digestion at 25°C for 25 min. Terminate the reaction by addition of 2 µL 0.5 M EDTA and heating to 70°C for 10 min.

##### Step 26
Purify the sample using AMPure XP beads:

* Perform purification in a 2 mL Eppendorf tube.
* Dilute the sample to 50 µL with nuclease-free water (18 µL).
* Use 0.6× beads.
* Wash 2× with freshly prepared 80% ethanol.
* Elude in 12 µL nuclease-free water.

#### Primary Library Amplification

##### Step 27
Prepare a library amplification reaction in a 200 µL PCR tube:

* 10 µL sample from above.
* 63.5 µL nuclease-free water.
* 10 µL 10× PCR buffer (Qiagen).
* 2 µL 10 mM dNTP (Qiagen).
* 5 µL 10 µM FSSU_rRNA_pcr_fw.
* 5 µL 10 µM FSSU_rRNA_pcr_rv.
* 4 µL 25 mM MgCl (Qiagen).
* 0.5 µL 5 U/µL Taq polymerase (Qiagen).

##### Step 28
Perform the PCR with an initial denaturation at 94°C for 3 min, followed by 20 cycles of denaturation at 94°C for 30 s, annealing at 62°C for 30 s, and extension at 72°C for 2 min and then a final extension at 72°C for 5 min.

##### Step 29
Purify the sample using AMPure XP beads:

* Perform purification in a 2 mL Eppendorf tube.
* Use 0.6× beads.
* Wash 2× with freshly prepared 80% ethanol.
* Elude in 20 µL nuclease-free water.

##### Step 30
Analyze the PCR product on an Agilent 2200 Tapestation using a D5000 screen tape.

#### Primary Library Size Selection

##### Step 31
Isolate the full-length SSU PCR products by size selection on an E-gel electrophoresis system with precast E-Gel CloneWell gels (Thermo Fisher Scientific):

* Use 20 µL of sample from above (100-300 ng of PCR product).
* Use 500 ng GeneRuler 1 kB DNA ladder (Thermo Fisher Scientific) as a reference.
* Run the gel until the SSU peak (ca. 1,500 bp) is approximately 1 mm from the elution well.
* Now collect 20 µL elution aliquots every 15 seconds, up to a total of 16 aliquots, and the visible passing of the full-length SSU cDNA peak.
* Pool every two aliquots to obtain 8 pooled aliquots per sample.

##### Step 32
Analyze the pooled aliquots on an Agilent 2200 Tapestation with the High Sensitivity D5000 Screentape and pool the aliquots that contains the full-length SSU cDNA peak.

##### Step 33
Purify the sample using AMPure XP beads:

* Perform purification in a 2 mL Eppendorf tube.
* Use 0.6× beads.
* Wash 2× with freshly prepared 80% ethanol.
* Elude in 15 µL nuclease-free water.

##### Step 34
Determine the quality and the concentration of the final library on an Agilent 2200 Tapestation with the High Sensitivity D5000 Screentape.

#### Clonal Library Preparation

##### Step 35
Dilute the primary libraries based on the tapestation data to 10,000 (MiSeq) or 100,000 (HiSeq) copies/µL with nuclease-free water.

**Note:**  
The number of amplicons in the primary library can be calculated using the following formula:

\[ \text{number} = \frac{(\text{amount in ng} \times 6.022 \times 10^{23})}{(\text{length in bp} \times 1 \times 10^9 \times 650)} \approx \text{amount in ng} \times 5.15 \times 10^8 \text{ copies/ng} \]

##### Step 36
Prepare a clonal library amplification reaction in a 200 µL PCR tube:

* 10 µL sample from above.
* 63.5 µL nuclease-free water.
* 10 µL 10× PCR buffer (Qiagen).
* 2 µL 10 mM dNTP (Qiagen).
* 5 µL 10 µM SSU_rRNA_pcr_fw.
* 5 µL 10 µM SSU_rRNA_pcr_rv.
* 4 µL 25 mM MgCl₂ (Qiagen).
* 0.5 µL 5 U/µL Taq polymerase (Qiagen).

##### Step 37
Perform the PCR with an initial denaturation at 94°C for 3 min, followed by 25 (MiSeq) or 20 (HiSeq) cycles of denaturation at 94°C for 30 s, annealing at 62°C for 30 s, and extension at 72°C for 2 min and then a final extension at 72°C for 5 min.

##### Step 38
Purify the sample using AMPure XP beads:

* Perform purification in a 2 mL Eppendorf tube