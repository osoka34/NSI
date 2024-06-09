CREATE table named_constants (
    id serial primary key,
    const_value varchar(255) not null default '',
    description varchar(255) not null default '',
    const_type varchar(255) not null default '',
    name varchar(255) not null default '',
    dimension varchar(255) not null default ''
);



INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (1, '3.141592653589793238463D0', 'Число ПИ', 'математическая', 'pi', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (2, '6.283185307179586476925D0', 'два ПИ', 'математическая', 'TWOPI', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (3, '1.570796326794896619231D0', 'Половина ПИ', 'математическая', 'HALFPI', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (4, '1.745329251994329576924D-2', 'Переводной коэффициент из градусов в радианы', 'математическая', 'CDEGRAD', 'RAD/DEG');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (5, '4.848136811095359935899D-6', 'Переводной коэффициент из угловых секунд в радианы', 'математическая', 'CARCRAD', 'RAD/ARCSECOND');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (6, '0,0000727220521664303', 'Переводной коэффициент из  секунд в радианы', 'математическая', 'CTIMRAD', 'RAD/TIME SECOND');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (7, '86400', '', 'математическая', 'SECDAY', 'SECONDS/DAY');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (8, '36525', '', 'математическая', 'JUL_CENT', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (9, '2451545', 'Среднее наклон эклиптики', 'математическая', 'JD2000', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (10, '2,99792458D8', 'Скороть света в вакуме', 'физическая', 'c', 'м/сек');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (11, '298,25765', 'выравнивание полюсов ', 'физическая', 'f', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (12, '6378136,3', 'Экваториальный радиус Земли', 'физическая', 'AE', 'м');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (13, '149597870700', 'Астрономическая единица', 'физическая', 'AU', 'м');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (14, '499,00478383616D0', 'Световое время на единицу расстояния', 'физическая', 'TAUA', 'с');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (15, '0,0000000000667428', 'Гравитационная постоянная', 'физическая', ' G', ' m^3*кг*с^2   ');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (16, '1,327124400409440D20', 'Гелиоцентрическая гравитационная постоянная', 'гравитационная', 'GSUN', ' m^3*кг*с^2   ');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (17, '3,98600436233D14', 'Геоцентрическая гравитационная постоянная', 'гравитационная', 'GEARTH', ' m^3*кг*с^2   ');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (18, '0,0123000371D0 ', 'Соотношение масс: Луны и Земли ', 'гравитационная', 'MU', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (19, '6023597,400017', 'Отношение масс: Солнца и Меркурия', 'гравитационная', 'MMERCURY', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (20, '408523,718655', 'Отношение масс: Солнца к Венере ', 'гравитационная', 'MVENUS', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (21, '3098703,590267D0', 'Отношение масс: Солнце и Марс', 'гравитационная', 'MMARS', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (22, '1047,348625D0', 'Отношение масс: Солнца к Юпитеру ', 'гравитационная', 'MJUPITER', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (23, '3497,901768D0', 'Соотношение масс: Солнца и Сатурна', 'гравитационная', 'MSATURN', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (24, '22902,981613D0', 'Отношение масс: Солнца к Урану ', 'гравитационная', 'MURANUS', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (25, '19412,237346D0', 'Отношение масс: Солнца к Нептун', 'гравитационная', 'MNEPTUNE', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (26, '135836683,767599D0', 'Отношение масс: Солнца к Плутону ', 'гравитационная', 'MPLUTO', 'б/р');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (27, '0,6078D0', '', '', 'H02', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (28, '0,0006D0', '', '', 'H22', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (29, '0,0025D0', '', '', 'HI_1', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (30, '0,292D0', '', '', 'H3', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (31, '0,0022D0', '', '', 'HI_2', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (32, '0,0012D0', '', '', 'L1_1', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (33, '0,0847D0', '', '', 'L02', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (34, '0,0002D0', '', '', 'L22', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (35, '0,0007D0', '', '', 'LI_1', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (36, ' 0,015D0', '', '', 'L3', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (37, '0,0007D0', '', '', 'LI_2', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (38, '0,0024D0', '', '', 'L1_2', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (39, '1,550519768D-8', 'Вспомогательные определяющие константы 1-d(TDB)/d(TCB)', '', 'L_B', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (40, '1,48082686741D-8', 'Среднее значение 1-d(TCG)/d(TCB) ', '', 'L_C', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (41, '6,969290134D-10', 'Вспомогательные определяющие константы 1-d(TT)/d(TCG) ', '', 'L_G', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (42, '-0,0000655', 'Вспомогательные определяющие константы TDB-TCB при T_0 = 2443144.5003725', '', 'TDB_0', '');
INSERT INTO named_constants (id, const_value, description, const_type, name, dimension) VALUES (43, '2443144,5003725D0', '', '', 'T_0', '');
