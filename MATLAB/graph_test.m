
axis([-4 4 -4 4]);
[X,Y]=meshgrid(-4:.2:4,-4:.2:4);
Z=(X.^2 +Y.^2);
[DX,DY]=gradient(Z,.2,.2);
axis([-2 2 -2 2])
subplot(1,2,1), surf(X,Y,Z)
subplot(2,2,2), contour(X,Y,Z,10)
subplot(2,2,4), quiver(X,Y,DX,DY)