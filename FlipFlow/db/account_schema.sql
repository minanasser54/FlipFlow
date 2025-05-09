BEGIN;
--
-- Create model Profile
--
CREATE TABLE "accounts_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "img" varchar(100) NULL, "slug" varchar(50) NULL, "bio" text NOT NULL, "country" varchar(2) NOT NULL, "address" varchar(100) NOT NULL, "birth_date" date NULL, "joindate" datetime NOT NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "accounts_profile_slug_8a7a322e" ON "accounts_profile" ("slug");
COMMIT;
