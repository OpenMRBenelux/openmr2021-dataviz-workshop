function show_slice(slice, orientation, slice_nr, x_lab, y_lab, color_map)
    %
    % Plots a slice
    %
    % USAGE::
    %
    %   show_slice(slice, orientation, slice_nr, x_lab, y_lab)
    %

    FONTSIZE = 20;

    if nargin < 6
        color_map = 'gray';
    end

    imagesc(slice);

    axis image;
    colormap(color_map);

    t = xlabel(x_lab);
    set(t, 'fontsize', FONTSIZE);
    t = ylabel(y_lab);
    set(t, 'fontsize', FONTSIZE);

    title(sprintf('%s slice #%i', orientation, slice_nr), 'fontsize', FONTSIZE);

end
