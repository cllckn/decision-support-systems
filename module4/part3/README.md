## 3.4.A Case Study on Authentication and Authorization

This is a **Node.js-based web application** with user authentication, role-based access control, and a customer management module.

**Main Features**

* Redirects users to different dashboards based on their role.
* Alerts users and redirects them to login if the session expires.
* Secure API Calls- uses `Authorization: Bearer <token>` in requests.



**Technologies Used**

- **Backend:** Node.js, Express, PostgreSQL
- **Authentication:** JWT (JSON Web Tokens), bcrypt for password hashing
- **Frontend:** HTML, jQuery, Tailwind CSS
- **API Requests:** AJAX with jQuery


**The database structure of the application**

```sql
CREATE DATABASE dss;
----------------------------
create table users
(
  id        serial primary key,
  username  varchar(50)  not null unique,
  password  varchar(255) not null,
  firstname varchar(50)  not null,
  lastname  varchar(50)  not null,
  role      smallint
);


----------------------------
create table customers
(
  id    serial primary key,
  name  varchar(50) not null,
  email varchar(50),
  phone varchar(50),
  city  varchar(50)
);

----------------------------
INSERT INTO customers (name, email, phone, city)
VALUES ('JR', 'jr@x.com', '1234', 'Astana'),
       ('Jane', 'jane@x.com', '6666', 'Petropavlovsk');

```
