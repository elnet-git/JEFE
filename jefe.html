<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Inventarios JQ Motors - theNET</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body { font-family: Arial, sans-serif; margin:0; padding:20px; background:#f4f6fa; text-align:center; }
h2 { margin-bottom:20px; }
input, select, button { width:90%; max-width:400px; padding:12px; font-size:18px; margin-bottom:10px; border-radius:6px; border:1px solid #ccc; }
table { width:95%; max-width:900px; margin:auto; border-collapse:collapse; background:white; border-radius:10px; overflow:hidden; box-shadow:0 2px 5px rgba(0,0,0,0.1); }
th { background:#0044cc; color:white; padding:10px; text-transform:uppercase; }
td { padding:10px; border-bottom:1px solid #ddd; text-align:center; }
tr:nth-child(even){background:#f2f2f2;}
#mensaje { color:red; margin-bottom:20px; font-weight:bold; }
button { cursor:pointer; background:#0044cc; color:white; border:none; }
button:hover { background:#003399; }
</style>
</head>
<body>

<h2>InventarioS JQ Motors - ofNET</h2>
<div id="mensaje"></div>

<input type="text" id="busqueda" placeholder="Ingresa el código para buscar..." onkeyup="filtrar()">

<div>
    <button onclick="verTodo()">Ver todo el inventario</button>
    <button onclick="exportarInventario()">Exportar inventario completo</button>
</div>

<table>
<thead>
<tr>
    <th>Código</th>
    <th>Descripción</th>
    <th>Stock</th>
    <th>Agencia</th>
</tr>
</thead>
<tbody id="resultados"></tbody>
</table>

<script>
let inventario = [];

// Mostrar mensaje
function mostrarMensaje(texto) {
    document.getElementById("mensaje").textContent = texto;
}

// Cargar inventario desde proxy
async function cargarInventario() {
    const SERVER_URL = "http://127.0.0.1:5002/proxy_matriz";
    mostrarMensaje("Cargando inventario de Matriz...");
    try {
        const res = await fetch(SERVER_URL);
        if (!res.ok) throw new Error("Error en la respuesta del servidor");
        inventario = await res.json();
        mostrarMensaje(""); // limpiar mensaje
    } catch(err) {
        console.error(err);
        mostrarMensaje("❌ No se pudo conectar con el servidor. Asegúrate de que proxy_matriz.py esté corriendo.");
    }
}

// Filtrar por código (o descripción opcional)
function filtrar() {
    const filtro = document.getElementById("busqueda").value.toLowerCase().trim();
    if(filtro === "") {
        document.getElementById("resultados").innerHTML = ""; // limpiar tabla si no hay búsqueda
        return;
    }
    const filtrados = inventario.filter(item =>
        (item.codigo && item.codigo.toLowerCase() === filtro) ||
        (item.descripcion && item.descripcion.toLowerCase().includes(filtro))
    );
    mostrarResultados(filtrados);
}

// Mostrar resultados en tabla
function mostrarResultados(datos) {
    const tbody = document.getElementById("resultados");
    tbody.innerHTML = "";
    if (!datos.length) {
        tbody.innerHTML = "<tr><td colspan='4'>No se encontraron resultados</td></tr>";
        return;
    }
    datos.forEach(item => {
        tbody.innerHTML += `
            <tr>
                <td>${item.codigo || ""}</td>
                <td>${item.descripcion || ""}</td>
                <td>${item.stock != null ? item.stock : ""}</td>
                <td>${item.agencia || ""}</td>
            </tr>
        `;
    });
}

// Ver todo el inventario
function verTodo() {
    mostrarResultados(inventario);
    mostrarMensaje("");
}

// Exportar inventario completo como CSV
function exportarInventario() {
    if(!inventario.length) {
        mostrarMensaje("❌ Inventario vacío, no hay datos para exportar");
        return;
    }
    let csv = "Código,Descripción,Stock,Agencia\n";
    inventario.forEach(item => {
        csv += `"${item.codigo || ''}","${item.descripcion || ''}","${item.stock != null ? item.stock : ''}","${item.agencia || ''}"\n`;
    });
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "inventario_matriz.csv";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

// Inicializar
cargarInventario();
</script>
</body>
</html>
