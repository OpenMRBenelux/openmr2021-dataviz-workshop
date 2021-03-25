function volume = simulate_volume(age, intercept, slope)
    %
    % Predict a volume based on an age, according to a 1D regression equation and some Gaussian noise.
    %
    % :param age: the age of the subject
    % :param intercept: intercept of the regression line between age and volume
    % :param slope: slope of the regression line between age and volume
    %

    % Predict the volume on regression line
    volume = intercept + slope * age;
    
    % Add noise (mean = 0, std = intercept/50)
    noise = randn(size(volume)) * intercept/50;
    volume =  volume + noise;
    
end