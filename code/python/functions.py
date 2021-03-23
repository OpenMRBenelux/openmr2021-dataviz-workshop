import matplotlib.pyplot as plt
import numpy as np

def show_slice(
    image, orientation, slice_nr, timepoint = None, color_map = None
):
    """
    Shows a preferred slice from the 3D/4D nifti image, for a specific timepoint if applicable
    Indexing: [Medio-lateral, Antero-posterior, Cranio-caudal, Time]
    
    :param image: numpy array with grey values
    :param orientation: str, choose from ["sagittal", "frontal", "axial"]
    :param slice_nr: int, desired slice number
    :param timepoint: int, desired timepoint
    :param color_map: str, color map that you want to use for fancy slice plotting
    """
    
    if timepoint is not None: 
        # Extract desired timepoint
        image = image[:, :, :, timepoint]
    
    # Get desired slice and the according x and y labels
    slice, x_lab, y_lab = _get_slice(image, orientation, slice_nr)

    # Get default color map if applicable: gray for anatomical, coolwarm for functional
    default_color_maps = {3:"gray", 4:"coolwarm"}
    if color_map is None:
        color_map = default_color_maps.get(image.ndim)
        
    # Plot
    fig, ax = plt.subplots(figsize=(8, 8))
    _plot_slice(ax, slice, slice_nr, orientation, x_lab, y_lab, color_map)

    
def _plot_slice(ax, slice, slice_nr, orientation, x_lab, y_lab, color_map):
    """
    Plot a slice on an ax object, along with labels and titles
    
    :param ax: matplotlib ax object
    :param slice: 2D numpy array with grey values
    :param slice_nr: int, the slice number
    :param orientation: str, choose from ["sagittal", "frontal", "axial"]
    :param slice_nr: int, desired slice number
    :param timepoint: int, desired timepoint
    :param color_map: str, color map that you want to use for fancy slice plotting
    """
    ax.imshow(slice.T, cmap = color_map, origin = "lower")
    ax.set_title(f'Slice #{slice_nr} - {orientation}', fontsize = 18)
    ax.set_xlabel(x_lab, fontsize = 18)
    ax.set_ylabel(y_lab, fontsize = 18)


def track_voxel(
    image,
    ML_position,
    AP_position,
    CC_position,
    slice_timepoint=0,
    color_map="coolwarm",
    voxel_color="white",
    plot_voxel_in_slice=True,
):
    """
    Tracks the BOLD signal within a voxel over time
    Indexing: [Medio-lateral, Antero-posterior, Cranio-caudal]
    
    :param image: 4D numpy array with grey values
    :param ML_position: int, position of voxel in Medio-lateral direction
    :param AP_position: int, position of voxel in Antero-posterior direction
    :param CC_position: int, position of voxel in Cranio-caudal direction
    :param slice_timepoint: int, at which timepoint you want to show the slices
    :param color_map: str, color map that you want to use for fancy slice plotting
    """

    font_size = 18

    # Get 1D vector containing the voxel's value over time
    voxel_over_time = image[ML_position, AP_position, CC_position, :]

    # Plotting
    # 0. Create figure and different subplots
    # Source: https://www.geeksforgeeks.org/how-to-create-different-subplot-sizes-in-matplotlib/
    fig = plt.figure()
    fig.set_figheight(20)
    fig.set_figwidth(20)

    axSagit = plt.subplot2grid(shape=(3, 3), loc=(0, 0), colspan=1)
    axFront = plt.subplot2grid(shape=(3, 3), loc=(0, 1), colspan=1)
    axAxial = plt.subplot2grid(shape=(3, 3), loc=(0, 2), colspan=2)
    axTime = plt.subplot2grid(shape=(3, 3), loc=(1, 0), colspan=3)

    # 1. Plot position of voxel on all 3 slices
    # Create 1 plot per orientation in a for-loop
    for orientation, ax, slice_nr in zip(
        ["sagittal", "frontal", "axial"],
        [axSagit, axFront, axAxial],
        [ML_position, AP_position, CC_position],
    ):

        # Get slice and corresponding x and y label
        image_3D = image[:, :, :, slice_timepoint]
        slice, x_lab, y_lab = _get_slice(image_3D, orientation, slice_nr)

        _plot_slice(ax, slice, slice_nr, orientation, x_lab, y_lab, color_map)

        # Plot position of voxel inside slice in red
        if plot_voxel_in_slice:
            x_y_voxel = [ML_position, AP_position, CC_position]
            x_y_voxel.remove(
                slice_nr
            )  # Only retain 2 necessary positions (x and y) from all positions
            ax.scatter(x_y_voxel[0], x_y_voxel[1], color=voxel_color)

    # 2. Plot voxel over time
    axTime.plot(voxel_over_time)
    axTime.set_title("BOLD signal inside voxel over time", fontsize=font_size)
    axTime.set_xlabel("Timepoint", fontsize=font_size)
    axTime.set_ylabel("BOLD signal", fontsize=font_size)
    plt.show()


def _get_slice(image, orientation, slice_nr):
    """
    Get preferred slice from 3D or 4D nifti image
    Indexing: [Medio-lateral, Antero-posterior, Cranio-caudal, Time]
    
    :param image: 3D/4D numpy array with grey values
    :param orientation: str, choose from ["sagittal", "frontal", "axial"]
    :param slice_nr: int, desired slice number
    :output: Slice: np array, x_lab: xlabel, y_lab: ylabel
    """

    # Get desired slice and the according x and y labels
    if orientation == "sagittal":
        # Medio-Lateral: slice_nr,
        # Antero-posterior: all voxels,
        # Cranio-caudal: all voxels,
        # Time: timepoint
        slice = image[slice_nr, :, :]
        y_lab = "Cranio-caudal"
        x_lab = "Antero-posterior"
    elif orientation == "frontal":
        # Medio-Lateral: all voxels,
        # Antero-posterior: slice_nr,
        # Cranio-caudal: all_voxels,
        # Time: timepoint
        slice = image[:, slice_nr, :]
        y_lab = "Cranio-caudal"
        x_lab = "Medio-lateral"
    elif orientation == "axial":
        # Medio-Lateral: all voxels,
        # Antero-posterior: all voxels,
        # Cranio-caudal: slice_nr,
        # Time: timepoint
        slice = image[:, :, slice_nr]
        y_lab = "Antero-posterior"
        x_lab = "Medio-lateral"

    return slice, x_lab, y_lab


def simulate_volume(age, intercept, slope):
    """ 
    Predict a volume based on an age, according to a 1D regression equation and some Gaussian noise.
    
    :param age: the age of the subject
    :param intercept: intercept of the regression line between age and volume
    :param slope: slope of the regression line between age and volume
    """
    
    # Predict the volume on regression line
    volume = intercept + slope*age
    
    # Add noise (mean = 0, std = intercept/50)
    noise = np.random.normal(0,intercept/50,1)[0]
    volume += noise
    
    return volume
