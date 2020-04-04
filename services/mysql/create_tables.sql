CREATE TABLE run_state(
	flag VARCHAR(100),
	state BOOLEAN,
	PRIMARY KEY (flag)
);

INSERT INTO run_state (flag,state) VALUES ('running particles',false);

CREATE TABLE functions (
	id INT,
	function VARCHAR(1000),
	PRIMARY KEY (id)
);

INSERT INTO functions (id,function) VALUES (1,'Z = (5.*sin(X./10)+5*cos(Y./10)+5.*sin(exp(Y.^2./10)+exp(X.^2./10)).*cos(X.*Y))-(0.001.*(X.^2+Y.^2));');

CREATE TABLE iteration_couter (
	id INT AUTO_INCREMENT,
	function_id INT NOT NULL,
	itteration INT NOT NULL,
	max_value FLOAT NOT NULL,
	x FLOAT NOT NULL,
	y FLOAT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (function_id) REFERENCES functions(id)
);