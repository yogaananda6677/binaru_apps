# BINARU — Product Requirements Document

**Document:** Product Requirements Document
**Version:** 2.0
**Product:** Binaru
**Tagline:** *Main. Jelajah. Bertumbuh.*
**Status:** Pre-Development / Architecture Planning
**Initial Platform:** Android
**Target User:** Anak usia 5–7 tahun
**Initial Domain:** Numerasi Dasar
**Language:** Bahasa Indonesia
**Primary Technology Direction:** Flutter + Rive
**Development Approach:** Offline-first, modular, rule-based adaptive learning

---

# 1. Product Overview

## 1.1 Product Name

**Binaru**

Binaru adalah aplikasi pembelajaran interaktif untuk anak usia 5–7 tahun yang menggabungkan:

* pembelajaran berbasis aktivitas;
* mini-game;
* visual dan audio;
* karakter learning companion;
* sistem penguasaan keterampilan;
* adaptive learning sederhana;
* reward;
* progress tracking;
* insight untuk orang tua.

Binaru tidak dirancang sebagai aplikasi kumpulan soal.

Binaru dirancang sebagai **learning companion** yang membawa anak melalui perjalanan belajar sesuai kemampuan dan perkembangannya.

---

# 2. Product Vision

> **Menciptakan pengalaman belajar digital yang terasa seperti petualangan, berkembang mengikuti kemampuan anak, dan membantu orang tua memahami perkembangan belajar mereka.**

Pengalaman utama Binaru:

**Explore → Learn → Practice → Feedback → Grow**

Anak merasa sedang menjelajah dan bermain.

Di belakang pengalaman tersebut, sistem melakukan:

* pencatatan kemampuan;
* evaluasi jawaban;
* identifikasi skill;
* penyesuaian tingkat kesulitan;
* rekomendasi aktivitas berikutnya.

---

# 3. Product Mission

Binaru memiliki empat misi utama:

1. Membuat anak menikmati proses belajar.
2. Membantu anak belajar sesuai tingkat kemampuannya.
3. Memberikan feedback positif tanpa membuat anak takut salah.
4. Memberikan informasi perkembangan yang sederhana kepada orang tua.

---

# 4. Problem Statement

Pembelajaran digital untuk anak sering memiliki beberapa masalah:

### 4.1 Quiz-oriented learning

Banyak aplikasi hanya mengubah lembar soal menjadi bentuk digital.

Anak tetap merasa sedang mengerjakan ujian.

### 4.2 Static difficulty

Semua anak menerima tingkat kesulitan yang sama meskipun kemampuan mereka berbeda.

### 4.3 Weak feedback

Feedback sering hanya berupa:

* benar;
* salah;
* skor.

Feedback seperti ini belum membantu anak memahami proses belajar.

### 4.4 Limited learning insight

Orang tua biasanya hanya melihat nilai tanpa mengetahui:

* kemampuan yang sudah dikuasai;
* konsep yang masih sulit;
* bentuk latihan yang direkomendasikan.

### 4.5 High cognitive load

Anak usia dini belum cocok dengan:

* navigasi kompleks;
* teks panjang;
* terlalu banyak tombol;
* terlalu banyak informasi dalam satu layar.

---

# 5. Product Goals

## Primary Goals

Binaru MVP harus mampu:

1. Membantu anak mempelajari numerasi dasar.
2. Menyediakan pengalaman belajar yang menyenangkan.
3. Mengukur perkembangan kemampuan anak berdasarkan skill.
4. Menyesuaikan tingkat latihan berdasarkan performa.
5. Memberikan feedback melalui karakter, visual, audio, dan animasi.
6. Menampilkan perkembangan kepada orang tua.
7. Berfungsi secara offline untuk core learning experience.

---

# 6. Non-Goals MVP

Versi pertama Binaru **tidak** bertujuan untuk:

* mencakup seluruh mata pelajaran;
* menyediakan AI chatbot;
* menggunakan generative AI;
* menyediakan multiplayer;
* menyediakan leaderboard;
* menyediakan social feature;
* menyediakan komunikasi antar-anak;
* menggunakan machine learning;
* menyediakan teacher dashboard lengkap;
* menyediakan marketplace;
* menyediakan sistem pembayaran dalam child experience;
* menyediakan cloud synchronization;
* menggantikan guru atau orang tua.

Fokus MVP adalah:

> **Membuat satu learning experience numerasi yang benar-benar matang.**

---

# 7. Target Users

## 7.1 Primary User

### Anak usia 5–7 tahun

Rentang pendidikan:

* TK B;
* kelas 1 SD;
* awal kelas 2 SD.

Karakteristik umum:

* mulai mengenal angka;
* mulai belajar operasi matematika dasar;
* tertarik pada karakter dan animasi;
* lebih mudah memahami visual daripada teks panjang;
* membutuhkan tombol besar;
* membutuhkan feedback cepat;
* memiliki kemampuan membaca yang berbeda-beda;
* memiliki durasi fokus relatif pendek.

Umur tidak boleh digunakan sebagai satu-satunya indikator kemampuan.

---

# 8. Secondary User

## Orang Tua / Wali

Orang tua membutuhkan informasi mengenai:

* aktivitas belajar anak;
* frekuensi belajar;
* skill yang berkembang;
* skill yang sudah dikuasai;
* bagian yang masih membutuhkan latihan;
* rekomendasi latihan sederhana.

Parent dashboard tidak perlu menampilkan analytics yang terlalu teknis.

---

# 9. Product Principles

Binaru dibangun berdasarkan prinsip berikut.

### 9.1 Child First

Keputusan produk harus memprioritaskan pengalaman dan perkembangan anak.

### 9.2 Learning Before Gamification

Game merupakan media pembelajaran.

Pembelajaran bukan alasan untuk memainkan game.

### 9.3 Encouragement Over Punishment

Kesalahan dianggap sebagai bagian dari proses belajar.

### 9.4 Visual Before Text

Gunakan visual dan interaksi sebelum memberikan teks panjang.

### 9.5 One Primary Action Per Screen

Setiap layar anak harus memiliki fokus utama yang jelas.

### 9.6 Simple Before Intelligent

Gunakan rule-based system sebelum machine learning.

### 9.7 Measurable Learning

Progress harus dapat diukur berdasarkan kemampuan tertentu.

### 9.8 Privacy by Design

Data anak harus diminimalkan sejak desain sistem.

### 9.9 Offline First

Aktivitas utama tidak boleh bergantung pada internet.

### 9.10 Content Is Data

Konten pembelajaran tidak boleh hard-coded langsung di UI.

Lesson dan activity harus dapat dibaca oleh learning engine sebagai data.

---

# 10. MVP Learning Domain

MVP hanya mencakup:

# Numerasi Dasar

Skill utama:

```text
NUMERACY
│
├── N01 Mengenal Angka
│
├── N02 Menghitung Objek
│
├── N03 Membandingkan Jumlah
│
├── N04 Penjumlahan
│
└── N05 Pengurangan
```

---

# 11. Skill Structure

Setiap domain dibagi menjadi:

```text
Domain
  ↓
Skill
  ↓
Level
  ↓
Lesson
  ↓
Activity
  ↓
Question / Interaction
```

Contoh:

```text
Numeracy

Skill:
Penjumlahan

Level 1:
Penjumlahan visual 1–5

Lesson:
Menggabungkan dua kelompok benda

Activity:
Bantu Aru mengumpulkan apel

Question:
2 apel + 2 apel
```

Dengan struktur ini, learning engine tidak bergantung pada bentuk layar.

---

# 12. Initial Numeracy Curriculum

## N01 — Mengenal Angka

### Level 1

Angka 1–5

### Level 2

Angka 6–10

### Level 3

Menghubungkan angka dengan jumlah objek

---

## N02 — Menghitung Objek

### Level 1

Menghitung 1–5 objek

### Level 2

Menghitung 1–10 objek

### Level 3

Objek dengan posisi bervariasi

---

## N03 — Membandingkan Jumlah

### Level 1

Lebih banyak

### Level 2

Lebih sedikit

### Level 3

Sama banyak

---

## N04 — Penjumlahan

### Level 1

Visual 1–5

### Level 2

Visual 1–10

### Level 3

Angka 1–5

### Level 4

Angka 1–10

### Level 5

Soal cerita sederhana

---

## N05 — Pengurangan

Struktur mengikuti pola yang sama:

```text
Visual
↓
Semi-visual
↓
Symbolic
↓
Simple story problem
```

---

# 13. Learning Profile

Binaru tidak hanya menyimpan skor global.

Setiap anak memiliki:

```text
Learning Profile
│
├── Numeracy
│   ├── Number Recognition
│   ├── Counting
│   ├── Comparison
│   ├── Addition
│   └── Subtraction
```

Setiap skill memiliki informasi:

```text
skill_id
current_level
mastery_state
total_attempt
correct_attempt
first_try_correct
hint_used
recent_performance
last_practiced
```

---

# 14. Mastery System

Untuk MVP, kemampuan direpresentasikan menggunakan empat state.

```text
🌱 Emerging
🌿 Developing
🌳 Proficient
⭐ Mastered
```

### Emerging

Anak baru mengenal konsep atau masih sering memerlukan bantuan.

### Developing

Anak mulai memahami tetapi performanya belum konsisten.

### Proficient

Anak mampu menjawab dengan benar secara konsisten.

### Mastered

Anak menunjukkan penguasaan konsep pada beberapa aktivitas berbeda.

---

# 15. Adaptive Learning MVP

Adaptive learning menggunakan sistem **rule-based**.

Tidak menggunakan machine learning.

Sistem mempertimbangkan:

* recent accuracy;
* first-attempt accuracy;
* penggunaan hint;
* konsistensi;
* difficulty level;
* jumlah aktivitas yang telah dilakukan.

Kecepatan menjawab tidak menjadi faktor utama.

---

# 16. Example Adaptive Rules

Contoh rule awal:

```text
Recent Accuracy < 60%
→ berikan aktivitas lebih sederhana
→ tambahkan visual support
→ rekomendasikan pengulangan
```

```text
Recent Accuracy 60–79%
→ pertahankan level
→ berikan aktivitas berbeda pada konsep yang sama
```

```text
Recent Accuracy >= 80%
AND
minimal 4 independent correct responses
→ pertimbangkan naik level
```

Jika performa turun secara konsisten:

```text
2 session berturut-turut mengalami kesulitan
→ kembali ke aktivitas sebelumnya
```

---

# 17. Baseline Experience

Baseline dilakukan ketika anak pertama kali menggunakan Binaru.

Baseline tidak ditampilkan sebagai:

**Tes**

atau:

**Ujian**

Gunakan framing:

> "Aru ingin mengenal cara kamu bermain. Yuk mulai petualangan kecil!"

Baseline terdiri dari sekitar:

**8–12 aktivitas sederhana.**

Tujuan:

* memperkirakan starting level;
* menghindari aktivitas terlalu mudah;
* menghindari aktivitas terlalu sulit.

Output:

```text
Number Recognition    Proficient
Counting              Developing
Comparison            Developing
Addition              Emerging
Subtraction           Emerging
```

Hasil baseline hanya merupakan estimasi awal.

Learning profile akan terus diperbarui.

---

# 18. Core Experience

Core loop Binaru:

```text
OPEN APP
   ↓
HOME / ADVENTURE MAP
   ↓
RECOMMENDED ACTIVITY
   ↓
ARU INTRODUCTION
   ↓
MICRO LESSON
   ↓
INTERACTIVE ACTIVITY
   ↓
ANSWER
   ↓
IMMEDIATE FEEDBACK
   ↓
REWARD
   ↓
MASTERY UPDATE
   ↓
NEXT RECOMMENDATION
```

---

# 19. Adventure Experience

Learning experience dibungkus sebagai perjalanan.

Contoh dunia:

```text
Dunia Binaru
│
├── Hutan Angka
├── Sungai Hitung
├── Bukit Perbandingan
├── Kebun Penjumlahan
└── Teluk Pengurangan
```

Nama area merupakan konsep awal dan dapat berubah pada tahap branding.

Setiap area merepresentasikan skill tertentu.

---

# 20. Learning Companion

## Character Working Name

**Aru**

## Species

Berang-berang.

## Role

Aru bukan logo.

Aru merupakan:

**Learning Companion.**

Aru bertugas:

* menyambut anak;
* memberikan instruksi;
* memperkenalkan aktivitas;
* memberikan feedback;
* memberi motivasi;
* bereaksi terhadap jawaban;
* merayakan perkembangan;
* menemani perjalanan.

---

# 21. Character Personality

Aru harus:

* penasaran;
* ceria;
* ramah;
* sabar;
* suka mencoba;
* suka menjelajah;
* encouraging;
* tidak menghakimi.

Aru tidak boleh mengejek atau memberikan respon negatif terhadap kesalahan.

---

# 22. Feedback Language

Hindari:

> "SALAH!"

Gunakan:

> "Hmm, belum tepat. Yuk kita coba lagi!"

atau:

> "Hampir! Coba hitung sekali lagi."

Ketika benar:

> "Yeay! Kamu berhasil!"

Ketika berhasil setelah mencoba ulang:

> "Hebat! Kamu terus mencoba sampai berhasil!"

Feedback harus menghargai:

**effort + learning process**

bukan hanya hasil.

---

# 23. Rive Character System

Rive digunakan untuk mengontrol ekspresi Aru.

Initial state:

```text
IDLE
GREETING
TALKING
THINKING
HAPPY
EXCITED
TRY_AGAIN
CELEBRATE
```

Application event:

```text
lesson_started
→ GREETING

instruction_started
→ TALKING

question_loaded
→ THINKING

answer_correct
→ HAPPY

answer_incorrect
→ TRY_AGAIN

skill_mastered
→ CELEBRATE
```

Rive state tidak boleh mengandung business logic.

Learning Engine menentukan event.

Character Engine hanya merespons event.

---

# 24. Audio System

Audio digunakan untuk:

* instruksi;
* penyebutan angka;
* feedback;
* cerita;
* motivasi.

MVP menggunakan audio terkontrol.

Tidak menggunakan generative voice.

Audio harus dapat digunakan secara offline.

Pengguna dapat:

* mute audio;
* mengatur sound effect;
* memutar ulang instruksi.

---

# 25. Activity Types

MVP sebaiknya tidak menggunakan satu bentuk quiz saja.

Minimum activity types:

### Select Answer

Pilih jawaban yang benar.

### Count Objects

Hitung jumlah objek.

### Compare

Pilih kelompok dengan jumlah lebih banyak/sedikit.

### Drag and Drop

Memindahkan objek.

### Match

Menghubungkan angka dengan jumlah.

### Story Activity

Menjawab berdasarkan situasi yang dialami Aru.

---

# 26. Content Model

Lesson tidak boleh ditulis langsung di Flutter widget.

Contoh conceptual structure:

```json
{
  "lesson_id": "NUM_ADD_L1_01",
  "skill_id": "NUM_ADD",
  "level": 1,
  "title": "Menggabungkan Apel",
  "activities": []
}
```

Activity:

```json
{
  "activity_id": "ACT_001",
  "type": "count_objects",
  "difficulty": 1,
  "instruction_audio": "audio_001",
  "skill_id": "NUM_COUNT"
}
```

Format final dapat berubah ketika arsitektur dirancang.

Prinsip penting:

> Content harus dapat berkembang tanpa mengubah presentation layer secara besar.

---

# 27. Question Strategy

Gunakan pendekatan hybrid.

## Authored Content

Digunakan untuk:

* cerita;
* tutorial;
* introduction;
* special activity.

## Generated Variation

Digunakan untuk:

* arithmetic values;
* jumlah objek;
* pilihan jawaban;
* posisi visual.

Generator harus memiliki constraint.

Contoh:

```text
Addition Level 1

a = 1..5
b = 1..5
a + b <= 5
```

Question generator tidak boleh menghasilkan soal di luar kompetensi level.

---

# 28. Gamification

Gamification mendukung learning loop.

Reward MVP:

* stars;
* badges;
* stickers;
* map progression;
* collectible sederhana;
* celebration animation.

Contoh:

```text
Complete lesson
↓
Gain stars
↓
Unlock map checkpoint
↓
Aru celebrates
```

Tidak ada:

* leaderboard;
* ranking;
* PvP;
* gacha;
* loot box;
* punishment streak;
* competitive pressure.

---

# 29. Progress System

Progress dibagi menjadi:

### Journey Progress

Seberapa jauh perjalanan yang telah diselesaikan.

### Learning Progress

Seberapa jauh kemampuan berkembang.

Dua hal tersebut tidak boleh disamakan.

Contoh:

```text
Journey:
Hutan Angka 70%

Learning:
Number Recognition — Mastered
Counting — Developing
```

---

# 30. Parent Mode

Parent Mode merupakan area berbeda dari Child Mode.

Parent dapat melihat:

* jumlah sesi;
* aktivitas selesai;
* learning streak opsional;
* mastery per skill;
* perkembangan minggu ini;
* rekomendasi.

Contoh:

> **Penjumlahan sedang berkembang 🌿**

> Anak sudah cukup baik ketika menggunakan benda visual, tetapi masih membutuhkan latihan ketika soal hanya menggunakan simbol angka.

Rekomendasi:

> Coba latihan penjumlahan menggunakan buah, mainan, atau benda di rumah.

---

# 31. Parental Gate

Child tidak boleh masuk Parent Mode secara tidak sengaja.

Parent Mode dilindungi dengan parental gate.

Contoh:

```text
Press and hold
+
simple adult challenge
```

atau mekanisme lain yang tidak mudah dilakukan anak secara tidak sengaja.

---

# 32. Information Architecture

```text
Splash
│
├── First Launch
│   ├── Parent Setup
│   ├── Child Profile
│   └── Baseline Adventure
│
└── Home
    │
    ├── Adventure
    │   ├── Map
    │   ├── Lesson
    │   └── Reward
    │
    ├── Collection
    │
    └── Parent Gate
        ├── Progress
        ├── Recommendations
        ├── Settings
        └── Child Profile
```

---

# 33. Child Profile

Data minimum:

```text
nickname
age_band
avatar
learning_profile
progress
preferences
```

Tidak perlu mengumpulkan:

* alamat;
* precise location;
* sekolah;
* foto anak;
* nomor telepon anak;
* tanggal lahir lengkap.

---

# 34. Privacy Principles

Binaru menggunakan prinsip:

**Minimum Data Collection**

Jika data tidak diperlukan untuk learning experience, jangan dikumpulkan.

MVP menggunakan local storage.

Tidak perlu akun online untuk anak.

---

# 35. Functional Requirements

## FR-01

User dapat membuat child profile.

## FR-02

User dapat memilih avatar.

## FR-03

Child dapat mengikuti baseline activity.

## FR-04

Child dapat memulai learning activity.

## FR-05

System dapat mengevaluasi jawaban.

## FR-06

System dapat menampilkan feedback.

## FR-07

System dapat mengubah character state.

## FR-08

System dapat memperbarui learning progress.

## FR-09

System dapat menyimpan progress secara lokal.

## FR-10

System dapat menentukan recommended activity.

## FR-11

System dapat menyesuaikan difficulty berdasarkan performance.

## FR-12

System dapat menampilkan reward.

## FR-13

Parent dapat melihat progress.

## FR-14

Parent dapat melihat rekomendasi.

## FR-15

User dapat mengatur audio.

## FR-16

Core learning experience dapat digunakan offline.

---

# 36. Non-Functional Requirements

## Performance

Target cold start harus serendah mungkin.

Interaction feedback harus terasa langsung.

Animasi tidak boleh mengganggu input.

## Reliability

Progress tidak boleh hilang ketika aplikasi ditutup normal.

## Offline

Core lesson dapat digunakan tanpa internet.

## Maintainability

Business logic harus dipisahkan dari UI.

## Scalability

Penambahan subject baru tidak membutuhkan rewrite learning engine.

## Testability

Learning logic harus dapat diuji tanpa menjalankan UI.

---

# 37. Accessibility Principles

UI harus mendukung:

* button besar;
* readable typography;
* audio instruction;
* repeat instruction;
* high visual clarity;
* tidak bergantung pada warna saja;
* simple navigation;
* reduced cognitive load.

Anak yang belum lancar membaca tetap harus dapat memahami aktivitas utama.

---

# 38. Design Direction

Keywords:

* warm;
* playful;
* adventurous;
* friendly;
* clean;
* modern;
* soft;
* child-friendly.

Hindari:

* terlalu banyak warna;
* UI penuh dekorasi;
* gradient berlebihan;
* typography kecil;
* terlalu banyak icon;
* pola visual seperti gambling game.

---

# 39. Initial Color Direction

Primary:

```text
Forest Green     #4F7A55
Soft Green       #8FB996
Warm Yellow      #F6C85F
Otter Brown      #9A6B45
Cream            #FFF7E8
Soft Blue        #8CC8D8
Coral            #F28C7A
Text Brown       #3F3832
```

Palette dapat disempurnakan pada tahap design system.

---

# 40. Typography Direction

Primary:

**Nunito**

Display:

**Baloo 2**

Typography harus diuji kembali terhadap readability pada Android device nyata.

---

# 41. Technology Direction

## Client

**Flutter**

## Character Animation

**Rive**

## Initial Persistence

Local database / structured local storage.

Pemilihan library dilakukan pada tahap Architecture Decision Record.

## Audio

Bundled local audio assets.

## Backend

Tidak wajib untuk MVP pertama.

Backend dipertimbangkan untuk:

* account;
* cloud sync;
* analytics;
* content update;
* remote configuration;
* multiple devices.

---

# 42. Conceptual System Boundaries

Binaru secara konseptual terdiri dari:

```text
BINARU
│
├── Presentation
│
├── Navigation
│
├── Learning Engine
│
├── Content Engine
│
├── Adaptive Engine
│
├── Progress Engine
│
├── Reward Engine
│
├── Character Engine
│
├── Audio Engine
│
├── Parent Insight
│
└── Persistence
```

Boundary final diputuskan pada tahap architecture design.

---

# 43. Learning Engine Responsibilities

Learning Engine bertanggung jawab atas:

* lesson execution;
* activity progression;
* validation request;
* lesson completion;
* interaction with mastery system.

Learning Engine tidak bertanggung jawab atas:

* rendering;
* animation;
* database implementation;
* UI navigation.

---

# 44. Adaptive Engine Responsibilities

Adaptive Engine menerima:

```text
learning profile
+
recent activity result
+
skill
+
difficulty
```

Kemudian menghasilkan:

```text
recommended skill
recommended difficulty
recommended activity type
```

MVP menggunakan deterministic rule.

---

# 45. Character Engine Responsibilities

Character Engine menerima semantic event.

Contoh:

```text
ANSWER_CORRECT
```

kemudian mengubah:

```text
animation
expression
sound
```

Character Engine tidak menentukan apakah jawaban benar.

---

# 46. Persistence Principles

Data harus dipisahkan menjadi:

### User Data

* profile;
* settings.

### Learning Data

* mastery;
* attempts;
* progress.

### Content Data

* lessons;
* activity definition;
* assets.

Jangan menyimpan semuanya dalam satu struktur besar.

---

# 47. Analytics Events

Walaupun MVP dapat berjalan lokal, event naming harus dirancang sejak awal.

Contoh:

```text
app_opened

lesson_started
lesson_completed

activity_started
activity_answered
activity_retried

hint_used

skill_level_up
skill_mastered

reward_unlocked
```

Jika analytics belum digunakan, interface tetap dapat dipersiapkan tanpa vendor dependency.

---

# 48. Metrics

## Product Metrics

* lesson completion rate;
* activity completion rate;
* session frequency;
* session duration.

## Learning Metrics

* baseline vs later performance;
* mastery progression;
* first-attempt accuracy;
* repeated-error reduction.

## UX Metrics

* task completion;
* child navigation success;
* parent usability.

---

# 49. Research Metrics

Jika Binaru digunakan sebagai penelitian:

### Pre-test

Kemampuan awal.

### Learning Intervention

Menggunakan Binaru.

### Post-test

Kemampuan akhir.

Kemungkinan evaluasi:

```text
Learning Gain
Engagement
Usability
Adaptive Accuracy
Parent Satisfaction
```

---

# 50. MVP Success Criteria

## Functional

MVP berhasil apabila:

* profile dapat dibuat;
* baseline berjalan;
* lima skill numerasi tersedia;
* lesson dapat dijalankan;
* activity dapat dijawab;
* jawaban dapat dievaluasi;
* Aru bereaksi terhadap hasil;
* progress tersimpan;
* mastery berubah;
* difficulty dapat menyesuaikan;
* reward bekerja;
* parent summary tersedia.

---

# 51. Learning Success

MVP harus dapat menunjukkan:

```text
Starting Ability
       ↓
Learning Activities
       ↓
Updated Mastery
       ↓
Measurable Progress
```

Binaru tidak boleh hanya menampilkan jumlah soal yang selesai.

---

# 52. Architecture Requirements Before Coding

Sebelum implementasi fitur dimulai, keputusan berikut harus terdokumentasi:

### ADR-001

Project architecture pattern.

### ADR-002

State management.

### ADR-003

Dependency injection.

### ADR-004

Navigation.

### ADR-005

Local database.

### ADR-006

Content serialization format.

### ADR-007

Asset management.

### ADR-008

Rive integration contract.

### ADR-009

Audio architecture.

### ADR-010

Testing strategy.

### ADR-011

Analytics abstraction.

### ADR-012

Error handling.

Setiap keputusan utama ditulis sebagai:

**Architecture Decision Record.**

---

# 53. Repository Strategy

Repository utama:

```text
binaru
```

Initial repository sebelum coding:

```text
binaru/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
│
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── DATA_MODEL.md
│   ├── CONTENT_MODEL.md
│   ├── ANALYTICS.md
│   │
│   └── adr/
│       └── README.md
│
├── design/
│   ├── README.md
│   └── assets/
│
└── .github/
    └── workflows/
```

Flutter project belum harus dibuat pada commit pertama.

Tujuan repository awal adalah:

> **mendokumentasikan keputusan sebelum implementasi.**

---

# 54. Repository Evolution

Setelah architecture disetujui:

```text
binaru/
│
├── apps/
│   └── mobile/
│
├── packages/
│
├── docs/
├── design/
└── .github/
```

Isi `packages/` baru ditentukan berdasarkan hasil architecture design.

Jangan membuat package hanya untuk terlihat modular.

Module dibuat ketika terdapat boundary yang jelas.

---

# 55. Documentation Strategy

Dokumen utama:

### README.md

Menjelaskan project secara singkat.

### docs/PRD.md

Menjelaskan **apa yang akan dibuat dan mengapa**.

### docs/ARCHITECTURE.md

Menjelaskan **bagaimana sistem dibangun**.

### docs/DATA_MODEL.md

Menjelaskan struktur data.

### docs/CONTENT_MODEL.md

Menjelaskan struktur lesson dan activity.

### docs/ANALYTICS.md

Menjelaskan event dan measurement.

### docs/adr/

Menjelaskan alasan setiap keputusan arsitektur.

---

# 56. Separation of Concerns

PRD tidak menentukan implementasi detail.

Contoh:

PRD boleh mengatakan:

> Progress harus tersimpan secara lokal.

PRD tidak harus menentukan:

> gunakan database library X.

Keputusan tersebut berada di:

**Architecture / ADR.**

Dengan demikian:

```text
PRD
= WHAT + WHY

ARCHITECTURE
= HOW

CODE
= IMPLEMENTATION
```

---

# 57. Testing Strategy Requirements

Architecture harus mendukung:

### Unit Test

Untuk:

* answer evaluator;
* question generation;
* mastery rules;
* adaptive engine;
* score calculation.

### Widget Test

Untuk critical UI.

### Integration Test

Untuk core learning flow.

Core business logic harus dapat diuji tanpa Rive atau Flutter UI.

---

# 58. MVP Development Sequence

## Stage 0 — Repository

Buat repository.

Tambahkan:

```text
README
PRD
Architecture placeholder
ADR structure
```

---

## Stage 1 — Architecture Design

Definisikan:

```text
system boundaries
data flow
domain model
state management
storage
dependency direction
content system
```

Tidak perlu membuat feature UI terlebih dahulu.

---

## Stage 2 — Technical Spike

Buat eksperimen kecil untuk:

* Flutter;
* Rive;
* audio;
* local storage.

Spike tidak menjadi production feature.

Tujuannya memastikan technology choices bekerja.

---

## Stage 3 — Vertical Slice

Bangun satu complete learning flow:

```text
Open lesson
↓
Aru instruction
↓
Question
↓
Answer
↓
Feedback
↓
Progress saved
```

Gunakan hanya:

**Counting 1–5.**

Jika vertical slice belum terasa bagus, jangan membuat lima modul sekaligus.

---

# 59. MVP Build Phase

Setelah vertical slice stabil:

```text
Baseline
↓
5 Numeracy Skills
↓
Mastery
↓
Adaptive Rules
↓
Adventure Map
↓
Rewards
↓
Parent Insight
```

---

# 60. Future Roadmap

## Phase 1

Numeracy MVP.

## Phase 2

Literacy.

```text
letters
phonics
syllables
words
simple reading
```

## Phase 3

English.

```text
vocabulary
listening
simple pronunciation
```

## Phase 4

Advanced Personalization.

```text
learning history
knowledge tracing
recommendation model
```

## Phase 5

Platform.

```text
cloud sync
parent account
teacher mode
content management
analytics
multiple subjects
```

---

# 61. Machine Learning Strategy

Machine learning bukan requirement awal.

Urutan:

```text
Rule-based
↓
Collect learning data
↓
Evaluate rules
↓
Build learning dataset
↓
Knowledge tracing / recommendation
```

ML hanya digunakan ketika tersedia:

* cukup data;
* masalah yang jelas;
* baseline rule-based untuk dibandingkan.

---

# 62. Key Product Risks

### Risk 1 — Terlalu Banyak Fitur

Mitigasi:

MVP hanya numerasi.

---

### Risk 2 — Game Lebih Dominan daripada Learning

Mitigasi:

Semua game harus memiliki learning objective.

---

### Risk 3 — Adaptive System Tidak Akurat

Mitigasi:

Gunakan transparent rule-based system terlebih dahulu.

---

### Risk 4 — Content Hard-coded

Mitigasi:

Gunakan content model terpisah.

---

### Risk 5 — Architecture Overengineering

Mitigasi:

Bangun modularity berdasarkan kebutuhan nyata.

---

### Risk 6 — Animasi Menambah Kompleksitas

Mitigasi:

Character Engine hanya menerima semantic event.

---

### Risk 7 — Learning Progress Hanya Menjadi Score

Mitigasi:

Gunakan skill mastery.

---

# 63. Definition of Ready — Coding

Feature implementation tidak dimulai sebelum tersedia:

* PRD v2;
* core user flow;
* initial curriculum;
* domain model;
* content model;
* architecture diagram;
* data flow;
* persistence decision;
* state management decision;
* testing strategy;
* initial ADR.

---

# 64. Definition of Done — MVP

MVP dianggap selesai apabila:

1. Anak dapat menggunakan core learning experience secara mandiri.
2. Numeracy curriculum tersedia.
3. Baseline bekerja.
4. Progress tersimpan.
5. Mastery dapat berubah berdasarkan performa.
6. Adaptive difficulty bekerja secara deterministic.
7. Character feedback sinkron dengan learning event.
8. Parent dapat memahami perkembangan anak.
9. Core experience bekerja offline.
10. Core business logic memiliki automated test.
11. Tidak terdapat critical crash pada learning flow.
12. Usability testing dasar telah dilakukan.

---

# 65. Final Product Statement

> **Binaru adalah aplikasi pembelajaran interaktif untuk anak usia 5–7 tahun yang mengubah proses belajar menjadi sebuah petualangan. Dengan learning companion bernama Aru, aktivitas visual dan audio, skill mastery, progress tracking, serta adaptive learning sederhana, Binaru membantu anak belajar sesuai kemampuan dan ritmenya sambil memberikan insight perkembangan yang mudah dipahami oleh orang tua.**

MVP Binaru berfokus pada numerasi dasar dan dibangun dengan pendekatan sederhana, offline-first, measurable, dan scalable sebelum berkembang menuju personalized learning platform yang lebih luas.

---

# 66. Development Principle

> **Build the learning system first.
> Build intelligence from evidence.
> Add complexity only when necessary.**

Urutan pengembangan:

```text
PRODUCT
   ↓
REPOSITORY
   ↓
ARCHITECTURE
   ↓
DOMAIN MODEL
   ↓
VERTICAL SLICE
   ↓
MVP
   ↓
DATA
   ↓
IMPROVEMENT
   ↓
ML / PERSONALIZATION
```

**Binaru tidak dimulai dari coding.**

Binaru dimulai dari pemahaman yang jelas tentang:

**apa yang ingin anak pelajari, bagaimana sistem mengetahui perkembangannya, dan bagaimana seluruh komponen bekerja bersama untuk mendukung proses tersebut.**
