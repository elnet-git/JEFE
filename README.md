
<<<<<<< HEAD
=======
<h2>Inventarios JQ Motors - ofNET</h2>
<div id="mensaje">Selecciona una opción o ingresa un código para buscar</div>

<input type="text" id="busqueda" placeholder="Ingresa el código para buscar..." onkeyup="filtrar()">

<div>
    <select id="selectAgencia">
        <option value="">--Selecciona agencia--</option>
    </select>
    <button onclick="filtrarAgencia()">Ver inventario de la agencia</button>
    <button onclick="exportarInventario()">Exportar inventario completo</button>
</div>

<table>
<thead>
<tr>
    <th>Agencia</th>
    <th>Código</th>
    <th>Descripción</th>
    <th>Stock</th>
</tr>
</thead>
<tbody id="resultados"></tbody>
</table>

<script>
let inventario = [];

// Convertir cualquier valor a string seguro
function valorStr(v) { return v != null ? v.toString() : ""; }

// Mostrar mensaje
function mostrarMensaje(texto) { document.getElementById("mensaje").textContent = texto; }

// URL del proxy
const SERVER_URL = "https://proxi-jqmotors.onrender.com/inventario-json";

// Cargar inventario desde proxy, pero **no mostrarlo hasta seleccionar**
async function cargarInventario() {
    mostrarMensaje("Cargando inventario desde Render...");
    try {
        const res = await fetch(SERVER_URL);
        if (!res.ok) throw new Error("Error en la respuesta del servidor");
        inventario = await res.json();
        mostrarMensaje("Selecciona una opción o ingresa un código para buscar");
        poblarAgencias();
    } catch(err) {
        console.error(err);
        mostrarMensaje("❌ No se pudo conectar con el servidor. Asegúrate de que el proxy en Render esté activo.");
    }
}

// Poblar select de agencias
function poblarAgencias() {
    const select = document.getElementById("selectAgencia");
    const agencias = [...new Set(inventario.map(i => valorStr(i.agencia)))].sort();
    agencias.forEach(a => {
        const option = document.createElement("option");
        option.value = a;
        option.textContent = a;
        select.appendChild(option);
    });
}

// Filtrar por código
function filtrar() {
    const filtro = document.getElementById("busqueda").value.toLowerCase().trim();
    if(filtro === "") {
        document.getElementById("resultados").innerHTML = "";
        mostrarMensaje("Selecciona una opción o ingresa un código para buscar");
        return;
    }
    const filtrados = inventario.filter(item =>
        valorStr(item.codigo).toLowerCase() === filtro ||
        valorStr(item.descripcion).toLowerCase().includes(filtro)
    );
    mostrarResultados(filtrados);
}

// Filtrar por agencia desde el botón
function filtrarAgencia() {
    const agencia = document.getElementById("selectAgencia").value;
    if(!agencia) { mostrarMensaje("❌ Selecciona una agencia"); return; }
    const filtrados = inventario.filter(item => valorStr(item.agencia) === agencia);
    mostrarResultados(filtrados);
    mostrarMensaje("");
}

// Mostrar resultados en tabla
function mostrarResultados(datos) {
    const tbody = document.getElementById("resultados");
    tbody.innerHTML = "";
    if(!datos.length) {
        tbody.innerHTML = "<tr><td colspan='4'>No se encontraron resultados</td></tr>";
        return;
    }
    datos.forEach(item => {
        tbody.innerHTML += `
            <tr>
                <td>${valorStr(item.agencia)}</td>
                <td>${valorStr(item.codigo)}</td>
                <td>${valorStr(item.descripcion)}</td>
                <td>${valorStr(item.stock)}</td>
            </tr>
        `;
    });
}

// Exportar inventario completo como CSV
function exportarInventario() {
    if(!inventario.length) { mostrarMensaje("❌ Inventario vacío"); return; }
    let csv = "Agencia,Código,Descripción,Stock\n";
    inventario.forEach(item => {
        csv += `"${valorStr(item.agencia)}","${valorStr(item.codigo)}","${valorStr(item.descripcion)}","${valorStr(item.stock)}"\n`;
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
>>>>>>> 685c052 (Actualización de jefe)
