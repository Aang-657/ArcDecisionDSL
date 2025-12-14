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
```
```output
Architecture Decision Result
----------------------------
System Name : ECommerce
System Type : web

- Architecture Style : Microservices
- API Style          : REST
- Database           : NoSQL
- Deployment         : Cloud
```
⚙️ Cara Instalasi<br>
1️⃣ Clone Repository<br>
```terminal
git clone https://github.com/Aang-657/ArchDecision-DSL.git
```
```terminal
cd ArchDecision-DSL
```

2️⃣ Install ANTLR Runtime untuk Python
```terminao
pip install antlr4-python3-runtime
```
<details>
  <summary>Generate Lexer & pasrer (Opsional)</summary>
java -jar antlr-4.13.1-complete.jar \
-Dlanguage=Python3 \
-visitor \
-o generated \
grammar/ArchDecision.g4
</details>

▶️ Cara Menjalankan Program

Pastikan file DSL tersedia di folder src/.
```terminal
python -m src.main
```

Program akan:
1. Membaca file .dsl
2. Melakukan parsing menggunakan ANTLR
3. Mengeksekusi interpreter
4. Menampilkan rekomendasi arsitektur
