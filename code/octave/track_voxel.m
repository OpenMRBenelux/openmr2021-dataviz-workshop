function track_voxel(bold_image, x, y, z)

    % voxel_color='lightgreen'

    FONTSIZE = 20;

    figure('name', '', ...
           'position', [0 0 1200 1200]);

    % compute the mean image over time points to plot
    mean_image = mean(bold_image, 4);

    voxel_coord = [size(mean_image, 1) - x, ...
                   size(mean_image, 2) - y, ...
                   size(mean_image, 3) - z];

    subplot(2, 3, 1);
    show_slice_from_volume(mean_image, 'sagittal', x);
    plot_voxel([y, voxel_coord(3)]);

    subplot(2, 3, 2);
    show_slice_from_volume(mean_image, 'frontal', y);
    plot_voxel(voxel_coord([1 3]));

    subplot(2, 3, 3);
    show_slice_from_volume(mean_image, 'axial', z);
    plot_voxel(voxel_coord([1 2]));

    subplot(2, 3, 4:6);
    voxel_BOLD_vector = bold_image(x, y, z, :);
    plot(squeeze(voxel_BOLD_vector), 'linewidth', 5);

    axis tight;

    t = xlabel('Timepoint');
    set(t, 'fontsize', FONTSIZE);
    t = ylabel('BOLD signal');
    set(t, 'fontsize', FONTSIZE);

    title('BOLD signal inside voxel over time', 'fontsize', FONTSIZE);

end

function plot_voxel(coord)
    hold on;
    plot(coord(1), coord(2), 'og', ...
         'markersize', 10, ...
         'markerfacecolor', 'g');
end
