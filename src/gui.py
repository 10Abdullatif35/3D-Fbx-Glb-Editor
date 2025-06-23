import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

import open3d as o3d


def preview_model(model_path: Path) -> None:
    """Display the 3D model in a rotating Open3D viewer."""
    mesh = o3d.io.read_triangle_mesh(str(model_path))
    if mesh.is_empty():
        raise ValueError(f"Could not load 3D model from {model_path}")
    mesh.compute_vertex_normals()

    def rotate(vis: o3d.visualization.Visualizer) -> None:
        ctr = vis.get_view_control()
        ctr.rotate(2.0, 0.0)

    o3d.visualization.draw_geometries_with_animation_callback([mesh], rotate)


def select_file() -> None:
    """Open a file dialog and preview the chosen model."""
    file_path = filedialog.askopenfilename(
        title="Select FBX or GLB file",
        filetypes=[("3D models", "*.fbx *.glb"), ("All files", "*.*")],
    )
    if not file_path:
        return
    try:
        preview_model(Path(file_path))
    except Exception as exc:
        messagebox.showerror("Error", str(exc))


def main() -> None:
    root = tk.Tk()
    root.title("3D Model Previewer")
    tk.Button(root, text="Open File", command=select_file).pack(padx=20, pady=20)
    root.mainloop()


if __name__ == "__main__":
    main()
