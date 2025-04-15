import numpy as np
import matplotlib.pyplot as plt
import os

def read_llc2160_faces(filepath, ny=4320, nx=4320):
    face_shapes = [
        (3 * ny, nx),
        (3 * ny, nx),
        (nx,ny),
        (ny, 3 * nx),
        (ny, 3 * nx)
    ]
    data = np.fromfile(filepath, dtype=">f4")
    total_elements = sum(np.prod(s) for s in face_shapes)
    if data.size != total_elements:
        raise ValueError(f"Expected {total_elements} elements, got {data.size}.")
    faces = []
    start = 0
    for shape in face_shapes:
        count = np.prod(shape)
        face_data = data[start:start + count].reshape(shape)
        faces.append(face_data)
        start += count
    return faces

def assemble_llc2160_row(faces):
    face0 = faces[0]
    face1 = faces[1]
    face3 = np.rot90(faces[3], k=1)
    face4 = np.rot90(faces[4], k=1)
    mosaic = np.concatenate([face0, face1, face3, face4], axis=1)
    return mosaic

def main():
    raw_dir = "./raw_metadata"
    xc_filepath = os.path.join(raw_dir, "XC.data")
    yc_filepath = os.path.join(raw_dir, "YC.data")
    lon_faces = read_llc2160_faces(xc_filepath)
    lat_faces = read_llc2160_faces(yc_filepath)
    lon_mosaic = assemble_llc2160_row(lon_faces)
    lat_mosaic = assemble_llc2160_row(lat_faces)
    print("Longitude mosaic shape:", lon_mosaic.shape)
    print("Latitude mosaic shape:", lat_mosaic.shape)
    fig, ax = plt.subplots(1, 2, figsize=(14, 7))
    c0 = ax[0].imshow(lon_mosaic, cmap="jet", origin="lower")
    ax[0].set_title("XC.data (Longitude)")
    fig.colorbar(c0, ax=ax[0], orientation="horizontal")
    c1 = ax[1].imshow(lat_mosaic, cmap="jet", origin="lower")
    ax[1].set_title("YC.data (Latitude)")
    fig.colorbar(c1, ax=ax[1], orientation="horizontal")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
