# Setup API Klasifikasi Teks

Ikuti instruksi terlebih dahulu untuk menjalankan API

## 0. URL
```http://127.0.0.1:8000/predict```

## 1. Buat Virtual Environment

### **Windows**
```sh
python -m venv venv
venv\Scripts\activate
```

### **macOS/Linux**
```sh
python3 -m venv venv
source venv/bin/activate
```

## 2. Install Dependencies

Setellah membuat dan aktivasi virtual environment silakan install library library dari `requirements.txt`.

```sh
pip install -r requirements.txt
```

## 3. Jalankan API

Untuk menjalankan API nya harus menggunakan **Uvicorn**:

```sh
uvicorn transaction_desc:app --host 0.0.0.0 --port 8000 --reload
```

## 4. Tes API Dengan Swagger UI
Buka browser, ketik **http://127.0.0.1:8000/docs** untuk akses API nya secara langsung.

## 5. Tes API Dengan Postman
Untuk postman, contoh struktur json untuk post request nya seperti ini:
```json
"text": "Makan di warteg"
```

## 6. Tes API Langsung dengan Express JS
Jika ingin integrasi dengan Express JS bisa mengambil response nya dengan langkah berikut:

Library JavaScript yang Dibutuhkan
```sh
npm install axios express
```
Contoh Menggunakan API nya dalam API JavaScript
```js
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/classify', async (req, res) => {
  try {
    const response = await axios.post('http://localhost:8000/predict', {
      text: req.body.text
    });

    const { category, confidence, processed_text } = response.data;

    res.json({
      success: true,
      classification: {
        category: category,
        confidence: confidence,
        processedText: processed_text
      },
      originalText: req.body.text
    });

  } catch (error) {
    console.error('Error calling FastAPI:', error.message);
    res.status(500).json({
      success: false,
      error: 'Classification failed',
      details: error.response?.data || error.message
    });
  }
});

app.listen(PORT, () => {
  console.log(`Express proxy server running on http://localhost:${PORT}`);
});
```

## 5. Matikan Virtual Environment

Habis selesai menggunakan atau berhenti menjalankan API nya, vortual environment nya langsung dimatikan.

```sh
deactivate
```

