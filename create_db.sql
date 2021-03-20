BEGIN;
--
-- Create model Customer
--
CREATE TABLE "customer" ("customer_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(191) NOT NULL, "email" varchar(191) NOT NULL UNIQUE);
--
-- Create model Order
--
CREATE TABLE "order" ("order_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "creation_date" date NOT NULL, "delivery_address" varchar(191) NOT NULL, "total" decimal NOT NULL, "customer_id" integer NOT NULL REFERENCES "customer" ("customer_id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Product
--
CREATE TABLE "product" ("product_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(191) NOT NULL, "product_description" varchar(191) NOT NULL, "price" decimal NOT NULL);
--
-- Create model OrderDetail
--
CREATE TABLE "order_detail" ("order_detail_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "product_description" varchar(191) NOT NULL, "price" decimal NOT NULL, "quantity" integer NOT NULL, "order_id" integer NOT NULL REFERENCES "order" ("order_id") DEFERRABLE INITIALLY DEFERRED, "product_id" integer NOT NULL REFERENCES "product" ("product_id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model CustomerProduct
--
CREATE TABLE "customer_product" ("customer_product_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customer_id" integer NOT NULL REFERENCES "customer" ("customer_id") DEFERRABLE INITIALLY DEFERRED, "product_id" integer NOT NULL REFERENCES "product" ("product_id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "order_customer_id_9da9253f" ON "order" ("customer_id");
CREATE INDEX "order_detail_order_id_b97dfbdf" ON "order_detail" ("order_id");
CREATE INDEX "order_detail_product_id_009a48e3" ON "order_detail" ("product_id");
CREATE UNIQUE INDEX "customer_product_product_id_customer_id_7b1f8c75_uniq" ON "customer_product" ("product_id", "customer_id");
CREATE INDEX "customer_product_customer_id_a7290aed" ON "customer_product" ("customer_id");
CREATE INDEX "customer_product_product_id_3b72b3ff" ON "customer_product" ("product_id");
COMMIT;
