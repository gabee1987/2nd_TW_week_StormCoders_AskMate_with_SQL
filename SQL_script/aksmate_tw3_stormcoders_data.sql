--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6
-- StormCoders modifications

ALTER TABLE IF EXISTS ONLY public.question DROP CONSTRAINT IF EXISTS pk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS pk_answer_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS fk_question_id CASCADE;

DROP TABLE IF EXISTS public.question;
DROP SEQUENCE IF EXISTS public.question_id_seq;
CREATE TABLE question (
    id serial NOT NULL,
    submission_time timestamp without time zone,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text,
    askmate_user_id integer

);

DROP TABLE IF EXISTS public.answer;
DROP SEQUENCE IF EXISTS public.answer_id_seq;
CREATE TABLE answer (
    id serial NOT NULL,
    submission_time timestamp without time zone,
    vote_number integer,
    question_id integer,
    message text,
    image text,
    askmate_user_id integer,
    acceptance boolean
);

DROP TABLE IF EXISTS public.askmate_user;
DROP SEQUENCE IF EXISTS public.user_id_seq;
CREATE TABLE askmate_user (
    id serial NOT NULL PRIMARY KEY,
    first_name varchar (255),
    last_name varchar (255),
    username varchar (15) UNIQUE NOT NULL,
    birth_date date,
    e_mail varchar UNIQUE,
    reputation integer

);

DROP TABLE IF EXISTS public.comment;
DROP SEQUENCE IF EXISTS public.comment_id_seq;

DROP TABLE IF EXISTS public.question_tag;


DROP TABLE IF EXISTS public.tag;
DROP SEQUENCE IF EXISTS public.tag_id_seq;



ALTER TABLE ONLY question
    ADD CONSTRAINT pk_question_id PRIMARY KEY (id);

ALTER TABLE ONLY question
    ADD CONSTRAINT fk_askmate_user_id FOREIGN KEY (askmate_user_id) REFERENCES askmate_user(id);
    
ALTER TABLE ONLY answer
    ADD CONSTRAINT pk_answer_id PRIMARY KEY (id);

ALTER TABLE ONLY answer
    ADD CONSTRAINT fk_askmate_user_id FOREIGN KEY (askmate_user_id) REFERENCES askmate_user(id);

ALTER TABLE ONLY answer
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES question(id);
    





