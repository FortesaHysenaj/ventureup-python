CREATE TABLE evidenca (
	id serial primary key,
	p_id int references puntori(id),
	check_in timestamp,
	check_out timestamp
);
