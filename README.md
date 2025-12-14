# 🏗️ ArchDecision DSL
**Software Architecture Decision Support Language**

ArchDecision DSL adalah sebuah *Domain-Specific Language (DSL)* yang dirancang untuk membantu **software developer** dan **software architect** dalam mengambil keputusan arsitektur perangkat lunak berdasarkan **kebutuhan non-fungsional** dan **constraint proyek**.

DSL ini dikembangkan sebagai **Tugas Besar Mata Kuliah Programming Language Pragmatics (PLP)**.

---

## 📌 Fitur Utama

- 📄 Spesifikasi sistem secara deklaratif
- ⚙️ Definisi kebutuhan non-fungsional:
  - Scalability
  - Performance
  - Security
  - Maintainability
- 🚧 Definisi constraint proyek:
  - Ukuran tim
  - Tingkat budget
- 🧠 Rekomendasi keputusan arsitektur otomatis
- 🔍 Grammar berbasis **ANTLR**
- 🐍 Interpreter menggunakan **Python**

---

## 🧩 Contoh ArchDecision DSL

```dsl
system ECommerce
type web

requirements {
    scalability high
    performance high
    security medium
    maintainability high
}

constraints {
    team medium
    budget high
}

recommendation

Architecture Decision Result
----------------------------
System Name : ECommerce
System Type : web

- Architecture Style : Microservices
- API Style          : REST
- Database           : NoSQL
- Deployment         : Cloud

⚙️ Cara Instalasi
1️⃣ Clone Repository
git clone https://github.com/username/ArchDecision-DSL.git
cd ArchDecision-DSL

2️⃣ Install ANTLR Runtime untuk Python
pip install antlr4-python3-runtime

3️⃣ Generate Lexer & Parser (Jika Diperlukan)
java -jar antlr-4.13.1-complete.jar \
-Dlanguage=Python3 \
-visitor \
-o generated \
grammar/ArchDecision.g4

▶️ Cara Menjalankan Program

Pastikan file DSL tersedia di folder src/.

python -m src.main


Program akan:

Membaca file .dsl

Melakukan parsing menggunakan ANTLR

Mengeksekusi interpreter

Menampilkan rekomendasi arsitektur

▶️ Cara Menjalankan Program

Pastikan file DSL tersedia di folder src/.

python -m src.main


Program akan:

Membaca file .dsl

Melakukan parsing menggunakan ANTLR

Mengeksekusi interpreter

Menampilkan rekomendasi arsitektur