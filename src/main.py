import argparse
from pathlib import Path


def copy_file(input_path: Path, output_path: Path) -> None:
    """Read input file and write its contents to the output file."""
    data = input_path.read_bytes()
    output_path.write_bytes(data)


def preview_model(model_path: Path) -> None:
    """Open a window displaying the model spinning slowly."""
    import open3d as o3d

    mesh = o3d.io.read_triangle_mesh(str(model_path))
    if mesh.is_empty():
        raise ValueError(f"Could not load 3D model from {model_path}")
    mesh.compute_vertex_normals()

    def rotate(vis: o3d.visualization.Visualizer) -> None:
        ctr = vis.get_view_control()
        ctr.rotate(2.0, 0.0)

    o3d.visualization.draw_geometries_with_animation_callback([mesh], rotate)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simple 3D FBX/GLB file copier and previewer"
    )
    parser.add_argument(
        "input", type=Path, help="Path to the input FBX/GLB file"
    )
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Optional path where the output file will be written",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview the model in a rotating window",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.output is not None:
        copy_file(args.input, args.output)
        print(f"Copied {args.input} to {args.output}")

    if args.preview or args.output is None:
        preview_model(args.input)


if __name__ == "__main__":
    main()
