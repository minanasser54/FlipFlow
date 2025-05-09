BEGIN;
--
-- Create model Transaction
--
CREATE TABLE "Market_transaction" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "transaction_type" varchar(10) NOT NULL, "amount" decimal NOT NULL, "created_at" datetime NOT NULL, "from_approve" bool NOT NULL, "to_approve" bool NOT NULL, "admin_approve" bool NOT NULL, "user_from_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "user_to_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "Market_transaction_items" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "transaction_id" bigint NOT NULL REFERENCES "Market_transaction" ("id") DEFERRABLE INITIALLY DEFERRED, "item_id" bigint NOT NULL REFERENCES "Item_item" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "Market_transaction_user_from_id_881516c1" ON "Market_transaction" ("user_from_id");
CREATE INDEX "Market_transaction_user_to_id_808af854" ON "Market_transaction" ("user_to_id");
CREATE UNIQUE INDEX "Market_transaction_items_transaction_id_item_id_1fef6597_uniq" ON "Market_transaction_items" ("transaction_id", "item_id");
CREATE INDEX "Market_transaction_items_transaction_id_94d64cc4" ON "Market_transaction_items" ("transaction_id");
CREATE INDEX "Market_transaction_items_item_id_bf91a943" ON "Market_transaction_items" ("item_id");
COMMIT;
