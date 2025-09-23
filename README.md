# RSMT Benchmarking: Cockayne, GeoSteiner 5.3, and FLUTE 3.1  

## Overview  
This project benchmarks **Rectilinear Steiner Minimum Tree (RSMT)** generation tools—**Cockayne**, **GeoSteiner 5.3**, and **FLUTE 3.1**—with a focus on **runtime and performance comparisons**.  

Our objective is to evaluate how these algorithms scale with problem size and complexity, highlighting trade-offs between accuracy and computational efficiency.  

⚠️ **Note**: The full experimental dataset belongs to the **VLSI Lab, Indian Statistical Institute (ISI)** and cannot be shared publicly. However, sample input/output files are included to demonstrate usage and expected program behavior.  

---

## Tools Compared  
- **Cockayne** – A classical heuristic-based RSMT generator.  
- **GeoSteiner 5.3** – A state-of-the-art exact algorithm for Steiner tree problems.  
- **FLUTE 3.1** – A fast lookup-table-based method widely used in VLSI design automation.  

---

## Repository Contents  
- `inputs/` – Example input files (subset only)  
- `outputs/` – Corresponding example output files  
- `scripts/` – Utility scripts for running and parsing results  
- `README.md` – Project documentation (this file)  

---

## Usage  

### 1. Requirements  
- Linux/Unix environment  
- C/C++ compiler  
- Python ≥ 3.8 (for parsing/plotting scripts)  

Make sure the external tools (**Cockayne**, **GeoSteiner 5.3**, **FLUTE 3.1**) are installed and accessible in your system’s `$PATH`.  

### 2. Running Benchmarks  
Example usage:  

```bash
# Run Cockayne
./cockayne inputs/sample.in > outputs/cockayne_sample.out

# Run GeoSteiner
geosteiner -f inputs/sample.in -o outputs/geosteiner_sample.out

# Run FLUTE
flute inputs/sample.in > outputs/flute_sample.out
