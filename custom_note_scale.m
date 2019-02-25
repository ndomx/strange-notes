clear all, close all, clc
original = 2.^((0:11)/12);

N = 13;
custom = 2.^((0:N-1)/N);

%% Plot custom note scale and original note scale
figure(1)
grid on
hold on
scatter(original, 0.4 * ones(1,12), 'x', 'LineWidth', 1.5)
scatter(custom, 0.6*ones(1,N), 'x', 'LineWidth', 1.5)
axis([1 2 0 1])
title(sprintf('12 note scale & %d note scale', N))
legend('12 note scale', sprintf('%d note scale', N))
for k = 1:12
    text(original(k), 0.35, int2str(k))
end
for k = 1:N
    text(custom(k), 0.55, int2str(k))
end

%% Test the custom note scale
F0 = 440; % Reference frequency

Fs = 8192;
Ts = 1/Fs;
t = 0:Ts:0.5-Ts; % Play the note for 0.5 seconds

for k=0:N
    f = F0 * 2^(k/N);
    x = cos(2*pi*f*t);
    sound(x, 1/Ts)
    pause(0.75)
end