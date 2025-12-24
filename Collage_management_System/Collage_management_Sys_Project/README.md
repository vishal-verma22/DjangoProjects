**# 🎓 Colleage Management System – Django CRUD Project**



**A complete \*\*Colleage Management System\*\* built using \*\*Django Framework\*\* that performs CRUD operations for \*\*Departments\*\* and \*\*Students\*\*.**  

**This project demonstrates Django \*\*Models, Forms, Views, Templates\*\*, and \*\*Foreign Key relationships\*\* in a clean and beginner-friendly way.**



**---**



**## ▶️ Demo Video**



**Watch the complete working demo of this project on LinkedIn:**

**🔗 https://www.linkedin.com/posts/vishal-verma-283305314\_djangoframework-pythondeveloper-webappdevelopment-activity-7405860363277168640-huKY?utm\_source=social\_share\_send\&utm\_medium=member\_desktop\_web\&rcm=ACoAAE\_Hh0MBBj6bfhGWPebnc2m1B01ZCS5Vd\_k**



**---**





**## 🚀 Project Features**



**### 🏫 Department Management**

**- Create new departments**

**- View all departments**

**- Delete department (with confirmation)**



**### 👨‍🎓 Student Management**

**- Add students**

**- Assign students to departments (ForeignKey)**

**- View all students**

**- Delete students**



**### ⚙️ Technical Highlights**

**- Django Function Based Views (FBV)**

**- Django ModelForms**

**- Proper use of `get\_object\_or\_404`**

**- ForeignKey relationship between Student \& Department**

**- Clean UI using HTML \& CSS**

**- Separate templates for each operation**



**---**



**## 🧩 Project Flow**



**1. Home Page**

**2. Create Department**

**3. View / Delete Department**

**4. Create Student**

**5. View / Delete Student**



**---**



**## 🛠️ Tech Stack Used**



**- \*\*Backend:\*\* Python, Django**

**- \*\*Frontend:\*\* HTML, CSS**

**- \*\*Database:\*\* SQLite (default Django DB)**

**- \*\*Tools:\*\* VS Code, Git, GitHub**



**---**



**## 🗂️ Models Used**



**### Department Model**

**- Dept ID (Primary Key)**

**- Dept Name**



**### Student Model**

**- Name**

**- Roll Number (Primary Key)**

**- Branch (Foreign Key → Department)**



**---**



**## 📂 Forms Used**



**- `DepartmentModelForm`**

**- `StudentModelForm`**



**(ModelForms are used to reduce boilerplate code and handle validations automatically.)**



**---**



**## 📁 Project Structure**



**Student\_management\_System(CRUD)\_optn|**

**├── Student\_management\_system\_project|**

**│   ├── manage.py|**

**│   ├── StudentManagementApp|**

**│   │   ├── migrations|**

**│   │   │   └── \_\_init\_\_.py|**

**│   │   ├── static|**

**│   │   │   └── css|**

**│   │   │       └── style.css|**

**│   │   ├── templates|**

**│   │   │   ├── home.html|**

**│   │   │   ├── createDepartment.html|**

**│   │   │   ├── Viewdepartment.html|**

**│   │   │   ├── deleteDepartment.html|**

**│   │   │   ├── createStudent.html|**

**│   │   │   ├── viewStudent.html|**

**│   │   │   └── deleteStudent.html|**

**│   │   ├── admin.py|**

**│   │   ├── apps.py|**

**│   │   ├── forms.py|**

**│   │   ├── models.py|**

**│   │   ├── views.py|**

**│   │   └── urls.py|**

**│   ├── Student\_management\_system\_project|**

**│   │   ├── \_\_init\_\_.py|**

**│   │   ├── settings.py|**

**│   │   ├── urls.py|**

**│   │   ├── asgi.py|**

**│   │   └── wsgi.py|**

**│   ├── db.sqlite3|**

**│   └── README.md|**

**├── screenshots|**

**│   ├── output1.png|**

**│   ├── output2.png|**

**│   ├── output3.png|**

**│   ├── output4.png|**

**│   ├── output5.png|**

**│   ├── output6.png|**

**│   ├── output7.png|**

**│   ├── output8.png|**

**│   ├── output9.png|**

**│   ├── output10.png|**

**│   ├── output11.png|**

**│   └── output12.png|**

**├── video|**

**│   └── Project\_demo\_video.mp4|**

**└── README.md**



