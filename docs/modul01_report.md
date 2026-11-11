LAPORAN PRAKTIKUM MODUL 1
Lingkungan Pengembangan ROS 2 Berbasis Docker

1. HASIL PENGUMPULAN DATA

Tabel 1.1: Metrik Lingkungan Pengembangan
- Waktu docker pull image dasar (ros:humble-ros-base-jammy): 14.89 detik
- Waktu build image pertama (tanpa cache): 148.17 detik
- Waktu build image kedua (dengan cache): 1.21 detik
- Ukuran image robotics-lab:dev: 2.03 GB
- Waktu startup container (docker compose up): 0.88 detik
- Waktu colcon build pertama: 2.25 detik
- Jumlah package terbangun: 1 buah
- Commit hash: 97f66c4

Tabel 1.2: Perbandingan Bind Mount vs Named Volume
- Terlihat di host:
  Bind Mount (../src:/ws/src): Ya
  Named Volume (ws_install / ws_build): Tidak
- Bertahan setelah docker compose down:
  Bind Mount: Ya
  Named Volume: Ya
- Cocok untuk kode sumber:
  Bind Mount: Ya
  Named Volume: Tidak
- Cocok untuk artefak build:
  Bind Mount: Tidak
  Named Volume: Ya


2. DOKUMENTASI BUKTI INSTALASI DAN EKSEKUSI LENGKAP

1. Verifikasi Sistem Operasi Ubuntu 22.04 (WSL2)
Perintah: lsb_release -a
Hasil: Terkonfirmasi menggunakan Ubuntu 22.04 LTS (Jammy Jellyfish) pada lingkungan WSL2.

2. Verifikasi Akun Git dan Repositori GitHub
Perintah: git config user.name && git remote -v
Hasil: Profil pengguna Git dan tautan remote repositori ke akun GitHub telah terkonfigurasi dengan benar.

3. Verifikasi Engine Docker dan Status Container
Perintah: docker compose -f docker/compose.yaml ps
Hasil: Docker v24+ aktif dan container robotics_dev dalam status Up di latar belakang.

4. Verifikasi Instalasi Lingkungan ROS 2 Humble
Perintah: ros2 doctor
Hasil: Seluruh paket ROS 2 Humble terpasang utuh dengan status ALL CLEAR tanpa kendala dependensi.

5. Pull Image Dasar (docker pull)
Perintah: time docker pull ros:humble-ros-base-jammy
Hasil: Berhasil mengunduh image dasar ROS 2 Humble Jammy dari Docker Hub dengan waktu eksekusi real 0m14.894s.

6. Build Image Pertama (Tanpa Cache)
Perintah: time docker compose -f docker/compose.yaml build --no-cache
Hasil: Membangun seluruh layer Docker dari awal termasuk kompilasi dependency python3-colcon-common-extensions dengan total waktu 2m28.165s (148.17 detik).

7. Build Image Kedua (Dengan Cache)
Perintah: time docker compose -f docker/compose.yaml build
Hasil: Seluruh instruksi layer memanfaatkan CACHED sehingga proses build instan, hanya memakan waktu 0m1.206s.

8. Verifikasi Ukuran Docker Image
Perintah: docker images --format "{{.Repository}}:{{.Tag}} {{.Size}}"
Hasil: Image hasil build robotics-lab:dev berukuran 2.03 GB, sedangkan base image ros:humble-ros-base-jammy berukuran 1.16 GB.

9. Startup Container ROS 2
Perintah: time docker compose -f docker/compose.yaml up -d
Hasil: Menyalakan container robotics_dev serta otomatis mengalokasikan volume ws_build dan ws_install dalam waktu 0m0.882s.

10. Build Package ROS 2 Pertama (colcon build)
Perintah: time colcon build --symlink-install (di dalam container)
Hasil: Berhasil mengompilasi package my_first_robot_package di folder /ws dengan total waktu 2.25 detik.

11. Verifikasi Version Control (Git Commit Hash)
Perintah: git rev-parse --short HEAD
Hasil: Repositori telah terhubung ke version control dengan commit hash aktif 97f66c4.


3. ANALISIS SINGKAT DAN KESIMPULAN

1. Efisiensi Caching: Caching Docker terbukti memangkas waktu build dari 148.17 detik menjadi 1.21 detik (efisiensi waktu lebih dari 99%).
2. Manajemen Volume: Bind mount memudahkan perubahan kode secara live dari OS Host, sedangkan Named Volume mencegah konflik permission pada direktori build Linux.
3. Kesimpulan: Seluruh instalasi Ubuntu 22.04, ROS 2 Humble, Docker, akun GitHub, dan workspace telah selesai dikonfigurasi serta siap digunakan.
