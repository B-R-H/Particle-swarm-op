CREATE TABLE functions (
	id INT,
	function VARCHAR(1000),
	PRIMARY KEY (id)
);

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

CREATE TABLE run_state(
	flag VARCHAR(100),
	state BOOLEAN,
	PRIMARY KEY (flag)
);