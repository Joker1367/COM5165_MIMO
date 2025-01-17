clear all
clc

% Initialize parameters
fc = 3e9; % Operating frequency in Hz (e.g., 3 GHz)
c = 3e8;  % Speed of light in m/s
lambda = c / fc; % Wavelength in meters
Lr = 2; % Total array length in wavelengths
nr_values = [2, 4, 6, 32]; % Different numbers of antennas

% Loop through different numbers of antennas
for i = 1:length(nr_values)
    nr = nr_values(i); % Number of antennas
    d = lambda * Lr / nr; % Antenna element spacing (in wavelengths)

    % Create the ULA (Uniform Linear Array)
    array = phased.ULA('NumElements', nr, 'ElementSpacing', d);

    % Compute steering vector
    angles = -180:180; % Azimuth angle range
    steeringVector = phased.SteeringVector('SensorArray', array, ...
                                           'PropagationSpeed', c);
    weights = steeringVector(fc, [0;90]); % Compute weights for 90° beam direction

    % Plot the beam pattern
    patterndata = pattern(array, fc, angles, 0, ... 
            'Type', 'power', ...
            'PropagationSpeed', c, ...
            'Weights', weights);

    normalizedPattern = patterndata / max(patterndata);

    s = sprintf('n_r = %d, L_r = %d',nr, Lr);
    % Customize plot
    subplot(2,2,i)
    polarplot(deg2rad(angles), normalizedPattern, 'LineWidth', 1.5);
    title(s);
    rlim([0 1]); % Set display range
end
