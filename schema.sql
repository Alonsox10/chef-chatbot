CREATE TABLE users(
	id SERIAL  PRIMARY KEY NOT NULL,
	nombre VARCHAR(100) NOT NULL,
	fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP	
);


CREATE TABLE categoria(
	id_categoria SERIAL PRIMARY KEY NOT NULL,
	nombre VARCHAR(100) NOT NULL
);


CREATE TABLE recetas(
	id_receta SERIAL PRIMARY KEY NOT NULL,
	nombre VARCHAR(150) NOT NULL,
	descripcion TEXT NOT NULL,
	tiempo_preparacion INT,
	dificultad VARCHAR(50),
	id_categoria INT,
	FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria)
	ON DELETE SET NULL
);


CREATE TABLE ingredientes(
	id_ingrediente SERIAL PRIMARY KEY NOT NULL,
	nombre VARCHAR(100)
)

CREATE TABLE receta_ingrediente(
	id_receta INT NOT NULL
	id_ingrediente INT NOT NULL
	cantidad 
)


CREATE TABLE receta_ingrediente (
    id_receta INT NOT NULL,
    id_ingrediente INT NOT NULL,
    PRIMARY KEY (id_receta, id_ingrediente),
    FOREIGN KEY (id_receta) REFERENCES recetas(id_receta) ON DELETE CASCADE,
    FOREIGN KEY (id_ingrediente) REFERENCES ingredientes(id_ingrediente) ON DELETE CASCADE
);



INSERT INTO ingredientes (nombre) VALUES
('pollo'),
('arroz'),
('ajo'),
('cebolla'),
('tomate'),
('papa'),
('zanahoria'),
('carne'),
('pescado'),
('huevo'),
('leche'),
('queso'),
('mantequilla'),
('aceite'),
('sal'),
('pimienta'),
('azucar'),
('harina'),
('limon'),
('vinagre'),
('perejil'),
('cilantro'),
('oregano'),
('albahaca'),
('comino'),
('aji'),
('chile'),
('pimiento'),
('brocoli'),
('coliflor'),
('espinaca'),
('lechuga'),
('pepino'),
('apio'),
('maiz'),
('frijoles'),
('lentejas'),
('garbanzos'),
('quinoa'),
('fideos'),
('pan'),
('jamon'),
('tocino'),
('salchicha'),
('atun'),
('mariscos'),
('calamar'),
('langostinos'),
('yogur'),
('crema'),
('chocolate'),
('vainilla'),
('miel'),
('canela'),
('clavo'),
('nuez'),
('almendra'),
('mani'),
('coco'),
('piña'),
('manzana'),
('pera'),
('platano'),
('fresa'),
('uva'),
('sandia'),
('melon'),
('kiwi'),
('mango'),
('papaya'),
('aguacate'),
('aceitunas'),
('champiñones'),
('setas'),
('calabaza'),
('berenjena'),
('zucchini'),
('remolacha'),
('rabano'),
('cebollin'),
('jengibre'),
('soya'),
('salsa de soja'),
('mostaza'),
('ketchup'),
('mayonesa'),
('salsa picante'),
('caldo de pollo'),
('caldo de carne'),
('caldo de verduras'),
('gelatina'),
('maicena'),
('levadura'),
('polvo de hornear'),
('gelatina sin sabor'),
('azucar morena'),
('azucar glas');




INSERT INTO recetas (nombre, descripcion, tiempo_preparacion, dificultad) VALUES
('Arroz con pollo', 'Receta clásica con arroz y pollo', 45, 'Media'),
('Pollo al horno', 'Pollo horneado con especias', 60, 'Fácil'),
('Pasta con tomate', 'Pasta con salsa de tomate casera', 30, 'Fácil'),
('Sopa de verduras', 'Sopa nutritiva de vegetales', 40, 'Fácil'),
('Carne guisada', 'Carne cocida a fuego lento', 90, 'Media'),
('Pescado a la plancha', 'Pescado cocinado con poco aceite', 25, 'Fácil'),
('Tortilla de huevo', 'Huevos batidos con ingredientes', 15, 'Fácil'),
('Ensalada fresca', 'Ensalada de vegetales variados', 10, 'Fácil'),
('Arroz chaufa', 'Arroz salteado estilo oriental', 35, 'Media'),
('Pollo frito', 'Pollo crujiente frito', 50, 'Media'),

('Lentejas guisadas', 'Lentejas con verduras', 60, 'Fácil'),
('Garbanzos estofados', 'Garbanzos cocidos con especias', 70, 'Media'),
('Pizza casera', 'Pizza hecha en casa', 80, 'Media'),
('Hamburguesa casera', 'Carne molida con pan', 30, 'Fácil'),
('Tacos de carne', 'Tacos con carne sazonada', 35, 'Fácil'),
('Arroz con mariscos', 'Arroz con mezcla de mariscos', 50, 'Media'),
('Pollo a la parrilla', 'Pollo asado a la parrilla', 45, 'Fácil'),
('Puré de papa', 'Papa triturada con mantequilla', 25, 'Fácil'),
('Crema de zanahoria', 'Sopa cremosa de zanahoria', 30, 'Fácil'),
('Caldo de pollo', 'Sopa caliente de pollo', 60, 'Fácil'),

('Spaghetti bolognesa', 'Pasta con carne y tomate', 40, 'Fácil'),
('Lasagna', 'Pasta en capas con carne y queso', 90, 'Difícil'),
('Risotto', 'Arroz cremoso italiano', 50, 'Media'),
('Paella', 'Arroz con mariscos y especias', 70, 'Difícil'),
('Pollo al curry', 'Pollo con salsa especiada', 45, 'Media'),
('Sopa de tomate', 'Sopa caliente de tomate', 30, 'Fácil'),
('Ensalada de pollo', 'Pollo con vegetales', 20, 'Fácil'),
('Sandwich mixto', 'Pan con jamón y queso', 10, 'Fácil'),
('Omelette', 'Huevos rellenos', 15, 'Fácil'),
('Empanadas', 'Masa rellena horneada o frita', 50, 'Media'),

-- (continúan más recetas...)
('Pollo con papas', 'Pollo acompañado con papas', 50, 'Fácil'),
('Carne al horno', 'Carne asada con especias', 80, 'Media'),
('Pescado al vapor', 'Pescado cocido al vapor', 25, 'Fácil'),
('Ensalada de frutas', 'Mezcla de frutas frescas', 15, 'Fácil'),
('Panqueques', 'Masa dulce cocida en sartén', 20, 'Fácil'),
('Arroz blanco', 'Arroz simple cocido', 20, 'Fácil'),
('Pollo con arroz', 'Plato básico de pollo y arroz', 40, 'Fácil'),
('Sopa de fideos', 'Caldo con pasta', 30, 'Fácil'),
('Carne salteada', 'Carne con verduras salteadas', 35, 'Media'),
('Pollo teriyaki', 'Pollo con salsa japonesa', 40, 'Media'),

('Sushi básico', 'Arroz con pescado crudo', 60, 'Difícil'),
('Ceviche', 'Pescado marinado en limón', 25, 'Media'),
('Ají de gallina', 'Pollo en salsa cremosa', 50, 'Media'),
('Lomo saltado', 'Carne salteada con papas', 35, 'Fácil'),
('Tallarines verdes', 'Pasta con salsa de espinaca', 40, 'Fácil'),
('Arroz tapado', 'Arroz relleno de carne', 45, 'Media'),
('Seco de carne', 'Carne cocida con cilantro', 70, 'Media'),
('Pollo broaster', 'Pollo frito crujiente', 50, 'Media'),
('Caldo de gallina', 'Sopa tradicional', 80, 'Fácil'),
('Chaufa de pollo', 'Arroz frito con pollo', 35, 'Fácil'),

('Hamburguesa de pollo', 'Pollo molido en pan', 30, 'Fácil'),
('Pizza pepperoni', 'Pizza con pepperoni', 40, 'Fácil'),
('Pasta al pesto', 'Pasta con albahaca', 30, 'Fácil'),
('Sopa de lentejas', 'Sopa espesa de lentejas', 50, 'Fácil'),
('Pollo al limón', 'Pollo con toque cítrico', 40, 'Fácil'),
('Arroz integral', 'Arroz más saludable', 35, 'Fácil'),
('Carne con verduras', 'Salteado de carne y vegetales', 35, 'Fácil'),
('Pescado frito', 'Pescado crocante', 30, 'Fácil'),
('Ensalada César', 'Lechuga con pollo y aderezo', 25, 'Fácil'),
('Pan con pollo', 'Sandwich de pollo', 15, 'Fácil')


INSERT INTO receta_ingrediente (id_receta, id_ingrediente, cantidad, unidad)
SELECT
    r.id_receta,
    i.id_ingrediente,
    (random() * 500 + 50)::int,
    'gramos'
FROM recetas r
JOIN LATERAL (
    SELECT id_ingrediente
    FROM ingredientes
    ORDER BY random()
    LIMIT 6
) i ON true;


SELECT COUNT(*) FROM recetas


INSERT INTO recetas (nombre, descripcion, tiempo_preparacion, dificultad, id_categoria) VALUES
('Pollo al horno', 'Pollo cocinado al horno con especias', 60, 'media', NULL),
('Pollo a la plancha', 'Pollo cocinado a la plancha bajo en grasa', 20, 'facil', NULL),
('Sopa de pollo', 'Sopa caliente con pollo y verduras', 45, 'facil', NULL),
('Pollo frito', 'Pollo crujiente frito en aceite', 30, 'media', NULL),
('Pollo con papas', 'Pollo acompañado con papas fritas', 50, 'facil', NULL),
('Pollo al curry', 'Pollo cocinado con salsa curry', 40, 'media', NULL),
('Pollo a la parrilla', 'Pollo asado a la parrilla', 35, 'facil', NULL),
('Ensalada con pollo', 'Ensalada fresca con trozos de pollo', 15, 'facil', NULL),
('Tacos de pollo', 'Tacos rellenos de pollo sazonado', 25, 'media', NULL),
('Pollo teriyaki', 'Pollo con salsa teriyaki estilo asiático', 30, 'media', NULL);




DELETE FROM ingredientes WHERE id_ingrediente = 88;


ALTER TABLE ingredientes ADD CONSTRAINT unique_nombre UNIQUE(nombre);

INSERT INTO receta_ingrediente (id_receta, id_ingrediente, cantidad, unidad)
SELECT 
    id_receta,
    1,  -- ← usa el ID REAL de pollo
    (random() * 200 + 100)::int,
    'gramos'
FROM recetas;


SELECT r.nombre
FROM recetas r
JOIN receta_ingrediente ri ON r.id_receta = ri.id_receta
JOIN ingredientes i ON ri.id_ingrediente = i.id_ingrediente
WHERE i.nombre ILIKE '%pollo%';