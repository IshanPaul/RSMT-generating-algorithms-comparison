````markdown
# Simulator.sh

A Bash-based simulation framework for generating and testing Steiner Tree algorithms using:

- **Flute** (`flute-3.1`)
- **GeoSteiner** (`geosteiner-5.3`)
- **Cockayne (RSMT implementation)** (`Steiner Tree/Code/RSMT.cpp`)

---

## Usage

```bash
./Simulator.sh [options] <lower limit of #terminals> <upper limit of #terminals>
````

### Options

| Flag | Argument         | Description                                                                     |
| ---- | ---------------- | ------------------------------------------------------------------------------- |
| `-h` | none             | Show help message                                                               |
| `-s` | `<seed>`         | Seed for the random number generator                                            |
| `-n` | `<iterations>`   | Number of test cases to generate/run                                            |
| `-a` | `<algo>`         | Algorithm(s) to run. Can include: `f` (Flute), `g` (GeoSteiner), `c` (Cockayne) |
| `-i` | `<input_folder>` | Path to input/output folder (default: current directory)                        |

---

## Examples

### Show help

```bash
./Simulator.sh -h
```

### Generate 10 test cases, terminals between 5 and 50

```bash
./Simulator.sh -n 10 5 50
```

### Run only Flute on 20 cases, terminals between 10–100

```bash
./Simulator.sh -a f -n 20 10 100
```

### Run all algorithms on an existing input file

```bash
./Simulator.sh -a fgc -i ./inputs -n 5 5 20
```

---

## Output Files

* **Inputs**: `in_<iterations>_<lower>-<upper>.txt`
* **Algorithm outputs**:

  * `flute_out_<iterations>_<lower>-<upper>.txt`
  * `geosteiner_out_<iterations>_<lower>-<upper>.txt`
  * `cockayne_out_<iterations>_<lower>-<upper>.txt`
* **Logs**:

  * `flute_logs_<iterations>_<lower>-<upper>.txt`
  * `geosteiner_logs_<iterations>_<lower>-<upper>.txt`
  * `cockayne_logs_<iterations>_<lower>-<upper>.txt`

---

## Requirements

* **Bash** (5+ recommended)
* **g++** (to compile Cockayne implementation)
* **make** (to build Flute and GeoSteiner)

Dependencies:

* `flute-3.1/` → must contain `rand-pts` and `flute-demo`
* `geosteiner-5.3/` → must contain `my_demo`
* `Steiner Tree/Code/RSMT.cpp`

---

## Notes

* You must provide `<lower>` and `<upper>` terminal limits
* At least one algorithm must be specified using `-a`
* Existing input files are truncated and regenerated automatically
* Runtime errors are logged to corresponding `*_logs_*.txt` files

---

## License

MIT (or replace with your preferred license)

```
```
