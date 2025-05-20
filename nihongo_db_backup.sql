--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: hiragana; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hiragana (
    id integer NOT NULL,
    "character" character varying(5) NOT NULL,
    romaji character varying(10) NOT NULL,
    meaning character varying(100),
    pronunciation character varying(100)
);


ALTER TABLE public.hiragana OWNER TO postgres;

--
-- Name: hiragana_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hiragana_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.hiragana_id_seq OWNER TO postgres;

--
-- Name: hiragana_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hiragana_id_seq OWNED BY public.hiragana.id;


--
-- Name: kanji; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kanji (
    id integer NOT NULL,
    "character" character varying(5) NOT NULL,
    onyomi character varying(100),
    kunyomi character varying(100),
    meaning text NOT NULL
);


ALTER TABLE public.kanji OWNER TO postgres;

--
-- Name: kanji_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.kanji_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.kanji_id_seq OWNER TO postgres;

--
-- Name: kanji_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.kanji_id_seq OWNED BY public.kanji.id;


--
-- Name: katakana; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.katakana (
    id integer NOT NULL,
    "character" character varying(5) NOT NULL,
    romaji character varying(10) NOT NULL,
    meaning character varying(100),
    pronunciation character varying(100)
);


ALTER TABLE public.katakana OWNER TO postgres;

--
-- Name: katakana_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.katakana_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.katakana_id_seq OWNER TO postgres;

--
-- Name: katakana_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.katakana_id_seq OWNED BY public.katakana.id;


--
-- Name: task_imagen; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task_imagen (
    id integer NOT NULL,
    image_path text NOT NULL,
    category character varying(50) NOT NULL,
    japanese_word character varying(100) NOT NULL,
    pronunciation character varying(100) NOT NULL
);


ALTER TABLE public.task_imagen OWNER TO postgres;

--
-- Name: task_imagen_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.task_imagen_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.task_imagen_id_seq OWNER TO postgres;

--
-- Name: task_imagen_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.task_imagen_id_seq OWNED BY public.task_imagen.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    password_hash character varying(128) NOT NULL,
    email character varying(120)
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_id_seq OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: word; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.word (
    id integer NOT NULL,
    japanese character varying(100) NOT NULL,
    english character varying(100) NOT NULL,
    pronunciation text
);


ALTER TABLE public.word OWNER TO postgres;

--
-- Name: word_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.word_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.word_id_seq OWNER TO postgres;

--
-- Name: word_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.word_id_seq OWNED BY public.word.id;


--
-- Name: hiragana id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hiragana ALTER COLUMN id SET DEFAULT nextval('public.hiragana_id_seq'::regclass);


--
-- Name: kanji id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kanji ALTER COLUMN id SET DEFAULT nextval('public.kanji_id_seq'::regclass);


--
-- Name: katakana id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.katakana ALTER COLUMN id SET DEFAULT nextval('public.katakana_id_seq'::regclass);


--
-- Name: task_imagen id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_imagen ALTER COLUMN id SET DEFAULT nextval('public.task_imagen_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: word id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.word ALTER COLUMN id SET DEFAULT nextval('public.word_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
9acba5d132b8
\.


--
-- Data for Name: hiragana; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hiragana (id, "character", romaji, meaning, pronunciation) FROM stdin;
1	あ	a	first Hiragana character	ah
2	い	i	Second Hiragana character	ee
3	う	u	Third Hiragana character	oo
4	あ	a	First Hiragana character	ah
5	い	i	Second Hiragana character	ee
6	う	u	Third Hiragana character	oo
7	え	e	Fourth Hiragana character	eh
8	お	o	Fifth Hiragana character	oh
9	か	ka	Represents "ka" sound	ka
10	き	ki	Represents "ki" sound	kee
11	く	ku	Represents "ku" sound	koo
12	け	ke	Represents "ke" sound	keh
13	こ	ko	Represents "ko" sound	koh
14	さ	sa	Represents "sa" sound	sa
15	し	shi	Represents "shi" sound	shee
16	す	su	Represents "su" sound	soo
17	せ	se	Represents "se" sound	seh
18	そ	so	Represents "so" sound	soh
19	た	ta	Represents "ta" sound	ta
20	ち	chi	Represents "chi" sound	chee
21	つ	tsu	Represents "tsu" sound	tsoo
22	て	te	Represents "te" sound	teh
23	と	to	Represents "to" sound	toh
24	な	na	Represents "na" sound	na
25	に	ni	Represents "ni" sound	nee
26	ぬ	nu	Represents "nu" sound	noo
27	ね	ne	Represents "ne" sound	neh
28	の	no	Represents "no" sound	noh
29	は	ha	Represents "ha" sound	ha
30	ひ	hi	Represents "hi" sound	hee
31	ふ	fu	Represents "fu" sound	foo
32	へ	he	Represents "he" sound	heh
33	ほ	ho	Represents "ho" sound	hoh
34	ま	ma	Represents "ma" sound	ma
35	み	mi	Represents "mi" sound	mee
36	む	mu	Represents "mu" sound	moo
37	め	me	Represents "me" sound	meh
38	も	mo	Represents "mo" sound	moh
39	や	ya	Represents "ya" sound	ya
40	ゆ	yu	Represents "yu" sound	yoo
41	よ	yo	Represents "yo" sound	yoh
42	ら	ra	Represents "ra" sound	ra
43	り	ri	Represents "ri" sound	ree
44	る	ru	Represents "ru" sound	roo
45	れ	re	Represents "re" sound	reh
46	ろ	ro	Represents "ro" sound	roh
47	わ	wa	Represents "wa" sound	wa
48	を	wo	Represents "wo" sound (used as particle)	woh
49	ん	n	Represents "n" sound	n
\.


--
-- Data for Name: kanji; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kanji (id, "character", onyomi, kunyomi, meaning) FROM stdin;
1	一	イチ, イツ	ひと-つ	One
2	二	ニ	ふた-つ	Two
3	三	サン	みっ-つ	Three
4	一	ichi	hito(tsu)	one
5	二	ni	futa(tsu)	two
6	三	san	mi(tsu)	three
7	四	shi	yo(tsu)	four
8	五	go	itsu(tsu)	five
9	六	roku	mu(tsu)	six
10	七	shichi	nana(tsu)	seven
11	八	hachi	yatsu	eight
12	九	kyuu	kokono(tsu)	nine
13	十	juu	to(o)	ten
14	百	hyaku	momo(tsu)	hundred
15	千	sen	chi	thousand
16	万	man	yorozu	ten thousand
17	円	en	maru	yen, circle
18	力	ryoku	chikara	power
19	男	dan	otoko	man
20	女	jo	onna	woman
21	子	shi	ko	child
22	手	shu	te	hand
23	足	soku	ashi	foot
24	目	moku	me	eye
25	耳	ji	mimi	ear
26	口	kou	kuchi	mouth
27	心	shin	kokoro	heart, mind
28	天	ten	ame	heaven
29	地	chi	ji	earth
30	火	ka	hi	fire
31	水	sui	mizu	water
32	木	moku	ki	tree
33	金	kin	kane	gold, money
34	土	do	tsuchi	earth, soil
35	生	sei	ikiru	life
36	学	gaku	manabu	study, learning
37	校	kou	kou	school
38	先	sen	saki	previous, ahead
39	年	nen	toshi	year
40	月	getsu	tsuki	month, moon
41	日	nichi	hi	day, sun
42	時	ji	toki	time
43	分	bun	fun	minute
44	半	han	naka	half
45	右	u	migi	right
46	左	sa	hidari	left
47	中	chuu	naka	middle
48	大	dai	oo	big
49	小	shou	chii	small
50	長	chou	naga	long
51	短	tan	mijika	short
52	新	shin	atarashi	new
53	古	ko	furu	old
54	高	kou	takai	high, expensive
55	安	an	yasu	cheap, safe
56	多	ta	oo	many
57	少	shou	suku	few
58	楽	raku	tanoshi	comfortable, music
59	悪	aku	waru	bad
60	正	sei	tadashii	correct
61	悪	aku	warui	evil
62	青	sei	ao	blue
63	赤	aka	aka	red
64	白	haku	shiro	white
65	黒	koku	kuro	black
66	明	mei	akarui	bright
67	暗	an	kurai	dark
68	強	kyou	tsuyoi	strong
69	弱	jaku	yowai	weak
70	大	dai	oo	big
71	小	shou	chii	small
72	高	kou	takai	high
73	低	tei	hikui	low
74	親	shin	oya	parent
75	兄	kei	ani	older brother
76	弟	tei	otouto	younger brother
77	姉	shi	ane	older sister
78	妹	mai	imouto	younger sister
79	友	yuu	tomo	friend
80	語	go	kataru	language, word
81	道	dou	michi	way
82	風	fuu	kaze	wind
83	車	sha	kuruma	car
84	電	den	den	electric
85	話	wa	hanasu	talk
86	空	kuu	sora	sky
87	海	kai	umi	sea
88	山	san	yama	mountain
89	川	sen	kawa	river
90	森	shin	mori	forest
91	田	den	ta	field
92	花	ka	hana	flower
93	草	sou	kusa	grass
94	石	seki	ishi	stone
95	金	kin	kane	gold
96	土	do	tsuchi	earth
97	銭	sen	zen	money
98	町	machi	machi	town
99	村	son	mura	village
100	街	gai	machi	street
101	日	nichi, jitsu	hi, bi	day, sun
102	月	getsu, gatsu	tsuki	moon, month
103	火	ka	hi	fire
104	水	sui	mizu	water
105	木	moku, boku	ki	tree, wood
106	金	kin, kon	kane	gold, money
107	土	do, to	tsuchi	earth, soil
108	空	kuu	sora	sky, air
109	天	ten	ame, ama	heaven
110	風	fuu, kaze	kaze	wind
111	山	san, zan	yama	mountain
112	川	sen, kawa	kawa	river
113	海	kai	umi	sea, ocean
114	島	tou	shima	island
115	道	dou, tou	michi	way, road
116	車	sha	kuruma	car
117	電	den	\N	electricity
118	話	wa	hanashi	talk, speak
119	音	on	oto	sound
120	言	gen, gon	iu	say, word
121	書	sho	kaku	write
122	読	doku	yomu	read
123	学	gaku	manabu	study, learning
124	生	sei, shou	ikiru	life, live
125	死	shi	shinu	death
126	男	dan, nan	otoko	man
127	女	jo, nyo	onna	woman
128	子	shi, su	ko	child
129	父	fu	chichi	father
130	母	bo	haha	mother
131	友	yuu	tomodachi	friend
132	人	jin, nin	hito	person
133	手	shu	te	hand
134	足	soku	ashi	foot
135	目	moku	me	eye
136	耳	ji	mimi	ear
137	口	kou	kuchi	mouth
138	鼻	bi	hana	nose
139	体	tai	karada	body
140	心	shin	kokoro	heart, mind
141	顔	gan	kao	face
142	声	sei	koe	voice
143	色	shiki	iro	color
144	食	shoku	taberu	eat, food
145	飲	in	nomu	drink
146	買	bai	kau	buy
147	売	bai	uru	sell
148	店	ten	mise	shop, store
149	道	dou	michi	road, way
150	駅	eki	\N	station
151	町	machi	\N	town
152	村	son	mura	village
153	学校	gakkou	\N	school
154	会社	kaisha	\N	company
155	事	ji	koto	thing, matter
156	時	ji	toki	time, hour
157	今	kon	ima	now
158	前	zen	mae	before, in front
159	後	go	ato	after, behind
160	上	jou	ue	up, above
161	下	ka, ge	shita	down, below
162	左	sa	hidari	left
163	右	u	migi	right
\.


--
-- Data for Name: katakana; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.katakana (id, "character", romaji, meaning, pronunciation) FROM stdin;
1	ア	a	First Katakana character	ah
2	イ	i	Second Katakana character	ee
3	ウ	u	Third Katakana character	oo
4	エ	e	Fourth Katakana character	eh
5	オ	o	Fifth Katakana character	oh
6	カ	ka	Represents "ka" sound	ka
7	キ	ki	Represents "ki" sound	kee
8	ク	ku	Represents "ku" sound	koo
9	ケ	ke	Represents "ke" sound	keh
10	コ	ko	Represents "ko" sound	koh
11	サ	sa	Represents "sa" sound	sa
12	シ	shi	Represents "shi" sound	shee
13	ス	su	Represents "su" sound	soo
14	セ	se	Represents "se" sound	seh
15	ソ	so	Represents "so" sound	soh
16	タ	ta	Represents "ta" sound	ta
17	チ	chi	Represents "chi" sound	chee
18	ツ	tsu	Represents "tsu" sound	tsoo
19	テ	te	Represents "te" sound	teh
20	ト	to	Represents "to" sound	toh
21	ナ	na	Represents "na" sound	na
22	ニ	ni	Represents "ni" sound	nee
23	ヌ	nu	Represents "nu" sound	noo
24	ネ	ne	Represents "ne" sound	neh
25	ノ	no	Represents "no" sound	noh
26	ハ	ha	Represents "ha" sound	ha
27	ヒ	hi	Represents "hi" sound	hee
28	フ	fu	Represents "fu" sound	foo
29	ヘ	he	Represents "he" sound	heh
30	ホ	ho	Represents "ho" sound	hoh
31	マ	ma	Represents "ma" sound	ma
32	ミ	mi	Represents "mi" sound	mee
33	ム	mu	Represents "mu" sound	moo
34	メ	me	Represents "me" sound	meh
35	モ	mo	Represents "mo" sound	moh
36	ヤ	ya	Represents "ya" sound	ya
37	ユ	yu	Represents "yu" sound	yoo
38	ヨ	yo	Represents "yo" sound	yoh
39	ラ	ra	Represents "ra" sound	ra
40	リ	ri	Represents "ri" sound	ree
41	ル	ru	Represents "ru" sound	roo
42	レ	re	Represents "re" sound	reh
43	ロ	ro	Represents "ro" sound	roh
44	ワ	wa	Represents "wa" sound	wa
45	ヲ	wo	Represents "wo" sound (used as particle)	woh
46	ン	n	Represents "n" sound	n
\.


--
-- Data for Name: task_imagen; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task_imagen (id, image_path, category, japanese_word, pronunciation) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, username, password_hash, email) FROM stdin;
1	test_user	hashed_password_example	\N
2	toni	$2b$12$88VBADLwBPmFqOFgSmwUMeSbfRGJrbp.11qpRkOPdtu8Gh0yi3Jyy	velociraptorcazador@me.com
\.


--
-- Data for Name: word; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.word (id, japanese, english, pronunciation) FROM stdin;
10	ねこ	cat	ne-ko
11	いぬ	dog	i-nu
12	さくら	cherry blossom	sa-ku-ra
13	ほん	book	hon
14	やま	mountain	yama
15	うみ	sea	umi
16	さけ	salmon	sa-ke
17	さとう	sugar	sa-to-u
18	きょう	today	kyo-u
19	あさ	morning	a-sa
20	よる	night	yo-ru
21	たべる	to eat	ta-be-ru
22	のむ	to drink	no-mu
23	ねる	to sleep	ne-ru
24	はな	flower	ha-na
25	おおきい	big	oo-ki-i
26	ちいさい	small	chi-i-sa-i
27	あたらしい	new	a-ta-ra-shi-i
28	ふるい	old	fu-ru-i
29	かわいい	cute	ka-wa-i-i
30	たかい	high	ta-ka-i
31	ひくい	low	hi-ku-i
32	あつい	hot	a-tsu-i
33	さむい	cold	sa-mu-i
34	あめ	rain	a-me
35	ゆき	snow	yu-ki
36	からだ	body	ka-ra-da
37	あたま	head	a-ta-ma
38	みみ	ear	mi-mi
39	め	eye	me
40	はし	chopsticks	ha-shi
41	くるま	car	ku-ru-ma
42	でんしゃ	train	den-sha
43	じてんしゃ	bicycle	ji-ten-sha
44	ひこうき	airplane	hi-kou-ki
45	バス	bus	ba-su
46	みせ	store	mi-se
47	レストラン	restaurant	res-to-ran
48	とけい	watch	to-ke-i
49	かばん	bag	ka-ban
50	ぺん	pen	pen
51	えんぴつ	pencil	en-pi-tsu
52	ノート	notebook	no-to
53	けいたい	cell phone	kei-ta-i
54	コンピュータ	computer	kon-pyu-ta
55	テレビ	television	te-re-bi
56	ラジオ	radio	ra-ji-o
57	うた	song	u-ta
58	おんがく	music	on-ga-ku
59	しごと	work	shi-go-to
60	べんきょう	study	ben-kyou
61	だいがく	university	dai-ga-ku
62	しゅくだい	homework	shu-ku-dai
63	おおさか	Osaka	o-o-sa-ka
64	とうきょう	Tokyo	to-u-kyo-u
1	こんにちは	Hello	Konnichiwa
2	ありがとう	Thank you	Arigatou
3	さようなら	Goodbye	Sayounara
\.


--
-- Name: hiragana_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hiragana_id_seq', 49, true);


--
-- Name: kanji_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.kanji_id_seq', 163, true);


--
-- Name: katakana_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.katakana_id_seq', 46, true);


--
-- Name: task_imagen_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.task_imagen_id_seq', 17, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 2, true);


--
-- Name: word_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.word_id_seq', 67, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: hiragana hiragana_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hiragana
    ADD CONSTRAINT hiragana_pkey PRIMARY KEY (id);


--
-- Name: kanji kanji_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kanji
    ADD CONSTRAINT kanji_pkey PRIMARY KEY (id);


--
-- Name: katakana katakana_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.katakana
    ADD CONSTRAINT katakana_pkey PRIMARY KEY (id);


--
-- Name: task_imagen task_imagen_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_imagen
    ADD CONSTRAINT task_imagen_pkey PRIMARY KEY (id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: word word_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.word
    ADD CONSTRAINT word_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

