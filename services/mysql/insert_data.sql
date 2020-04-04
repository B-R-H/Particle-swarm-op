INSERT INTO run_state (flag,state)
VALUES ('running particles',false)
INSERT INTO functions (id,function)
VALUES (1,'Z = (5.*sin(X./10)+5*cos(Y./10)+5.*sin(exp(Y.^2./10)+exp(X.^2./10)).*cos(X.*Y))-(0.001.*(X.^2+Y.^2)); [(-100,-100),(100,100)]')