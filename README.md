Asistente de Estudio IA:
Aplicación de escritorio desarrollada en Python que permite a estudiantes cargar archivos PDF, obtener resúmenes automáticos mediante inteligencia artificial (ChatGPT), generar preguntas tipo examen y programar recordatorios de estudio.

Funcionalidades principales:
- Carga de PDFs  
  Selecciona un archivo PDF y extrae su texto completo.

- Resumen de texto con ChatGPT (próximamente)  
  Resumen automático del contenido usando la API de OpenAI.

- Generación de preguntas tipo examen (próximamente)  
  Preguntas de opción múltiple, verdadero/falso y respuesta corta.

- Recordatorios de estudio (próximamente)  
  Notificaciones programadas para retomar el material estudiado.

- Interfaz visual con `tkinter`  
  Aplicación sencilla y multiplataforma (Windows, macOS y Linux).

Estructura del proyecto:
ai_assistant/
├── main.py
├── requirements.txt
├── README.md
├── gui/
│   ├── init.py
│   └── interface.py
├── core/
│   ├── init.py
│   └── pdf_parser.py
├── data/
│   ├── texto_extraido.txt
│   └── original.pdf

Instalación:
1. Clonar el repositorio
bash
git clone https://github.com/tu_usuario/ai_assistant.git
cd ai_assistant

2. Crear y activar un entorno virtual (opcional pero recomendado)

python3 -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

3. Instalar las dependencias

pip install -r requirements.txt

4. Ejecutar la aplicación

python main.py

Requisitos:
	•	Python 3.10 o superior
	•	Librerías:
	•	pdfplumber
	•	tkinter (incluido en la mayoría de las instalaciones de Python)
	•	plyer (para notificaciones)
	•	openai (si se usa GPT para resumir)

Actualizaciones procimas: 
	•	Integrar API de OpenAI para resúmenes.
	•	Generar preguntas automáticamente.
	•	Crear módulo de notificaciones.
	•	Mejorar el diseño visual.

Autor
Desarrollado por aletguillen03
Estudiante de Ingeniería Informática.
