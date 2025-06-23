import argparse
from pathlib import Path


def copy_file(input_path: Path, output_path: Path) -> None:
    """Read input file and write its contents to the output file."""
    data = input_path.read_bytes()
    output_path.write_bytes(data)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple 3D FBX/GLB file copier")
    parser.add_argument("input", type=Path, help="Path to the input FBX/GLB file")
    parser.add_argument("output", type=Path, help="Path where the output file will be written")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    copy_file(args.input, args.output)
    print(f"Copied {args.input} to {args.output}")


if __name__ == "__main__":
    main()
