clear all
r=0.0001
f=@(V) [-r*V(1)*V(2),r*V(1)*V(2)]; %Defino el campo vectorial del problema depredador presa,
%Noten que V es un vector cuya primera entrada representa a X y la segunda
%entrada representa a Y, para verlo más fácil en su cabeza cambien V(1) por
%x y V(2) por y para obtener las 2 ecuaciones del problema.
a=0; %El valor inicial de t es 0
b=5; %quiero llegar hasta t=20, esto lo pueden modificar ustedes
h=0.1; %quiero dar saltos de 0.1, esto lo pueden modificar ustedes
x0=103135; %el valor inicial de x es 3, es decir x(t0)=x(0)=3
y0=10431; %el valor inicial de y es 4, es decir y(t0)=y(0)=4
t= a:h:b; %Creo un vector con ebtrada inicial a, entrada final b y dando saltos de h
for i=1:length(t) %Recorro todas las entradas del vector que cree ahorita
    zf = RungeKutta_Vec(f,[a,t(i)],[x0,y0],h); %Calculo cuanto es X y Y evaluados en el valor de la iteracón t(i)
    x(i) = zf(1); %Guardo el valor de X(i) en la i-ésima entrada de X (Valga la redundancia)
    y(i) = zf(2); %Guardo el valor de Y(i) en la i-ésima entrada de Y (Valga la redundancia)
end
plot(t,x); %Teniendo X y Y evaluados en todos los puntos de t (lo que hizo el for) ploteo Y con respecto a X
%Si quieren pueden plotear X con respecto a t o Y con respecto a t para
%jugar un poco con eso
hold on 
plot(t,y);
hold off
legend("S","I")