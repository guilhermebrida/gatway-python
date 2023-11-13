
CREATE TABLE IF NOT EXISTS public.iridium
(
    "received_message" text COLLATE pg_catalog."default" ,
    reception_datetime timestamp with time zone DEFAULT timezone('America/Sao_Paulo', now())
    );
INSERT INTO public.iridium ("received_message") VALUES ('teste');

