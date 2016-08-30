syms x y lambda;
f = (x-1)^2 +y^2 * (y^2-1) + (x-1)*(y^2 - 1);
fx = diff(f,x);
fy = diff(f,y);
fxx = diff(fx,x);
fyy = diff(fy,y);
fxy = diff(fx,y);

fxx
fxy
fyy
[xcr, ycr] = solve(fx, fy);

H = [fxx fxy; fxy fyy];
A = H - (eye(2)*lambda);
d = det(A);
for k = (1:3)
    xcr(k), ycr(k), solve(subs(d, [x, y], [xcr(k), ycr(k)]))
end


        