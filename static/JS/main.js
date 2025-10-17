// 1. Define la URL base sin el ID del personaje
let baseURL = 'http://127.0.0.1:5000/api/characters/'; 

for(let i = 1; i <= 17; i++){
    // 2. Construye la URL completa (ej: .../characters/1, .../characters/2, etc.)
    const fullURL = baseURL + i; 

    fetch(fullURL)
        .then((response) => response.json()) // Convierte la respuesta a formato JSON
        .then(data => {
            console.log(`Personaje #${i}:`, data); // Imprime el objeto de datos en la consola
        })
        .catch(error => {
            // Manejo de errores por si falla la red o la API
            console.error(`Error al obtener el personaje ${i}:`, error);
        });
}