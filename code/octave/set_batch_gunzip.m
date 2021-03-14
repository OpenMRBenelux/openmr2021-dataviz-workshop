function matlabbatch = set_batch_gunzip(input_files, ouput_dir)

    matlabbatch{1}.cfg_basicio.file_dir.file_ops.cfg_gunzip_files.files = cellstr(input_files);
    matlabbatch{1}.cfg_basicio.file_dir.file_ops.cfg_gunzip_files.outdir = {ouput_dir};
    matlabbatch{1}.cfg_basicio.file_dir.file_ops.cfg_gunzip_files.keep = true;

end