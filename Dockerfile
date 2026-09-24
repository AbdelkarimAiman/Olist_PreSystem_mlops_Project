# استخدام صورة بايثون خفيفة
FROM python:3.9-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ متطلبات المشروع وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع إلى الحاوية
COPY . .

# فتح المنفذ الذي يعمل عليه سيرفر FastAPI
EXPOSE 8000

# أمر تشغيل السيرفر تلقائياً عند تشغيل الحاوية
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]