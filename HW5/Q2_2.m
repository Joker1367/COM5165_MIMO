clear all
clc

% 1. 定義參數
fc = 3e9;                  % 頻率 (3 GHz)
c = 3e8;                   % 光速 (m/s)
lambda = c / fc;           % 波長 (m)
elementNum = 4;           % 天線數量
Lr = 2;
elementSpacing = lambda * Lr / elementNum; % 天線間距

myAnt1 = phased.IsotropicAntennaElement;

% 2. 建立 Uniform Linear Array (ULA)
ula = phased.ULA('Element', myAnt1, 'NumElements', elementNum, ...
                 'ElementSpacing', elementSpacing);

% 3. 波束形成方向 (例如，波束指向 [0, -90])
beamDirection = [90; 0];  % 方位角 0 度，高度角 -90 度

steervec = phased.SteeringVector('SensorArray',ula);
w = steervec(fc,beamDirection);

% 4. 計算方向圖並歸一化
angles = -180:180; % 方位角範圍
patternData = pattern(ula, fc, angles, 0, ...
    'Type', 'power', ...    % 使用功率模式（線性比例）
    'PropagationSpeed', c, ...
    'Weight', w); % 關閉自動歸一化

% 歸一化為最大增益的比值
normalizedPattern = patternData / max(patternData); % 線性比例計算

% 5. 繪製波束圖 (極座標，線性比例)
figure;
polarplot(deg2rad(angles), normalizedPattern, 'LineWidth', 1.5);
title('Normalized ULA Beamforming Pattern (Linear Scale)');
rlim([0 1]); % 設定顯示範圍為 0 到 1
grid on;
