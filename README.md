# Micro Jet Engine – Design and Development

**Overview**  
This project focuses on the **design, fabrication, and performance testing of a turbine-less hybrid micro jet engine**, where an **electric motor drives the centrifugal compressor**. The goal is to achieve thrust through complete expansion of high-enthalpy gases at the nozzle exit while maintaining compactness and serviceability for UAV-scale applications.

---

## Objectives
- Design and test a micro jet engine.
- Analyze compressor and combustor characteristics through both experimental and simulation-based approaches.  
- Focus on **Design for Manufacturability (DFM)** and **Design for Serviceability (DFS)** in all stages of development.  
- Develop a **real-time active control system** in the next phase for autonomous engine control.  

---

## Current Scope
The current stage involves:
- **Centrifugal compressor design, analysis, and testing** using ANSYS suite tools.  
- **Combustion chamber design** and fabrication with performance evaluation under various flow conditions.  
- **Instrumentation setup** using sensors such as:
  - **Thermocouples** for temperature mapping,
  - **Pressure transducers** for pressure ratio measurement,
  - **Motor driver and encoder** for RPM and torque control.  

The turbine-less prototype is being tested for stable operation across RPM ranges while maintaining safe compressor operation above the surge line.

---

## Software Used
- **ANSYS Vista CCD** – Compressor design and performance prediction  
- **ANSYS BladeGen** – Impeller geometry creation and modification  
- **ANSYS TurboGrid** – High-quality meshing for turbomachinery  
- **ANSYS Fluent** – CFD simulation for flow and thermal analysis  
- **SolidWorks** – CAD modeling and assembly design  
- **MATLAB / Simulink** – Data analysis and control modeling  

---

## Future Work
- Design and integration of a **turbine stage** for a fully functional jet engine.  
- Development of a **real-time active control system** to regulate fuel flow, compressor speed, and combustion parameters.  
- System-level optimization for thrust, efficiency, and durability through hardware-in-loop (HIL) testing.  

---

## Contributors
- **L. G. Deepak, Ashish, Abjeeth, Kanniah**, Mechanical Engineering, IIT Ropar  
- Under the guidance of **Dr. Rajendra Munian** and **Dr. Sreekanth Sekhar Padhee**

---

**Status:** Ongoing – Fabrication and testing in progress.  
**Focus Areas:** Thermodynamic performance | Experimental validation | Control system integration
