# 🕹️ YT Shop - Game Account Marketplace

## 📌 About the Project

**YT Shop** is a complete and fully responsive **game account marketplace** built with **Django**. This project includes features for both **buyers** and **sellers**, ensuring a smooth and user-friendly experience.

---

## ✨ Features
### **🔹General Features**
- Fully responsive design for all devices
- User authentication system with registration and login functionality
- Comprehensive pagination to enhance user experience on product pages
- Dedicated blog section for content sharing and updates

### 👤 User Types

- **Buyer**

  - Can register and log in.
  - Browse available game accounts for sale.
  - View detailed information about each account, including images.
  - Filter products using various criteria.
  - The **shop page** includes **pagination** to manage large numbers of products efficiently.
  - Access blog content related to gaming and account trading.

- **Seller**
  - Can register and log in.
  - Post ads for game accounts they wish to sell.
  - Must confirm acceptance of the site's rules before submitting account details.
  - Each listing includes information such as **level**, **region**, **description**, **four required images**, and one optional image.
  - After posting, the seller is redirected to the detailed view of their listing.
  - Can view their posted ads on their **profile page**.

### 🛡️ Admin Panel

- Every newly submitted listing requires **admin approval**. The admin must tick the **Validation** option in the admin panel for the ad to become publicly visible.

---

## 📌 Project Structure

- **Django Backend** (Root directory)
- **SQLite Database** (Default database used)

---

## 🚀 How to Run the Project

1. **Clone the Repository:**

```sh
git clone https://github.com/sajad-18/ytshop.git
```

2. **Navigate to the Project Directory:**

```sh
cd ytshop
```

3. **Install Dependencies:**

```sh
pip install -r requirements.txt
```

4. **Apply Database Migrations:**

```sh
python manage.py migrate
```

5. **Create a Superuser for Admin Access:**

```sh
python manage.py createsuperuser
```

6. **Run the Development Server:**

```sh
python manage.py runserver
```

7. Visit the following URLs:

- **Main Site:** `http://localhost:8000`
- **Admin Panel:** `http://localhost:8000/admin`

---

## 🛠 Technologies Used

- **Django** (For backend and core functionality)
- **SQLite** (Database)
- **HTML / CSS / JavaScript** (For frontend and interactivity)

---

## 👨‍💻 Contact Me
- 📧 Email: [sajjad.ir8415@gmail.com](mailto:sajjad.ir8415@gmail.com)
- 💼 LinkedIn: [Sajjad Esmaeilzadeh](https://www.linkedin.com/in/sajad-esmaeilzadeh/)
- 🌐 Personal Website: [Sevelop.ir](https://www.sevelop.ir)

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it.

---

## 📌 خلاصه فارسی

**YT Shop** یک پروژه فروشگاه آنلاین برای خرید و فروش اکانت‌های بازی است که با **Django** ساخته شده و کاملاً واکنش‌گرا طراحی شده است. این پروژه دارای دو نوع کاربر است:

### ✨ امکانات:
 - طراحی کاملاً ریسپانسیو
 - سیستم ثبت‌نام و ورود کاربران
 - صفحه جزئیات اکانت‌ها با توضیحات کامل و نمایش تصاویر
 - قابلیت فیلتر کردن محصولات در صفحه فروشگاه
 - صفحه فروشگاه دارای صفحه‌بندی (Pagination) برای نمایش بهتر محصولات
 - کاربران فروشنده می‌توانند با تأیید قوانین، اکانت‌های خود را در سایت ثبت کنند
 - هر آگهی پس از ثبت توسط کاربر، باید در پنل ادمین تأیید (Validation) شود تا در سایت نمایش داده شود
 - بخش پروفایل کاربر شامل آگهی‌های ثبت‌شده توسط همان کاربر

### 👤 کاربران

- **خریدار**:

  - می‌تواند ثبت‌نام کرده و وارد سایت شود.
  - امکان مشاهده اکانت‌های بازی، فیلتر کردن محصولات و مطالعه بلاگ را دارد.
  - صفحه فروشگاه دارای **صفحه‌بندی (Pagination)** برای مدیریت بهتر نمایش محصولات است.

- **فروشنده**:
  - می‌تواند ثبت‌نام کرده و وارد سایت شود.
  - امکان ثبت آگهی فروش اکانت بازی با جزئیات کامل و تصاویر دارد.
  - آگهی‌های ثبت‌شده در صفحه پروفایل فروشنده نمایش داده می‌شود.
  - پس از ثبت آگهی، باید توسط ادمین تأیید شود تا در سایت نمایش داده شود.

### 🚀 راه‌اندازی پروژه

1. پروژه را کلون کنید:

```sh
git clone https://github.com/sajad-18/ytshop.git
```

2. وارد پوشه پروژه شوید:

```sh
cd ytshop
```

3. وابستگی‌ها را نصب کنید:

```sh
pip install -r requirements.txt
```

4. مایگریشن‌های پایگاه داده را اعمال کنید:

```sh
python manage.py migrate
```

5. ادمین ایجاد کنید:

```sh
python manage.py createsuperuser
```

6. سرور توسعه را اجرا کنید:

```sh
python manage.py runserver
```

آدرس‌های پروژه:

- **سایت اصلی:** `http://localhost:8000`
- **ادمین پنل:** `http://localhost:8000/admin`
