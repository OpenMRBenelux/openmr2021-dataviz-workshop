function [slice, x_lab, y_lab] = get_slice(image, orientation, slice_nr)
    %
    % Get preferred slice from 3D or 4D nifti image
    % Indexing: [Medio-lateral, Antero-posterior, Cranio-caudal, Time]
    %
    % USAGE::
    %
    %   [slice, x_lab, y_lab] = get_slice(image, orientation, slice_nr)
    %
    % :param image: 3D/4D array
    % :param orientation: choose from ["sagittal", "frontal", "axial"]
    % :type orientation: str
    % :param slice_nr: desired slice number
    % :type slice_nr: int
    %
    % :output: - slice: array
    %          - x_lab: x label
    %          - y_lab: y label

    % Get desired slice and the according x and y labels
    switch lower(orientation)

        case 'axial'
            x_lab = 'Medio-lateral';
            y_lab = 'Antero-posterior';
            slice = image(:, :, slice_nr);

        case 'sagittal'
            x_lab = 'Antero-posterior';
            y_lab = 'Cranio-caudal';
            slice = image(slice_nr, :, :);

        case 'frontal'
            x_lab = 'Medio-lateral';
            y_lab = 'Cranio-caudal';
            slice = image(:, slice_nr, :);

    end

    slice = rot90(squeeze(slice));

end
