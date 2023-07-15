CREATE DATABASE eoms;
-- \connect eoms

-- DROP TABLE IF EXISTS "order_item";
-- DROP TABLE IF EXISTS "item";
-- DROP TABLE IF EXISTS "order";
-- DROP TABLE IF EXISTS "customer";

--
-- TODO: Make multi-customer / multi-user
--

-- CREATE TABLE company (
--     id SERIAL PRIMARY KEY,
--     company_name TEXT
-- );

-- CREATE TABLE company_user (
--     id SERIAL PRIMARY KEY,
--     company_id SERIAL REFERENCES company(id),
--     user_id SERIAL REFERENCES user(id)
-- );

-- CREATE TABLE user (
--     id SERIAL PRIMARY KEY,
--     email_address TEXT,
--     `password` TEXT
-- );

-- --
-- -- Orders
-- --

-- CREATE TABLE "order"(
--     id SERIAL PRIMARY KEY,
--     order_customer_id SERIAL,
--     order_reference TEXT,
--     order_status TEXT,
--     updated_on TIMESTAMPTZ,
--     created_on TIMESTAMPTZ,
--     FOREIGN KEY(order_customer_id) REFERENCES customer(id)
-- );

-- CREATE TABLE order_item(
--     id SERIAL PRIMARY KEY,
--     order_id SERIAL,
--     item_id SERIAL,
--     FOREIGN KEY(order_id) REFERENCES "order"(id),
--     FOREIGN KEY(item_id) REFERENCES item(id)
-- );
