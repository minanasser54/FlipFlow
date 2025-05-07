

---
## Horizontal
```sql
-- Active users
CREATE TABLE auth_user_active AS
SELECT * FROM auth_user WHERE is_active = 1;

-- Inactive users
CREATE TABLE auth_user_inactive AS
SELECT * FROM auth_user WHERE is_active = 0;

-- Profiles from US
CREATE TABLE accounts_profile_us AS
SELECT * FROM accounts_profile WHERE country = 'US';

-- Profiles from other countries
CREATE TABLE accounts_profile_other AS
SELECT * FROM accounts_profile WHERE country != 'US';

-- Published items
CREATE TABLE Item_item_published AS
SELECT * FROM Item_item WHERE Item_published = 1;

-- Unpublished items
CREATE TABLE Item_item_unpublished AS
SELECT * FROM Item_item WHERE Item_published = 0;

-- Completed transactions
CREATE TABLE Market_transaction_completed AS
SELECT * FROM Market_transaction WHERE transaction_status = 'completed';

-- Pending transactions
CREATE TABLE Market_transaction_pending AS
SELECT * FROM Market_transaction WHERE transaction_status = 'pending';

```

## Vertical

```sql
-- Personal details
CREATE TABLE auth_user_identity AS
SELECT id, username, first_name, last_name, email FROM auth_user;

-- Account details
CREATE TABLE auth_user_security AS
SELECT id, password, is_active, is_staff, is_superuser, last_login, date_joined FROM auth_user;

-- Public info
CREATE TABLE accounts_profile_public AS
SELECT id, slug, bio, img, country FROM accounts_profile;

-- Private info
CREATE TABLE accounts_profile_private AS
SELECT id, address, birth_date, joindate, balance, user_id FROM accounts_profile;

-- Item summary
CREATE TABLE Item_item_main AS
SELECT id, Item_name, Item_price, Item_quantity, Item_published FROM Item_item;

-- Item details
CREATE TABLE Item_item_details AS
SELECT id, Item_description, Item_createdat, Item_slug, Item_category_id, Item_img, Item_owner_id FROM Item_item;

-- Transaction meta
CREATE TABLE Market_transaction_info AS
SELECT id, transaction_type, amount, created_at, transaction_status FROM Market_transaction;

-- Approval and linkage
CREATE TABLE Market_transaction_approval AS
SELECT id, from_approve, to_approve, admin_approve, user_from_id, user_to_id, items_id FROM Market_transaction;

```

## Hybrid

```sql
-- Published items
CREATE TABLE Item_item_published_main AS
SELECT id, Item_name, Item_price, Item_quantity FROM Item_item WHERE Item_published = 1;

CREATE TABLE Item_item_published_detail AS
SELECT id, Item_description, Item_createdat, Item_slug, Item_category_id, Item_img, Item_owner_id
FROM Item_item WHERE Item_published = 1;

-- Unpublished items
CREATE TABLE Item_item_unpublished_main AS
SELECT id, Item_name, Item_price, Item_quantity FROM Item_item WHERE Item_published = 0;

CREATE TABLE Item_item_unpublished_detail AS
SELECT id, Item_description, Item_createdat, Item_slug, Item_category_id, Item_img, Item_owner_id
FROM Item_item WHERE Item_published = 0;

-- Completed transactions
CREATE TABLE Market_transaction_completed_info AS
SELECT id, transaction_type, amount, created_at, transaction_status
FROM Market_transaction WHERE transaction_status = 'completed';

CREATE TABLE Market_transaction_completed_approval AS
SELECT id, from_approve, to_approve, admin_approve, user_from_id, user_to_id, items_id
FROM Market_transaction WHERE transaction_status = 'completed';

-- Pending transactions
CREATE TABLE Market_transaction_pending_info AS
SELECT id, transaction_type, amount, created_at, transaction_status
FROM Market_transaction WHERE transaction_status = 'pending';

CREATE TABLE Market_transaction_pending_approval AS
SELECT id, from_approve, to_approve, admin_approve, user_from_id, user_to_id, items_id
FROM Market_transaction WHERE transaction_status = 'pending';

```