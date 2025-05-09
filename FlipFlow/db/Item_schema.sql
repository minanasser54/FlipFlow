BEGIN;
--
-- Create model Category
--
CREATE TABLE "Item_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Category_name" varchar(100) NOT NULL, "Category_slug" varchar(50) NULL UNIQUE);
--
-- Create model Item
--
CREATE TABLE "Item_item" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Item_name" varchar(100) NOT NULL, "Item_description" text NOT NULL, "Item_price" decimal NOT NULL, "Item_quantity" integer NOT NULL, "Item_published" bool NOT NULL, "Item_createdat" datetime NOT NULL, "Item_slug" varchar(50) NULL UNIQUE, "Item_category_id" bigint NULL REFERENCES "Item_category" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "Item_item_Item_category_id_6f28564b" ON "Item_item" ("Item_category_id");
COMMIT;
