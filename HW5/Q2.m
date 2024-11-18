clear all
clc

% 1. Define parameters
fc = 1e9;                  % Frequency (1 GHz)
c = 3e8;                   % Speed of light (m/s)
lambda = c / fc;           % Wavelength (m)
elementNum = 4;            % Number of antenna elements
Lr = 2;
elementSpacing = lambda * Lr / elementNum; % Spacing between antenna elements

% 2. Create a Uniform Linear Array (ULA)
ula = phased.ULA('NumElements', elementNum, ...
                 'ElementSpacing', elementSpacing);

% 3. Beamforming direction (e.g., beam points to [0, -90])
beamDirection = [90; 0];  % Azimuth angle: 90 degrees, Elevation angle: 0 degrees

steervec = phased.SteeringVector('SensorArray', ula);
w = steervec(fc, beamDirection);

% 4. Calculate the radiation pattern and normalize
angles = -180:180; % Azimuth angle range
patternData = pattern(ula, fc, angles, 0, ...
    'Type', 'power', ...    % Use power mode (linear scale)
    'PropagationSpeed', c, ...
    'Weight', w); 

% Normalize to the maximum gain
normalizedPattern = patternData / max(patternData); % Compute in linear scale

% 5. Plot the beam pattern (polar coordinates, linear scale)
figure;
polarplot(deg2rad(angles), normalizedPattern, 'LineWidth', 1.5);
title('Normalized ULA Beamforming Pattern (Linear Scale)');
rlim([0 1]); % Set display range
