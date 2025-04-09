-- Table: django_migrations
CREATE TABLE IF NOT EXISTS "django_migrations" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app" VARCHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "applied" DATETIME NOT NULL
);

-- Internal SQLite Sequence Table
CREATE TABLE sqlite_sequence(name, seq);

-- Table: auth_group_permissions
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "group_id" INTEGER NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" INTEGER NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
);

-- Table: auth_user_groups
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" INTEGER NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED
);

-- Table: auth_user_user_permissions
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" INTEGER NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
);

-- Indexes for auth_group_permissions
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq"
ON "auth_group_permissions" ("group_id", "permission_id");

CREATE INDEX "auth_group_permissions_group_id_b120cbf9"
ON "auth_group_permissions" ("group_id");

CREATE INDEX "auth_group_permissions_permission_id_84c5c92e"
ON "auth_group_permissions" ("permission_id");

-- Indexes for auth_user_groups
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq"
ON "auth_user_groups" ("user_id", "group_id");

CREATE INDEX "auth_user_groups_user_id_6a12ed8b"
ON "auth_user_groups" ("user_id");

CREATE INDEX "auth_user_groups_group_id_97559544"
ON "auth_user_groups" ("group_id");

-- Indexes for auth_user_user_permissions
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq"
ON "auth_user_user_permissions" ("user_id", "permission_id");

CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b"
ON "auth_user_user_permissions" ("user_id");

CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c"
ON "auth_user_user_permissions" ("permission_id");

-- Table: django_admin_log
CREATE TABLE IF NOT EXISTS "django_admin_log" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "object_id" TEXT NULL,
    "object_repr" VARCHAR(200) NOT NULL,
    "action_flag" SMALLINT UNSIGNED NOT NULL CHECK ("action_flag" >= 0),
    "change_message" TEXT NOT NULL,
    "content_type_id" INTEGER NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "user_id" INTEGER NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "action_time" DATETIME NOT NULL
);

-- Indexes for django_admin_log
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb"
ON "django_admin_log" ("content_type_id");

CREATE INDEX "django_admin_log_user_id_c564eba6"
ON "django_admin_log" ("user_id");

-- Table: django_content_type
CREATE TABLE IF NOT EXISTS "django_content_type" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app_label" VARCHAR(100) NOT NULL,
    "model" VARCHAR(100) NOT NULL
);

CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq"
ON "django_content_type" ("app_label", "model");

-- Table: auth_permission
CREATE TABLE IF NOT EXISTS "auth_permission" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "content_type_id" INTEGER NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "codename" VARCHAR(100) NOT NULL,
    "name" VARCHAR(255) NOT NULL
);

CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq"
ON "auth_permission" ("content_type_id", "codename");

CREATE INDEX "auth_permission_content_type_id_2f476e4b"
ON "auth_permission" ("content_type_id");

-- Table: auth_group
CREATE TABLE IF NOT EXISTS "auth_group" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" VARCHAR(150) NOT NULL UNIQUE
);

-- Table: auth_user
CREATE TABLE IF NOT EXISTS "auth_user" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "password" VARCHAR(128) NOT NULL,
    "last_login" DATETIME NULL,
    "is_superuser" BOOL NOT NULL,
    "username" VARCHAR(150) NOT NULL UNIQUE,
    "last_name" VARCHAR(150) NOT NULL,
    "email" VARCHAR(254) NOT NULL,
    "is_staff" BOOL NOT NULL,
    "is_active" BOOL NOT NULL,
    "date_joined" DATETIME NOT NULL,
    "first_name" VARCHAR(150) NOT NULL
);

-- Table: django_session
CREATE TABLE IF NOT EXISTS "django_session" (
    "session_key" VARCHAR(40) NOT NULL PRIMARY KEY,
    "session_data" TEXT NOT NULL,
    "expire_date" DATETIME NOT NULL
);

CREATE INDEX "django_session_expire_date_a5c62663"
ON "django_session" ("expire_date");

-- Table: Item_category
CREATE TABLE IF NOT EXISTS "Item_category" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "Category_name" VARCHAR(100) NOT NULL,
    "Category_slug" VARCHAR(50) NULL UNIQUE
);

-- Table: Item_item
CREATE TABLE IF NOT EXISTS "Item_item" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "Item_name" VARCHAR(100) NOT NULL,
    "Item_description" TEXT NOT NULL,
    "Item_price" DECIMAL NOT NULL,
    "Item_quantity" INTEGER NOT NULL,
    "Item_published" BOOL NOT NULL,
    "Item_createdat" DATETIME NOT NULL,
    "Item_slug" VARCHAR(50) NULL UNIQUE,
    "Item_category_id" BIGINT NULL REFERENCES "Item_category" ("id") DEFERRABLE INITIALLY DEFERRED,
    "Item_img" VARCHAR(100) NULL,
    "Item_owner_id" INTEGER NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "Item_item_Item_category_id_6f28564b"
ON "Item_item" ("Item_category_id");

CREATE INDEX "Item_item_Item_owner_id_995d40b6"
ON "Item_item" ("Item_owner_id");

-- Table: accounts_profile
CREATE TABLE IF NOT EXISTS "accounts_profile" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "slug" VARCHAR(50) NULL,
    "bio" TEXT NOT NULL,
    "country" VARCHAR(2) NOT NULL,
    "address" VARCHAR(100) NOT NULL,
    "birth_date" DATE NULL,
    "joindate" DATETIME NOT NULL,
    "user_id" INTEGER NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "balance" DECIMAL NOT NULL,
    "img" VARCHAR(100) NULL
);

CREATE INDEX "accounts_profile_slug_8a7a322e"
ON "accounts_profile" ("slug");

-- Table: Market_transaction
CREATE TABLE IF NOT EXISTS "Market_transaction" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "transaction_type" VARCHAR(10) NOT NULL,
    "amount" DECIMAL NOT NULL,
    "created_at" DATETIME NOT NULL,
    "from_approve" BOOL NOT NULL,
    "to_approve" BOOL NOT NULL,
    "admin_approve" BOOL NOT NULL,
    "user_from_id" INTEGER NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "user_to_id" INTEGER NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "transaction_status" VARCHAR(10) NOT NULL,
    "items_id" BIGINT NULL REFERENCES "Item_item" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "Market_transaction_user_from_id_881516c1"
ON "Market_transaction" ("user_from_id");

CREATE INDEX "Market_transaction_user_to_id_808af854"
ON "Market_transaction" ("user_to_id");

CREATE INDEX "Market_transaction_items_id_c1c0ee37"
ON "Market_transaction" ("items_id");
