clear all;
clc;

rho = [0:9] / 10; 
%rho = [rho 0.91 0.92 0.93 0.94 0.95];
Nr = 4;
Nt = 4;

samples = 1000;

H = zeros(Nr, Nt);

avg_condition_independent = [];
avg_condition_correlated = [];

for n = 1 : length(rho)
    avg = 0;
    for sample = 1 : samples
        for i = 1 : Nr
            for j = 1 : Nt
                H(i, j) = rand + 1j*rand;
            end
        end
        singular_values = svd(H);
        avg = avg + max(singular_values) / min(singular_values);
    end
    avg_condition_independent = [avg_condition_independent avg / samples];
end


for n = 1 : length(rho)
    avg = 0;
    R = [1        rho(n)    rho(n)^2 rho(n)^3;
         rho(n)   1         rho(n)   rho(n)^2;
         rho(n)^2 rho(n)    1        rho(n)  ;
         rho(n)^3 rho(n)^2  rho(n)   1       ];

    for sample = 1 : samples
        for i = 1 : Nr
            for j = 1 : Nt
                H(i, j) = rand + 1j*rand;
            end
        end
        singular_values = svd(sqrtm(R) * H * sqrtm(R));
        avg = avg + max(singular_values) / min(singular_values);
    end
    avg_condition_correlated = [avg_condition_correlated avg / samples];
end

figure
hold on
grid on
plot(rho, avg_condition_independent);
plot(rho, avg_condition_correlated);
xlabel("\rho");
ylabel("condition number")
legend("i.i.d rayleigh fading", "correlated");

