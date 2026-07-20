# BimBam Buy - Agente Inteligente RAG 

Este repositorio contiene el desarrollo de un sistema de **Generación Aumentada por Recuperación (RAG)** diseñado para actuar como un asistente comercial inteligente para **BimBam Buy**. El agente es capaz de interactuar con clientes, resolver dudas frecuentes y consultar catálogos en formato PDF de manera precisa, segura y eficiente.

El proyecto está construido utilizando **Python**, **Google GenAI (Gemini)** y **PyPDF**.

---

##  Estructura del Repositorio

*   📁 **`Data/`**: Contiene los documentos y catálogos en formato PDF que sirven como base de conocimiento local para el agente.
*   📁 **`Screenshots/`**: Evidencia visual del correcto funcionamiento del sistema y sus mecanismos de defensa.
*   📄 **`BimBam_Buy_RAG_Agent.ipynb`**: Notebook de Google Colab con el código fuente estructurado paso a paso (Extracción, Procesamiento, Prompt Engineering y Ejecución).

---

##  Estrategia de Seguridad: "Gold Rule"

Para garantizar un comportamiento ético y evitar fallos comunes en modelos de lenguaje comerciales, se implementó una estricta directiva de seguridad mediante Prompt Engineering:
1.  **Mitigación de Alucinaciones:** Si la respuesta a la consulta del usuario no se encuentra explícitamente en la base de conocimiento (`Data/`), el agente responde estrictamente con un mensaje estandarizado, evitando inventar información.
2.  **Defensa contra Prompt Injection:** El sistema está blindado contra intentos de manipulación maliciosa (instrucciones del usuario que intenten forzar al agente a salir de su rol o ignorar las restricciones comerciales).

---

##  Evidencia de Ejecución en la Nube (Alternativa Cloud)

> **Nota sobre el entorno de despliegue:** Debido a las restricciones globales de facturación y validación de identidad requeridas para el alta de servicios en Oracle Cloud Infrastructure (OCI) mediante tarjeta de crédito, se optó por una arquitectura Cloud alternativa e igualmente robusta utilizando la infraestructura de **Google**.

El agente inteligente se encuentra completamente operativo en la nube bajo el entorno de **Google Colab**, consumiendo los modelos fundacionales de Google GenAI a través de su API en producción. 

### Evidencias de Funcionamiento Cloud
Las capturas de pantalla que demuestran la ejecución exitosa del script, el procesamiento del PDF con PyPDF y las respuestas del modelo en tiempo real dentro del entorno de Google Colab se encuentran almacenadas en la carpeta correspondiente del repositorio:

*  **Evidencias visuales:** Podés consultar las capturas detalladas directamente en la carpeta [`/Screenshots/`](./Screenshots/).

---

##  Evidencia de Funcionamiento y Pruebas

A continuación se detallan los casos de prueba ejecutados en el entorno de desarrollo:

### 1. Consulta Exitosa (Flujo Principal)
El agente recupera correctamente la información detallada desde los PDFs locales (políticas de devolución, plazos, condiciones y canales oficiales), estructurando la respuesta de manera clara para el usuario. Debido a la extensión y el detalle de la respuesta, la evidencia se divide en dos partes:

<p align="center">
  <img src="Screenshots/exitoso_parte1.png" alt="Consulta Exitosa Parte 1" width="85%">
</p>
<p align="center">
  <img src="Screenshots/exitoso_parte2.png" alt="Consulta Exitosa Parte 2" width="85%">
</p>

### 2. Consulta Fuera de Contexto (Filtro de Alucinación)
Al recibir una pregunta completamente ajena al negocio (como la receta de una chocotorta), el agente activa la regla de seguridad y rechaza la solicitud de forma controlada.

<p align="center">
  <img src="Screenshots/fuera_contexto.png" alt="Filtro de Alucinación" width="85%">
</p>

### 3. Intento de Prompt Injection (Ataque de Inyección)
Un intento explícito de hackeo ideado para romper las reglas del sistema y forzar respuestas arbitrarias es bloqueado con éxito por las directivas del sistema.

<p align="center">
  <img src="Screenshots/inyeccion.png" alt="Defensa Prompt Injection" width="85%">
</p>

---




