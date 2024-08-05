```markdown
Goal/Experiment:

The goal of this experiment is to assess coastal flood risk and the economics of climate adaptation. This involves identifying areas at risk, quantifying losses and damages under various scenarios, and comparing potential adaptation solutions using cost-benefit analysis.

# Assessing Coastal Risk and the Economics of Climate Adaptation

**Authors:** Borja G. Reguero, David N. Bresch

**Citation:** Borja G. Reguero, David N. Bresch Assessing Coastal Risk and the Economics of Climate Adaptation. protocols.io dx.doi.org/10.17504/protocols.io.miyc4fw

**Published:** 10 Jan 2018

## Abstract

As climate change progresses, so does the risk from hurricanes, flooding, and other natural disasters. As sea levels rise, tropical cyclones will pose a greater risk of extreme flooding and are likely to inflict the greatest damages on highly populated shorelines. This protocol describes a quantitative risk assessment framework to evaluate the cost-effectiveness of different adaptation measures. These options may include natural solutions (e.g., oyster reef restoration), structural solutions (e.g., seawalls), and policy measures (e.g., home elevation or coastal development policies).

## Guidelines

The protocol is part of the ‘Economics of Climate Adaptation’ framework and is implemented in climada, particularly the ‘coastal module’.

For more information, consult: [www.swissre.com/eca/](http://www.swissre.com/eca/)

## Before Start

Risk occurs at the intersection of economic assets and the hazard of coastal flooding. Adaptation can impact each risk component. There are three parts to assess the cost-effectiveness of adaptation measures:

### 1. Assessing Current Risk

Risk is quantified as a probable loss. The total loss from a natural hazard (e.g., floods) is a combination of three factors:

- **Hazard (or 'peril')**: Defined by the location, frequency, and intensity of events.
- **Assets exposed**: Defined by the location and value of buildings and assets.
- **Damages to assets**: The relationship between the extent of damage and event intensity, determined by damage (or vulnerability) curves.

### 2. Assessing Future Risk

Future risk arises from climate and economic changes. Factors include land subsidence, sea level rise, and changes in storm patterns. Coastal exposure changes, due to development intensification, also contribute to future risk.

### 3. Assessing the Economics of Adaptation Measures

The cost and benefits (losses averted) of adaptation measures are assessed by:

1. Defining adaptation strategies.
2. Estimating the benefits of each measure in protecting a percentage of property.
3. Calculating the cost of each measure.
4. Calculating the Net Present Value (NPV) of costs and benefits, calculated as follows:
   - Calculate both baseline risk (current) and future risk (e.g., 2050).
   - Discount benefits and costs to present terms.
5. Calculating the benefit-to-cost ratio.

Cost estimates for each adaptation measure can be derived from the review of past projects or local estimates.

## Protocol

### Assessment of Coastal Flooding

**Step 1.** 
- Historical and synthetic storms are simulated with climada.
- Total water levels are calculated based on surges, tides, sea level rise, and wave runup.

**Software Package (Matlab):** [CLIMADA - COASTAL, 1.0](https://github.com/borjagreguero/climada_coastal_hazards_module)
**Dataset:** [Sea Level Rise NOAA measurements](#)

### Assessment of Coastal Exposure

**Step 2.**
- In GIS, data on building value is calculated for each ground height.
- Flood maps are created using a bathtub approach for each ground height.

**Dataset:** [Elevation model](#)

### Calculation of Damages

**Step 3.**
- Damages are calculated in climada, considering asset distribution for each ground height.

**Software Package (Matlab):** [CLIMADA - COASTAL, 1.0](https://github.com/borjagreguero/climada_coastal_hazards_module)

### Calculation of Cost and Benefits

**Step 4.**
a) Estimate adaptation strategies for hazard attenuation, location, cost, and protection percentage.

b) Calculate net present value over the period the adaptation measure is designed for.

**Software Package (Matlab):** [CLIMADA - COASTAL, 1.0](https://github.com/borjagreguero/climada_coastal_hazards_module)

---

endofoutput
```