drop table if exists person; -- löschen der tabelle
drop table f exists ort; -- löschen der tabelle

CREATE table person(
    id integer primary key,
    name varchar(50), 
    wohnort integer, -- (1) spalte für fremdschlüssel anlegen
    foreign key (wohnort) references ort(ortid) -- (2) fremdschlüssel definieren
);

CREATE table ort(
    ortid integer primary key,
    bezeichnung varchar(100)
); -- ort muss zuerst angelegt werden, da person mit dem fremdschlüssel davon abhängig ist

INSERT into person values
(1, 'Peter'),
(2, 'Julia'),
(3, 'Finn');

INSERT into ort values
(1, 'Karlsruhe'),
(2, 'Berlin'),
(3, 'Stuttgart');

insert into person values (1, 'Lara'); -- fehlermeldung wegen duplicate key

insert into person values (4, 'Lara');

select * from person;
