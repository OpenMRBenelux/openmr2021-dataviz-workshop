function show_slice_from_timeseries(image, orientation, slice_nr, timepoint, color_map)
    %
    % Shows a preferred slice from the 4D nifti image
    % Indexing: [Medio-lateral, Antero-posterior, Cranio-caudal, Time]
    %
    % USAGE::
    %
    %   show_functional_slice(image, orientation, slice_nr, timepoint, color_map)
    %
    % :param image: 3D/4D array
    % :param orientation: choose from 'sagittal', 'frontal', 'axial'
    % :type orientation: str
    % :param slice_nr: desired slice number
    % :type slice_nr: int
    % :param timepoint: desired time point
    % :type timepoint: int
    % :param color_map: 'gray' is the default
    % :type color_map: str
    %

    if nargin < 5
        color_map = 'gray';
    end

    image = image(:, :, :, timepoint);

    [slice, x_lab, y_lab] = get_slice(image, orientation, slice_nr);
    show_slice(slice, orientation, slice_nr, x_lab, y_lab, color_map);

end
