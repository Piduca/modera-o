PGDMP  ;                    }         	   moderacao    17.4    17.4 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    41098 	   moderacao    DATABASE     o   CREATE DATABASE moderacao WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'pt-PT';
    DROP DATABASE moderacao;
                     postgres    false            �            1259    41110 	   conteudos    TABLE     �   CREATE TABLE public.conteudos (
    id character varying NOT NULL,
    tipo character varying,
    caminho text,
    conteudo text,
    status character varying
);
    DROP TABLE public.conteudos;
       public         heap r       postgres    false            �          0    41110 	   conteudos 
   TABLE DATA           H   COPY public.conteudos (id, tipo, caminho, conteudo, status) FROM stdin;
    public               postgres    false    217   �       W           2606    41116    conteudos conteudos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.conteudos
    ADD CONSTRAINT conteudos_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.conteudos DROP CONSTRAINT conteudos_pkey;
       public                 postgres    false    217            X           1259    41118    ix_conteudos_id    INDEX     C   CREATE INDEX ix_conteudos_id ON public.conteudos USING btree (id);
 #   DROP INDEX public.ix_conteudos_id;
       public                 postgres    false    217            Y           1259    41117    ix_conteudos_tipo    INDEX     G   CREATE INDEX ix_conteudos_tipo ON public.conteudos USING btree (tipo);
 %   DROP INDEX public.ix_conteudos_tipo;
       public                 postgres    false    217            �   �   x���KN�0��u{�;Yr�FB������Bp"���l@#Шk��Y/Zـ5X�ǐ���l8&Do�M߷e8�������U�MGI̙S���<v�D��(e��p��oח��2�䝏BP�!�*�U�S�jY�
�f1�����Ε��d�6�f��?�h�S�rZo���i�׏i���:�˿���Be���_�7���Qr���\-V��LAHZ���d�r���!����_����8�ߢ�4     