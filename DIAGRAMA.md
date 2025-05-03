graph TD
    %% Módulos Principales
    A[run.py - Punto de entrada] -->|Inicia| B[ui.py - Ventana Principal]
    B -->|Usa Operaciones CRUD| C[database.py - Clases Cliente/Clientes]
    B -->|Valida DNI| D[helpers.py - Validaciones]
    C -->|Persistencia| E[clientes.csv - Base de Datos]
    B -->|Configura Rutas| F[config.py - Configuración]
    B -->|Interacción Menú| G[menu.py - Menú Terminal (Opcional)]
    
    %% Relaciones Adicionales
    D -->|Regex DNI| H[re - Módulo Python]
    F -->|Define Rutas| E
    G -.->|Alternativa CLI| B

    %% Estilos
    classDef py fill:#f9f,color:#333;
    classDef csv fill:#9f9,color:#333;
    class A,B,C,D,F,G py
    class E csv
