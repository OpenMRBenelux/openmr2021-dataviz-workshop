function show_slice_from_volume(image, orientation, slice_nr, color_map)
    %
    % Shows a preferred slice from the 3D nifti image
    % Indexing: [Medio-lateral, Antero-posterior, Cranio-caudal, Time]
    %
    % USAGE::
    %
    %   show_anatomical_slice(image, orientation, slice_nr)
    %
    % :param image: 3D/4D array
    % :param orientation: choose from 'sagittal', 'frontal', 'axial'
    % :type orientation: str
    % :param slice_nr: desired slice number
    % :type slice_nr: int
    %

    if nargin < 4
        color_map = 'gray';
    end

    [slice, x_lab, y_lab] = get_slice(image, orientation, slice_nr);
    show_slice(slice, orientation, slice_nr, x_lab, y_lab, color_map);

end
