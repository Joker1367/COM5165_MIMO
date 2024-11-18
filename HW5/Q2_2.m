clear all
clc

% 設定參數
fc = 1e9; % 載波頻率 (1 GHz)
lambda = physconst('LightSpeed') / fc; % 波長
elementSpacing = lambda / 2; % 元件間距
array = phased.ULA('NumElements', 8, 'ElementSpacing', elementSpacing);

steeringAngle = 90; % 偏移波束方向到 30 度
steerVector = phased.SteeringVector('SensorArray', array, ...
                                    'PropagationSpeed', physconst('LightSpeed'));
weights = steerVector(fc, steeringAngle); % 生成加權

azimuthAngles = -180:1:180; % 方位角範圍（-180 到 180 度）
elevationAngle = 90; % 固定仰角（俯視圖表示垂直觀察）

% 繪製 2D 波束圖
figure;
pattern(array, fc, azimuthAngles, elevationAngle, 'Type', 'directivity', ...
    'CoordinateSystem', 'rectangular');
title('2D俯視波束圖 - 上往下看');
xlabel('方位角 (°)');
ylabel('增益 (dBi)');
