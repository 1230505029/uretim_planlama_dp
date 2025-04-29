# Üretim Planlama - Dinamik Programlama Yaklaşımı

Bu proje, bir üretim hattındaki işlerin farklı makinelerde işlenme sırasını optimize ederek **toplam üretim süresini en aza indirmeyi** amaçlamaktadır. Problem, dinamik programlama yöntemiyle çözülmüştür.

## 🧠 Problem Tanımı

Bir ürünün üretiminde her iş, sırayla belirli makinelerde gerçekleştirilmelidir. Makinelerin her bir iş için farklı süreleri vardır. Amaç, işlerin sırasını en uygun şekilde belirleyerek toplam üretim süresini ve makine geçiş maliyetlerini azaltmaktır.

## 🧮 Kullanılan Yöntem

- Dinamik programlama ile alt problemler çözülerek tüm olası iş sıralamaları analiz edilir.
- Amaç: M makineli bir üretim hattında, N işin minimum sürede tamamlanması.

## 📁 Dosyalar

- `uretim_planlama.py`: Dinamik programlama algoritmasının yer aldığı Python dosyası.
- `README.md`: Proje hakkında açıklamalar.

## ▶️ Çalıştırma

Terminal üzerinden:

```bash
python uretim_planlama.py
