# BimBam Buy - Agente Inteligente RAG 

Este repositorio contiene el desarrollo de un sistema de **Generación Aumentada por Recuperación (RAG)** diseñado para actuar como un asistente comercial inteligente para **BimBam Buy**. El agente es capaz de interactuar con clientes, resolver dudas frecuentes y consultar catálogos en formato PDF de manera precisa, segura y eficiente.

El proyecto está construido utilizando **Python**, **Google GenAI (Gemini)** y **PyPDF**.

---

##  Estructura del Repositorio

*   📁 `Data/`: Contiene los documentos y catálogos en formato PDF que sirven como base de conocimiento local para el agente.
*   📁 `Screenshots/`: Evidencia visual del correcto funcionamiento del sistema y sus mecanismos de defensa.
*   📄 `BimBam_Buy_RAG_Agent.ipynb`: Notebook de Google Colab con el código fuente estructurado paso a paso (Extracción, Procesamiento, Prompt Engineering y Ejecución).

---

##  Estrategia de Seguridad: "Gold Rule"

Para garantizar un comportamiento ético y evitar fallos comunes en modelos de lenguaje comerciales, se implementó una estricta directiva de seguridad mediante Prompt Engineering:
1.  **Mitigación de Alucinaciones:** Si la respuesta a la consulta del usuario no se encuentra explícitamente en la base de conocimiento (`Data/`), el agente responde estrictamente con un mensaje estandarizado, evitando inventar información.
2.  **Defensa contra Prompt Injection:** El sistema está blindado contra intentos de manipulación maliciosa (instrucciones del usuario que intenten forzar al agente a salir de su rol o ignorar las restricciones comerciales).

---

##  Evidencia de Funcionamiento y Pruebas

A continuación se detallan los casos de prueba ejecutados en el entorno de desarrollo:

### 1. Consulta Exitosa (Flujo Principal)
El agente recupera correctamente la información detallada desde los PDFs locales (políticas de devolución, plazos, condiciones y canales oficiales), estructurando la respuesta de manera clara para el usuario. Debido a la extensión y el detalle de la respuesta, la evidencia se divide en dos partes:

<p align="center">
  <img src="screenshots/exitoso_part1.png" alt="Consulta Exitosa Parte 1" width="85%">
</p>
<p align="center">
  <img src="screenshots/exitoso_part2.png" alt="Consulta Exitosa Parte 2" width="85%">
</p>

### 2. Consulta Fuera de Contexto (Filtro de Alucinación)
Al recibir una pregunta completamente ajena al negocio (como la receta de una chocotorta), el agente activa la regla de seguridad y rechaza la solicitud de forma controlada.

<p align="center">
  <img src="screenshots/fuera_contexto.png" alt="Filtro de Alucinación" width="85%">
</p>

### 3. Intento de Prompt Injection (Ataque de Inyección)
Un intento explícito de hackeo ideado para romper las reglas del sistema y forzar respuestas arbitrarias es bloqueado con éxito por las directivas del sistema.

<p align="center">
  <img src="screenshots/inyeccion.png" alt="Defensa Prompt Injection" width="85%">
</p>
