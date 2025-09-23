import csv
import re

def parse_input_file(input_file):
    """Parse input file and return dict[test_id] = {num_points, grid_size}"""
    results = {}
    with open(input_file, "r") as f:
        lines = f.readlines()

    t = int(lines[0].strip())  # number of test cases
    idx = 1
    for test_id in range(1, t + 1):
        n = int(lines[idx].strip())  # number of points
        idx += 1
        coords = []
        for _ in range(n):
            x, y = map(int, lines[idx].split())
            coords.append((x, y))
            idx += 1

        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        grid_size = max(max(xs) - min(xs), max(ys) - min(ys))

        results[test_id] = {
            "num_points": n,
            "grid_size": grid_size
        }

    return results


def parse_log_file(log_file, method_name):
    """Parse one method's log file line by line."""
    results = {}
    with open(log_file, "r") as f:
        lines = f.readlines()

    test_id = 0
    metrics = {}
    for line in lines:
        line = line.strip()
        if line.startswith("Num_Terminals"):
            metrics["num_terminals"] = int(line.split("=")[1].strip())
        elif line.startswith("Wirelength"):
            metrics["wirelength"] = int(line.split("=")[1].strip())
        elif line.startswith("Num Steiner Points"):
            metrics["steiner"] = int(line.split("=")[1].strip())
        elif line.startswith("CPU Time"):
            metrics["time"] = float(line.split("=")[1].strip().split()[0])
            # End of a test case
            test_id += 1
            results[test_id] = {
                f"{method_name}_wirelength": metrics["wirelength"],
                f"{method_name}_steiner": metrics["steiner"],
                f"{method_name}_time": metrics["time"]
            }
            metrics = {}  # reset for next test case
    return results



def compile_all(input_file, cockayne_log, geosteiner_log, flute_log, result_csv):
    input_data = parse_input_file(input_file)
    cockayne = parse_log_file(cockayne_log, "cockayne")
    geosteiner = parse_log_file(geosteiner_log, "geosteiner")
    flute = parse_log_file(flute_log, "flute")

    all_ids = sorted(input_data.keys())

    with open(result_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "test_id", "num_points", "grid_size",
            "cockayne_steiner", "geosteiner_steiner", "flute_steiner",
            "cockayne_wirelength", "geosteiner_wirelength", "flute_wirelength",
            "cockayne_time", "geosteiner_time", "flute_time"
        ])

        for test_id in all_ids:
            base = input_data[test_id]
            writer.writerow([
                test_id, base["num_points"], base["grid_size"],
                cockayne.get(test_id, {}).get("cockayne_steiner", ""),
                geosteiner.get(test_id, {}).get("geosteiner_steiner", ""),
                flute.get(test_id, {}).get("flute_steiner", ""),
                cockayne.get(test_id, {}).get("cockayne_wirelength", ""),
                geosteiner.get(test_id, {}).get("geosteiner_wirelength", ""),
                flute.get(test_id, {}).get("flute_wirelength", ""),
                cockayne.get(test_id, {}).get("cockayne_time", ""),
                geosteiner.get(test_id, {}).get("geosteiner_time", ""),
                flute.get(test_id, {}).get("flute_time", "")
            ])

    print(f"✅ Combined results saved to {result_csv}")

if __name__ == "__main__":
    compile_all("../inputs/input.txt", "../logs/cockayne.txt", "../logs/geosteiner.txt", "../logs/flute.txt", "summary.csv")
